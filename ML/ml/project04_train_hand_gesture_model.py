from __future__ import annotations

import argparse
import random
import shutil
from pathlib import Path

import cv2
import numpy as np
import tensorflow as tf

from project04_hand_gesture_utils import GESTURE_CLASSES, gesture_folder


BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "hand_gesture_dataset"
MODEL_PATH = BASE_DIR / "project04_hand_gesture.keras"
RANDOM_SEED = 42


def load_images(folder: Path, image_size: tuple[int, int]) -> list[np.ndarray]:
    images = []
    for image_path in sorted(folder.glob("*.jpg")):
        image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        if image is None:
            continue
        image = cv2.resize(image, image_size, interpolation=cv2.INTER_AREA)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        images.append(image)
    return images


def select_balanced_images(
    images: list[np.ndarray],
    sample_count: int,
    *,
    seed: int = RANDOM_SEED,
) -> list[np.ndarray]:
    if len(images) <= sample_count:
        return images
    return random.Random(seed).sample(images, sample_count)


def build_dataset(
    dataset_dir: Path,
    image_size: tuple[int, int],
    balance_classes: bool = True,
) -> tuple[np.ndarray, np.ndarray, dict[str, int]]:
    loaded = {
        class_name: load_images(gesture_folder(dataset_dir, class_name), image_size)
        for class_name in GESTURE_CLASSES
    }
    counts = {class_name: len(images) for class_name, images in loaded.items()}
    if any(count == 0 for count in counts.values()):
        raise FileNotFoundError(f"Each gesture class needs images: {counts}")

    sample_count = min(counts.values()) if balance_classes else None
    x_items = []
    y_items = []
    for class_index, class_name in enumerate(GESTURE_CLASSES):
        images = loaded[class_name]
        if sample_count is not None:
            images = select_balanced_images(images, sample_count, seed=RANDOM_SEED + class_index)
        for image in images:
            label = np.zeros(len(GESTURE_CLASSES), dtype=np.float32)
            label[class_index] = 1.0
            x_items.append(image)
            y_items.append(label)

    pairs = list(zip(x_items, y_items))
    random.Random(42).shuffle(pairs)
    x, y = zip(*pairs)
    return np.asarray(x, dtype=np.float32) / 255.0, np.asarray(y, dtype=np.float32), counts


def build_sample_weights(y: np.ndarray) -> np.ndarray:
    class_indices = np.argmax(y, axis=1)
    class_counts = np.bincount(class_indices, minlength=len(GESTURE_CLASSES))
    total = len(class_indices)
    class_weights = {
        class_index: total / (len(GESTURE_CLASSES) * count)
        for class_index, count in enumerate(class_counts)
        if count > 0
    }
    return np.asarray([class_weights[int(class_index)] for class_index in class_indices], dtype=np.float32)


def build_model(image_size: tuple[int, int]):
    model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=(image_size[1], image_size[0], 3)),
            tf.keras.layers.RandomFlip("horizontal"),
            tf.keras.layers.RandomRotation(0.04),
            tf.keras.layers.RandomZoom(0.08),
            tf.keras.layers.Conv2D(32, 3, activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(64, 3, activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Conv2D(96, 3, activation="relu"),
            tf.keras.layers.MaxPooling2D(),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dropout(0.35),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(len(GESTURE_CLASSES), activation="softmax"),
        ]
    )
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train project04 hand gesture model.")
    parser.add_argument("--dataset-dir", type=Path, default=DATASET_DIR)
    parser.add_argument("--model", type=Path, default=MODEL_PATH)
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--image-size", type=int, default=128)
    parser.add_argument("--no-balance", action="store_true")
    parser.add_argument("--no-sample-weight", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    image_size = (args.image_size, args.image_size)
    x, y, counts = build_dataset(
        args.dataset_dir,
        image_size=image_size,
        balance_classes=not args.no_balance,
    )
    print(f"Gesture counts: {counts}")
    print(f"Training samples: {len(x)}")

    model = build_model(image_size=image_size)
    checkpoint_dir = args.model.parent / f"{args.model.stem}_checkpoints"
    if checkpoint_dir.exists():
        shutil.rmtree(checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_pattern = checkpoint_dir / "epoch_{epoch:02d}_{val_accuracy:.4f}.keras"
    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            filepath=str(checkpoint_pattern),
            monitor="val_accuracy",
            mode="max",
            save_best_only=True,
            verbose=1,
        ),
        tf.keras.callbacks.EarlyStopping(
            monitor="val_accuracy",
            mode="max",
            patience=6,
            restore_best_weights=True,
        ),
    ]
    sample_weight = build_sample_weights(y) if args.no_balance and not args.no_sample_weight else None
    history = model.fit(
        x,
        y,
        epochs=args.epochs,
        batch_size=args.batch_size,
        validation_split=0.2,
        sample_weight=sample_weight,
        callbacks=callbacks,
        verbose=1,
    )
    best_epoch = int(np.argmax(history.history["val_accuracy"])) + 1
    best_matches = sorted(checkpoint_dir.glob(f"epoch_{best_epoch:02d}_*.keras"))
    if best_matches:
        best_model_path = best_matches[-1]
        best_model_path.replace(args.model)
        shutil.rmtree(checkpoint_dir)
    else:
        model.save(args.model)
    print(f"Model saved: {args.model}")
    print(f"Final accuracy: {history.history['accuracy'][-1]:.4f}")
    print(f"Final val_accuracy: {history.history['val_accuracy'][-1]:.4f}")
    print(f"Best val_accuracy: {max(history.history['val_accuracy']):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

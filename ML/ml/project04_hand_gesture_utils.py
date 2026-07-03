from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


GESTURE_CLASSES = ("open_hand", "fist", "peace", "unknown")
GESTURE_KEY_MAP = {
    ord("1"): "open_hand",
    ord("2"): "fist",
    ord("3"): "peace",
    ord("4"): "unknown",
}


def class_from_key(key: int) -> str | None:
    return GESTURE_KEY_MAP.get(key)


def gesture_folder(base_dir: Path, class_name: str) -> Path:
    if class_name not in GESTURE_CLASSES:
        raise ValueError(f"Unknown gesture class: {class_name}")
    return base_dir / class_name


def preprocess_hand_roi(
    roi: np.ndarray,
    image_size: tuple[int, int] = (128, 128),
) -> np.ndarray:
    if roi is None or roi.size == 0:
        raise ValueError("roi must be a non-empty array")
    if roi.ndim != 3 or roi.shape[2] != 3:
        raise ValueError("roi must be a BGR color image with 3 channels")

    resized = cv2.resize(roi, image_size, interpolation=cv2.INTER_AREA)
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    normalized = rgb.astype(np.float32) / 255.0
    return normalized.reshape(1, image_size[1], image_size[0], 3)


def choose_gesture_label(
    prediction: np.ndarray,
    threshold: float = 0.75,
    unknown_margin: float = 0.15,
) -> tuple[str, float]:
    probabilities = np.asarray(prediction, dtype=np.float32).reshape(-1)
    if probabilities.size != len(GESTURE_CLASSES):
        raise ValueError("prediction size must match gesture class count")

    class_index = int(np.argmax(probabilities))
    confidence = float(probabilities[class_index])
    sorted_probabilities = np.sort(probabilities)
    margin = float(sorted_probabilities[-1] - sorted_probabilities[-2])
    label = GESTURE_CLASSES[class_index]
    if confidence < threshold:
        return "unknown", confidence
    if label != "unknown" and margin < unknown_margin:
        return "unknown", confidence
    return label, confidence


def predict_gesture(
    model,
    roi: np.ndarray,
    threshold: float = 0.75,
    unknown_margin: float = 0.15,
    image_size: tuple[int, int] = (128, 128),
) -> tuple[str, float, np.ndarray]:
    sample = preprocess_hand_roi(roi, image_size=image_size)
    prediction = model.predict(sample, verbose=0)[0]
    label, confidence = choose_gesture_label(
        prediction,
        threshold=threshold,
        unknown_margin=unknown_margin,
    )
    return label, confidence, np.asarray(prediction, dtype=np.float32)

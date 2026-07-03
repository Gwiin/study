from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import cv2
import tensorflow as tf

from project04_hand_gesture_collect import save_sample
from project04_hand_gesture_utils import GESTURE_CLASSES, class_from_key, predict_gesture
from project04_realtime_utils import crop_center_roi


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "project04_hand_gesture.keras"
DATASET_DIR = BASE_DIR / "hand_gesture_dataset"
CAPTURE_DIR = BASE_DIR / "hand_gesture_captures"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run project04 hand gesture ROI classifier.")
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument("--model", type=Path, default=MODEL_PATH)
    parser.add_argument("--dataset-dir", type=Path, default=DATASET_DIR)
    parser.add_argument("--save-dir", type=Path, default=CAPTURE_DIR)
    parser.add_argument("--roi-size", type=int, default=320)
    parser.add_argument("--threshold", type=float, default=0.75)
    parser.add_argument("--unknown-margin", type=float, default=0.15)
    return parser.parse_args()


def draw_prediction(frame, bounds, label: str, confidence: float):
    x1, y1, x2, y2 = bounds
    color = (0, 180, 255) if label == "unknown" else (0, 220, 0)
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    cv2.rectangle(frame, (10, 10), (430, 96), (0, 0, 0), -1)
    cv2.putText(
        frame,
        f"{label} ({confidence * 100:.1f}%)",
        (20, 44),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        color,
        2,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        "1 open | 2 fist | 3 peace | 4 unknown | s save | q quit",
        (20, 78),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )


def save_capture(save_dir: Path, roi, label: str, confidence: float) -> Path:
    save_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    image_path = save_dir / f"{label}_{timestamp}_{confidence:.2f}.jpg"
    cv2.imwrite(str(image_path), roi)
    return image_path


def main() -> int:
    args = parse_args()
    if not args.model.exists():
        print(f"Model not found: {args.model}")
        print("Collect samples and train first.")
        return 1

    model = tf.keras.models.load_model(args.model)
    if model.output_shape[-1] != len(GESTURE_CLASSES):
        print(f"Model output shape does not match classes: {model.output_shape}")
        return 1

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print(f"Could not open camera index {args.camera}")
        return 1

    print("Running hand gesture classifier.")
    print("Feedback: 1=open_hand, 2=fist, 3=peace, 4=unknown. s=capture, q/ESC=quit.")
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Could not read frame from camera.")
                return 1

            display = cv2.flip(frame, 1)
            roi, bounds = crop_center_roi(display, roi_size=args.roi_size)
            label, confidence, _ = predict_gesture(
                model,
                roi,
                threshold=args.threshold,
                unknown_margin=args.unknown_margin,
            )
            draw_prediction(display, bounds, label, confidence)
            cv2.imshow("project04 hand gesture classifier", display)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):
                break
            if key == ord("s"):
                image_path = save_capture(args.save_dir, roi, label, confidence)
                print(f"Captured: {image_path}")
            class_name = class_from_key(key)
            if class_name:
                image_path = save_sample(args.dataset_dir, roi, class_name)
                print(f"Feedback saved as {class_name}: {image_path}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

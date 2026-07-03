from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import cv2

from project04_hand_gesture_utils import GESTURE_CLASSES, class_from_key, gesture_folder
from project04_realtime_utils import crop_center_roi


BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "hand_gesture_dataset"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect OpenCV ROI samples for project04 hand gesture classification."
    )
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument("--roi-size", type=int, default=320)
    parser.add_argument("--output-dir", type=Path, default=DATASET_DIR)
    return parser.parse_args()


def draw_overlay(frame, bounds, saved_label: str | None = None):
    x1, y1, x2, y2 = bounds
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 220, 255), 2)
    lines = [
        "1: open_hand",
        "2: fist",
        "3: peace",
        "4: unknown",
        "q/ESC: quit",
    ]
    if saved_label:
        lines.append(f"saved: {saved_label}")
    cv2.rectangle(frame, (10, 10), (260, 185), (0, 0, 0), -1)
    for index, line in enumerate(lines):
        cv2.putText(
            frame,
            line,
            (20, 42 + index * 28),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.72,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )
    return frame


def save_sample(dataset_dir: Path, roi, class_name: str) -> Path:
    folder = gesture_folder(dataset_dir, class_name)
    folder.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    image_path = folder / f"{class_name}_{timestamp}.jpg"
    cv2.imwrite(str(image_path), roi)
    return image_path


def main() -> int:
    args = parse_args()
    for class_name in GESTURE_CLASSES:
        gesture_folder(args.output_dir, class_name).mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print(f"Could not open camera index {args.camera}")
        return 1

    print("Collect hand gesture ROI samples: 1=open_hand, 2=fist, 3=peace, 4=unknown.")
    saved_label = None
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Could not read frame from camera.")
                return 1

            display = cv2.flip(frame, 1)
            roi, bounds = crop_center_roi(display, roi_size=args.roi_size)
            draw_overlay(display, bounds, saved_label=saved_label)
            cv2.imshow("project04 hand gesture collector", display)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):
                break
            class_name = class_from_key(key)
            if class_name:
                image_path = save_sample(args.output_dir, roi, class_name)
                saved_label = class_name
                print(f"Saved {class_name}: {image_path}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

from typing import Sequence

import numpy as np


CLASS_NAMES = ("Person", "Animal", "Unknown")


def crop_center_roi(
    frame: np.ndarray,
    roi_size: int = 320,
) -> tuple[np.ndarray, tuple[int, int, int, int]]:
    """Crop a square ROI from the center of an OpenCV BGR frame."""
    if frame is None or frame.size == 0:
        raise ValueError("frame must be a non-empty array")
    if frame.ndim != 3 or frame.shape[2] != 3:
        raise ValueError("frame must be a BGR color image with 3 channels")
    if roi_size <= 0:
        raise ValueError("roi_size must be positive")

    height, width = frame.shape[:2]
    size = min(int(roi_size), width, height)
    x1 = (width - size) // 2
    y1 = (height - size) // 2
    x2 = x1 + size
    y2 = y1 + size
    return frame[y1:y2, x1:x2], (x1, y1, x2, y2)


def roi_has_content(roi: np.ndarray, min_stddev: float = 8.0) -> bool:
    """Return True when the ROI has enough visual variation to classify."""
    if roi is None or roi.size == 0:
        return False
    return float(np.std(roi)) >= min_stddev


def is_roi_stable(
    previous_roi: np.ndarray | None,
    current_roi: np.ndarray,
    max_mean_delta: float = 6.0,
) -> bool:
    """Return True when the current ROI is visually close to the previous ROI."""
    if previous_roi is None or current_roi is None:
        return False
    if previous_roi.shape != current_roi.shape:
        return False

    delta = np.abs(
        current_roi.astype(np.float32) - previous_roi.astype(np.float32)
    )
    return float(delta.mean()) <= max_mean_delta


def prepare_frame_for_project04(
    frame: np.ndarray,
    image_size: tuple[int, int] = (128, 128),
) -> np.ndarray:
    """Convert an OpenCV BGR frame to a CNN-ready project04 sample."""
    if frame is None or frame.size == 0:
        raise ValueError("frame must be a non-empty array")
    if frame.ndim != 3 or frame.shape[2] != 3:
        raise ValueError("frame must be a BGR color image with 3 channels")

    import cv2

    resized = cv2.resize(frame, image_size, interpolation=cv2.INTER_AREA)
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    normalized = rgb.astype(np.float32) / 255.0
    return normalized.reshape(1, image_size[1], image_size[0], 3)


def choose_prediction_label(
    prediction: Sequence[float] | np.ndarray,
    threshold: float = 0.7,
    unknown_margin: float = 0.0,
    class_names: Sequence[str] = CLASS_NAMES,
) -> tuple[str, float]:
    """Return the display label and confidence for one softmax prediction."""
    probabilities = np.asarray(prediction, dtype=np.float32).reshape(-1)
    if probabilities.size != len(class_names):
        raise ValueError("prediction size must match class_names size")

    class_index = int(np.argmax(probabilities))
    confidence = float(probabilities[class_index])
    sorted_probabilities = np.sort(probabilities)
    margin = float(sorted_probabilities[-1] - sorted_probabilities[-2])
    if confidence < threshold:
        return "Unknown", confidence
    if class_names[class_index] != "Unknown" and margin < unknown_margin:
        return "Unknown", confidence
    return class_names[class_index], confidence


def predict_frame(
    model,
    frame: np.ndarray,
    threshold: float = 0.7,
    unknown_margin: float = 0.0,
    image_size: tuple[int, int] = (128, 128),
) -> tuple[str, float, np.ndarray]:
    """Run project04 preprocessing and model inference for one OpenCV frame."""
    sample = prepare_frame_for_project04(frame, image_size=image_size)
    prediction = model.predict(sample, verbose=0)[0]
    label, confidence = choose_prediction_label(
        prediction,
        threshold=threshold,
        unknown_margin=unknown_margin,
    )
    return label, confidence, np.asarray(prediction, dtype=np.float32)


def predict_center_roi(
    model,
    frame: np.ndarray,
    roi_size: int = 320,
    threshold: float = 0.7,
    unknown_margin: float = 0.0,
    image_size: tuple[int, int] = (128, 128),
) -> tuple[str, float, np.ndarray, np.ndarray, tuple[int, int, int, int]]:
    """Crop the center ROI, preprocess it, and run model inference."""
    roi, bounds = crop_center_roi(frame, roi_size=roi_size)
    label, confidence, probabilities = predict_frame(
        model,
        roi,
        threshold=threshold,
        unknown_margin=unknown_margin,
        image_size=image_size,
    )
    return label, confidence, probabilities, roi, bounds

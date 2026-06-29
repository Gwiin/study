import numpy as np


def _resize_to_mnist(image: np.ndarray) -> np.ndarray:
    try:
        import cv2

        return cv2.resize(image, (28, 28), interpolation=cv2.INTER_AREA)
    except ModuleNotFoundError:
        y_idx = np.linspace(0, image.shape[0] - 1, 28).astype(np.int64)
        x_idx = np.linspace(0, image.shape[1] - 1, 28).astype(np.int64)
        return image[np.ix_(y_idx, x_idx)]


def prepare_digit_for_cnn(image: np.ndarray) -> np.ndarray:
    """Convert a processed digit image to a CNN-ready MNIST sample."""
    if image is None or image.size == 0:
        raise ValueError("image must be a non-empty array")

    if image.ndim == 3:
        import cv2

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    resized = _resize_to_mnist(image)
    normalized = resized.astype(np.float32) / 255.0
    return normalized.reshape(1, 28, 28, 1)

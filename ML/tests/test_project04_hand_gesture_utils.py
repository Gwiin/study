import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ml"))

from project04_hand_gesture_utils import (
    GESTURE_CLASSES,
    class_from_key,
    gesture_folder,
    preprocess_hand_roi,
)
from project04_train_hand_gesture_model import build_sample_weights, select_balanced_images


class HandGestureUtilsTest(unittest.TestCase):
    def test_class_names_are_portfolio_gestures(self):
        self.assertEqual(GESTURE_CLASSES, ("open_hand", "fist", "peace", "unknown"))

    def test_class_from_key_maps_number_keys(self):
        self.assertEqual(class_from_key(ord("1")), "open_hand")
        self.assertEqual(class_from_key(ord("2")), "fist")
        self.assertEqual(class_from_key(ord("3")), "peace")
        self.assertEqual(class_from_key(ord("4")), "unknown")
        self.assertIsNone(class_from_key(ord("x")))

    def test_gesture_folder_uses_dataset_directory(self):
        base_dir = Path("dataset")

        self.assertEqual(gesture_folder(base_dir, "peace"), base_dir / "peace")

    def test_preprocess_hand_roi_returns_normalized_rgb_batch(self):
        roi = np.zeros((8, 12, 3), dtype=np.uint8)
        roi[:, :] = [10, 20, 30]

        sample = preprocess_hand_roi(roi, image_size=(4, 4))

        self.assertEqual(sample.shape, (1, 4, 4, 3))
        self.assertEqual(sample.dtype, np.float32)
        self.assertAlmostEqual(float(sample[0, 0, 0, 0]), 30 / 255.0)
        self.assertAlmostEqual(float(sample[0, 0, 0, 1]), 20 / 255.0)
        self.assertAlmostEqual(float(sample[0, 0, 0, 2]), 10 / 255.0)

    def test_preprocess_hand_roi_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            preprocess_hand_roi(np.array([], dtype=np.uint8))

    def test_select_balanced_images_samples_from_full_list(self):
        images = [np.full((1, 1, 3), index, dtype=np.uint8) for index in range(10)]

        selected = select_balanced_images(images, sample_count=4, seed=7)

        self.assertEqual(len(selected), 4)
        self.assertNotEqual([int(image[0, 0, 0]) for image in selected], [0, 1, 2, 3])

    def test_build_sample_weights_balances_imbalanced_labels(self):
        labels = np.asarray(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
            ],
            dtype=np.float32,
        )

        weights = build_sample_weights(labels)

        self.assertGreater(float(weights[0]), float(weights[1]))


if __name__ == "__main__":
    unittest.main()

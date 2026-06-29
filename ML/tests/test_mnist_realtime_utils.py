import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ml"))

from mnist_realtime_utils import prepare_digit_for_cnn


class PrepareDigitForCnnTest(unittest.TestCase):
    def test_returns_single_normalized_cnn_sample(self):
        image = np.zeros((12, 20), dtype=np.uint8)
        image[3:9, 7:13] = 255

        result = prepare_digit_for_cnn(image)

        self.assertEqual(result.shape, (1, 28, 28, 1))
        self.assertEqual(result.dtype, np.float32)
        self.assertGreaterEqual(float(result.min()), 0.0)
        self.assertLessEqual(float(result.max()), 1.0)
        self.assertEqual(float(result.max()), 1.0)

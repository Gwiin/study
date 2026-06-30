from datetime import date
import unittest

import numpy as np

from ml.project03_korean_air_forecast import (
    calculate_regression_metrics,
    get_two_week_forecast_dates,
    make_samples,
    recursive_forecast_scaled,
)


class KoreanAirWeeklyForecastTest(unittest.TestCase):
    def test_make_samples_builds_sliding_windows_and_targets(self):
        data = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])

        x, y = make_samples(data, window=2)

        np.testing.assert_array_equal(x, np.array([[[1.0], [2.0]], [[2.0], [3.0]], [[3.0], [4.0]]]))
        np.testing.assert_array_equal(y, np.array([[3.0], [4.0], [5.0]]))

    def test_two_week_forecast_dates_start_after_last_observed_date(self):
        forecast_dates = get_two_week_forecast_dates(
            today=date(2026, 6, 30),
            last_observed_date=date(2026, 6, 29),
        )

        self.assertEqual(
            forecast_dates,
            [
                date(2026, 6, 30),
                date(2026, 7, 1),
                date(2026, 7, 2),
                date(2026, 7, 3),
                date(2026, 7, 6),
                date(2026, 7, 7),
                date(2026, 7, 8),
                date(2026, 7, 9),
                date(2026, 7, 10),
                date(2026, 7, 13),
            ],
        )

    def test_recursive_forecast_scaled_rolls_predictions_into_next_window(self):
        class LastValuePlusOneModel:
            def predict(self, x, verbose=0):
                return np.array([[x[0, -1, 0] + 1.0]])

        seed_window = np.array([[10.0], [20.0], [30.0]])

        predicted = recursive_forecast_scaled(LastValuePlusOneModel(), seed_window, steps=3)

        np.testing.assert_array_equal(predicted, np.array([[31.0], [32.0], [33.0]]))

    def test_calculate_regression_metrics_reports_error_and_direction_accuracy(self):
        actual = np.array([100.0, 110.0, 105.0, 120.0])
        predicted = np.array([98.0, 112.0, 108.0, 118.0])

        metrics = calculate_regression_metrics(actual, predicted)

        self.assertAlmostEqual(metrics["test_mae"], 2.25)
        self.assertAlmostEqual(metrics["test_rmse"], 2.29128784747792)
        self.assertAlmostEqual(metrics["test_mape_percent"], 2.085497835497835)
        self.assertAlmostEqual(metrics["test_regression_accuracy_percent"], 97.91450216450216)
        self.assertAlmostEqual(metrics["test_direction_accuracy_percent"], 100.0)


if __name__ == "__main__":
    unittest.main()

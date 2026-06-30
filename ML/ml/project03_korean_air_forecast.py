from __future__ import annotations

import json
import random
from datetime import date, datetime, timedelta
from pathlib import Path

import FinanceDataReader as fdr
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler


STOCK_CODE = "003490"
STOCK_NAME = "Korean Air"
WINDOW = 40
TEST_SIZE = 220
EPOCHS = 35
RANDOM_SEED = 42
FORECAST_BUSINESS_DAYS = 10

BASE_DIR = Path(__file__).resolve().parent
PNG_PATH = BASE_DIR / "project03_korean_air_weekly_forecast.png"
CSV_PATH = BASE_DIR / "project03_korean_air_weekly_forecast.csv"
SUMMARY_PATH = BASE_DIR / "project03_korean_air_weekly_forecast_summary.json"

TOKENS = {
    "surface": "#FCFCFD",
    "panel": "#FFFFFF",
    "ink": "#1F2430",
    "muted": "#6F768A",
    "grid": "#E6E8F0",
    "axis": "#D7DBE7",
}

BLUE = {
    "base": "#A3BEFA",
    "mid": "#5477C4",
    "dark": "#2E4780",
}

ORANGE = {
    "base": "#F0986E",
    "dark": "#804126",
}


def make_samples(data: np.ndarray, window: int) -> tuple[np.ndarray, np.ndarray]:
    train = []
    target = []
    for i in range(len(data) - window):
        train.append(data[i : i + window])
        target.append(data[i + window])
    return np.array(train), np.array(target)


def get_two_week_forecast_dates(today: date, last_observed_date: date) -> list[date]:
    first_forecast_date = max(today, last_observed_date + timedelta(days=1))
    forecast_dates = []
    current = first_forecast_date
    while len(forecast_dates) < FORECAST_BUSINESS_DAYS:
        if current.weekday() < 5:
            forecast_dates.append(current)
        current += timedelta(days=1)
    return forecast_dates


def recursive_forecast_scaled(model, seed_window: np.ndarray, steps: int) -> np.ndarray:
    current_window = seed_window.astype(float).copy()
    predictions = []

    for _ in range(steps):
        predicted = float(model.predict(current_window.reshape(1, current_window.shape[0], 1), verbose=0)[0, 0])
        predictions.append([predicted])
        current_window = np.vstack([current_window[1:], [[predicted]]])

    return np.array(predictions)


def calculate_regression_metrics(actual: np.ndarray, predicted: np.ndarray) -> dict[str, float]:
    actual = np.asarray(actual, dtype=float).ravel()
    predicted = np.asarray(predicted, dtype=float).ravel()
    error = actual - predicted

    mae = float(np.mean(np.abs(error)))
    rmse = float(np.sqrt(np.mean(error**2)))
    mape = float(np.mean(np.abs(error / actual)) * 100)
    direction_accuracy = float(np.mean(np.sign(np.diff(actual)) == np.sign(np.diff(predicted))) * 100)

    return {
        "test_mae": mae,
        "test_rmse": rmse,
        "test_mape_percent": mape,
        "test_regression_accuracy_percent": 100 - mape,
        "test_direction_accuracy_percent": direction_accuracy,
    }


def build_lstm_model(window: int):
    import tensorflow as tf
    from tensorflow.keras.layers import LSTM, Dense, Input
    from tensorflow.keras.models import Sequential

    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    tf.random.set_seed(RANDOM_SEED)

    model = Sequential(
        [
            Input(shape=(window, 1)),
            LSTM(16, activation="tanh", return_sequences=False),
            Dense(1),
        ]
    )
    model.compile(loss="mse", optimizer="adam")
    return model


def fetch_open_prices() -> pd.DataFrame:
    stock = fdr.DataReader(STOCK_CODE, "2016")
    if stock.empty or "Open" not in stock.columns:
        raise ValueError(f"No open-price data returned for {STOCK_CODE}.")

    open_prices = stock[["Open"]].dropna().copy()
    open_prices.index = pd.to_datetime(open_prices.index)
    return open_prices


def train_and_forecast(open_prices: pd.DataFrame, today: date) -> tuple[pd.DataFrame, dict]:
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(open_prices[["Open"]])

    test_size = min(TEST_SIZE, max(WINDOW + 1, len(scaled) // 5))
    train_data = scaled[:-test_size]
    test_data = scaled[-test_size:]

    x_train, y_train = make_samples(train_data, WINDOW)
    x_test, y_test = make_samples(test_data, WINDOW)

    model = build_lstm_model(WINDOW)
    history = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=32, verbose=0)
    test_loss = float(model.evaluate(x_test, y_test, verbose=0))
    y_test_pred = model.predict(x_test, verbose=0)
    actual_test_open = scaler.inverse_transform(y_test).ravel()
    predicted_test_open = scaler.inverse_transform(y_test_pred).ravel()
    test_metrics = calculate_regression_metrics(actual_test_open, predicted_test_open)

    last_observed_date = open_prices.index[-1].date()
    forecast_dates = get_two_week_forecast_dates(today=today, last_observed_date=last_observed_date)

    scaled_forecast = recursive_forecast_scaled(model, scaled[-WINDOW:], len(forecast_dates))
    forecast_values = scaler.inverse_transform(scaled_forecast).ravel()

    forecast = pd.DataFrame(
        {
            "Date": pd.to_datetime(forecast_dates),
            "Predicted_Open": np.round(forecast_values, 0).astype(int),
        }
    )

    summary = {
        "stock_code": STOCK_CODE,
        "stock_name": STOCK_NAME,
        "data_start": open_prices.index[0].strftime("%Y-%m-%d"),
        "last_observed_date": open_prices.index[-1].strftime("%Y-%m-%d"),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "window": WINDOW,
        "epochs": EPOCHS,
        "forecast_business_days": FORECAST_BUSINESS_DAYS,
        "train_rows": int(len(x_train)),
        "test_rows": int(len(x_test)),
        "final_train_loss": float(history.history["loss"][-1]),
        "test_loss": test_loss,
        **test_metrics,
        "forecast_start": forecast["Date"].min().strftime("%Y-%m-%d"),
        "forecast_end": forecast["Date"].max().strftime("%Y-%m-%d"),
    }
    return forecast, summary


def add_chart_header(fig, ax, title: str, subtitle: str) -> None:
    ax.set_title("")
    fig.subplots_adjust(top=0.83)
    left = ax.get_position().x0
    fig.text(left, 0.965, title, ha="left", va="top", fontsize=14, fontweight="semibold", color=TOKENS["ink"])
    fig.text(left, 0.915, subtitle, ha="left", va="top", fontsize=9, color=TOKENS["muted"])
    sns.despine(ax=ax)


def use_chart_theme() -> None:
    sns.set_theme(
        style="whitegrid",
        rc={
            "figure.facecolor": TOKENS["surface"],
            "axes.facecolor": TOKENS["panel"],
            "axes.edgecolor": TOKENS["axis"],
            "axes.labelcolor": TOKENS["ink"],
            "grid.color": TOKENS["grid"],
            "grid.linewidth": 0.8,
            "font.family": "sans-serif",
            "font.sans-serif": ["Malgun Gothic", "Segoe UI", "DejaVu Sans", "Arial"],
        },
    )


def plot_forecast(open_prices: pd.DataFrame, forecast: pd.DataFrame, summary: dict) -> None:
    use_chart_theme()
    recent = open_prices.tail(80).reset_index().rename(columns={"index": "Date", "Open": "Actual_Open"})

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.lineplot(data=recent, x="Date", y="Actual_Open", ax=ax, color=BLUE["mid"], linewidth=1.3, label="Actual open")
    sns.lineplot(
        data=forecast,
        x="Date",
        y="Predicted_Open",
        ax=ax,
        color=ORANGE["base"],
        linewidth=1.5,
        marker="o",
        label="Two-week forecast",
    )

    boundary = pd.to_datetime(summary["last_observed_date"])
    ax.axvline(boundary, color=TOKENS["ink"], linestyle=":", linewidth=1.0)
    ax.text(boundary, ax.get_ylim()[1], " last observed", ha="left", va="top", fontsize=8, color=TOKENS["muted"])

    ax.set_xlabel("Date")
    ax.set_ylabel("Open price (KRW)")
    ax.yaxis.set_major_formatter(mticker.StrMethodFormatter("{x:,.0f}"))
    locator = mdates.AutoDateLocator(minticks=4, maxticks=7)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.02), frameon=False, ncol=2, borderaxespad=0)

    subtitle = (
        f"Open price, KRW; training data {summary['data_start']} to {summary['last_observed_date']}; "
        f"LSTM window={summary['window']}, epochs={summary['epochs']}."
    )
    add_chart_header(fig, ax, "Korean Air two-week open-price forecast", subtitle)
    fig.savefig(PNG_PATH, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    open_prices = fetch_open_prices()
    forecast, summary = train_and_forecast(open_prices, today=date.today())
    forecast.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    plot_forecast(open_prices, forecast, summary)

    print(f"Saved chart: {PNG_PATH}")
    print(f"Saved forecast CSV: {CSV_PATH}")
    print(f"Saved summary JSON: {SUMMARY_PATH}")
    print(forecast.to_string(index=False))


if __name__ == "__main__":
    main()

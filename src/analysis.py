import numpy as np
import pandas as pd
from pathlib import Pathlib

def load_stock_date(file_path):
    df = pd.read.csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").sort_index

    return df


def align_close_prices(stock_data, tickers):
    close_prices = pd.concat(
        [stock_data[ticker]["close"] for ticker in tickers],
        axis=1,
        join="inner"
    )

    close_prices.columns = tickers

    return close_prices


def align_volume(stock_data, tickers):
    volume_data = pd.concat(
        [stock_data[ticker]["close"] for ticker in tickers],
        axis=1,
        join="inner"
    )

    volume_data.columns = tickers

    return volume_data


def calculate_returns(close_prices):
    return close_prices.pct_change().dropna()


def calculate_rolling_volatility(daily_returns, window=20):
    return daily_returns.rolling(window=window).std() * np.sqrt(252)


def classify_regimes(market_volatility):
    low_threshold = market_volatility.quantile(0.33)
    high_threshold = market_volatility.quantile(0.67)

    regime = pd.Series(
        index=market_volatility.index,
        dtype="object"
    )

    regime[market_volatility <= low_threshold] = "Low"

    regime[
        (market_volatility > low_threshold)
        & (market_volatility < high_threshold)
    ] = "Normal"


    regime[market_volatility >= high_threshold] = "High"

    return regime, low_threshold, high_threshold
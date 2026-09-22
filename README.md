# Regime-Aware Equity Behavior Analyzer

## Overview

This project analyzes how individual stocks behave under different market volatility regimes.

The analysis focuses on four large U.S. stocks:

- AAPL
- MSFT
- JPM
- XOM

The project studies how returns, volatility, drawdowns, correlations, and trading volume change when market conditions move between Low, Normal, and High volatility regimes.

The goal is to understand whether market stress changes not only the level of risk, but also how strongly assets move together and how deeply they fall from previous peaks.

---

## Research Question

How do return, volatility, drawdown, correlation, and trading volume change across different market regimes, and how differently do individual stocks behave when market conditions deteriorate?

---

## Assets and Data

The project uses historical price and volume data for:

- Apple Inc. — AAPL
- Microsoft Corp. — MSFT
- JPMorgan Chase & Co. — JPM
- Exxon Mobil Corp. — XOM

The stock datasets contain:

- Date
- Open
- High
- Low
- Close
- Volume

The individual stock histories were aligned using only dates shared by all four stocks.

The final aligned dataset contains more than 10,000 common trading days.

---

## Methodology

### 1. Data Preparation

Each stock dataset was:

- loaded with Pandas
- converted to a DatetimeIndex
- sorted chronologically
- checked for missing values
- checked for duplicate dates
- aligned across common trading dates

Separate aligned DataFrames were created for closing prices and trading volume.

### 2. Daily Returns

Daily percentage returns were calculated from closing prices using:

```python
daily_returns = close_prices.pct_change().dropna()
```

The returns were used to calculate:

- average daily return
- daily volatility
- extreme gains and losses
- cumulative performance
- drawdowns
- correlations

### 3. Rolling Volatility

A 20-day rolling volatility measure was calculated for each stock.

Daily volatility was annualized using:

```python
rolling_vol_20 = daily_returns.rolling(20).std() * np.sqrt(252)
```

The average rolling volatility across the four stocks was used as a cross-asset volatility stress proxy.

### 4. Market Regime Classification

Volatility regimes were defined using the 33rd and 67th percentiles of the cross-asset volatility stress proxy.

The regimes were classified as:

- Low Volatility — bottom 33%
- Normal Volatility — middle 34%
- High Volatility — top 33%

This approach allows the regime thresholds to be determined by the historical distribution of the data rather than by arbitrary fixed values.

### 5. Drawdown Analysis

Cumulative growth was calculated using:

```python
cumulative_growth = (1 + daily_returns).cumprod()
```

Running historical peaks were calculated with:

```python
running_peak = cumulative_growth.cummax()
```

Drawdowns were then calculated as:

```python
drawdowns = cumulative_growth / running_peak - 1
```

This measures how far each stock falls below its previous historical peak.

### 6. Correlation Analysis

Correlation matrices were calculated separately for Low, Normal, and High volatility regimes.

This allowed the project to examine whether diversification benefits change during stressed market conditions.

### 7. Trading Volume Analysis

Average and median trading volume were compared across volatility regimes.

The use of both mean and median helps distinguish broad changes in trading activity from isolated extreme-volume events.

### 8. Historical Stress Case Studies

Three major historical stress periods were examined:

- 1987 Market Crash
- 2008–2009 Financial Crisis
- 2020 COVID Crash

For each period, the project analyzed:

- average daily return
- daily volatility
- average drawdown
- worst drawdown
- volatility regime composition

---

## Key Findings

### Volatility

High-volatility regimes produced substantially higher realized volatility across all four stocks.

For example, AAPL daily volatility increased from approximately 1.6% in Low-volatility periods to approximately 3.7% in High-volatility periods.

This suggests that the regime framework successfully separates calm and stressed market environments.

### Returns

High volatility did not always produce negative average returns.

This is because high-volatility periods can contain both severe losses and strong rebound days.

Therefore, volatility measures the magnitude of price movement rather than the direction of returns.

### Drawdowns

Average drawdowns were generally deeper during High-volatility regimes.

However, the single worst drawdown did not always occur during the High-volatility regime.

This occurs because drawdown is path-dependent. A stock may remain far below its previous peak even after volatility has fallen from High to Normal.

### Correlations

Correlations generally increased during High-volatility regimes.

For example:

- AAPL–MSFT correlation increased from approximately 0.32 in the Low regime to approximately 0.45 in the High regime.
- MSFT–XOM correlation increased from approximately 0.16 to approximately 0.37.
- JPM–XOM correlation increased from approximately 0.36 to approximately 0.42.

All six pairwise stock correlations were stronger in the High-volatility regime than in the Low-volatility regime.

This suggests that diversification benefits may weaken during periods of market stress.

### Trading Volume

Average trading volume was highest in the High-volatility regime for all four stocks.

AAPL and MSFT also had their highest median trading volume during High-volatility periods.

For JPM and XOM, mean volume increased during High-volatility regimes while median volume showed a more mixed pattern.

This suggests that extreme-volume days may contribute more strongly to their average trading activity during stressed periods.

---

## Stress-Period Case Studies

### 1987 Market Crash

The selected 1987 period contained 63 trading days.

Regime distribution:

- High: 53 days
- Normal: 10 days
- Low: 0 days

All four stocks produced negative average daily returns during the period.

Worst drawdowns included approximately:

- AAPL: -53%
- MSFT: -51%
- JPM: -50%
- XOM: -33%

The regime model classified most of the period as High volatility, indicating sustained market stress.

### 2008–2009 Financial Crisis

The selected Financial Crisis window contained 146 trading days.

All 146 trading days were classified as High volatility.

JPM experienced the highest daily volatility, at approximately 8%, and one of the deepest drawdowns.

Worst drawdowns included approximately:

- AAPL: -61%
- MSFT: -72%
- JPM: -75%
- XOM: -35%

This was the most consistently stressed period in the regime analysis.

### 2020 COVID Crash

The selected COVID period contained 82 trading days.

Regime distribution:

- High: 65 days
- Normal: 15 days
- Low: 2 days

AAPL and MSFT produced positive average daily returns over the full window, while JPM and XOM produced negative average daily returns.

Worst drawdowns included approximately:

- AAPL: -31%
- MSFT: -28%
- JPM: -44%
- XOM: -62%

This shows that individual assets can react differently during the same market stress event.

---

## Final Research Findings

The project reveals several important patterns.

First, High-volatility regimes are associated with substantially greater realized risk.

Second, drawdowns tend to be deeper when volatility is elevated.

Third, stock correlations increase during stressed conditions, which suggests that diversification may become less effective exactly when investors need it most.

Fourth, trading activity generally increases during High-volatility periods.

Finally, the regime framework identifies major historical stress periods effectively, including the 1987 crash, the 2008–2009 Financial Crisis, and the 2020 COVID shock.

Overall, the analysis suggests that market stress affects more than just volatility. It also changes drawdown behavior, asset co-movement, and trading activity.

---

## Project Structure

```text
regime-aware-equity-analyzer/
│
├── data/
│   ├── AAPL.csv
│   ├── MSFT.csv
│   ├── JPM.csv
│   └── XOM.csv
│
├── notebooks/
│   └── regime_analysis.ipynb
│
├── src/
│   └── analysis.py
│
├── results/
│   ├── regime_summary.csv
│   ├── drawdown_summary.csv
│   ├── average_volume_by_regime.csv
│   ├── median_volume_by_regime.csv
│   └── stress_regime_summary.csv
│
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- pathlib

---

## Skills Demonstrated

This project demonstrates:

- financial time-series analysis
- data cleaning and alignment
- Pandas DataFrame manipulation
- rolling-window calculations
- volatility estimation
- drawdown analysis
- correlation analysis
- regime classification
- trading-volume analysis
- historical stress-event analysis
- research-style interpretation
- reproducible project organization

---

## Limitations

This project has several limitations.

First, the analysis uses only four individual stocks, so the volatility proxy should not be interpreted as a complete measure of the overall market.

Second, the regime classification is based entirely on historical volatility percentiles.

Third, the regime model is descriptive rather than predictive.

Fourth, relationships observed in historical data may not remain stable in future markets.

Finally, the analysis does not yet include transaction costs, portfolio optimization, statistical significance testing, or predictive modeling.

---

## Future Improvements

Future versions of the project could include:

- a larger universe of stocks and ETFs
- S&P 500 or VIX market benchmarks
- rolling correlation analysis
- sector-level regime comparison
- formal statistical significance tests
- SciPy-based optimization
- regression analysis using statsmodels
- machine-learning regime classification
- portfolio allocation strategies that respond dynamically to changing regimes
- interactive visualizations and dashboards

A future extension could also test whether a regime-aware portfolio improves risk-adjusted performance compared with a static portfolio.

---

## Disclaimer

This project is for educational and research purposes only.

The analysis is based on historical market data and should not be interpreted as financial advice, an investment recommendation, or a prediction of future market performance.
# Multi-Asset Portfolio Risk Analysis

A portfolio-risk case study covering Indian equities, NIFTY 50, USD/INR, and silver. The analysis compares volatility models, three Value-at-Risk methods, backtests their assumptions, and explores option Greeks and delta-neutral hedging.

## What we found

- EGARCH produced the strongest volatility-model fit by AIC.
- Historical and Student-t Monte Carlo VaR were more conservative than the parametric approach.
- The 99% VaR backtest found independent exceptions, but its coverage still needed recalibration.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The full analysis and saved outputs are in [`FRAM_Assignment.ipynb`](FRAM_Assignment.ipynb). The public explorer uses those recorded 2019–2024 results, so it does not require a market-data API.

## Stack

Python, pandas, NumPy, SciPy, statsmodels, ARIMA, GARCH-family models, Monte Carlo simulation, and Streamlit.

Built by Rushi Patel, Khush Bhuta, and Daksh Jain.

> Educational case study only—not current market data or investment advice.

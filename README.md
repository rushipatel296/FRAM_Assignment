
# Multi-Asset Portfolio Risk Analysis

## Overview

This project replicates the role of a portfolio risk analyst at a trading or investment firm. We construct and analyze a multi-asset portfolio consisting of equities, an index, FX rate, and a commodity, and then apply advanced risk modeling and hedging techniques.

The workflow covers:
*	Portfolio construction and return analysis
*	Volatility modeling and forecasting (Historical, GARCH-type models)
*	Value-at-Risk (VaR) estimation across different methods
*	Backtesting and model validation
*	Option pricing and Greeks analysis
*	Hedging strategies (Delta/Vega/Diversification hedge)

The final deliverable demonstrates how a risk manager can measure, forecast, and mitigate risks in real-world markets.


## Tools & Libraries
*	Data Sources: Yahoo Finance, Investing.com, RBI Database
*	Languages & Libraries:
	*	Python (Pandas, NumPy, Matplotlib, Seaborn)
	*	Statsmodels (ARIMA, time series analysis)
	*	Arch/GARCH package (Volatility modeling)
	*	Scipy, NumPy Random (Monte Carlo simulation)



## Methodology

1. Asset Selection & Data Preprocessing
	*	Large-cap stock (e.g., INFY, RELIANCE, AAPL)
	*	Market index (e.g., NIFTY 50, S&P 500)
	*	FX Rate (e.g., USD/INR, EUR/USD)
	*	Small-cap stock
	*	Commodity (e.g., Gold, Crude Oil)

    Steps:
      *	Data aligned on common dates, missing values handled via forward-fill.
      *	Log returns computed.
      *	Initial summary statistics (mean, std, skewness, kurtosis).
    


2. Volatility Modeling & Forecasting
	*	Historical Volatility: Rolling-window estimation.
	*	GARCH models:
	*	GARCH(1,1)
	*	EGARCH / GJR-GARCH (asymmetric models)
	*	Model selection via AIC/BIC comparison.
	*	30-day volatility forecast for each asset and portfolio.


3. Value at Risk (VaR)
  Computed at 95% and 99% confidence levels using:
    *	Variance-Covariance Method
    *	Historical Simulation
    *	Monte Carlo Simulation


4. Backtesting & Model Validation
	*	1-day 99% VaR validated using Kupiec Test and Christoffersen Test.
	*	GARCH residuals tested with Ljung-Box for autocorrelation.
	*	Discussion of exceptions and recalibration needs.



5. Option Pricing & Greeks
	*	Simulated Geometric Brownian Motion (GBM) paths.
	*	European call/put option pricing.
	*	Greeks estimated (Δ, Γ, Vega, Θ) and interpreted.
	*	Sensitivity of Greeks across strikes and maturities.


6. Hedging Strategies
	*	Implemented Delta-Neutral Hedging (with dynamic rebalancing).
	*	Alternative strategies (Vega-neutral & diversification hedge) also discussed.
	*	Interpretation of hedge effectiveness.



## Key Deliverables

*	Portfolio return distributions & volatility plots
*	30-day volatility forecasts (GARCH vs Historical)
*	VaR comparison across methods
*	Backtest results with exceptions and p-values
*	Option Greeks analysis & hedging strategy outcomes



## Executive Summary (Business View)

*	Portfolio Profile: 5-asset portfolio spanning equities, FX, and commodities.
*	Risk Findings: Portfolio exhibits volatility clustering; asymmetric models outperform symmetric ones; Monte Carlo VaR provides more conservative estimates.
*	Hedging Recommendation: A delta-neutral hedge combined with diversification provides robust downside protection.
*	Limitations: Limited to 5-year daily data, model assumptions (GBM, normality) may not fully capture extreme market events.


## How to Run
	
1.	Clone the repo
```bash
git clone <repo-link>
cd <repo>
```

2. Install dependencies

```python
pip install -r requirements.txt
```

3. Open notebook
```
jupyter notebook notebooks/Portfolio_Risk_Analysis.ipynb
```


## Contributors

*	Rushi Patel
*	Khush Bhuta
*	Daksh Jain


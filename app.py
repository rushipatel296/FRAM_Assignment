import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Multi-Asset Risk Lab",
    page_icon="📉",
    layout="wide",
)

VAR_RESULTS = pd.DataFrame(
    [
        {
            "Method": "Historical simulation",
            "95% · 1 day": 0.0122,
            "99% · 1 day": 0.0264,
            "95% · 10 days": 0.0387,
            "99% · 10 days": 0.0835,
        },
        {
            "Method": "Parametric",
            "95% · 1 day": 0.0110,
            "99% · 1 day": 0.0161,
            "95% · 10 days": 0.0349,
            "99% · 10 days": 0.0511,
        },
        {
            "Method": "Monte Carlo (Student-t)",
            "95% · 1 day": 0.0129,
            "99% · 1 day": 0.0242,
            "95% · 10 days": 0.0408,
            "99% · 10 days": 0.0767,
        },
    ]
)

ASSETS = [
    "Bharti Airtel",
    "NIFTY 50",
    "USD/INR",
    "BASF India",
    "Silver",
]

st.title("Multi-Asset Risk Lab")
st.caption(
    "A portfolio-risk case study spanning Indian equities, an index, FX, and commodities."
)

st.info(
    "This explorer uses the assignment's saved 2019–2024 results, so it is reproducible "
    "and does not depend on a live market-data API."
)

overview, validation, methodology = st.tabs(
    ["Risk snapshot", "Model validation", "Methodology"]
)

with overview:
    confidence = st.segmented_control("Confidence level", ["95%", "99%"], default="99%")
    horizon = st.segmented_control("Horizon", ["1 day", "10 days"], default="1 day")
    result_column = f"{confidence} · {horizon}"
    view = VAR_RESULTS[["Method", result_column]].copy()
    view["VaR (%)"] = (view.pop(result_column) * 100).round(2)

    metric_cols = st.columns(3)
    for column, (_, row) in zip(metric_cols, view.iterrows()):
        column.metric(row["Method"], f"{row['VaR (%)']:.2f}%")

    st.bar_chart(view.set_index("Method"), horizontal=True)

    st.subheader("What the comparison says")
    st.write(
        "The parametric model reports the lowest tail risk. Historical simulation and the "
        "Student-t Monte Carlo model are more conservative because they better reflect the "
        "heavy-tailed return distribution observed in the notebook."
    )

with validation:
    left, middle, right = st.columns(3)
    left.metric("Portfolio observations", "1,341")
    middle.metric("99% VaR exceptions", "17")
    right.metric("Best volatility model", "EGARCH")

    st.subheader("Diagnostics")
    st.dataframe(
        pd.DataFrame(
            [
                ["Portfolio volatility", "0.925% daily", "Volatility clustering present"],
                ["ARCH test", "p < 0.001", "Conditional heteroskedasticity present"],
                ["Kupiec coverage", "p < 0.001", "Exception rate needs recalibration"],
                ["Violation independence", "p = 0.638", "Exceptions are not clustered"],
            ],
            columns=["Check", "Result", "Interpretation"],
        ),
        hide_index=True,
        width="stretch",
    )
    st.warning(
        "The original backtest rejects the coverage assumption. That is a useful model-risk "
        "finding—not a passing score—and motivates recalibration before production use."
    )

with methodology:
    st.subheader("Equal-weight portfolio")
    st.write(" · ".join(ASSETS))
    st.markdown(
        """
1. Align adjusted closing prices and compute daily log returns.
2. Fit ARIMA residual models, test for conditional heteroskedasticity, and compare GARCH variants.
3. Estimate 95% and 99% VaR with parametric, historical, and Monte Carlo methods.
4. Backtest coverage and independence; simulate option prices, Greeks, and delta-neutral hedges.
"""
    )
    st.caption("Analysis by Rushi Patel, Khush Bhuta, and Daksh Jain.")

st.divider()
st.caption(
    "Educational case study only. Saved historical results are not current prices, investment "
    "advice, or a production risk limit."
)

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Product KPI Dashboard",
    layout="wide"
)

st.title("AI Product KPI Dashboard")
st.write("Milestone 11 — Guided Dashboard Build")

# ============================================================
# STEP 1 — KPI DATA
# ============================================================
# Review the nine PolicyAssist product KPIs.
#
# Students will progressively build the dashboard by adding:
# 1. KPI cards
# 2. Target vs. Actual visualization
# 3. Trend visualization
# 4. Status / threshold logic
# 5. PM decision support
# ============================================================

kpi_data = {
    "KPI": [
        "Policy Search-Time Reduction",
        "Retrieval Accuracy",
        "Answer Accuracy",
        "Hallucination Rate",
        "Citation Correctness",
        "Unsupported-Question Refusal",
        "Response Latency",
        "User Satisfaction",
        "Critical Security Incidents"
    ],
    "Target": [
        50,
        90,
        90,
        2,
        100,
        100,
        10,
        85,
        0
    ],
    "Actual": [
        58,
        92,
        89,
        2.5,
        100,
        95,
        8,
        82,
        0
    ]
}

df = pd.DataFrame(kpi_data)

# ============================================================
# STEP 1 — REVIEW KPI DATA
# ============================================================

st.subheader("KPI Data")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# STEP 2 — KPI CARDS
# ============================================================
# Display each KPI so the PM can quickly assess product health.

st.subheader("Current KPI Performance")

columns = st.columns(3)

for index, row in df.iterrows():
    column = columns[index % 3]

    with column:
        st.metric(
            label=row["KPI"],
            value=row["Actual"],
            delta=f"Target: {row['Target']}"
        )

# ============================================================
# FUTURE BUILD STEPS
# ============================================================
#
# STEP 3 — Target vs. Actual visualization
#
# STEP 4 — Trend visualization
#
# STEP 5 — Status / threshold logic
#
# STEP 6 — Run and review dashboard
#
# STEP 7 — Interpret results
#
# STEP 8 — Make PM decision
# ============================================================

st.info(
    "Next: Add a Target vs. Actual visualization."
)

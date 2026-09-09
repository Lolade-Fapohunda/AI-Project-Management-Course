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
# Your first task is to review and work with the KPI data below.

kpi_data = {
    "KPI": [
        "Policy Search-Time Reduction",
        "Retrieval Accuracy",
        "Answer Accuracy",
        "Hallucination Rate",
        "Citation Correctness",
        "Response Latency"
    ],
    "Target": [
        50,
        90,
        90,
        2,
        100,
        10
    ],
    "Actual": [
        58,
        92,
        89,
        2.5,
        100,
        8
    ]
}

df = pd.DataFrame(kpi_data)

# ============================================================
# STUDENT TASK
# ============================================================
# Step 1: Review the KPI data.
#
# Step 2: Create KPI cards.
#
# Step 3: Add a Target vs. Actual visual.
#
# Step 4: Add a trend visual.
#
# Step 5: Add KPI status / threshold logic.
#
# Step 6: Run and review the dashboard.
#
# Step 7: Interpret the results.
#
# Step 8: Make the PM decision.
# ============================================================

st.subheader("KPI Data")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.info(
    "Next: Build the KPI cards, Target vs. Actual visual, "
    "trend visual, and status logic."
)

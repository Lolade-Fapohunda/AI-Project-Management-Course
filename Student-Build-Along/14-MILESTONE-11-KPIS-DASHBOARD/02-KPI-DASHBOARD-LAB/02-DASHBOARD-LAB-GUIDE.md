# KPI Dashboard Lab

## Objective

Build and interpret a simple Artificial Intelligence (AI) product Key Performance Indicator (KPI) dashboard.

This is an **optional technical Build-Along**.

All students complete the Project Management (PM) analysis in Milestone 11.

You do not need to code to complete the PM portion.

---

# Build Sequence

You will progressively build the dashboard using the provided starter file.

**Watch → Build → Run → Test → Interpret → Document → Decide**

---

## Step 1 — Review the KPI Data

Open:

`01-DASHBOARD-STARTER.py`

Review the provided KPI names, targets, and actual values.

Consider:

* What does each KPI measure?
* Is higher or lower performance better?
* Which KPIs are meeting target?
* Which KPIs are missing target?

### PM Decision

Identify the KPI you would investigate first and explain why.

---

## Step 2 — KPI Cards

Review the KPI cards in the starter application.

The cards provide a quick view of current product performance.

### PM Question

If you had only 30 seconds to assess product health, what would the KPI cards tell you?

---

## Step 3 — Target vs. Actual

Modify the dashboard to add a visual comparison between:

**Target vs. Actual**

### PM Question

Which KPIs are performing above target?

Which KPIs are performing below target?

---

## Step 4 — Trend

Add performance-over-time data and a trend visualization.

### PM Question

Is the product:

* Improving?
* Declining?
* Remaining stable?

Explain the evidence.

---

## Step 5 — Status & Threshold Logic

Add logic that classifies each KPI as:

* **On Target**
* **Needs Attention**
* **Below Threshold**

# KPI Decision Thresholds

Use the following decision rules for the PolicyAssist reference dashboard.

| KPI                          |      Target | On Target | Needs Attention | Below Threshold |
| ---------------------------- | ----------: | --------- | --------------- | --------------- |
| Policy Search-Time Reduction |        ≥50% | ≥50%      | 45%–49.9%       | <45%            |
| Retrieval Accuracy           |        ≥90% | ≥90%      | 81%–89.9%       | <81%            |
| Answer Accuracy              |        ≥90% | ≥90%      | 81%–89.9%       | <81%            |
| Hallucination Rate           |         <2% | <2%       | 2%–2.49%        | ≥2.5%           |
| Citation Correctness         |        100% | 100%      | 90%–99.9%       | <90%            |
| Unsupported-Question Refusal |        100% | 100%      | 90%–99.9%       | <90%            |
| Response Latency             | ≤10 seconds | ≤10 sec   | >10–12.5 sec    | >12.5 sec       |
| User Satisfaction            |        ≥85% | ≥85%      | 76.5%–84.9%     | <76.5%          |
| Critical Security Incidents  |           0 | 0         | 1               | ≥2              |

## How to Apply the Thresholds

### On Target

The KPI meets or exceeds the required performance level.

**PM action:** Continue monitoring.

### Needs Attention

The KPI is outside the target but has not reached the critical threshold.

**PM action:** Investigate the cause, define corrective action, assign an owner, and monitor the KPI more closely.

### Below Threshold

The KPI has reached a level that represents significant product, business, safety, security, or user risk.

**PM action:** Escalate the issue and determine whether the product should be improved, paused, rolled back, or reassessed.

## Important Rule for AI Safety and Security

For **Critical Security Incidents**, the normal performance logic does not apply.

* **0 incidents:** On Target
* **1 incident:** Needs Attention and immediate investigation
* **2 or more incidents:** Below Threshold and escalation required

For safety, security, governance, or compliance issues, the PM should not rely solely on the numerical KPI status. The severity and impact of the incident must also be assessed.

## PM Decision Framework

Use the KPI status together with business context:

**On Target → Continue**

**Needs Attention → Improve**

**Below Threshold → Escalate / Reassess**

The threshold tells the PM **when action is required**. The PM must still determine **what action is appropriate and why**.

Remember that some KPIs are better when the value is **higher**, while others are better when the value is **lower**.

### PM Question

Which KPI requires the most immediate attention?

---

## Step 6 — Run and Test

Run the Streamlit dashboard.

Verify that:

* KPI cards display correctly.
* Target values are correct.
* Actual values are correct.
* Target vs. Actual visualization works.
* Trend information displays correctly.
* Status logic works.
* Threshold conditions are identified correctly.

Document any issues discovered during testing.

---

## Step 7 — Interpret the Dashboard

Review the completed dashboard.

Identify:

* KPIs meeting target
* KPIs missing target
* Improving trends
* Declining trends
* Threshold breaches
* Business risks
* Product risks

Use:

**KPI → Target → Actual → Trend → Threshold → Action**

---

## Step 8 — Make the PM Decision

Use the dashboard evidence to select one:

**Continue → Improve → Escalate → Reassess**

Document:

1. The evidence.
2. The business or product impact.
3. The recommended action.
4. The action owner.
5. The next review point.

---

# Final PM Checkpoint

Answer:

> **What is the product telling us through its KPIs, and what should the PM do about it?**

Your answer should be based on measurable evidence rather than assumptions.

---

# Build-Along Completion Criteria

The technical dashboard is complete when it includes:

* KPI data
* KPI cards
* Target vs. Actual visualization
* Trend visualization
* Status/threshold logic
* PM decision support

The PM portion is complete when you can explain the product's current health and recommend an evidence-based action.

---

# Important

The purpose of this lab is **not** to turn you into a software engineer.

The purpose is to help you understand how an AI product's technical performance data can support:

**Monitoring → Analysis → PM Decision → Corrective Action → Continuous Improvement**

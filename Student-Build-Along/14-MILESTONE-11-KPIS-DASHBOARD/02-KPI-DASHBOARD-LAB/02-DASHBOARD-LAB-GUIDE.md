# KPI Dashboard Lab

## Objective

Build and interpret a simple Artificial Intelligence (AI) product Key Performance Indicator (KPI) dashboard.

This is an optional technical Build-Along.

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

The purpose of this visualization is to make performance gaps easy to identify.

### PM Question

* Which KPIs are performing above target?
* Which KPIs are performing below target?
* Which gaps require further investigation?

---

## Step 4 — Trend

Add performance-over-time data and a trend visualization.

The trend should help the PM determine whether product performance is:

* Improving
* Declining
* Remaining stable

### PM Question

Is the product improving, declining, or remaining stable?

Explain the evidence.

---

## Step 5 — Status & Threshold Logic

Add logic that classifies each KPI as:

* **On Target**
* **Needs Attention**
* **Below Threshold**

Use the **KPI Decision Thresholds** defined in:

**Milestone 11 → Part 1 — KPI Decision Thresholds**

Do not create separate thresholds for the technical lab.

The technical dashboard should implement the same PM decision framework used by all students.

### PM Decision Framework

**On Target → Continue**

**Needs Attention → Improve**

**Below Threshold → Escalate / Reassess**

### PM Question

Which KPI requires the most immediate attention?

Explain your reasoning using the KPI's:

* Target
* Actual performance
* Trend
* Threshold
* Business or product impact

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
* The dashboard provides information that supports PM decision-making.

Document any issues discovered during testing.

---

## Step 7 — Interpret the Dashboard

Review the completed dashboard.

Identify:

* KPIs meeting target.
* KPIs missing target.
* Improving trends.
* Declining trends.
* Threshold breaches.
* Business risks.
* Product risks.

Use:

**KPI → Target → Actual → Trend → Threshold → Action**

Do not simply describe what the dashboard shows.

Explain what the information means for the product.

---

## Step 8 — Make the PM Decision

Use the dashboard evidence to select the appropriate action:

**Continue → Improve → Escalate → Reassess**

Document:

1. The evidence.
2. The business or product impact.
3. The recommended action.
4. The action owner.
5. The next review point.

Your decision should be based on measurable evidence rather than assumptions.

---

# Final PM Checkpoint

Answer:

> What is the product telling us through its KPIs, and what should the PM do about it?

Your answer should connect:

**Performance → Risk → Action → Outcome**

---

# Build-Along Completion Criteria

The technical dashboard is complete when it includes:

* KPI data
* KPI cards
* Target vs. Actual visualization
* Trend visualization
* Status/threshold logic
* PM decision support

The PM portion is complete when you can:

* Explain the product's current health.
* Identify performance gaps.
* Identify meaningful trends.
* Recognize threshold breaches.
* Explain the associated risks.
* Recommend an evidence-based action.

---

# Important

The purpose of this lab is not to turn you into a software engineer.

The purpose is to help you understand how an AI product's technical performance data can support:

**Monitoring → Analysis → PM Decision → Corrective Action → Continuous Improvement**

The technical dashboard is simply a tool for making the PM analysis visible and actionable.

The **PM decision is the outcome — not the code.**

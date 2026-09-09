# Milestone 11 — KPI Dashboard & Monitoring

## PM Objective

Use product performance data to monitor an AI product, identify issues, and make informed Project Management (PM) decisions.

This milestone connects product performance measurement to ongoing product management after release.

---

## What You Will Learn

By completing this milestone, you will learn how to:

* Define and interpret Key Performance Indicators (KPIs).
* Compare actual performance against targets.
* Identify improving and declining trends.
* Recognize performance threshold breaches.
* Determine when corrective action is required.
* Use dashboard evidence to support PM decisions.
* Establish monitoring ownership and review cadence.
* Explain how monitoring continues after product release.
* Connect performance data to continuous improvement.

---

# Part 1 — Everyone: KPI & Dashboard Analysis

**This section is part of the core PM Track and is required for all students.**

No coding is required.

You will analyze an AI product dashboard and use the results to make a Project Management decision.

## Your PM Analysis Process

Use the following sequence:

**KPI → Target → Actual → Trend → Threshold → Action → PM Decision**

### Step 1 — Review Each KPI

For each KPI:

1. Identify what the KPI measures.
2. Review the target.
3. Review the actual performance.
4. Determine whether the KPI is meeting the target.
5. Identify whether performance is improving, declining, or stable.
6. Check whether a decision threshold has been reached.
7. Determine whether corrective action is required.

---

## Step 2 — Compare Actual Performance Against Target

Ask:

* Is the product meeting the required performance target?
* Which KPIs are performing above target?
* Which KPIs are below target?
* Which KPI gaps could affect the product's business outcome?
* Which KPI gaps could create user, security, governance, or operational risk?

Do not assume that every KPI has the same interpretation.

For example:

* Higher retrieval accuracy is generally better.
* Lower hallucination rate is better.
* Lower response latency is better.
* Zero critical security incidents is the required outcome.

---

## Step 3 — Identify Trends

A single KPI measurement provides a snapshot.

A trend provides additional information about product health.

Look for:

* Improving performance
* Declining performance
* Stable performance
* Sudden changes
* Repeated threshold breaches
* Performance that is approaching a threshold

Ask:

> Is the product improving, remaining stable, or becoming less reliable?

---

## Step 4 — Identify Threshold Breaches

A KPI may be below its target without being at a critical level.

Use the decision thresholds below to determine the appropriate PM response.

# KPI Decision Thresholds

| KPI                          |      Target | On Target | Needs Attention | Below Threshold |
| ---------------------------- | ----------: | --------: | --------------: | --------------: |
| Policy Search-Time Reduction |        ≥50% |      ≥50% |       45%–49.9% |            <45% |
| Retrieval Accuracy           |        ≥90% |      ≥90% |       81%–89.9% |            <81% |
| Answer Accuracy              |        ≥90% |      ≥90% |       81%–89.9% |            <81% |
| Hallucination Rate           |         <2% |       <2% |        2%–2.49% |           ≥2.5% |
| Citation Correctness         |        100% |      100% |       90%–99.9% |            <90% |
| Unsupported-Question Refusal |        100% |      100% |       90%–99.9% |            <90% |
| Response Latency             | ≤10 seconds |   ≤10 sec |    >10–12.5 sec |       >12.5 sec |
| User Satisfaction            |        ≥85% |      ≥85% |     76.5%–84.9% |          <76.5% |
| Critical Security Incidents  |           0 |         0 |               1 |              ≥2 |

---

## How to Apply the Thresholds

### On Target

The KPI meets or exceeds the required performance level.

**PM action:** Continue monitoring.

---

### Needs Attention

The KPI is outside the target but has not reached the critical threshold.

**PM action:**

* Investigate the cause.
* Define corrective action.
* Assign an owner.
* Monitor the KPI more closely.
* Determine whether the issue requires escalation.

---

### Below Threshold

The KPI has reached a level that represents significant product, business, safety, security, or user risk.

**PM action:**

* Escalate the issue.
* Determine the root cause.
* Define corrective action.
* Assess product impact.
* Determine whether the product should be improved, paused, rolled back, or reassessed.

---

## Important Rule for AI Safety and Security

For **Critical Security Incidents**:

* **0 incidents:** On Target
* **1 incident:** Needs Attention and immediate investigation
* **2 or more incidents:** Below Threshold and escalation required

For safety, security, governance, or compliance issues, the PM should not rely solely on the numerical KPI status.

The **severity and impact of the issue** must also be assessed.

A single severe security incident may require immediate escalation even if the numerical threshold has not been reached.

---

# PM Decision Framework

Use KPI status together with business and product context.

### On Target → Continue

Continue normal monitoring and product operations.

### Needs Attention → Improve

Investigate the issue and implement corrective action.

### Below Threshold → Escalate / Reassess

Escalate the issue and determine whether the product should be improved, paused, rolled back, or otherwise reassessed.

The threshold tells the PM **when action is required**.

The PM must still determine **what action is appropriate and why**.

---

# PM Deliverable

Complete a short KPI analysis that identifies:

* KPIs meeting their targets.
* KPIs missing their targets.
* Improving or declining trends.
* Threshold breaches.
* Product risks.
* Recommended corrective actions.
* Owners or responsible teams where appropriate.
* Overall PM recommendation.

Your final recommendation should answer:

> **Should the product continue operating as-is, require improvement, or require escalation/reassessment? Why?**

---

# Part 2 — Optional Hands-On Dashboard Build

This section is part of the **optional Student Build-Along**.

Students who choose the hands-on path will use the provided starter dashboard to implement the KPI monitoring concepts from Part 1.

The technical work is intentionally lightweight and PM-focused.

You are **not** expected to become a software engineer or AI engineer.

You will progressively build and test a simple dashboard that helps a PM interpret product performance.

## Build Sequence

**Watch → Build → Run → Test → Interpret → Document → Decide**

---

## Step 1 — Review KPI Data

Open the provided dashboard starter.

Review the nine PolicyAssist product KPIs and understand:

* What each KPI measures.
* The target.
* The actual value.
* Whether higher or lower performance is better.

---

## Step 2 — Create KPI Cards

Display the current KPI values so a PM can quickly assess product health.

The dashboard should make important performance information easy to scan.

---

## Step 3 — Add Target vs. Actual Visualization

Create a visualization that allows the PM to compare:

**Target vs. Actual**

The purpose is not simply to create a chart.

The purpose is to make performance gaps visible so that the PM can identify where action may be required.

---

## Step 4 — Add Trend Visualization

Add a simple trend view where appropriate.

Use the trend to help determine whether performance is:

* Improving
* Declining
* Stable

Trend information should support the PM's interpretation of product health.

---

## Step 5 — Add Status / Threshold Logic

Implement the KPI decision framework from **Part 1 — KPI Decision Thresholds**.

The dashboard should help identify whether each KPI is:

* **On Target**
* **Needs Attention**
* **Below Threshold**

Use the thresholds defined earlier in this milestone rather than creating different thresholds for the technical lab.

---

## Step 6 — Run and Test the Dashboard

Run the dashboard and verify that:

* KPI values display correctly.
* Targets display correctly.
* Target vs. Actual information is understandable.
* Trend information displays correctly where implemented.
* Status logic reflects the defined thresholds.
* The dashboard provides useful information for PM decision-making.

---

## Step 7 — Interpret the Results

Do not stop after the dashboard works technically.

Interpret what the dashboard is telling you.

Ask:

* What is working well?
* What is below target?
* Which KPIs require attention?
* Which thresholds have been breached?
* What risks are emerging?
* What should the PM investigate?
* What corrective action may be required?

---

## Step 8 — Make the PM Decision

Use the dashboard evidence to make a recommendation.

Your decision should follow the framework:

**Continue → Improve → Escalate → Reassess**

Document:

1. The KPI evidence.
2. The problem or risk identified.
3. The recommended action.
4. The responsible owner or team.
5. The expected outcome.
6. The next review point.

---

# Monitoring After Release

KPI monitoring does not end when the product is released.

The PM establishes an ongoing monitoring process.

This should include:

* KPI ownership.
* Monitoring frequency.
* Performance thresholds.
* Alert conditions.
* Review cadence.
* Corrective-action process.
* Escalation process.
* Stakeholder reporting.
* Continuous improvement.

The ongoing management cycle is:

**Measurement → Insight → Decision → Action → Improvement**

---

# PM Checkpoint

Before completing this milestone, confirm that you can answer:

* What are the most important KPIs for the AI product?
* What is the target for each KPI?
* Which KPIs are currently meeting target?
* Which KPIs require attention?
* What constitutes a threshold breach?
* When should the PM investigate?
* When should the PM escalate?
* How should security-related KPI breaches be handled?
* Who owns ongoing KPI monitoring?
* How frequently should KPIs be reviewed?
* What action should occur when performance declines?
* How does KPI monitoring support continuous improvement?

---

# Technical Build-Along Checkpoint

If you are completing the optional hands-on build, confirm that you can:

* Run the dashboard.
* Display KPI data.
* Display KPI cards.
* Compare target vs. actual performance.
* Display trend information where implemented.
* Apply KPI status and threshold logic.
* Interpret the dashboard.
* Document a PM decision.

---

# Key Principle

A dashboard is not the outcome.

**The PM decision is the outcome.**

The purpose of KPI monitoring is to transform product performance data into informed decisions, corrective actions, and continuous improvement.

**Data → Insight → Decision → Action → Improvement**

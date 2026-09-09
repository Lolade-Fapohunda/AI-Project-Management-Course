# Milestone 11 — KPIs, Dashboard & Monitoring

## Objective

In this milestone, you will learn how to use **Key Performance Indicators (KPIs)** and dashboards to monitor an Artificial Intelligence (AI) product after release.

You will use measurable evidence to:

* Assess product health.
* Identify performance gaps.
* Recognize trends.
* Identify risks.
* Determine when action is required.
* Recommend corrective action.
* Support continuous improvement.

The goal is not simply to read a dashboard.

The goal is to use product evidence to make a **Project Management (PM) decision**.

---

# Why KPI Monitoring Matters

An AI product can meet its initial release requirements and still experience performance problems after deployment.

For example:

* Users may become less satisfied.
* Answer accuracy may decline.
* Hallucinations may increase.
* Response times may increase.
* Retrieval quality may deteriorate.
* Security incidents may occur.
* The product may fail to deliver the expected business outcome.

A PM needs a structured way to detect these conditions and determine what to do next.

The monitoring lifecycle is:

**Measure → Analyze → Decide → Act → Monitor Again**

---

# Part 1 — KPI Analysis

## What Is a KPI?

A **Key Performance Indicator (KPI)** is a measurable value used to evaluate whether a product, project, process, or business outcome is performing as expected.

A useful KPI should help answer:

> **How do we know whether the product is working?**

For AI products, KPIs can measure:

* Business outcomes.
* AI quality.
* User experience.
* Operational performance.
* Security.
* Reliability.

---

# PolicyAssist KPI Framework

For the Petadel PolicyAssist reference project, the following KPIs are used.

| KPI                          |      Target | Direction        |
| ---------------------------- | ----------: | ---------------- |
| Policy Search-Time Reduction |        ≥50% | Higher is better |
| Retrieval Accuracy           |        ≥90% | Higher is better |
| Answer Accuracy              |        ≥90% | Higher is better |
| Hallucination Rate           |         <2% | Lower is better  |
| Citation Correctness         |        100% | Higher is better |
| Unsupported-Question Refusal |        100% | Higher is better |
| Response Latency             | ≤10 seconds | Lower is better  |
| User Satisfaction            |        ≥85% | Higher is better |
| Critical Security Incidents  |           0 | Lower is better  |

---

# Target vs. Decision Threshold

Do not treat the KPI target and the decision threshold as the same thing.

## Target

The **target** is the required performance goal.

Example:

**Answer Accuracy ≥90%**

An actual result of 89% means the KPI has **missed its target**.

That does not automatically mean the product has crossed the escalation threshold.

---

## Decision Threshold

The **decision threshold** identifies when performance has deteriorated far enough to require a stronger PM response.

This creates three decision states:

### On Target

The KPI meets the required target.

**PM Action: Continue**

---

### Needs Attention

The KPI has missed the target but remains within the defined attention range.

**PM Action: Improve**

---

### Below Threshold

The KPI has crossed the defined unacceptable-performance threshold.

**PM Action: Escalate / Reassess**

---

# KPI Decision Thresholds

Use the following framework throughout the course.

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

### Important

The direction of the KPI matters.

For **higher-is-better** KPIs, performance deteriorates as the number decreases.

For **lower-is-better** KPIs, performance deteriorates as the number increases.

For example:

* Answer Accuracy of 89% → misses target.
* Hallucination Rate of 2.5% → crosses the unacceptable threshold.
* Response Latency of 11 seconds → misses target but remains within the attention range.
* Response Latency of 13 seconds → crosses the unacceptable threshold.

---

# PM Decision Framework

Use the same framework throughout your AI product lifecycle:

**On Target → Continue**

**Needs Attention → Improve**

**Below Threshold → Escalate / Reassess**

This framework helps prevent two common PM mistakes:

### Mistake 1 — Treating Every Missed Target as a Crisis

A KPI can miss its target without requiring immediate escalation.

The PM should investigate the severity, trend, impact, and decision threshold.

### Mistake 2 — Ignoring a Threshold Breach

A KPI that crosses the unacceptable threshold requires a stronger response.

The PM should not simply record the result and continue normal operations.

---

# Security Exception

Security, safety, privacy, and governance decisions require more than numerical analysis.

For **Critical Security Incidents**:

* **0 incidents** → On Target → Continue monitoring.
* **1 incident** → Needs Attention → Immediate investigation and corrective action.
* **2 or more incidents** → Below Threshold → Escalate / Reassess.

However, severity matters.

A single critical security incident may justify immediate escalation even if the numerical threshold framework would otherwise classify it as Needs Attention.

The PM should assess:

* Severity.
* Scope.
* User impact.
* Data exposure.
* Regulatory or compliance implications.
* Ability to contain the issue.
* Risk of recurrence.

---

# Step 1 — Review KPI Data

Review the KPI values provided in the technical dashboard starter.

Consider:

* What does each KPI measure?
* Is higher or lower performance better?
* Which KPIs meet their target?
* Which KPIs miss their target?
* Which KPIs cross the decision threshold?
* Which KPI could create the greatest business or product impact?

### PM Decision

Identify the KPI you would investigate first.

Explain **why** using measurable evidence.

---

# Step 2 — KPI Cards

KPI cards provide a quick view of current product performance.

Review the KPI cards in the starter dashboard.

### PM Question

If you had only 30 seconds to assess product health:

> **What would the KPI cards tell you?**

Do not simply repeat the numbers.

Identify what the numbers mean for product health.

---

# Step 3 — Target vs. Actual

Modify the dashboard to add a visual comparison between:

**Target vs. Actual**

The purpose of this visualization is to make performance gaps easier to identify.

Consider:

* Which KPIs are performing at or above target?
* Which KPIs are missing target?
* Which KPIs have crossed their decision threshold?
* Which gaps require investigation?
* Which gaps could affect the business outcome?

### PM Question

> **Which performance gaps require action, and why?**

---

# Step 4 — Trend

Add performance-over-time data and a trend visualization.

The trend should help you determine whether product performance is:

* Improving.
* Declining.
* Remaining stable.

A single KPI value provides a snapshot.

A trend provides context.

For example, a KPI that is currently within target may still require investigation if it has deteriorated consistently over several reporting periods.

### PM Question

> **Is the product improving, declining, or remaining stable?**

Explain the evidence supporting your conclusion.

---

# Step 5 — Status and Decision Threshold Logic

Add logic that classifies each KPI as:

* **On Target**
* **Needs Attention**
* **Below Threshold**

Use the **KPI Decision Thresholds** defined in this milestone.

Do not create separate thresholds for the technical dashboard.

The technical dashboard should implement the same PM decision framework used by all students.

### Decision Framework

**On Target → Continue**

**Needs Attention → Improve**

**Below Threshold → Escalate / Reassess**

### PM Question

Which KPI requires the most immediate attention?

Explain your reasoning using:

* Target.
* Actual performance.
* Trend.
* Decision threshold.
* Business impact.
* Product impact.
* Risk.

---

# Step 6 — Run and Test

Run the Streamlit dashboard.

Verify that:

* KPI cards display correctly.
* KPI names are correct.
* Target values are correct.
* Actual values are correct.
* Target vs. Actual visualization works.
* Trend information displays correctly.
* Status logic works.
* Decision threshold conditions are identified correctly.
* Higher-is-better KPIs are evaluated correctly.
* Lower-is-better KPIs are evaluated correctly.
* Security conditions are handled appropriately.
* The dashboard supports PM decision-making.

Document any issues discovered during testing.

---

# Step 7 — Interpret the Dashboard

Review the completed dashboard.

Identify:

* KPIs meeting target.
* KPIs missing target.
* KPIs in the Needs Attention range.
* KPIs crossing the Below Threshold boundary.
* Improving trends.
* Declining trends.
* Stable trends.
* Business risks.
* Product risks.
* Operational risks.

Use:

**KPI → Target → Actual → Trend → Threshold → Action**

Do not simply describe what the dashboard shows.

Explain what the information means for the product.

---

# Step 8 — Make the PM Decision

Use the dashboard evidence to select the appropriate action:

**Continue → Improve → Escalate → Reassess**

Document:

1. The evidence.
2. The business or product impact.
3. The risk.
4. The recommended action.
5. The action owner.
6. The next review point.

Your decision should be based on measurable evidence rather than assumptions.

---

# PM Decision Example

Suppose:

* Answer Accuracy target = ≥90%.
* Actual Answer Accuracy = 89%.
* Below Threshold = <81%.

The correct interpretation is:

**Target missed → Needs Attention → Improve**

The KPI has not crossed the Below Threshold boundary.

Now suppose:

* Hallucination target = <2%.
* Actual Hallucination Rate = 2.5%.
* Below Threshold = ≥2.5%.

The correct interpretation is:

**Threshold breached → Below Threshold → Escalate / Reassess**

This distinction is important.

---

# Optional Technical Build-Along

The technical dashboard activity is optional.

All students complete the PM analysis.

You may also build the dashboard implementation using the provided starter file.

The technical build follows:

**Watch → Build → Run → Test → Interpret → Document → Decide**

The purpose of the technical activity is not to turn you into a software engineer.

It is to help you understand how technical product data can support PM decision-making.

---

# KPI Dashboard Lab

If you choose the technical Build-Along, open:

`01-DASHBOARD-STARTER.py`

You will progressively build the dashboard by adding:

* KPI data.
* KPI cards.
* Target vs. Actual visualization.
* Trend visualization.
* Status logic.
* Decision threshold logic.
* PM decision support.

The technical dashboard should use the same KPI targets and decision thresholds defined in this milestone.

Do not invent separate thresholds.

---

# PM Analysis vs. Technical Build

The PM analysis and technical dashboard serve different purposes.

### PM Analysis

You determine:

* What the KPI means.
* Whether performance meets the target.
* Whether the KPI requires attention.
* Whether the decision threshold has been crossed.
* What action should be taken.
* Who owns the action.
* When the result should be reviewed again.

### Technical Dashboard

The dashboard makes that information visible.

It may display:

* KPI cards.
* Charts.
* Trends.
* Status indicators.
* Threshold conditions.

The dashboard supports the PM decision.

**The PM decision is the outcome — not the code.**

---

# Monitoring After Release

Monitoring does not stop after the initial release.

After deployment, the PM should establish an ongoing monitoring cycle.

A monitoring process should define:

* KPI owner.
* Data source.
* Reporting frequency.
* Target.
* Decision threshold.
* Review cadence.
* Escalation process.
* Corrective-action process.

---

# Continuous Improvement

Monitoring should lead to action.

When performance changes, the PM should determine:

1. What changed?
2. Why did it change?
3. How significant is the change?
4. What is the business or product impact?
5. Does the issue require corrective action?
6. Who owns the action?
7. When will the result be reviewed?
8. Did the corrective action improve the KPI?

The cycle becomes:

**Monitor → Identify → Analyze → Improve → Re-measure**

---

# Final PM Checkpoint

Answer:

> **What is the product telling us through its KPIs, and what should the PM do about it?**

Your answer should connect:

**Performance → Risk → Action → Outcome**

Do not answer with a list of KPI values.

Make a PM decision.

---

# Milestone Completion Criteria

## PM Portion

The PM portion is complete when you can:

* Explain the purpose of each KPI.
* Identify whether higher or lower performance is better.
* Compare actual performance against the target.
* Distinguish a missed target from a threshold breach.
* Identify meaningful trends.
* Recognize decision threshold breaches.
* Explain associated business and product risks.
* Recommend an evidence-based action.
* Identify an action owner.
* Establish a follow-up review point.
* Explain how monitoring supports continuous improvement.

## Technical Build-Along

The optional technical dashboard is complete when it includes:

* KPI data.
* KPI cards.
* Target vs. Actual visualization.
* Trend visualization.
* Status logic.
* Decision threshold logic.
* PM decision support.

---

# Key Takeaways

Remember:

### Target

**What performance are we trying to achieve?**

### Decision Threshold

**When does performance become unacceptable enough to require escalation or reassessment?**

### KPI

**What measurable evidence tells us how the product is performing?**

### Dashboard

**How do we make that evidence visible and actionable?**

### PM Decision

**What should we do based on the evidence?**

---

# Final Principle

A dashboard is not the decision.

A KPI is not the action.

A PM uses evidence to understand product health, identify risk, determine the appropriate response, and drive the next action.

**Measure → Analyze → Decide → Act → Monitor Again**

The objective is not simply to know whether an AI product is performing.

The objective is to know **what the evidence means and what the PM should do about it.**

# Milestone 11 — KPIs & Dashboard

## PM Objective

Use Key Performance Indicators (KPIs) and dashboards to determine whether an AI project is being delivered effectively and whether the AI product is achieving its intended business, user, and performance outcomes.

## Hands-On Objective

Design a practical KPI framework for PolicyAssist that connects measurable performance to Project Management (PM) decisions.

You will learn how to move from:

**KPI → Target → Actual → Trend → Threshold → Action**

You will create two views:

1. **Project / Delivery Dashboard**
2. **AI Product Performance Dashboard**

You do not need to build a technically sophisticated dashboard to complete this milestone.

The goal is to demonstrate that you can define meaningful KPIs, interpret performance, identify issues, and recommend actions.

---

# Section 1: Understand What a KPI Does

A Key Performance Indicator (KPI) is a measurable indicator used to understand whether an important objective is being achieved.

A good KPI should help answer a meaningful management question.

For example:

> **Are employees finding policy information faster?**

A KPI might measure:

> **Average Policy Search Time**

The KPI alone is not enough.

You also need:

**Target:** What level of performance do we expect?

**Actual:** What performance did we observe?

**Trend:** Is performance improving, declining, or remaining stable?

**Threshold:** When does the result require attention or action?

**Action:** What should the PM or team do in response?

---

# Section 2: Build the KPI Logic

Use the following model throughout this milestone:

**KPI → Target → Actual → Trend → Threshold → Action**

### Example

**KPI:** Average Policy Response Time

**Target:** ≤ 10 seconds

**Actual:** 8.7 seconds

**Trend:** Improving

**Threshold:** > 10 seconds

**Action:** Investigate performance and determine whether corrective action is required.

The value of the KPI is not simply the number.

The value comes from what the number tells you and what decision it supports.

---

# Section 3: Separate Delivery KPIs from Product KPIs

A Project / Delivery Dashboard and an AI Product Performance Dashboard answer different questions.

## Project / Delivery Dashboard

This dashboard answers:

> **Are we delivering the project effectively?**

Examples include:

* Milestone completion.
* Schedule performance.
* Requirements completion.
* Open defects.
* Risk status.
* UAT completion.
* Release readiness.
* Planned versus actual work.
* Delivery dependencies.

## AI Product Performance Dashboard

This dashboard answers:

> **Is the AI product performing as intended?**

Examples include:

* Response accuracy.
* Retrieval accuracy.
* Unsupported response rate.
* Citation performance.
* Response time.
* User satisfaction.
* Escalation rate.
* Usage or adoption.
* Policy search time reduction.

Do not combine project delivery and AI product performance into one score.

They measure different aspects of success.

---

# Section 4: Start With Business Outcomes

Return to the business outcomes established earlier in the Build-Along.

For PolicyAssist, consider outcomes such as:

* Reduce employee time spent searching for policy information.
* Reduce repetitive policy questions directed to Human Resources (HR).
* Improve access to accurate, current, authoritative policy information.
* Improve employee confidence in policy answers.

Ask:

> **What evidence would show that the product is actually creating these outcomes?**

Complete:

| Business Outcome               | What Should Change? | Possible KPI | Why It Matters |
| ------------------------------ | ------------------- | ------------ | -------------- |
| Reduce policy search time      |                     |              |                |
| Reduce repetitive HR questions |                     |              |                |
| Improve answer quality         |                     |              |                |
| Improve employee confidence    |                     |              |                |

---

# Section 5: Define AI Product KPIs

Create at least **six AI Product KPIs**.

Use the evidence and requirements from earlier milestones where possible.

Consider:

* Response accuracy.
* Retrieval accuracy.
* Unsupported response rate.
* Citation accuracy.
* Citation support.
* Response time.
* User satisfaction.
* Escalation rate.
* Policy search time.
* HR question reduction.

For each KPI, define:

| KPI | Definition | Target | Data Source | Frequency | Decision Supported |
| --- | ---------- | -----: | ----------- | --------- | ------------------ |
|     |            |        |             |           |                    |
|     |            |        |             |           |                    |
|     |            |        |             |           |                    |
|     |            |        |             |           |                    |
|     |            |        |             |           |                    |
|     |            |        |             |           |                    |

A KPI should have a clear definition.

Avoid vague KPIs such as:

* "AI quality"
* "Good user experience"
* "System works well"

Define exactly what is being measured.

---

# Section 6: Use Existing PolicyAssist Targets

Use the targets established earlier in the Build-Along where they apply.

Examples include:

| KPI                        | PolicyAssist Target |
| -------------------------- | ------------------: |
| Response Accuracy          |               ≥ 90% |
| Retrieval Accuracy         |               ≥ 90% |
| Unsupported Response Rate  |                < 2% |
| Response Time              |        ≤ 10 seconds |
| Citation Presence          |                100% |
| Citation Accuracy          |               ≥ 95% |
| Citation Support           |               ≥ 95% |
| Authorization Issues       |                   0 |
| Confidential Data Exposure |                   0 |

Use the relevant target for each KPI.

Do not create a target simply because a number is easy to measure.

A target should connect to a business requirement, user expectation, risk tolerance, or agreed quality standard.

---

# Section 7: Establish Baselines

A target describes where you want to be.

A baseline describes where you are starting.

Ask:

> **What was the performance before improvement?**

For each KPI, determine whether a baseline is available.

| KPI | Baseline Available? | Baseline | Target | Gap |
| --- | ------------------- | -------: | -----: | --: |
|     |                     |          |        |     |
|     |                     |          |        |     |
|     |                     |          |        |     |
|     |                     |          |        |     |

### Important

Do not invent a baseline.

If a real baseline is unavailable:

* Record that the baseline is unavailable.
* Identify how it should be collected.
* Do not present an invented value as actual performance.

For example, if the goal is to reduce employee policy search time by 50 percent but no pre-PolicyAssist search-time data exists, identify the required baseline measurement rather than making up a starting number.

---

# Section 8: Define Actual Performance

Use actual evidence from the Build-Along where appropriate.

Examples may include:

* Milestone 6 retrieval test results.
* Milestone 7 AI evaluation results.
* Milestone 8 security findings.
* Milestone 9 UAT results.
* Milestone 10 deployment validation results.

Record:

| KPI | Target | Actual | Source of Actual | Date / Period | Status |
| --- | -----: | -----: | ---------------- | ------------- | ------ |
|     |        |        |                  |               |        |
|     |        |        |                  |               |        |
|     |        |        |                  |               |        |
|     |        |        |                  |               |        |
|     |        |        |                  |               |        |
|     |        |        |                  |               |        |

### Important

Clearly label whether the actual is:

**Prototype / Test Result**

or

**Production / Operational Result**

Do not present a small prototype test as though it were enterprise-wide production performance.

---

# Section 9: Analyze Trends

A single KPI value is only a snapshot.

A trend shows how performance changes over time or across repeated measurements.

Use:

* Improving.
* Stable.
* Declining.
* Not Enough Data.

For each KPI, identify the trend.

| KPI | Previous Result | Current Result | Trend | Interpretation |
| --- | --------------: | -------------: | ----- | -------------- |
|     |                 |                |       |                |
|     |                 |                |       |                |
|     |                 |                |       |                |
|     |                 |                |       |                |

Ask:

> **Is performance moving toward or away from the target?**

Do not label a result as improving or declining when there is insufficient evidence.

---

# Section 10: Define Thresholds

A threshold identifies when a KPI requires attention.

A threshold may represent:

* Warning level.
* Critical level.
* Required intervention point.

For example:

**Target:** Response time ≤ 10 seconds

**Warning:** > 8 seconds

**Critical:** > 10 seconds

The threshold should lead to a defined action.

Create thresholds for at least **four important KPIs**.

| KPI | Target | Warning Threshold | Critical Threshold | Required Action |
| --- | -----: | ----------------: | -----------------: | --------------- |
|     |        |                   |                    |                 |
|     |        |                   |                    |                 |
|     |        |                   |                    |                 |
|     |        |                   |                    |                 |

A threshold is useful only when someone knows what to do when it is crossed.

---

# Section 11: PolicyAssist Decision Thresholds

Use the following PolicyAssist decision thresholds for the KPI dashboard where applicable.

| KPI                                       |   Target | Attention Range | Below Threshold / Critical |
| ----------------------------------------- | -------: | --------------: | -------------------------: |
| Policy Search-Time Reduction              |     ≥50% |        45–49.9% |                       <45% |
| Retrieval Accuracy                        |     ≥90% |        81–89.9% |                       <81% |
| Answer Accuracy                           |     ≥90% |        81–89.9% |                       <81% |
| Unsupported / Hallucinated Response Rate  |      <2% |         2–2.49% |                      ≥2.5% |
| Citation Correctness                      |     100% |        90–99.9% |                       <90% |
| Unsupported-Question Refusal / Escalation |     100% |        90–99.9% |                       <90% |
| Response Latency                          | ≤10 sec. |   >10–12.5 sec. |                 >12.5 sec. |
| User Satisfaction                         |     ≥85% |      76.5–84.9% |                     <76.5% |
| Critical Security Incidents               |        0 |               1 |                         ≥2 |

For security metrics, consider severity and the nature of the incident in addition to the numerical result.

A serious security or authorization failure may require immediate escalation even when other KPIs are performing well.

---

# Section 12: Connect KPI Results to Actions

A dashboard should support decisions, not simply display numbers.

Choose at least **three KPI conditions** and define the PM action.

Examples:

### Condition

Response accuracy falls below target.

### PM Action

Review failed scenarios, determine whether the issue relates to data, retrieval, prompting, or another product factor, and initiate corrective action.

Complete:

| KPI Condition | What Does It Tell You? | PM Action | Owner | Expected Outcome |
| ------------- | ---------------------- | --------- | ----- | ---------------- |
|               |                        |           |       |                  |
|               |                        |           |       |                  |
|               |                        |           |       |                  |

---

# Section 13: Build the Project / Delivery Dashboard

Create a **Project / Delivery Dashboard** containing at least **five delivery KPIs**.

Consider:

* Milestone completion.
* Schedule status.
* Requirements completion.
* Open defects.
* High-priority risks.
* UAT status.
* Release readiness.
* Outstanding dependencies.

Use:

| KPI | Target | Actual | Trend | Threshold | Action |
| --- | -----: | -----: | ----- | --------- | ------ |
|     |        |        |       |           |        |
|     |        |        |       |           |        |
|     |        |        |       |           |        |
|     |        |        |       |           |        |
|     |        |        |       |           |        |

The dashboard should allow a PM or stakeholder to quickly understand:

> **Are we on track?**

---

# Section 14: Build the AI Product Performance Dashboard

Create an **AI Product Performance Dashboard** containing at least **six product KPIs**.

Consider:

* Response Accuracy.
* Retrieval Accuracy.
* Unsupported Response Rate.
* Citation Accuracy.
* Citation Support.
* Response Time.
* User Satisfaction.
* Escalation Rate.
* Policy Search Time.

Use:

| KPI                       |    Target | Actual | Trend | Threshold | Action |
| ------------------------- | --------: | -----: | ----- | --------- | ------ |
| Response Accuracy         |     ≥ 90% |        |       |           |        |
| Retrieval Accuracy        |     ≥ 90% |        |       |           |        |
| Unsupported Response Rate |      < 2% |        |       |           |        |
| Citation Accuracy         |     ≥ 95% |        |       |           |        |
| Citation Support          |     ≥ 95% |        |       |           |        |
| Response Time             | ≤ 10 sec. |        |       |           |        |

Add other KPIs when they provide meaningful value.

The dashboard should allow a PM or product stakeholder to quickly understand:

> **Is the AI product performing as intended?**

---

# Section 15: Interpret the Dashboard

Review both dashboards together.

Ask:

## Project Performance

Is the project being delivered as planned?

## Product Performance

Is the AI product performing as intended?

## Business Outcome

Is the product creating the expected value?

A project can be on schedule while the AI product is underperforming.

An AI product can perform well technically while the overall project is behind schedule.

Strong performance in one dashboard does not automatically mean overall success.

Record your interpretation:

| Area               | Finding | Evidence | PM Implication |
| ------------------ | ------- | -------- | -------------- |
| Project / Delivery |         |          |                |
| AI Product         |         |          |                |
| Business Outcome   |         |          |                |

---

# Section 16: Prepare an Executive Performance Summary

A dashboard should support communication with leadership and stakeholders.

Create a short executive summary containing:

**Overall Status:**

[Your assessment]

**Top Positive Result:**

[Most important success]

**Top Concern:**

[Most important issue]

**Business Impact:**

[Why it matters]

**Recommended Action:**

[What should happen next]

**Decision Needed:**

[Decision or support required from leadership]

Keep the summary focused on decisions and business implications rather than technical details.

---

# Section 17: Define Monitoring and Continuous Improvement

KPI monitoring should continue after release.

Identify at least **three KPIs that should be monitored on an ongoing basis**.

For each KPI, define:

* Owner.
* Review frequency.
* Threshold.
* Required action.
* Escalation path.

Use:

| KPI | Owner | Review Frequency | Threshold | Action | Escalation |
| --- | ----- | ---------------- | --------- | ------ | ---------- |
|     |       |                  |           |        |            |
|     |       |                  |           |        |            |
|     |       |                  |           |        |            |

Then answer:

> **What should happen when a KPI repeatedly misses its target?**

Consider:

* Root Cause Analysis (RCA).
* Corrective action.
* Backlog prioritization.
* Additional testing.
* Process change.
* Product improvement.
* Governance review.

---

# Section 18: Make PM Decisions From the Dashboard

Use the dashboard results to make at least **three PM decisions**.

Your decisions should be based on evidence.

Examples:

* Continue current approach.
* Investigate declining performance.
* Prioritize a corrective action.
* Add a backlog item.
* Increase testing.
* Change a threshold.
* Reassess a target.
* Escalate a risk.
* Hold a release or enhancement.
* Increase monitoring.

Record:

| PM Decision | KPI Evidence | Business Reason | Risk / Opportunity | Action |
| ----------- | ------------ | --------------- | ------------------ | ------ |
|             |              |                 |                    |        |
|             |              |                 |                    |        |
|             |              |                 |                    |        |

---

# Section 19: Technical Dashboard Implementation

If you are following the PolicyAssist technical Build-Along, you may implement your dashboards using the tools available to you.

Your technical dashboard may display:

* KPI values.
* Targets.
* Actuals.
* Trends.
* Thresholds.
* Status indicators.
* Actions or recommendations.

Technical implementation is optional for understanding the PM concepts.

Your dashboard should not display invented production results.

When using prototype or test data, clearly label the data source and context.

---

# Deliverable: KPI & Dashboard Package

Create a **KPI & Dashboard Package** containing:

## Project / Delivery Dashboard

At least five delivery KPIs showing:

* KPI.
* Definition.
* Target.
* Actual.
* Trend.
* Threshold.
* Action.

## AI Product Performance Dashboard

At least six AI product KPIs showing:

* KPI.
* Definition.
* Target.
* Actual.
* Trend.
* Threshold.
* Action.

## Supporting KPI Framework

Include:

* Business outcomes.
* KPI definitions.
* Data sources.
* Baselines where available.
* Monitoring frequency.
* KPI owners.
* Thresholds.
* PM actions.

## Executive Performance Summary

Include:

* Overall status.
* Top positive result.
* Top concern.
* Business impact.
* Recommended action.
* Decision needed.

## PM Decisions

Include at least three evidence-based decisions supported by KPI results.

---

# PM Checkpoint

Before moving forward, you should be able to answer:

> **Are we delivering the project effectively, is the AI product performing as intended, and what should the PM do about the results?**

You should also be able to explain:

* What makes a KPI meaningful.
* The difference between a KPI, target, actual, trend, threshold, and action.
* The difference between a Project / Delivery KPI and an AI Product KPI.
* How to establish and use a baseline.
* Why actual results must be supported by evidence.
* How to interpret trends.
* How thresholds trigger action.
* Why dashboards should support decisions rather than simply display numbers.
* How AI product performance differs from project delivery performance.
* How KPI monitoring supports continuous improvement.
* How to communicate performance to executives and stakeholders.

---

# PM Perspective

**A dashboard is not a collection of numbers. It is a decision-making tool.**

The PM's job is not simply to report performance.

The PM must understand:

**What is the target?**

**What is the actual result?**

**What is the trend?**

**Has a threshold been crossed?**

**Why is performance changing?**

**What action is required?**

**Who needs to know or decide?**

The progression is:

**KPI → Target → Actual → Trend → Threshold → Action → PM Decision**

You have now moved from building and validating the AI product to measuring whether the project and product are actually delivering value.

The next milestone will focus on **Milestone 12: Capstone & Portfolio**, where you will bring your work together into a professional demonstration of your AI Project Management capabilities.

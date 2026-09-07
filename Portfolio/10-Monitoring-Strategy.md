# 10: Monitoring Strategy

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Decision Area:** Monitoring & Continuous Improvement

---

# Purpose

This artifact demonstrates how the AI Project Manager will monitor PolicyAssist after release and use production evidence to identify issues, manage incidents, prioritize improvements, and maintain AI quality over time.

Production release is not the end of the project lifecycle.

AI systems can change because of:

* New or changed policies.
* Model changes.
* Data changes.
* User behavior.
* Retrieval changes.
* Application changes.
* Performance changes.
* Emerging risks.

---

# Monitoring Objective

The monitoring strategy must determine whether PolicyAssist continues to:

* Provide accurate answers.
* Retrieve appropriate evidence.
* Ground responses in authoritative information.
* Provide correct citations.
* Refuse unsupported questions safely.
* Protect authorized information.
* Meet performance expectations.
* Provide an acceptable user experience.
* Support the intended business outcome.

---

# Monitoring Vs. Evaluation

### Evaluation

Evaluation is structured measurement performed against a controlled evaluation dataset.

It asks:

> "How does the system perform under defined test conditions?"

### Monitoring

Monitoring observes the system during actual use.

It asks:

> "How is the system performing in production, and is anything changing?"

Evaluation and monitoring support each other.

---

# Monitoring Categories

PolicyAssist monitoring should cover:

1. AI Quality
2. Retrieval
3. Grounding
4. Citations
5. Unsupported Questions
6. Performance
7. Security
8. Knowledge Changes
9. User Feedback
10. Incidents
11. Business Outcomes
12. Cost / Resource Utilization

---

# Key Production Metrics

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |
| User Satisfaction            |        ≥ 85% |
| Critical Security Incidents  |            0 |
| Unauthorized Policy Access   |            0 |

These targets provide the baseline for production monitoring.

---

# Retrieval Monitoring

Monitor whether the system continues to retrieve appropriate policy evidence.

Potential indicators include:

* Retrieval success rate.
* Relevant evidence retrieved.
* Retrieval failures.
* Low-confidence retrieval.
* Policy category performance.
* Multi-policy retrieval performance.
* Changes in retrieval behavior after knowledge updates.

A decline in retrieval quality may indicate:

* New documents.
* Poor metadata.
* Duplicate content.
* Changed document structure.
* Embedding changes.
* Retrieval configuration changes.

---

# Answer Quality Monitoring

Monitor:

* Answer accuracy.
* Unsupported claims.
* Incomplete responses.
* Incorrect interpretation.
* User-reported incorrect answers.
* Repeated correction requests.

Production feedback should be evaluated rather than automatically treated as proof that the model failed.

---

# Grounding Monitoring

The project should periodically review whether responses remain supported by retrieved evidence.

A grounding review should ask:

* Was appropriate evidence retrieved?
* Does the response reflect that evidence?
* Did the model introduce unsupported information?
* Was the source authoritative?
* Was the source active?
* Was the source appropriate for the user?

---

# Citation Monitoring

PolicyAssist should monitor citation quality.

Two conditions must be distinguished:

### Citation Presence

A source citation appears.

### Citation Correctness

The cited source actually supports the response.

The production target is:

**Citation Correctness = 100%**

An incorrect citation is a significant trust and governance issue.

---

# Unsupported-Question Monitoring

PolicyAssist must safely handle questions where sufficient evidence is unavailable.

Monitor:

* Unsupported-question refusal rate.
* False answers to unsupported questions.
* User attempts to obtain unsupported information.
* Repeated refusal patterns.
* New question categories that are not covered by the knowledge base.

A refusal can be correct behavior.

The concern is not simply the number of refusals.

The concern is whether the system refuses when it should and answers when it should.

---

# Performance Monitoring

Monitor:

* Response latency.
* Error rate.
* Timeout rate.
* Processing failures.
* System availability.
* Resource utilization.

The primary response target is:

**≤ 10 seconds**

Performance should be reviewed under realistic production conditions.

---

# Security Monitoring

Monitor:

* Unauthorized access attempts.
* Access-control failures.
* Sensitive information exposure.
* Suspicious query patterns.
* Prompt-injection attempts.
* Data leakage indicators.
* Security incidents.

Critical security incidents should trigger immediate escalation.

---

# Knowledge Change Monitoring

Policy information changes over time.

The PM should establish a process for detecting:

* New policies.
* Updated policies.
* Superseded policies.
* Archived policies.
* Expired policies.
* Ownership changes.
* Approval changes.
* Authority changes.

A material policy change should trigger appropriate validation and knowledge-base updates.

---

# Model Change Monitoring

Model changes can affect system behavior.

Examples include:

* New model version.
* Updated model configuration.
* Prompt changes.
* Embedding-model changes.
* Retrieval changes.
* Application logic changes.

Material model or system changes should trigger:

* Impact assessment.
* Evaluation.
* Regression testing.
* UAT when appropriate.
* Approval.
* Documentation.

---

# Data Drift

Data drift occurs when the information used by the system changes over time.

For PolicyAssist, this may include:

* New policy categories.
* Changes in terminology.
* Significant document growth.
* Changes in document structure.
* Increased duplicates.
* New departments or business areas.

The PM should determine whether the existing system continues to support the changed information environment.

---

# User Feedback

User feedback can reveal problems that controlled testing did not identify.

Examples:

> "The answer is technically correct, but I cannot understand it."

> "The citation does not contain the information described."

> "The system keeps refusing this type of question."

> "The response takes too long."

Feedback should be categorized.

Possible categories:

* Defect.
* Enhancement.
* Training issue.
* Data issue.
* Usability issue.
* Knowledge gap.
* Security concern.

---

# Feedback Vs. Defects

Not every complaint is automatically a defect.

The PM should determine:

* What happened?
* What was expected?
* Is the behavior a requirement failure?
* Is the behavior documented?
* Is the issue reproducible?
* What is the business impact?
* Does it require immediate action?

This prevents the backlog from becoming an unstructured collection of complaints.

---

# Incident Management

An AI incident may involve:

* Incorrect critical information.
* Unauthorized disclosure.
* Security failure.
* Major performance degradation.
* Widespread incorrect responses.
* Knowledge-base corruption.
* Production outage.

The PM should establish:

1. Detection.
2. Triage.
3. Severity.
4. Ownership.
5. Containment.
6. Investigation.
7. Communication.
8. Resolution.
9. Verification.
10. Closure.

---

# Root-Cause Analysis

Production failures should be investigated across the entire system.

Possible root causes include:

```text id="w6j8tz"
Data
  ↓
Document Processing
  ↓
Retrieval
  ↓
Prompt / Application Logic
  ↓
Model
  ↓
Response Handling
  ↓
User Interface
```

The PM should avoid assuming every AI failure is a model failure.

---

# Continuous Improvement Loop

The production improvement process is:

```text id="p7a2cx"
Monitor
   ↓
Identify Problem
   ↓
Create Backlog Item
   ↓
Prioritize
   ↓
Develop
   ↓
Test
   ↓
Evaluate
   ↓
UAT
   ↓
Release
   ↓
Monitor
```

This connects production learning to controlled product improvement.

---

# Backlog Prioritization

Monitoring findings should be prioritized using:

* Business impact.
* User impact.
* Security impact.
* Compliance impact.
* Frequency.
* Severity.
* Effort.
* Dependencies.
* Strategic value.

Security and critical business risks should receive higher priority than cosmetic improvements.

---

# Technical Debt

Technical debt may develop when teams make short-term implementation decisions.

Examples:

* Temporary retrieval rules.
* Manual data processes.
* Incomplete monitoring.
* Hard-coded configurations.
* Limited test coverage.
* Manual policy updates.

The PM should ensure important technical debt is visible and tracked.

---

# Performance And Cost Monitoring

The PM should monitor whether system performance remains acceptable as usage changes.

Consider:

* Number of users.
* Query volume.
* Processing time.
* Infrastructure usage.
* Model usage.
* Storage.
* Operational cost.

An increase in usage may create new technical or financial constraints.

---

# Business Outcome Monitoring

Technical metrics are not enough.

The PM should determine whether PolicyAssist continues to achieve its business objective.

The original business target includes:

**Reduce employee policy-search time by 50%.**

Potential business indicators include:

* Average policy-search time.
* Successful task completion.
* User satisfaction.
* Search abandonment.
* Support requests related to policy questions.
* Repeated searches.
* Escalations.

---

# Monitoring Ownership

Monitoring responsibilities should be clearly assigned.

| Area              | Primary Responsibility          |
| ----------------- | ------------------------------- |
| AI Quality        | AI / Product Team               |
| Retrieval         | Technical Team                  |
| Data / Knowledge  | Data / Policy Owner             |
| Security          | Security Team                   |
| Performance       | Technical / Infrastructure Team |
| User Feedback     | Product / Support Team          |
| Business Outcomes | Business Owner                  |
| Risk              | Project / Governance Team       |
| Release Decisions | Authorized Governance Authority |

The PM coordinates across these responsibilities and ensures unresolved issues have clear ownership.

---

# Production Review

A regular production review should examine:

* Metric trends.
* Threshold breaches.
* Incidents.
* Defects.
* User feedback.
* Knowledge changes.
* Security findings.
* Model changes.
* Backlog priorities.
* Business outcomes.

The review cadence should be defined by project risk and organizational requirements.

---

# Monitoring Alerts

Alerts should be triggered when defined thresholds are breached.

Examples:

* Hallucination ≥ 2%.
* Citation correctness < 100%.
* Retrieval accuracy < 90%.
* Answer accuracy < 90%.
* Latency exceeds 10 seconds.
* Unauthorized access detected.
* Critical security incident detected.
* User satisfaction falls below 85%.
* Authority conflict detected.

Alerts should have:

* Owner.
* Severity.
* Response procedure.
* Escalation path.
* Resolution criteria.

---

# Production Monitoring Scenario

After three months in production, PolicyAssist reports:

| Metric                      | Result |       Target |
| --------------------------- | -----: | -----------: |
| Retrieval Accuracy          |    89% |        ≥ 90% |
| Answer Accuracy             |    91% |        ≥ 90% |
| Hallucination Rate          |   2.3% |         < 2% |
| Citation Correctness        |    99% |         100% |
| Responses ≤ 10 Seconds      |    93% | Target ≥ 95% |
| User Satisfaction           |    82% |        ≥ 85% |
| Critical Security Incidents |      0 |            0 |

Additional findings:

* One unresolved policy authority conflict exists.
* User complaints are increasing.
* Multi-policy questions remain a common source of complaints.

---

# Scenario Analysis

The PM should identify:

### Failed Targets

* Retrieval Accuracy.
* Hallucination Rate.
* Citation Correctness.
* Performance target.
* User Satisfaction.

### Passing Target

* Answer Accuracy.
* Critical Security Incidents.

### Governance Issue

The unresolved policy authority conflict requires escalation.

### Quality Concern

The multi-policy issue suggests that category-level performance remains weaker than aggregate metrics may indicate.

---

# Required Escalation

The PM should escalate:

* Hallucination threshold breach.
* Citation correctness failure.
* Retrieval degradation.
* Performance degradation.
* User satisfaction decline.
* Unresolved policy authority conflict.

The severity of each issue should be determined based on business impact.

---

# Root-Cause Investigation

The PM should coordinate investigation into:

### Data

* New or changed documents.
* Duplicate policies.
* Metadata problems.
* Authority conflicts.

### Retrieval

* Retrieval configuration.
* Embedding behavior.
* Multi-policy retrieval.
* Relevance thresholds.

### Model / Prompt

* Response behavior.
* Unsupported claims.
* Grounding failures.

### Application

* Citation logic.
* Eligibility filtering.
* Error handling.

### User Experience

* Terminology.
* Response clarity.
* User expectations.

---

# Corrective Action

Potential actions may include:

* Resolve policy authority conflict.
* Review recent knowledge-base changes.
* Improve multi-policy retrieval.
* Expand evaluation coverage.
* Correct citation behavior.
* Investigate hallucination causes.
* Improve monitoring.
* Update user guidance.
* Add targeted regression tests.
* Prioritize high-impact defects.

Corrective actions should be evidence-based.

---

# Rollback Consideration

Rollback should be considered when a production change has caused unacceptable behavior.

The PM should determine:

* What changed?
* When did the problem begin?
* Is the change reversible?
* Is the issue severe enough to justify rollback?
* Does rollback restore a known-good state?
* What risks would rollback create?

Rollback is a risk-management decision, not an automatic response to every defect.

---

# Authority Conflict Response

The unresolved authority conflict should not be ignored.

Until authority is established:

* The conflicting policy should not be treated as authoritative.
* The issue should be escalated to the appropriate policy owner/governance authority.
* Retrieval eligibility should be reviewed.
* The decision should be documented.

---

# Continuous Improvement Backlog

Example backlog items:

| Priority | Item                                 | Reason                 |
| -------- | ------------------------------------ | ---------------------- |
| High     | Resolve policy authority conflict    | Governance risk        |
| High     | Reduce hallucination rate            | AI quality risk        |
| High     | Restore citation correctness to 100% | Trust / evidence risk  |
| High     | Improve retrieval accuracy           | Core product quality   |
| High     | Improve multi-policy retrieval       | Repeated user failure  |
| High     | Improve response latency             | Performance target     |
| Medium   | Improve terminology handling         | User experience        |
| Medium   | Improve feedback categorization      | Operational efficiency |

---

# Current Monitoring Position

Monitoring is **not yet production-ready** until:

* Metrics are operational.
* Thresholds are configured.
* Owners are assigned.
* Alerts are tested.
* Escalation paths are established.
* Production review cadence is defined.
* Knowledge changes are monitored.
* Model changes trigger evaluation.
* Incidents are documented.
* Corrective-action workflow is established.

---

# PM Decision

The production scenario demonstrates why monitoring must continue after launch.

The system should not be considered healthy simply because some metrics remain above target.

The PM should:

1. Escalate threshold breaches.
2. Investigate root causes.
3. Resolve the authority conflict.
4. Analyze multi-policy failures.
5. Prioritize corrective actions.
6. Determine whether rollback is necessary.
7. Retest changes.
8. Continue monitoring after remediation.

---

# Portfolio Evidence

This artifact demonstrates the ability to:

* Design production monitoring.
* Distinguish monitoring from evaluation.
* Define AI production metrics.
* Establish thresholds and alerts.
* Monitor security and governance.
* Manage knowledge changes.
* Analyze production failures.
* Coordinate root-cause analysis.
* Convert feedback into actionable backlog items.
* Manage continuous improvement.
* Evaluate rollback decisions.
* Connect technical metrics to business outcomes.

---

# Key PM Judgment

> **AI quality must be managed throughout the product lifecycle, not only before launch.**

Production evidence can reveal problems that development and pre-release evaluation did not identify.

The PM must therefore maintain a continuous feedback loop between:

**Production → Evidence → Decisions → Improvements → Validation → Production**

---

# Final Monitoring Principle

> **A production AI system is not "done" when it launches. It is successful only when its performance, risks, data, user outcomes, and governance continue to be actively managed.**

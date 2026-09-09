# Milestone 13 — Instructor Answer Key

## Purpose

This answer key provides the expected reasoning and evaluation guidance for the Final Assessment.

Answers do not need to use the exact wording below. Award credit when the response demonstrates sound AI Project Management judgment and is supported by appropriate evidence.

---

# Part 1 — AI Project Management Knowledge

## Question 1 — AI Project Manager

### Expected Answer

The primary responsibility of an AI Project Manager is to align the AI product with the business problem and manage the people, scope, requirements, risks, decisions, delivery, and outcomes required to achieve that objective.

The role is broader than maintaining a schedule.

A strong answer should recognize that an AI Project Manager coordinates business and technical stakeholders, manages uncertainty and AI-specific risks, establishes governance, tracks quality and performance, and supports decisions throughout the product lifecycle.

### Full-Credit Indicators

The answer identifies:

* Business alignment.
* Cross-functional coordination.
* Scope and requirements.
* Risk and governance.
* Delivery and decision-making.
* Outcomes and continuous improvement.

---

# Question 2 — Business Problem

### Expected Answer

The business problem should be defined before selecting technology because the technology is a means to achieve a business outcome.

Starting with technology can result in:

* Solving the wrong problem.
* Building unnecessary functionality.
* Poor adoption.
* Uncontrolled scope.
* Weak return on investment.
* An AI solution that technically works but provides little business value.

### Full-Credit Indicator

The answer clearly connects:

**Business Need → Solution → Outcome**

rather than:

**Technology → Solution**

---

# Question 3 — Minimum Viable Product

### Expected Answer

A **Minimum Viable Product (MVP)** is the smallest version of a product that delivers enough value to validate the core business and user need.

An MVP helps control scope by focusing the team on the highest-priority capabilities required to test the product's value.

A strong answer may also explain that an MVP is not simply a product with fewer features. It should contain enough functionality to produce meaningful evidence and feedback.

---

# Question 4 — RACI

### Expected Answer

A **Responsible, Accountable, Consulted, and Informed (RACI)** matrix clarifies who performs work, who owns the outcome, who provides input, and who needs to be kept informed.

Clear ownership reduces:

* Confusion.
* Duplicated work.
* Missed responsibilities.
* Delayed decisions.
* Accountability gaps.

### Full-Credit Indicator

The answer recognizes that **Accountable** ownership is particularly important for major project decisions.

---

# Question 5 — Authoritative Information

### Expected Answer

AI systems that retrieve organizational information must use authoritative and approved sources.

If outdated, duplicate, or unauthorized information is used, the AI may produce responses that are technically plausible but operationally incorrect.

Potential consequences include:

* Incorrect employee guidance.
* Conflicting answers.
* Compliance issues.
* Security or access violations.
* Loss of trust.
* Increased hallucination or unsupported-answer risk.

A strong answer connects source authority and governance directly to AI reliability.

---

# Part 2 — Scenario-Based PM Decisions

# Question 6 — Scope Change

### Expected Answer

The Project Manager should not automatically add the requested features.

The request should first be evaluated against:

* Business value.
* User need.
* MVP objectives.
* Requirements.
* Priority.
* Schedule impact.
* Resource impact.
* Risk.
* Dependencies.
* Release impact.

The PM should document the change and use the established change-control or prioritization process.

If the features are not essential to the MVP, they may be deferred to a later release or backlog.

### Strong PM Response

A strong response follows:

**Request → Impact Analysis → Prioritization → Decision → Documentation → Communication**

---

# Question 7 — AI Evaluation

### Evidence

* Retrieval Accuracy = 92% — meets target.
* Answer Accuracy = 89% — below target.
* Hallucination Rate = 2.5% — below required performance.
* Citation Correctness = 100% — meets target.

### Expected Decision

The product has mixed evaluation results and requires improvement before unrestricted release.

The most significant concern is that the system is generating answers below the required accuracy target while hallucination is also above the acceptable threshold.

The PM should:

1. Investigate the failed evaluation cases.
2. Determine root causes.
3. Identify whether retrieval, prompting, grounding, source quality, or another component is contributing.
4. Define corrective actions.
5. Re-test.
6. Reassess release readiness.

### Key Principle

Passing some KPIs does not automatically make the product ready for release.

---

# Question 8 — Data Governance

### Expected Answer

The team should not simply use every document.

The authoritative source must be identified before the documents are treated as trusted knowledge for the AI system.

The PM should require:

* Version identification.
* Authority validation.
* Approval/status verification.
* Required metadata.
* Duplicate/conflicting document review.
* Appropriate access controls.
* Removal or exclusion of unauthorized sources.

### Core Relationship

**Data Quality → Authority → Governance → AI Reliability**

More information is not automatically better information.

---

# Question 9 — Security

### Expected Answer

The product should not proceed to unrestricted production release while an authorization defect allows users to retrieve information they should not be able to access.

This is a release-blocking security issue because access control is a fundamental product requirement.

The PM should require:

* Investigation.
* Root-cause analysis.
* Remediation.
* Retesting.
* Regression testing.
* Verification that unauthorized access is prevented.
* Appropriate security/governance sign-off.

### Key Principle

Security decisions should consider **severity and impact**, not simply how frequently the issue is expected to occur.

---

# Question 10 — User Acceptance Testing

### Expected Answer

The product should not be considered fully accepted solely because its technical accuracy targets are met.

UAT evaluates whether the product meets the users' practical needs.

If responses are technically correct but difficult to understand, the PM should:

* Document the user feedback.
* Determine whether usability affects the acceptance criteria.
* Assess business impact.
* Identify improvements.
* Re-test where appropriate.
* Obtain appropriate user acceptance.

### Key Principle

**Technical correctness ≠ complete user acceptance.**

---

# Part 3 — Release Decision

# Question 11 — Go / Conditional Go / No-Go

### Expected Answer

The strongest expected recommendation is:

**Conditional Go**

The product demonstrates several positive release indicators:

* Requirements complete.
* Zero critical defects.
* UAT passed.
* Retrieval Accuracy meets target.
* Citation Correctness meets target.
* Response Latency meets target.
* Zero critical security incidents.
* Release plan complete.
* Rollback plan complete.

However:

* Answer Accuracy is 89% against a ≥90% target.
* Hallucination Rate is 2.5% against a <2% target.
* User Satisfaction is 82% against an ≥85% target.

These gaps require corrective action or explicit risk acceptance before unrestricted production operation.

### Acceptable Alternative

**No-Go** may receive full credit if the learner clearly explains that the failed AI quality and user-experience thresholds represent unacceptable release risk.

The important factor is the quality of the reasoning, not selecting the exact same label.

### Full-Credit Decision Logic

A strong answer should identify:

**Evidence → Risk → Conditions → Decision → Monitoring**

---

# Part 4 — KPI Decision

# Question 12 — Monitoring and Performance

### KPI Interpretation

| KPI                          | Actual | Assessment      |
| ---------------------------- | -----: | --------------- |
| Policy Search-Time Reduction |    58% | On Target       |
| Retrieval Accuracy           |    92% | On Target       |
| Answer Accuracy              |    89% | Needs Attention |
| Hallucination Rate           |   2.5% | Below Threshold |
| Citation Correctness         |   100% | On Target       |
| Unsupported-Question Refusal |    95% | Needs Attention |
| Response Latency             |  8 sec | On Target       |
| User Satisfaction            |    82% | Needs Attention |
| Critical Security Incidents  |      0 | On Target       |

### Expected Priority

The hallucination rate should receive immediate attention because it is **below threshold** and represents a direct AI reliability risk.

The PM should also investigate:

* Answer Accuracy.
* Unsupported-Question Refusal.
* User Satisfaction.

### Expected Action

A strong recommendation is to investigate the AI quality failures, identify root causes, implement corrective actions, and continue monitoring the affected KPIs.

### Key Principle

Use:

**KPI → Target → Actual → Trend → Threshold → Action**

The PM should not simply report the numbers.

---

# Part 5 — Executive Communication

# Question 13 — Executive Recommendation

### Expected Answer

The executive response should be concise and decision-oriented.

A strong response should communicate that the product shows meaningful readiness evidence but has unresolved performance gaps that should be addressed or explicitly accepted before unrestricted production use.

The executive should understand:

1. Current recommendation.
2. Evidence supporting the recommendation.
3. Primary risks.
4. Required actions.
5. How success will be measured.

### Strong Communication Structure

**Recommendation → Evidence → Risk → Action → Success Measure**

The learner should avoid overwhelming the executive with unnecessary technical detail.

---

# Part 6 — Final PM Challenge

# Question 14 — End-to-End AI PM Challenge

### Expected Approach

There is no single required wording.

A strong response should demonstrate an end-to-end lifecycle:

**Business Problem**
→ Define the problem and desired outcome.

**Stakeholders & Users**
→ Identify affected users, decision-makers, technical teams, and governance stakeholders.

**Requirements**
→ Translate business and user needs into measurable requirements and acceptance criteria.

**Scope**
→ Establish what is included, excluded, and prioritized.

**MVP**
→ Define the smallest useful solution that can validate the core need.

**AI Solution**
→ Understand the proposed architecture well enough to manage dependencies, risks, and decisions.

**Data & Knowledge**
→ Validate source quality, authority, versioning, metadata, access, and governance.

**AI Evaluation**
→ Establish measurable quality and performance targets.

**Risk & Governance**
→ Identify AI, security, privacy, operational, and business risks.

**Testing & UAT**
→ Validate functionality, quality, security, usability, and user acceptance.

**Release**
→ Evaluate readiness against defined criteria.

**Go/No-Go**
→ Make an evidence-based release recommendation.

**KPIs**
→ Measure product performance and business outcomes.

**Monitoring**
→ Continuously review product health.

**Continuous Improvement**
→ Use evidence, feedback, incidents, and KPI trends to prioritize corrective actions and future improvements.

### Full-Credit Principle

The learner should demonstrate connections between stages rather than presenting the lifecycle as an unrelated checklist.

---

# Final Reflection

# Question 15 — Your AI PM Approach

There is no single correct answer.

Strong responses should demonstrate genuine reflection and show that the learner can connect course concepts to future PM practice.

Good responses may identify principles such as:

* Start with the business problem.
* Use evidence instead of assumptions.
* Define measurable outcomes.
* Control scope.
* Establish clear ownership.
* Treat data authority as a governance issue.
* Evaluate AI before release.
* Treat security as a release concern.
* Include users in acceptance decisions.
* Monitor AI after deployment.
* Continuously improve based on evidence.

---

# Assessment Review Standard

Review the assessment as a demonstration of **PM judgment**, not memorization.

A strong submission should consistently demonstrate:

### Business Thinking

Can the learner connect product decisions to business value?

### PM Discipline

Can the learner manage scope, requirements, stakeholders, risks, ownership, and delivery?

### AI Understanding

Can the learner discuss AI concepts sufficiently to manage an AI product without needing to be an AI engineer?

### Evidence-Based Decision Making

Does the learner use measurable evidence rather than assumptions?

### Governance

Does the learner recognize authority, security, privacy, access, and compliance considerations?

### Quality

Does the learner understand that AI quality requires measurable evaluation?

### Release Readiness

Can the learner distinguish between a product that is technically functional and one that is actually ready for release?

### Monitoring

Does the learner understand that deployment is not the end of the AI product lifecycle?

### Communication

Can the learner communicate a clear recommendation to both technical and executive audiences?

---

# Final Instructor Principle

The strongest AI Project Managers do not simply coordinate tasks.

They create a disciplined connection between:

**Problem → Evidence → Decision → Action → Outcome**

That is the standard this final assessment is designed to validate.

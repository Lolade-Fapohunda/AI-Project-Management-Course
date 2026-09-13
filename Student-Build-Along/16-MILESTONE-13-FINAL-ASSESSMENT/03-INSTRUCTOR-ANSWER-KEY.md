# Milestone 13 — Instructor Answer Key

## Purpose

Use this answer key to evaluate student responses consistently.

The answer key identifies:

* The core concept being assessed.
* The strongest expected response.
* Important reasoning points.
* Acceptable alternative answers where appropriate.
* Scoring guidance.

For scenario-based questions, evaluate **reasoning and PM judgment**, not exact wording.

A student may reach a different conclusion and still receive full or partial credit when the recommendation is supported by the evidence and demonstrates sound Project Management (PM) judgment.

---

# Scoring Overview

| Section                    | Questions |  Points |
| -------------------------- | --------: | ------: |
| AI PM Knowledge            |       1–5 |      20 |
| Scenario-Based PM Judgment |      6–10 |      30 |
| Release Decision           |        11 |      10 |
| KPI Analysis               |        12 |      10 |
| Executive Recommendation   |        13 |      10 |
| End-to-End AI PM Challenge |        14 |      15 |
| Reflection                 |        15 |       5 |
| **Total**                  |    **15** | **100** |

## Scoring Standard

Use:

**Full Credit:** Correct concept, appropriate reasoning, and clear PM application.

**Partial Credit:** General understanding is demonstrated, but important reasoning, risk, evidence, or PM implications are missing.

**No / Minimal Credit:** The response demonstrates a material misunderstanding of the concept or scenario.

---

# Question 1 — AI Project Management

## Expected Answer

The primary role of an AI Project Manager is to manage the product, business objectives, stakeholders, risks, requirements, delivery, evaluation, governance, readiness, and outcomes associated with the AI initiative.

AI projects require additional attention to areas such as:

* Data quality.
* AI evaluation.
* Model or response behavior.
* Grounding.
* Hallucinations or unsupported responses.
* Security and authorization.
* Governance.
* Uncertainty and changing AI behavior.
* Monitoring after release.

A PM should not simply manage the technology implementation.

The PM must connect:

**Business Need → Product → AI → Risk → Evidence → Outcome**

## Full-Credit Indicators

The student identifies both traditional PM responsibilities and AI-specific considerations.

---

# Question 2 — Business Problem

## Expected Answer

An AI project should begin with a clearly defined business problem so that the team can determine:

* Whether AI is appropriate.
* Who the users are.
* What problem must be solved.
* What outcome is expected.
* What success should be measured.

Starting with technology can lead to a solution looking for a problem, unnecessary complexity, poor adoption, or no measurable business value.

## Strong Example

An organization builds an AI chatbot because the technology is available but never establishes what employee problem it must solve. Employees do not find it useful, so adoption remains low despite a technically functioning system.

## Full-Credit Indicators

The student connects problem definition to value, scope, and measurable outcomes.

---

# Question 3 — Minimum Viable Product

## Expected Answer

A **Minimum Viable Product (MVP)** is the smallest useful version of a product that can provide core value and generate meaningful evidence about whether the product solves the intended problem.

An MVP is useful because it allows the team to:

* Validate assumptions.
* Learn from users.
* Test the product.
* Manage cost and complexity.
* Reduce unnecessary scope.

MVP scope is not necessarily the same as later release scope.

A later release may contain additional capabilities, controls, fixes, and approved changes.

## Full-Credit Indicators

The student clearly distinguishes:

**MVP = smallest useful version for validation**

from:

**Release Scope = approved capabilities, controls, fixes, and changes for a specific release**

---

# Question 4 — RACI

## Expected Answer

A **Responsible, Accountable, Consulted, and Informed (RACI)** matrix clarifies roles and ownership.

* **Responsible:** Performs the work.
* **Accountable:** Owns the outcome and decision.
* **Consulted:** Provides input.
* **Informed:** Needs to know the outcome or status.

A PM can use RACI to prevent confusion over decision ownership, identify gaps, and clarify who must be involved.

## Example

For PolicyAssist policy approval:

**Responsible:** HR Policy Manager

**Accountable:** HR Executive / designated policy owner

**Consulted:** PM, Legal, IT, Security

**Informed:** Employees / relevant stakeholders

Exact roles may differ by organization.

---

# Question 5 — Source of Truth

## Expected Answer

An AI product needs an authoritative source of truth so that responses are based on approved and current information.

For PolicyAssist, approved policy content is the source of truth.

The Large Language Model (LLM) generates language but should not automatically determine what the organization's policy is.

The PM should ensure that:

* Sources are authorized.
* Versions are identifiable.
* Effective dates are known.
* Conflicts are addressed.
* Outdated content is controlled.

## Full-Credit Principle

**The AI generates the response. The authoritative policy provides the truth.**

---

# Question 6 — Scope Change

## Expected Answer

The PM should not automatically accept the requested feature.

The PM should assess:

* Business value.
* Alignment with product goals.
* MVP / release impact.
* Cost and schedule.
* Security implications.
* Testing requirements.
* Dependencies.
* Resources.
* Risk.

The PM should then present the impact and seek the appropriate prioritization and approval decision.

The feature may be:

* Added to the current release.
* Added to a later release.
* Deferred.
* Rejected.

## Full-Credit Example

> The feature has potential value, but adding it now would increase security and testing requirements and delay the planned release. I would assess the value and impacts, present the trade-offs to the appropriate decision-maker, and determine whether it belongs in the current release or should be deferred.

## Do Not Require

The student does not have to select a specific outcome if the reasoning is strong.

---

# Question 7 — AI Evaluation

## Expected Answer

The product performs well in some areas but has meaningful quality gaps.

| Metric                                   |  Target | Actual | Assessment   |
| ---------------------------------------- | ------: | -----: | ------------ |
| Retrieval Accuracy                       |    ≥90% |    92% | Meets target |
| Answer Accuracy                          |    ≥90% |    89% | Below target |
| Unsupported / Hallucinated Response Rate |     <2% |   2.5% | Below target |
| Citation Correctness                     |    100% |   100% | Meets target |
| Response Time                            | ≤10 sec |  8 sec | Meets target |

The unsupported / hallucinated response rate deserves significant attention because unsupported AI guidance can directly affect user decisions and trust.

Answer accuracy also requires corrective action.

The PM should not recommend unrestricted progression without addressing the quality gaps.

## Full-Credit Indicators

The student:

* Identifies missed targets.
* Does not allow strong metrics to hide weak ones.
* Recognizes unsupported responses as a significant AI risk.
* Recommends corrective action or controlled progression.

---

# Question 8 — Data Governance

## Expected Answer

Document A should be treated as authoritative because it is:

* Approved.
* Current.
* Versioned.
* Effective as of the relevant date.

Document B should not override Document A because it is:

* Older.
* Employee-created.
* Not approved.
* Lacking authoritative governance information.

The system should use authority, version, effective date, approval status, and ownership to determine which source controls.

## Strong PM Response

The PM should ensure the outdated or unauthorized document is removed, excluded, or appropriately classified so it cannot be mistakenly treated as authoritative.

---

# Question 9 — Security & Authorization

## Expected Answer

This is a critical authorization failure.

The system disclosed restricted information to a user who was not authorized to receive it.

The PM should:

1. Treat the issue as a serious security failure.
2. Stop or restrict the affected behavior as appropriate.
3. Escalate through the appropriate security / governance process.
4. Determine scope and impact.
5. Correct the authorization control.
6. Retest the affected access scenarios.
7. Add the scenario to regression testing.
8. Prevent release or deployment until the issue is appropriately resolved.

## Key Principle

**Target: 0 unauthorized information disclosures.**

A technically correct response does not make an unauthorized disclosure acceptable.

## Full-Credit Indicator

The student identifies the issue as release-blocking or otherwise requiring resolution before the affected product stage proceeds.

---

# Question 10 — User Acceptance Testing

## Expected Answer

UAT should not automatically be considered successful.

Technical correctness does not equal user acceptance.

If users cannot easily understand the answer or determine what action to take, the product may not satisfy the intended user need.

The PM should:

* Document the UAT findings.
* Determine whether the usability issue affects acceptance criteria.
* Address the issue where necessary.
* Retest affected scenarios.
* Determine whether UAT should be accepted, accepted with conditions, or not accepted.

## Full-Credit Principle

**Technical testing asks whether the product works as designed.**

**UAT asks whether intended users can successfully use and accept it for the intended purpose.**

---

# Question 11 — Release Readiness

## Strongest Expected Answer

**B. CONDITIONAL GO**

The product demonstrates sufficient value and several strong performance indicators, but not every target has been met.

### Evidence Supporting Conditional Go

**Met:**

* Retrieval Accuracy: 92% ≥ 90%.
* Citation Correctness: 100%.
* Response Time: 8 seconds ≤ 10 seconds.
* Critical Security Incidents: 0.
* Requirements complete.
* Critical defects: 0.
* UAT passed.
* Release and rollback plans complete.

**Not Met:**

* Answer Accuracy: 89% < 90%.
* Unsupported / Hallucinated Response Rate: 2.5% > 2%.
* User Satisfaction: 82% < 85%.

These gaps should result in specific conditions, owners, monitoring, and follow-up.

## Why Not GO?

The product does not meet all defined quality targets.

A blanket GO would overlook meaningful AI quality and user-experience gaps.

## Why Not Automatically HOLD?

A well-reasoned student may select HOLD if they determine that the failed metrics prevent even a controlled release.

However, to receive full credit for HOLD, the student must explain why the unmet targets create a release-level blocker rather than merely requiring managed conditions.

## Why Not Automatically NO-GO?

The product has meaningful value, several strong results, no critical security incidents, passed UAT, and no critical defects.

NO-GO can receive full credit only if the student provides a strong risk-based justification for why the unsupported-response rate or other evidence makes the product unacceptable at the intended release stage.

## Important Terminology

**GO = Proceed**

**CONDITIONAL GO = Proceed under defined conditions**

**HOLD = Do not proceed yet because required evidence, remediation, validation, or readiness work is incomplete**

**NO-GO = Do not release the current version**

---

# Question 12 — KPI Decision

## Strongest Expected Answer

The **Unsupported / Hallucinated Response Rate** should receive the highest priority.

Actual:

**2.5%**

Target:

**<2%**

This is important because unsupported AI guidance can cause employees to make decisions based on information that is not supported by policy evidence.

The PM should also consider:

* Answer Accuracy: 89% vs. 90%.
* Refusal / Escalation: 95% vs. 100%.
* User Satisfaction: 82% vs. 85%.

These metrics indicate related response-quality and experience problems.

## Recommended Action

Investigate the root causes, improve grounding / refusal behavior, retest, and monitor the metric after corrective changes.

A strong answer may prioritize answer accuracy first if the student provides a convincing risk-based justification.

---

# Question 13 — Executive Recommendation

## Expected Answer

The recommendation should be concise and evidence-based.

A strong response might be:

> PolicyAssist demonstrates meaningful value and strong performance in retrieval, citation correctness, response time, and search-time reduction. However, answer accuracy, unsupported-response performance, and user satisfaction remain below target. I recommend a Conditional Go for a controlled release stage, subject to defined corrective actions and monitoring. Production deployment should remain on hold until required production authorization controls are implemented and validated.

## Full-Credit Indicators

The response includes:

* Current status.
* Strongest evidence.
* Primary risk.
* Business value.
* Clear recommendation.
* Specific next actions.

---

# Question 14 — End-to-End AI PM Challenge

## Expected Answer

A strong answer should show an integrated lifecycle approach.

### 1. Business Problem

Define the business problem and desired outcome.

### 2. Users & Stakeholders

Identify primary users, stakeholders, needs, influence, and decision-makers.

### 3. Requirements

Translate needs into measurable functional, non-functional, AI, security, and business requirements.

### 4. Scope & MVP

Define what is in scope, out of scope, and required for the MVP.

### 5. AI Solution

Define the PM-level solution architecture, major components, dependencies, and trade-offs.

### 6. Data & Knowledge

Identify authoritative sources, data-quality requirements, metadata, versioning, retrieval, and governance.

### 7. AI Evaluation

Define evaluation scenarios and measures for retrieval, responses, grounding, citations, unsupported responses, performance, and other applicable quality dimensions.

### 8. Security & Governance

Address authorization, privacy, confidential information, governance ownership, auditability, escalation, and change control.

### 9. Testing & UAT

Validate requirements, product behavior, user experience, and acceptance.

### 10. Release Readiness

Assess evidence, defects, risks, security, governance, UAT, monitoring, and operational readiness.

Use:

**GO / CONDITIONAL GO / HOLD / NO-GO**

### 11. Deployment

Assess whether the approved release is actually ready for deployment.

Use:

**DEPLOY / HOLD DEPLOYMENT / ROLLBACK**

### 12. KPI Monitoring

Measure:

**KPI → Target → Actual → Trend → Threshold → Action**

### 13. Business Outcomes

Compare the target outcome with measured and projected results.

### 14. Continuous Improvement

Prioritize improvements based on evidence, risk, value, and feasibility.

## Full-Credit Standard

The student demonstrates a connected lifecycle rather than listing unrelated project activities.

---

# Question 15 — PM Reflection

## Expected Answer

There is no single correct answer.

A strong response should:

* Demonstrate genuine reflection.
* Identify a meaningful AI PM lesson.
* Discuss an AI-specific risk or challenge.
* Identify a PM skill strengthened.
* Explain what the student would do differently.
* Show how the student's understanding changed.

## Full-Credit Example

> I learned that AI quality depends on more than whether the model produces an answer. Data authority, retrieval, grounding, evaluation, security, and governance all influence whether the product is acceptable. I would establish stronger negative testing and evidence requirements earlier in my next AI project.

---

# Critical Competency Guidance

Regardless of the numerical score, pay particular attention to Questions:

* 7: AI Evaluation
* 8: Data Governance
* 9: Security / Authorization
* 10: UAT
* 11: Release Readiness
* 12: KPI Decision
* 14: End-to-End AI PM

A student who demonstrates a serious misunderstanding of these areas may require reassessment.

Examples include:

* Treating the LLM as the source of truth.
* Treating a successful technical test as proof of UAT acceptance.
* Accepting unauthorized disclosure because the answer was accurate.
* Ignoring unsupported AI responses.
* Treating one strong KPI as evidence that all quality requirements are satisfied.
* Confusing release approval with deployment approval.
* Using GO, HOLD, or NO-GO without reasoning from the evidence.

---

# Release Terminology Reference

Use these definitions consistently when grading.

## Release Decision

**GO**

Proceed with release.

**CONDITIONAL GO**

Proceed with defined conditions, owners, validation requirements, and monitoring.

**HOLD**

Do not proceed yet because required evidence, remediation, validation, or readiness work is incomplete.

**NO-GO**

Do not release the current version.

## Deployment Decision

**DEPLOY**

The approved release is ready for deployment.

**HOLD DEPLOYMENT**

The release may be approved, but a deployment-specific condition remains unresolved.

**ROLLBACK**

The deployment created an unacceptable condition requiring recovery to a previous known-good state.

## Monitoring Decision

**CONTINUE**

Performance remains acceptable and the current direction should continue.

**IMPROVE**

Performance or product quality requires corrective action.

**ESCALATE**

The issue requires leadership, governance, or additional intervention.

**REASSESS**

The assumptions, product direction, scope, or business case should be reconsidered.

## Final PM Recommendation

**CONTINUE / IMPROVE / ESCALATE / REASSESS / SCALE**

This is the overall forward-looking PM recommendation.

---

# Important Grading Principle

Do not grade students based solely on whether they selected the same decision as the answer key.

For judgment questions, grade:

**Evidence → Analysis → Risk → Decision → Action**

A different answer can receive full credit when the student's reasoning is logically sound and supported by the scenario.

---

# Final Assessment Standard

A successful student demonstrates the ability to move beyond:

> **"The AI works."**

to:

> **"The evidence shows what is working, what is not, what risks remain, what decision is appropriate, and what should happen next."**

The ultimate competency being assessed is:

**Evidence-Based AI Project Management**
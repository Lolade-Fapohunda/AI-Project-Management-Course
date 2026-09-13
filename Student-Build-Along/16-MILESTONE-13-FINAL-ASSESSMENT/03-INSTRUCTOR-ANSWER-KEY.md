# Milestone 13 — Instructor Answer Key

## Purpose

Use this answer key to evaluate student responses consistently.

The key identifies:

* The core competency being assessed.
* The strongest expected response.
* Important reasoning points.
* Acceptable alternative responses.
* Scoring guidance.

For scenario-based questions, evaluate **reasoning and PM judgment**, not exact wording.

A student may reach a different conclusion and still receive full credit when the recommendation is logically supported by the evidence provided.

---

# Scoring Overview

| Section                         | Questions |  Points |
| ------------------------------- | --------: | ------: |
| AI Project Management Knowledge |       1–5 |      20 |
| Scenario-Based PM Judgment      |      6–10 |      30 |
| Release Decision                |        11 |      10 |
| KPI Analysis                    |        12 |      10 |
| Executive Recommendation        |        13 |      10 |
| End-to-End AI PM Challenge      |        14 |      15 |
| Reflection                      |        15 |       5 |
| **Total**                       |    **15** | **100** |

## Scoring Standard

**Full Credit:** The student demonstrates the correct concept, applies it appropriately, uses the scenario evidence, and demonstrates sound PM judgment.

**Partial Credit:** The student demonstrates general understanding but misses important evidence, risk, implications, or recommended action.

**Minimal / No Credit:** The response demonstrates a material misunderstanding or fails to address the question.

---

# Question 1 — AI Project Management

## Core Competency

Understanding the PM role in an AI product lifecycle.

## Expected Answer

The primary role of an AI Project Manager is to manage the business objective, product requirements, stakeholders, scope, delivery, risks, AI evaluation, governance, testing, readiness, performance, and outcomes.

AI projects require additional attention to areas such as:

* Data quality.
* AI behavior.
* Retrieval and grounding.
* Unsupported or hallucinated responses.
* Evaluation.
* Security and authorization.
* Governance.
* Monitoring and changing system behavior.

The PM connects:

**Business Need → Product → AI → Risk → Evidence → Outcome**

## Full-Credit Indicators

The student explains that AI PM is broader than coordinating technical development and recognizes the additional uncertainty and governance requirements associated with AI.

---

# Question 2 — Business Problem

## Core Competency

Problem definition and value alignment.

## Expected Answer

An AI initiative should begin with a clearly defined business problem so the team can determine:

* Whether AI is appropriate.
* Who the users are.
* What problem must be solved.
* What outcome is expected.
* How success will be measured.

Starting with technology rather than the problem can create a solution looking for a use case, unnecessary complexity, poor adoption, and limited business value.

## Example

An organization builds an AI chatbot because the technology is available but never establishes the employee problem it should solve. The system works technically, but employees do not find it useful.

## Full-Credit Indicators

The student connects problem definition to business value, product scope, and measurable outcomes.

---

# Question 3 — Minimum Viable Product

## Core Competency

MVP and product strategy.

## Expected Answer

A **Minimum Viable Product (MVP)** is the smallest useful version of a product that can provide core value and generate meaningful evidence about whether the product solves the intended problem.

An MVP helps the team:

* Validate assumptions.
* Learn from users.
* Test the product.
* Reduce unnecessary scope.
* Manage cost and complexity.

MVP scope is not necessarily the same as later release scope.

A later release may include additional capabilities, controls, fixes, or approved changes.

## Full-Credit Principle

**MVP = smallest useful version for validation**

**Release Scope = approved capabilities, controls, fixes, and changes for a specific release**

---

# Question 4 — RACI

## Core Competency

Ownership and governance.

## Expected Answer

A **Responsible, Accountable, Consulted, and Informed (RACI)** matrix clarifies ownership.

* **Responsible:** Performs the work.
* **Accountable:** Owns the outcome or decision.
* **Consulted:** Provides input.
* **Informed:** Needs to know the result or status.

A PM can use RACI to clarify responsibilities, prevent ownership gaps, and identify who has authority to make decisions.

## Example

For policy approval:

**Responsible:** Policy team / policy manager

**Accountable:** Designated policy owner

**Consulted:** PM, Legal, Information Technology, Security

**Informed:** Relevant employees or stakeholders

Exact assignments depend on organizational governance.

---

# Question 5 — Source of Truth

## Core Competency

Data authority and AI grounding.

## Expected Answer

An AI product needs an authoritative source of truth so responses are based on approved and current information.

For PolicyAssist, approved policy content is the source of truth.

The **Large Language Model (LLM)** generates language but should not independently determine organizational policy.

The PM should ensure that source authority, version, effective date, approval status, and ownership are appropriately managed.

## Full-Credit Principle

**The AI generates the response. The authoritative source provides the information.**

---

# Question 6 — Scope Change

## Core Competency

Scope, prioritization, trade-offs, and governance.

## Expected Answer

The PM should not automatically accept the request.

The PM should evaluate:

* Business value.
* Alignment with product goals.
* Impact to scope and MVP.
* Schedule.
* Resources.
* Security.
* Testing.
* Dependencies.
* Risk.
* Impact on the planned release.

The PM should present the trade-offs to the appropriate decision-maker and determine whether the feature should be:

* Included in the current release.
* Added to a later release.
* Deferred.
* Rejected.

## Full-Credit Example

> The feature may provide value, but adding it would increase security and testing requirements and could affect the planned delivery date. I would assess the value and impacts, present the trade-offs, and obtain the appropriate prioritization and approval decision before changing the scope.

## Alternative Answers

Any outcome may receive full credit when properly justified.

---

# Question 7 — AI Evaluation

## Core Competency

Interpreting AI quality evidence.

## Expected Answer

The results show mixed performance.

| Metric                                   |  Target | Actual | Assessment   |
| ---------------------------------------- | ------: | -----: | ------------ |
| Retrieval Accuracy                       |    ≥90% |    92% | Meets target |
| Answer Accuracy                          |    ≥90% |    89% | Below target |
| Unsupported / Hallucinated Response Rate |     <2% |   2.5% | Below target |
| Citation Correctness                     |    100% |   100% | Meets target |
| Response Time                            | ≤10 sec |  8 sec | Meets target |

The unsupported / hallucinated response rate deserves significant attention because unsupported policy guidance can lead employees to make incorrect decisions.

Answer accuracy also requires improvement.

The PM should not recommend unrestricted progression without addressing the quality gaps.

## Full-Credit Indicators

The student:

* Identifies missed targets.
* Does not allow strong metrics to conceal weak metrics.
* Recognizes unsupported responses as a material AI risk.
* Recommends corrective action or appropriately controlled progression.

---

# Question 8 — Data Governance

## Core Competency

Authority, versioning, and source governance.

## Expected Answer

Document A should control because it is:

* Approved.
* Versioned.
* Current.
* Effective for the relevant period.

Document B should not override it because it is:

* Older.
* Employee-created.
* Unapproved.
* Missing reliable governance information.

PolicyAssist should use source authority, approval status, version, effective date, ownership, and other governance metadata to determine the authoritative answer.

## Strong PM Response

The PM should ensure that the older unauthorized source is removed, excluded, classified appropriately, or otherwise prevented from being treated as authoritative.

---

# Question 9 — Security & Authorization

## Core Competency

Security, authorization, and risk management.

## Expected Answer

This is a serious authorization failure.

Restricted information was disclosed to an unauthorized user.

The PM should:

1. Treat the issue as a critical security concern.
2. Restrict or stop the affected behavior as appropriate.
3. Escalate through the security and governance process.
4. Determine the scope and impact.
5. Correct the authorization control.
6. Retest the affected scenarios.
7. Add the scenario to regression testing.
8. Prevent affected release or deployment progression until the issue is appropriately resolved.

## Full-Credit Principle

**Target: 0 unauthorized information disclosures.**

An answer being factually correct does not make an unauthorized disclosure acceptable.

---

# Question 10 — User Acceptance Testing

## Core Competency

UAT and user-centered validation.

## Expected Answer

UAT should not automatically be considered successful.

Technical correctness does not equal user acceptance.

If intended users cannot understand the response or determine what action to take, the product may not satisfy the intended user need.

The PM should:

* Document the feedback.
* Determine whether usability affects acceptance criteria.
* Address the issue where necessary.
* Retest affected scenarios.
* Determine whether UAT should be accepted, accepted with conditions, or not accepted.

## Full-Credit Principle

**Technical testing asks whether the product works as designed.**

**UAT asks whether intended users can successfully use and accept the product for its intended purpose.**

---

# Question 11 — Release Readiness

## Core Competency

Evidence-based release decision-making.

## Strongest Expected Answer

**B. CONDITIONAL GO**

The product demonstrates meaningful value and several strong performance indicators, but not all quality targets have been met.

## Evidence

### Met

* Retrieval Accuracy: 92% ≥ 90%.
* Citation Correctness: 100%.
* Response Time: 8 seconds ≤ 10 seconds.
* Critical Security Incidents: 0.
* Requirements complete.
* Critical defects: 0.
* UAT passed.
* Release plan complete.
* Rollback plan complete.

### Not Met

* Answer Accuracy: 89% < 90%.
* Unsupported / Hallucinated Response Rate: 2.5% > 2%.
* User Satisfaction: 82% < 85%.

A Conditional Go can be justified because the product has demonstrated substantial value, while specific conditions can be established to address the remaining gaps.

## Why Not GO?

A GO would overlook multiple unmet quality targets.

## Why Not HOLD?

A strong student may select HOLD when they reasonably determine that the failed criteria prevent even controlled progression.

For full credit, the student must explain why the evidence creates a release-level blocker.

## Why Not NO-GO?

A strong student may select NO-GO when they demonstrate that the unsupported-response rate or another risk makes the product unacceptable for the intended release stage.

For full credit, the risk-based reasoning must be strong.

## Required Terminology

**GO = Proceed with release**

**CONDITIONAL GO = Proceed with defined conditions**

**HOLD = Do not proceed yet because required evidence, remediation, validation, or readiness work is incomplete**

**NO-GO = Do not release the current version**

The answer should not confuse a release decision with a deployment decision.

---

# Question 12 — KPI Decision

## Core Competency

KPI interpretation and prioritization.

## Strongest Expected Answer

The **Unsupported / Hallucinated Response Rate** should receive the highest priority.

Actual:

**2.5%**

Target:

**<2%**

This is significant because unsupported AI guidance can cause employees to act on information that is not supported by policy evidence.

The student should also recognize related indicators:

* Answer Accuracy: 89% vs. 90%.
* Refusal / Escalation: 95% vs. 100%.
* User Satisfaction: 82% vs. 85%.

These may represent related response-quality and user-experience problems.

## Recommended Action

Investigate the root causes, improve response grounding and refusal behavior, retest, and monitor the KPI after corrective changes.

## Alternative

A student may prioritize Answer Accuracy if the reasoning clearly explains why that metric represents the greatest business or user risk.

---

# Question 13 — Executive Recommendation

## Core Competency

Executive communication.

## Strongest Expected Answer

A strong response might state:

> PolicyAssist demonstrates meaningful business value and strong performance in retrieval, citation correctness, response time, and search-time reduction. However, answer accuracy, unsupported-response performance, and user satisfaction remain below target. I recommend a Conditional Go for a controlled release stage, subject to defined corrective actions and monitoring. Production deployment should remain on hold until required production authorization controls are implemented and validated.

## Full-Credit Indicators

The response identifies:

* Current status.
* Strongest evidence.
* Primary risk.
* Business value.
* Recommended action.
* Next steps.

The response should be concise and decision-oriented.

---

# Question 14 — End-to-End AI PM Challenge

## Core Competency

Integrated AI PM lifecycle management.

## Expected Answer

A strong response should cover the complete lifecycle.

### Business Problem

Define the problem and desired outcome.

### Users & Stakeholders

Identify users, stakeholders, needs, influence, and decision-makers.

### Requirements

Translate needs into measurable business, functional, non-functional, AI, security, and access requirements.

### Scope & MVP

Define what is in scope, out of scope, and required for MVP validation.

### AI Solution

Describe the PM-level architecture, major components, dependencies, and trade-offs.

### Data & Knowledge

Identify authoritative sources, data-quality requirements, metadata, versioning, retrieval, and governance.

### AI Evaluation

Define test scenarios and measures for retrieval, responses, grounding, citations, unsupported responses, performance, and other relevant dimensions.

### Security & Governance

Address authorization, privacy, confidential information, governance ownership, auditability, human escalation, and change control.

### Testing & UAT

Validate requirements, product behavior, user experience, and acceptance.

### Release

Assess readiness and use:

**GO / CONDITIONAL GO / HOLD / NO-GO**

### Deployment

Assess deployment readiness separately and use:

**DEPLOY / HOLD DEPLOYMENT / ROLLBACK**

### KPI Monitoring

Use:

**KPI → Target → Actual → Trend → Threshold → Action**

### Business Outcomes

Compare target, measured, and projected outcomes.

### Continuous Improvement

Prioritize improvements based on evidence, business value, user impact, risk, and feasibility.

## Full-Credit Standard

The student demonstrates how decisions in one area affect other parts of the AI product lifecycle.

---

# Question 15 — PM Reflection

## Core Competency

Learning reflection and PM growth.

## Expected Answer

There is no single correct response.

A strong response should:

* Demonstrate genuine reflection.
* Identify a meaningful AI PM lesson.
* Discuss an AI-specific risk or challenge.
* Identify a PM skill strengthened.
* Explain what the student would do differently.
* Demonstrate changed understanding.

## Example

> I learned that AI quality depends on more than whether the model produces an answer. Data authority, retrieval, grounding, evaluation, security, and governance all influence whether the product is acceptable. I would establish stronger negative testing and evidence requirements earlier in my next AI project.

---

# Critical Competency Guidance

Pay particular attention to Questions:

* 7: AI Evaluation
* 8: Data Governance
* 9: Security / Authorization
* 10: UAT
* 11: Release Readiness
* 12: KPI Decision
* 14: End-to-End AI PM

A student who demonstrates a serious misunderstanding of these areas may require reassessment.

Examples of serious misunderstandings include:

* Treating the LLM as the source of truth.
* Treating technical testing as proof of UAT acceptance.
* Accepting unauthorized disclosure because the information was accurate.
* Ignoring unsupported AI responses.
* Assuming one strong KPI means the entire product is successful.
* Confusing release approval with deployment readiness.
* Selecting a release decision without reasoning from the evidence.

---

# Decision Terminology Reference

Use these terms consistently when grading.

## Release Decision

**GO**

Proceed with release.

**CONDITIONAL GO**

Proceed with clearly defined conditions, owners, validation requirements, and monitoring.

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

The issue requires additional leadership, governance, or intervention.

**REASSESS**

The product direction, assumptions, scope, or business case should be reconsidered.

## Final PM Recommendation

**CONTINUE / IMPROVE / ESCALATE / REASSESS / SCALE**

This is the overall forward-looking recommendation.

---

# Grading Judgment Questions

For Questions 6–14, do not grade solely by whether the student selected the same recommendation as this key.

Evaluate:

**Evidence → Analysis → Risk → Decision → Action**

A different recommendation can receive full credit when the student:

* Uses the evidence correctly.
* Identifies the relevant risks.
* Understands the applicable PM framework.
* Provides a defensible recommendation.
* Explains the action that should follow.

---

# Final Instructor Standard

The strongest students will demonstrate that they understand that AI Project Management is not simply about delivering AI technology.

They will recognize that:

**Business Need → Requirements → Product → Data → AI → Evaluation → Governance → Testing → Release → Deployment → Monitoring → Improvement**

must remain connected.

The ultimate competency being assessed is:

**Evidence-Based AI Project Management**

A successful student should be able to move beyond:

> **"The AI works."**

to:

> **"The evidence shows what is working, what is not, what risks remain, what decision is appropriate, and what should happen next."**

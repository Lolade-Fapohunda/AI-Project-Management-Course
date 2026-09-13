# Milestone 13 — Instructor Answer Key

## Purpose

Use this answer key to evaluate student responses to the Milestone 13 Final Assessment.

The purpose of the answer key is to support **consistent evaluation of Project Management (PM) judgment**, not to require exact wording.

Students may receive full credit for a different conclusion when their reasoning is well supported by the evidence and demonstrates sound PM judgment.

---

# Scoring Overview

The Final Assessment is worth **100 points**.

| Assessment Area             | Questions |  Points |
| --------------------------- | --------: | ------: |
| AI PM Knowledge             |       1–5 |      20 |
| Scenario-Based PM Decisions |      6–10 |      30 |
| Release Decision            |        11 |      10 |
| KPI Decision                |        12 |      10 |
| Executive Communication     |        13 |      10 |
| End-to-End AI PM Challenge  |        14 |      15 |
| Final Reflection            |        15 |       5 |
| **Total**                   |    **15** | **100** |

**Passing Score: 80 points**

---

# General Grading Standard

Evaluate whether the student:

* Understands the question.
* Uses the evidence provided.
* Applies an appropriate PM concept or framework.
* Explains the reasoning.
* Identifies relevant risks or impacts.
* Recommends an appropriate action.
* Connects the decision to the expected outcome.

Do not require students to use the exact wording shown in this answer key.

A technically different answer may receive full credit when it is logically supported by the scenario.

---

# Part 1 — AI Project Management Knowledge

## Question 1 — AI Project Management

### Expected Understanding

An AI Project Manager is responsible for managing the business, product, delivery, risk, stakeholder, governance, and operational dimensions of an AI product.

A strong response should recognize that AI projects introduce additional considerations such as:

* Data quality and authority.
* AI evaluation.
* Hallucination or unsupported responses.
* Grounding.
* Model limitations.
* Security and authorization.
* AI governance.
* Monitoring and continuous improvement.

The PM does not need to engineer the AI model but must understand enough about the technology to make informed decisions, manage dependencies, communicate with technical teams, and evaluate risks.

### Full-Credit Response Should Include

Business alignment, requirements, stakeholder management, AI-specific risks, evaluation, governance, release readiness, and post-release monitoring.

### Partial Credit

Award partial credit when the student describes general project management responsibilities but does not meaningfully address AI-specific considerations.

**Points: 4**

---

# Question 2 — Business Problem

### Expected Answer

The project should not proceed directly to development.

The problem is that the team has not established:

* A defined business problem.
* A specific user group.
* A measurable business outcome.
* Evidence that AI is an appropriate solution.

The PM should conduct discovery with stakeholders and users, validate the problem, establish measurable outcomes, assess whether AI is appropriate, and define the business case before approving development.

### Strong PM Reasoning

A student should recognize that:

**AI adoption is not itself a business problem.**

The product should be driven by a validated need.

### Points: 4

---

# Question 3 — Minimum Viable Product

### Expected Answer

The MVP should focus on the original business problem:

**Helping employees find accurate and current company policies.**

The initial MVP could reasonably include:

* Policy search.
* Retrieval of authoritative policy information.
* AI-generated responses grounded in approved content.
* Citations.
* Appropriate refusal or escalation when evidence is insufficient.

Capabilities such as:

* Payroll support.
* Sentiment analysis.
* Benefits recommendations.
* Executive analytics.
* Mobile applications.
* Voice assistance.

should generally be deferred unless evidence demonstrates they are necessary to solve the core problem.

### Key PM Principle

Scope should be tied to:

**Business Problem → Core User Need → Measurable Value**

The MVP should be the smallest useful version that provides core value and enables meaningful validation.

### Points: 4

---

# Question 4 — RACI

### Expected Answer

A **Responsible, Accountable, Consulted, and Informed (RACI)** framework clarifies ownership and reduces ambiguity.

A reasonable example:

| RACI Role   | Example                                                          |
| ----------- | ---------------------------------------------------------------- |
| Responsible | Engineering Lead responsible for building the product            |
| Accountable | Product Manager accountable for requirements and product outcome |
| Consulted   | HR provides policy expertise                                     |
| Informed    | Executive Sponsor receives major status and decision updates     |

Other logically appropriate assignments should receive credit.

### Key PM Principle

The exact assignment may vary by organization.

The important point is that ownership must be explicit.

### Points: 4

---

# Question 5 — Source of Truth

### Expected Answer

The strongest authoritative source is:

**The approved Human Resources policy, Version 3.0, effective January 2026.**

The PM should consider:

* Approval status.
* Effective date.
* Version.
* Policy owner.
* Authority of the source.
* Currency.

The 2023 employee-created document, draft policy, unofficial FAQ, and older approved policy should not be treated as equivalent authoritative sources.

An older approved policy may still be useful historically, but should not be treated as the current policy when a newer approved effective version exists.

### Key PM Principle

**The Large Language Model (LLM) is not the source of truth.**

The authoritative policy information is the source of truth.

### Points: 4

---

# Part 2 — Scenario-Based PM Decisions

## Question 6 — Scope Change

### Expected Answer

The PM should not automatically accept or reject the request.

The new capability should go through a formal scope and prioritization assessment.

The PM should evaluate:

* Business value.
* Alignment with the original problem.
* User need.
* Requirements impact.
* Schedule impact.
* Resource impact.
* AI and data risks.
* Security and governance implications.
* Impact on MVP or release scope.
* Opportunity cost.

The request should then be brought through the appropriate prioritization and stakeholder decision process.

### Strong Response

A strong answer may recommend:

**Defer to a later release**

unless evidence shows that the capability is necessary to achieve the original business outcome.

### Key PM Principle

An executive request does not automatically override approved scope.

### Points: 6

---

# Question 7 — AI Evaluation

### Evidence

| Metric                                   |    Target | Actual | Assessment                  |
| ---------------------------------------- | --------: | -----: | --------------------------- |
| Retrieval Accuracy                       |     ≥ 90% |    92% | Meets target                |
| Answer Accuracy                          |     ≥ 90% |    89% | Misses target               |
| Unsupported / Hallucinated Response Rate |      < 2% |   2.5% | Misses target and threshold |
| Citation Correctness                     |      100% |   100% | Meets target                |
| Response Time                            | ≤ 10 sec. | 8 sec. | Meets target                |

### Expected Assessment

Performing well:

* Retrieval accuracy.
* Citation correctness.
* Response time.

Below target:

* Answer accuracy.
* Unsupported / hallucinated response rate.

The **unsupported / hallucinated response rate is the strongest PM concern** because it exceeds the defined unacceptable threshold and directly creates trust and business risk.

Answer accuracy is also important and should be addressed.

### Recommended PM Action

The PM should recommend corrective action and investigation before treating the product as fully ready.

Possible actions include:

* Analyze failed evaluation scenarios.
* Determine whether failures originate in retrieval, prompting, grounding, or response generation.
* Improve handling of insufficient evidence.
* Add or strengthen regression tests.
* Reassess release readiness.
* Monitor the unsupported-response metric closely.

### Alternative Acceptable Reasoning

A student may prioritize answer accuracy if the response explains why it presents the greatest business impact.

### Key PM Principle

The PM should not allow strong performance in one metric to hide unacceptable performance in another.

### Points: 6

---

# Question 8 — Data Governance

### Expected Answer

Document A should be treated as authoritative because it is:

* Approved by HR.
* Current.
* Versioned.
* Effective.

Document B should not be treated as an equivalent policy source.

The PM should require metadata such as:

* Policy owner.
* Approval status.
* Version.
* Effective date.
* Review date.
* Policy identifier.

Depending on governance requirements, Document B should be:

* Removed from authoritative retrieval.
* Clearly classified as non-authoritative.
* Archived or retained separately when appropriate.

### Risk

Treating both documents equally could result in retrieval of outdated or unauthorized policy information and produce an incorrect response.

### Points: 6

---

# Question 9 — Security and Authorization

### Expected Answer

**The product should not be released in its current state.**

The system disclosed information to a user who was not authorized to receive it.

The fact that the response was factually correct does not make the response acceptable.

### Why It Matters

This is an authorization and information-disclosure failure.

It can create:

* Security risk.
* Privacy risk.
* Compliance risk.
* User trust risk.
* Business impact.

### PM Recommendation

The issue should be treated as a critical release blocker.

Before release, the team should:

* Correct the authorization control.
* Validate the fix.
* Perform additional negative authorization testing.
* Confirm that unauthorized users cannot access restricted information.
* Update release evidence and readiness assessment.

### Key PM Principle

**Authorization failures are zero-tolerance issues for PolicyAssist.**

### Points: 6

---

# Question 10 — User Acceptance Testing

### Expected Answer

The engineering team's argument is incomplete.

Technical correctness does not automatically mean UAT acceptance.

UAT evaluates whether the product actually meets user needs and is usable for its intended purpose.

The reported problems affect:

* Comprehension.
* Usability.
* Ability to identify important policy conditions.
* Citation usability.
* Confidence about when to contact HR.

These are legitimate product issues even when the underlying policy answer is technically correct.

### PM Recommendation

The PM should:

* Document the UAT findings.
* Assess their severity and business impact.
* Determine whether they represent acceptance-blocking issues.
* Prioritize corrective action where necessary.
* Re-test with users after improvements.

### Key PM Principle

**A technically correct system can still fail user acceptance.**

### Points: 6

---

# Part 3 — Release Decision

## Question 11 — Release Readiness

### Strongest Recommendation

**B. CONDITIONAL GO**

### Reasoning

Positive evidence includes:

* Requirements complete.
* No critical defects.
* UAT passed.
* Retrieval accuracy above target.
* Citation correctness at target.
* Response time within target.
* Security incidents at zero.
* Monitoring plan complete.
* Rollback plan complete.

However:

* Answer accuracy is below target at 89%.
* Unsupported / hallucinated response rate is 2.5%, above the <2% target.
* User satisfaction is 82%, below the 85% target.

The product therefore has meaningful quality gaps.

A Conditional Go can be justified when clearly defined conditions, owners, monitoring, and remediation requirements are established.

### Strong Conditions Could Include

* Reduce unsupported response rate below the defined target.
* Improve answer accuracy to target.
* Address user-satisfaction concerns.
* Establish enhanced monitoring.
* Complete validation before broad deployment.

### Alternative Answers

**HOLD** may receive full credit when the student argues that the threshold breach and quality gaps require additional evidence or remediation before proceeding.

**NO-GO** may receive full credit when the student convincingly argues that the unsupported-response threshold makes release unacceptable.

**GO** should generally receive little or no credit unless the student provides exceptionally strong reasoning that explains why the stated target and threshold should not block release.

### Key PM Principle

A release decision must consider the complete evidence, not simply count successful metrics.

### Points: 10

---

# Part 4 — KPI Decision

## Question 12 — KPI Analysis

### A. KPIs Meeting Target

* Retrieval Accuracy: 92% ≥ 90%
* Citation Accuracy: 100% ≥ 95%
* Response Time: 8 seconds ≤ 10 seconds

### B. KPIs Requiring Attention

* Answer Accuracy: 89% versus 90% target
* User Satisfaction: 82% versus 85% target

### C. Threshold Breach

**Unsupported Response Rate: 2.5%**

The threshold is breached at **≥ 2.5%**.

### D. Highest-Priority Issue

**Unsupported Response Rate**

This is the clearest priority because it has crossed the defined unacceptable threshold.

### E. PM Action

The PM should:

* Escalate the issue.
* Conduct Root Cause Analysis (RCA).
* Review failed scenarios.
* Determine whether the problem originates in data, retrieval, prompting, grounding, or generation.
* Prioritize corrective action.
* Add or strengthen regression tests.
* Monitor the KPI after remediation.
* Reassess release or product readiness as appropriate.

### Key PM Principle

The PM should distinguish:

**Missed Target**

from:

**Threshold Breach**

A target miss requires attention.

A threshold breach requires escalation or reassessment.

### Points: 10

---

# Part 5 — Executive Communication

## Question 13 — Executive Recommendation

### Expected Content

A strong response should recommend something such as:

**Conditional Go or Hold, depending on the student's reasoning.**

The response should identify the strongest evidence:

* Retrieval accuracy is strong.
* Citation correctness is strong.
* Response time is acceptable.
* Answer accuracy is below target.
* Unsupported response rate has exceeded its threshold.
* User satisfaction is below target.

The response should explain that the product has value but should proceed only with defined conditions or should be held until critical quality concerns are addressed.

### Example of Strong Reasoning

> PolicyAssist is not ready for an unconditional release. Retrieval, citations, and response time are performing well, but answer accuracy is below target and the unsupported-response rate has crossed the defined threshold. I recommend a Conditional Go only with corrective actions to reduce unsupported responses and improve answer accuracy, with owners and validation criteria established before deployment.

Equivalent executive-level reasoning should receive full credit.

### Points: 10

---

# Part 6 — Final PM Challenge

## Question 14 — End-to-End AI Project Management

### Expected Structure

The student should demonstrate a connected lifecycle rather than an unrelated list.

A strong response should include:

### Business Problem

Validate the problem, users, impact, and desired business outcome.

### Users & Stakeholders

Identify affected users and stakeholders, understand their needs, influence, and concerns.

### Requirements

Translate needs into measurable requirements and acceptance criteria.

### Scope & MVP

Prioritize the smallest useful solution that addresses the problem and generates meaningful validation evidence.

### AI Solution

Determine whether AI is appropriate and understand the major architecture, technical dependencies, and risks at a PM level.

### Data & Knowledge

Establish authoritative sources, data quality, versioning, metadata, retrieval requirements, and access considerations.

### Evaluation

Define measurable quality criteria and evaluate retrieval, response quality, grounding, citations, unsupported responses, performance, and refusal behavior.

### Risk & Governance

Identify AI-specific risks and establish ownership, controls, governance, escalation, and monitoring requirements.

### Security

Validate authentication, authorization, privacy, confidential-data protection, and other required controls.

### Testing & UAT

Test requirements and workflows, identify defects, validate usability, and confirm acceptance with intended users.

### Release

Review readiness evidence and make an evidence-based:

**GO / CONDITIONAL GO / HOLD / NO-GO**

recommendation.

### Deployment

Determine whether the approved release is actually ready to deploy:

**DEPLOY / HOLD DEPLOYMENT / ROLLBACK**

### KPI Monitoring

Track:

**KPI → Target → Actual → Trend → Threshold → Action**

### Continuous Improvement

Use performance, user feedback, risk, and business outcomes to prioritize future improvements.

### Full-Credit Indicator

The strongest responses explicitly show how one stage informs the next.

### Points: 15

---

# Part 7 — Final Reflection

## Question 15 — PM Reflection

### Expected Response

There is no single correct answer.

A strong reflection should demonstrate meaningful learning and may discuss:

* Starting with the business problem rather than the technology.
* Using measurable outcomes.
* Managing scope and MVP decisions.
* Treating data authority and quality as PM concerns.
* Evaluating AI rather than assuming quality.
* Understanding hallucination and unsupported-response risk.
* Treating security and authorization as release considerations.
* Recognizing that technical correctness does not guarantee UAT acceptance.
* Using KPIs for evidence-based decision-making.
* Monitoring after release.
* Managing continuous improvement.

### Full Credit

Award full credit when the reflection is specific, thoughtful, and demonstrates practical application of course principles.

### Points: 5

---

# Critical Assessment Considerations

The following issues require particular attention during grading.

## Unauthorized Information Disclosure

A student should recognize that unauthorized disclosure is a serious security failure and a release blocker.

A recommendation to release despite a known unresolved authorization bypass demonstrates inadequate PM judgment.

## Unsupported AI Guidance

A student should recognize that unsupported material policy guidance is a serious product-risk issue.

A strong PM should recommend investigation, corrective action, and reassessment rather than ignoring the result because other metrics are strong.

## Data Authority

Students should distinguish current, approved, authoritative content from:

* Drafts.
* Employee-created materials.
* Unofficial FAQs.
* Outdated versions.

## UAT

Students should recognize that usability, clarity, and user confidence matter.

Technical correctness alone is insufficient.

## Release vs. Deployment

Students should understand that an approved release does not automatically mean the product is ready for deployment.

## KPI Thresholds

Students should distinguish:

**Target Miss**

from:

**Threshold Breach**

A threshold breach should trigger escalation or reassessment.

---

# Grading Guidance for Alternative Answers

The answer key provides the strongest expected reasoning, but grading should not become a keyword-matching exercise.

Award full credit when a student's answer:

1. Uses the scenario evidence correctly.
2. Identifies the relevant risk or business impact.
3. Applies an appropriate PM concept.
4. Reaches a defensible decision.
5. Identifies an appropriate next action.

For example, on Question 11, **Conditional Go**, **Hold**, and **No-Go** may all receive strong or full credit when the student clearly explains why the evidence supports the selected decision.

The quality of the reasoning matters more than matching one predetermined label.

---

# Recommended Feedback Format

When providing feedback, use:

**What You Did Well**

[Identify strong PM reasoning.]

**What Needs Improvement**

[Identify the missing concept, evidence, or reasoning.]

**Why It Matters**

[Explain the PM or business impact.]

**What Stronger Reasoning Would Include**

[Provide guidance without simply replacing the student's answer.]

This reinforces the course objective of improving judgment rather than memorizing model answers.

---

# Final Grading Principle

The Final Assessment is designed to determine whether the student can move from:

**Evidence → Risk → Decision → Action → Outcome**

The instructor should evaluate whether the student demonstrates the judgment expected of an AI Project Manager.

The objective is not to reward technical vocabulary.

The objective is to determine whether the student can:

**Understand the problem → Define success → Manage scope → Evaluate evidence → Manage risk → Govern the product → Validate with users → Assess readiness → Measure outcomes → Drive continuous improvement**

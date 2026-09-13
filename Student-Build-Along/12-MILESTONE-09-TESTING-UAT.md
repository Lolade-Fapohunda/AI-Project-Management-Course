# Milestone 9 — Testing & User Acceptance Testing (UAT)

## Objective

In this milestone, you will validate whether the AI product works as intended, satisfies its requirements, supports user needs, and provides enough evidence to support a release decision.

You will bring together:

**Requirements → Acceptance Criteria → Testing → Evidence → UAT → Release Recommendation**

The goal is not simply to prove that the application runs.

The goal is to determine whether the product is:

* Functionally acceptable.
* AI-quality acceptable.
* Secure enough for its intended stage.
* Usable by intended users.
* Consistent with approved requirements.
* Ready for the next release decision.

---

# What You Will Do

You will:

1. Review the approved requirements and MVP.
2. Build a focused testing plan.
3. Define representative test scenarios.
4. Execute applicable tests.
5. Record actual results and evidence.
6. Classify and prioritize issues.
7. Evaluate User Acceptance Testing (UAT).
8. Trace requirements to test evidence.
9. Determine which issues must be fixed and which may be deferred.
10. Assess release readiness.
11. Make a release recommendation based on the evidence.
12. Identify the appropriate release decision authority.

---

# Why Testing & UAT Matter

An AI application can appear to work while still failing important product requirements.

For example:

* The application may run but return incorrect information.
* Retrieval may be technically functional but retrieve the wrong policy.
* An answer may be correct but cite the wrong source.
* An unsupported question may receive an invented answer.
* A user may technically complete a task but find the response difficult to understand.
* A security control may exist but fail under an unauthorized-access test.
* Requirements may exist without sufficient evidence that they were actually satisfied.

Testing provides evidence.

UAT determines whether the product is acceptable to its intended users.

The PM uses both to support the release decision.

---

# Testing vs. UAT

Testing and UAT are related but different.

## Testing

Testing determines whether the product behaves according to defined requirements and expected technical or product conditions.

Testing may evaluate:

* Functionality.
* Integration.
* AI behavior.
* Citations.
* Performance.
* Security.
* Regression behavior.

## User Acceptance Testing

UAT determines whether the intended users consider the product acceptable for its intended use.

UAT focuses on:

* User goals.
* User workflows.
* Usability.
* Expected outcomes.
* Acceptance criteria.
* Practical usefulness.

A product can pass technical tests and still fail UAT.

Likewise, a product that users like may still have technical, security, or governance defects that prevent release.

---

# Part 1 — Review Requirements and MVP

Review:

* Milestone 3 requirements.
* Milestone 4 backlog and MVP.
* Milestone 7 evaluation results.
* Milestone 8 security and governance findings.

Identify the requirements that must be validated before the intended release stage.

Do not automatically retest every earlier activity.

Instead, determine what evidence is already available and what additional validation is necessary.

---

# Part 2 — Build a Focused Test Plan

Create a small but representative test plan.

Your plan should cover at least **6 test scenarios** across the following areas:

| Test Area                      | What You Are Validating                                            |
| ------------------------------ | ------------------------------------------------------------------ |
| Core User Task                 | Can the user complete the primary task?                            |
| AI Behavior                    | Does the AI behave as expected?                                    |
| Citation / Evidence            | Does the response provide appropriate supporting evidence?         |
| Unsupported Behavior           | Does the product refuse or escalate when evidence is insufficient? |
| User Experience                | Can the intended user understand and use the result?               |
| Business / Operational Outcome | Does the product support the intended outcome?                     |

You may include additional security, performance, integration, or regression tests where applicable.

---

# Reusable Test Scenario Template

Use the following structure for each test scenario.

| Field                      | Student Entry |
| -------------------------- | ------------- |
| Test ID                    |               |
| Requirement / User Need    |               |
| Test Area                  |               |
| Scenario                   |               |
| Preconditions              |               |
| Expected Result            |               |
| Acceptance Criteria        |               |
| Actual Result              |               |
| Pass / Fail / Not Testable |               |
| Evidence Reference         |               |
| Issue ID                   |               |
| Severity                   |               |
| Release Impact             |               |

You may create additional test scenarios using this same structure.

The purpose is consistency.

Every important test should make it possible to understand:

**What was tested → What should happen → What actually happened → What evidence exists → What the result means**

---

# Part 3 — Define Expected Results Before Testing

Define the expected result before observing the actual result.

This reduces the risk of changing the standard after seeing the outcome.

For each test, document:

* Test ID.
* Requirement or user need.
* Scenario.
* Expected result.
* Acceptance criteria.
* Test conditions.

### Example

**Test ID:** T01

**Scenario:** Employee asks how many paid time off days are available.

**Expected Result:** The product provides the current approved policy information and appropriate supporting evidence.

**Acceptance Criteria:**

* Relevant information is retrieved.
* Response is grounded in the policy source.
* Citation or supporting evidence is provided.
* No unsupported material claim is introduced.

---

# Part 4 — Execute the Tests

Run the applicable tests against the current product.

Record:

* Actual result.
* Pass or Fail.
* Evidence Reference.
* Issue ID, where applicable.

Use the following structure:

| Test ID | Test Area | Scenario | Expected Result | Actual Result | Pass/Fail | Evidence Reference | Issue ID |
| ------- | --------- | -------- | --------------- | ------------- | --------- | ------------------ | -------- |
| T01     |           |          |                 |               |           |                    |          |
| T02     |           |          |                 |               |           |                    |          |
| T03     |           |          |                 |               |           |                    |          |
| T04     |           |          |                 |               |           |                    |          |
| T05     |           |          |                 |               |           |                    |          |
| T06     |           |          |                 |               |           |                    |          |

Add additional rows as required.

---

# Evidence Reference

**Evidence Reference** identifies the proof supporting your test result.

Examples include:

* Screenshot.
* Response capture.
* Evaluation result.
* UAT observation.
* Defect record.
* Prior milestone result.
* Test output.
* Approval record.

Use the same **Evidence Reference** concept throughout this milestone.

The goal is to make every important test conclusion traceable to evidence.

---

# Test Result Rules

Use these rules consistently.

## Pass

The actual result meets the defined acceptance criteria and expected outcome.

## Fail

The actual result does not meet the defined acceptance criteria or expected outcome.

## Not Testable

The test cannot be performed in the current application or environment.

Do not convert **Not Testable** into Pass.

Do not claim a requirement has been validated when the required test could not be performed.

---

# Part 5 — Identify Issues and Defects

For each failed or concerning result, determine what type of problem exists.

Classify the issue as one of the following:

## Defect

The product does not perform according to an approved requirement or acceptance criterion.

## Requirement Gap

The product may behave as designed, but an important requirement was never adequately defined.

## Data Issue

The source data or knowledge is incomplete, inaccurate, outdated, conflicting, or otherwise unsuitable.

## Process Issue

The problem results from a workflow, ownership, governance, or operational process.

## Enhancement

The current product may meet its approved requirements, but a potential improvement has been identified.

Do not classify every improvement as a defect.

---

# Part 6 — Assign Severity

Assign a severity level to significant issues.

## Critical

The issue creates unacceptable risk or prevents safe or appropriate use.

Examples:

* Unauthorized disclosure.
* Critical security bypass.
* Material data exposure.
* Severe product failure.
* Critical release requirement failure.

## High

The issue materially affects product quality, user value, release readiness, or business outcome.

## Medium

The issue affects quality or usability but may not prevent the intended release.

## Low

The issue has limited impact and can generally be addressed through normal backlog management.

---

# Part 7 — Determine Must Fix vs. Can Defer

Not every issue must block release.

For each open issue, determine:

**Must Fix**

The issue should be resolved before the intended release stage.

or:

**Can Defer**

The issue may be moved to a later release when the associated risk is understood and accepted.

Consider:

* Severity.
* User impact.
* Business impact.
* Security.
* Governance.
* Regulatory implications.
* Frequency.
* Workaround availability.
* Release stage.
* Risk of recurrence.

---

# Release-Blocking Conditions

An issue may be release-blocking when it:

* Creates unacceptable security or privacy risk.
* Allows unauthorized access.
* Exposes confidential information.
* Causes material unsupported policy guidance.
* Violates a critical requirement.
* Prevents required acceptance criteria from being met.
* Creates unacceptable business or user risk.

A lower-severity enhancement should not automatically block release.

---

# Part 8 — Carry Forward Earlier Evidence

Do not unnecessarily repeat every test from Milestones 6–8.

Use prior evidence where it remains valid.

For example:

* Milestone 6 retrieval evidence can support retrieval-related traceability.
* Milestone 7 AI evaluation evidence can support response-quality conclusions.
* Milestone 8 security findings can support governance readiness.

Use an **Evidence Reference** to connect the earlier result to the current assessment.

Retest when:

* The underlying capability changed.
* New evidence is required.
* A previous result is no longer valid.
* A regression risk exists.
* A release condition requires fresh validation.

The PM should avoid both unnecessary duplication and unsupported carry-forward assumptions.

---

# Part 9 — User Acceptance Testing (UAT)

UAT evaluates whether intended users can use the product successfully for their intended purpose.

Complete at least **3 representative UAT scenarios**.

Your scenarios should represent realistic user goals.

Examples:

* Finding a known policy.
* Asking a policy question requiring retrieval.
* Receiving a cited response.
* Asking a question where evidence is insufficient.
* Understanding the response and knowing what to do next.

Use:

| UAT ID | User Type | User Goal | Scenario | Expected Result | Actual Result | Acceptance Result | Evidence Reference |
| ------ | --------- | --------- | -------- | --------------- | ------------- | ----------------- | ------------------ |
| UAT-01 |           |           |          |                 |               |                   |                    |
| UAT-02 |           |           |          |                 |               |                   |                    |
| UAT-03 |           |           |          |                 |               |                   |                    |

---

# UAT Acceptance Rule

A UAT scenario is accepted when:

1. The intended user can complete the required task.
2. The expected outcome is achieved.
3. The user considers the result acceptable for the intended use.

A technically correct response does not automatically guarantee acceptance.

For example, a response may contain correct information but still fail the intended user experience if users cannot understand or use it effectively.

---

# Part 10 — Capture User Feedback

Document significant UAT feedback.

Consider:

* Usefulness.
* Clarity.
* Trust.
* Ease of use.
* Confidence.
* Response quality.
* Citation usefulness.
* Workflow fit.
* Missing capabilities.

Distinguish feedback from defects.

A user suggestion may be an enhancement rather than a failure.

---

# Part 11 — Requirements Traceability

Create a traceability record connecting requirements to testing evidence.

Use:

| Requirement ID | Requirement | Acceptance Criteria | Test ID | Test Result | Evidence Reference | Release Impact |
| -------------- | ----------- | ------------------- | ------- | ----------- | ------------------ | -------------- |
| R-01           |             |                     |         |             |                    |                |
| R-02           |             |                     |         |             |                    |                |
| R-03           |             |                     |         |             |                    |                |
| R-04           |             |                     |         |             |                    |                |
| R-05           |             |                     |         |             |                    |                |

Add additional rows as needed.

The goal is to answer:

> **How do we know the approved requirement was actually validated?**

---

# Part 12 — Review the Overall Evidence

Bring together:

**Requirements + Testing + UAT + AI Evaluation + Security + Risks**

Do not rely on a single test result.

Consider:

* What passed?
* What failed?
* What was not testable?
* What remains open?
* What is release-blocking?
* What can be deferred?
* What user concerns remain?
* What risk remains?

---

# Part 13 — Release Recommendation

Use the four-way release decision framework established in this course.

## GO

The product meets the required release conditions and identified risks are acceptable.

**Decision: Proceed with release.**

## CONDITIONAL GO

The product is approved to proceed **only under clearly defined conditions**.

Conditions should have:

* A specific requirement, risk, or limitation.
* An identified owner.
* A required action.
* A due point or review point.
* A success or validation measure.
* Appropriate monitoring or oversight.

**Decision: Proceed within the approved conditions.**

Conditional Go should not be used to bypass a critical unresolved security, authorization, privacy, or safety issue.

## HOLD

The release decision **cannot proceed yet** because required evidence, remediation, validation, or readiness work is incomplete.

Examples include:

* A required test has not been completed.
* A required security control has not been implemented or validated.
* A release criterion has not been demonstrated.
* A significant dependency is unresolved.
* Evidence is insufficient to support a responsible release decision.

**Decision: Do not proceed until the condition is resolved, validated, or formally reassessed.**

## NO-GO

The evidence demonstrates that the product should not be released in its current state.

Examples include:

* A critical security or authorization failure.
* Unacceptable privacy or data-exposure risk.
* A material product failure creates unacceptable risk.
* A critical release requirement is not satisfied.
* The product is not suitable for the intended release stage.

**Decision: Do not release. Significant remediation or reassessment is required.**

---

# The Key Distinction

Use this rule:

**GO = Proceed**

**CONDITIONAL GO = Proceed with defined conditions**

**HOLD = Do not proceed yet**

**NO-GO = Do not release in the current state**

When deciding between Conditional Go and Hold, ask:

> **Has the organization approved proceeding under controlled conditions, or is a required condition still preventing approval?**

If the condition prevents approval, use **HOLD**.

If approval has been granted with controlled, documented conditions, use **CONDITIONAL GO**.

---

# Release Decision Authority

The Project Manager coordinates the release-readiness assessment, reviews the evidence, identifies risks, and makes or facilitates the appropriate release recommendation.

The PM should **not assume personal authority to approve a release** unless that authority has been explicitly assigned.

The person or group with formal release authority depends on the organization's governance model.

Examples may include:

* Product Owner.
* Executive Sponsor.
* Steering Committee.
* Change-approval authority.
* Business owner.
* Governance or release board.
* Other formally designated decision-maker.

The PM should identify the applicable decision authority before the final release recommendation is recorded.

Use:

**PM Assessment → PM Recommendation → Authorized Decision → Conditions / Actions → Ownership → Follow-Up**

---

# Release Decision Record

Complete the following:

| Decision Element              | Assessment |
| ----------------------------- | ---------- |
| PM Release Recommendation     |            |
| Decision Authority            |            |
| Final Decision                |            |
| Strongest Evidence            |            |
| Open Issues                   |            |
| Critical / High Risks         |            |
| Must-Fix Conditions           |            |
| Conditions, if Conditional Go |            |
| Action Owner(s)               |            |
| Decision Date                 |            |
| Next Review Point             |            |

If the PM recommendation and authorized final decision differ, document both.

For example:

**PM Recommendation:** Conditional Go

**Authorized Decision:** Hold

This is not automatically an error.

The purpose of governance is to make the decision authority and decision rationale visible.

---

# Part 14 — Exit Criteria

Before recommending release, verify whether the following conditions have been satisfied.

| Exit Criterion                                  | Status | Evidence Reference |
| ----------------------------------------------- | ------ | ------------------ |
| Representative testing completed                |        |                    |
| Critical defects resolved or formally addressed |        |                    |
| AI evaluation reviewed                          |        |                    |
| Security findings reviewed                      |        |                    |
| UAT completed                                   |        |                    |
| User acceptance determined                      |        |                    |
| Requirements traceability completed             |        |                    |
| Release-blocking issues identified              |        |                    |
| Open risks documented                           |        |                    |
| Release recommendation supported by evidence    |        |                    |
| Decision authority identified                   |        |                    |

Do not mark an item complete without supporting evidence.

---

# Deliverable

Complete a **Testing & UAT Results Record** containing:

1. A focused test plan.
2. At least 6 representative test scenarios.
3. Expected and actual results.
4. Pass / Fail / Not Testable results.
5. Evidence References.
6. Issue and defect classifications.
7. Severity assessments.
8. Must-Fix vs. Can-Defer decisions.
9. At least 3 UAT scenarios.
10. UAT acceptance results.
11. User feedback.
12. Requirements traceability.
13. Release recommendation.
14. Release decision authority.
15. Final decision, when available.
16. Open issues and risks.
17. Evidence supporting the recommendation.

---

# Final PM Checkpoint

Answer:

> **Does the evidence show that the product meets its requirements, satisfies intended users, manages material risks, and is ready for the intended release stage?**

Then answer:

> **Who has the authority to make the final release decision, and what evidence should that decision be based on?**

Your answer should connect:

**Requirements → Evidence → Risk → UAT → PM Recommendation → Authorized Decision**

Do not answer based only on whether the application works.

---

# PM Perspective

Testing provides evidence.

UAT provides user acceptance evidence.

Risk and governance review provide control evidence.

The PM brings these together to make a release recommendation.

The PM does not simply ask:

> **"Did the test pass?"**

The PM asks:

> **"What does the evidence mean for the product, the users, the business, and the release decision?"**

The PM also asks:

> **"Who has the authority to approve the decision, and what conditions must be satisfied?"**

The next milestone separates **release approval** from **deployment readiness and execution**.

---

# Milestone Completion Standard

Milestone 9 is complete when you have:

* Reviewed the approved requirements and MVP.
* Defined at least 6 representative test scenarios.
* Used the reusable test scenario structure.
* Defined expected results before testing.
* Recorded actual results and Evidence References.
* Applied Pass / Fail / Not Testable consistently.
* Classified significant issues.
* Assigned severity where appropriate.
* Determined Must Fix vs. Can Defer.
* Completed at least 3 UAT scenarios.
* Captured significant user feedback.
* Completed requirements traceability.
* Reviewed relevant prior evidence.
* Identified release-blocking conditions.
* Documented a PM release recommendation.
* Identified the formal release decision authority.
* Documented the final decision when available.
* Completed the release exit-criteria review.
* Completed the final PM checkpoint.

The quality standard is not the number of tests.

The quality standard is whether the evidence is sufficient to explain:

**What was tested → What happened → What it means → What risk remains → What the PM recommends → Who decides → What happens next**

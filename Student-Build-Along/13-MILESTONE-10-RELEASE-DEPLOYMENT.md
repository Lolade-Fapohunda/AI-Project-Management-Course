# Milestone 10 — Release & Deployment

## Objective

In this milestone, you will determine whether the AI product is ready to be released and whether it is ready to be deployed into its intended environment.

The goal is not simply to deploy the application.

The goal is to make a controlled, evidence-based decision about:

**Release Approval → Deployment Readiness → Deployment → Validation → Stabilization**

You will apply the evidence collected in earlier milestones to determine whether the product should move forward.

---

# What You Will Do

You will:

1. Review the testing and User Acceptance Testing (UAT) evidence from Milestone 9.
2. Review AI evaluation results.
3. Review security and governance conditions.
4. Define release criteria.
5. Review open defects, risks, and dependencies.
6. Make a release recommendation.
7. Identify the authorized release decision-maker.
8. Determine deployment readiness separately from release approval.
9. Define the deployment approach.
10. Define post-deployment validation.
11. Define rollback conditions and procedures.
12. Define operational readiness and stabilization monitoring.
13. Complete the Release & Deployment Readiness Record.
14. Document the final release and deployment decisions.

---

# Why Release & Deployment Are Different

A product can be ready for release approval without being ready for production deployment.

For example, an AI product may:

* Pass applicable functional tests.
* Meet UAT expectations.
* Have acceptable evaluation results.
* Receive release approval.

But production deployment may still need to wait because:

* Role-based access control has not been implemented.
* Required production configuration is incomplete.
* Security validation is outstanding.
* Monitoring is not configured.
* Production secrets have not been established.
* Support ownership is not confirmed.
* Rollback capability has not been validated.

Therefore:

**Release approval and deployment readiness are separate decisions.**

---

# The PolicyAssist Example

For PolicyAssist, consider this sequence:

**Testing / UAT Passed**

↓

**Release Recommendation: GO**

↓

**Production Authorization Control Outstanding**

↓

**Deployment: HOLD**

↓

**Control Implemented and Validated**

↓

**Deployment Reassessed**

↓

**Deploy**

This distinction prevents the PM from assuming that approval to release automatically means the product can safely enter production.

---

# Release vs. Deployment

## Release

A **release** is the formal decision that a defined version of the product is approved to move to its intended release stage.

The release decision answers:

> **Should this version be approved to proceed?**

## Deployment

A **deployment** is the controlled technical and operational act of moving the approved version into an environment.

The deployment decision answers:

> **Can the approved version safely be deployed into this environment now?**

---

# Part 1 — Review M9 Evidence

Review the evidence from Milestone 9.

Include:

* Test results.
* UAT results.
* Requirements traceability.
* Defects.
* Open issues.
* Evidence References.
* Security findings.
* User feedback.
* Acceptance results.

Also review relevant evidence from:

* Milestone 7 AI evaluation.
* Milestone 8 security and governance.
* Milestone 6 data and retrieval.
* Milestone 4 MVP and backlog.

Do not restart the entire testing process.

Use valid prior evidence and identify where fresh validation is required.

---

# Part 2 — Define Release Criteria

Define at least **8 release criteria**.

Release criteria should reflect the requirements and risks of the product.

Examples include:

* Approved requirements satisfied.
* Acceptance criteria satisfied.
* No unresolved critical defects.
* UAT accepted or formally conditionally accepted.
* AI evaluation reviewed.
* Required AI quality targets met or formally addressed.
* Security requirements satisfied for the intended release stage.
* Governance responsibilities established.
* Monitoring available.
* Support ownership established.
* Rollback approach documented.
* Known risks accepted by the appropriate authority.

Your criteria should be specific enough to support a release decision.

---

# Release Criteria Table

Use:

| Release Criterion   | Required Result | Actual Result | Status | Evidence Reference |
| ------------------- | --------------- | ------------- | ------ | ------------------ |
| Requirements        |                 |               |        |                    |
| Acceptance Criteria |                 |               |        |                    |
| AI Evaluation       |                 |               |        |                    |
| Security            |                 |               |        |                    |
| UAT                 |                 |               |        |                    |
| Defects             |                 |               |        |                    |
| Monitoring          |                 |               |        |                    |
| Support             |                 |               |        |                    |
| Rollback            |                 |               |        |                    |

Add criteria as needed.

---

# Part 3 — Review AI Quality

Review the AI evaluation evidence.

Consider:

* Retrieval accuracy.
* Answer accuracy.
* Grounded response performance.
* Unsupported-response behavior.
* Citation quality.
* Hallucination rate.
* Response latency.

Do not treat one successful metric as proof of readiness.

A product may meet retrieval accuracy while still experiencing answer-quality or hallucination problems.

Use:

**Metric → Target → Actual → Risk → Decision**

---

# Part 4 — Review Security & Governance

Review the security and governance evidence from Milestones 8 and 9.

Consider:

* Authentication.
* Authorization.
* Role-based access control.
* Confidential data protection.
* Privacy.
* Auditability.
* Policy authority.
* Version control.
* Governance ownership.
* Human escalation.
* Production security testing.

## Important

Do not claim that a control is implemented or validated when it has not been.

Classify controls appropriately as:

**Implemented and Validated**

**Implemented but Not Fully Validated**

**Not Implemented**

**Not Tested**

The release decision should reflect the actual state.

---

# Part 5 — Review Open Defects and Risks

Review all unresolved items.

For each significant issue, determine:

* Severity.
* Business impact.
* Product impact.
* Security impact.
* User impact.
* Workaround.
* Owner.
* Due point.
* Release impact.

Use:

**Must Fix**

or

**Can Defer**

Do not allow an issue to disappear simply because it is inconvenient to address.

---

# Critical Release Conditions

A condition may block release when it creates:

* Unacceptable security risk.
* Unauthorized access.
* Confidential data exposure.
* Material unsupported policy guidance.
* Critical product failure.
* Failure of a critical requirement.
* Unacceptable business or user risk.

A lower-severity enhancement does not automatically block release.

---

# Part 6 — Release Decision

Use the four-way release decision framework.

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

* A required security control has not been implemented or validated.
* A required test has not been completed.
* A release criterion has not been demonstrated.
* A significant dependency remains unresolved.
* Required evidence is insufficient.

**Decision: Do not proceed until the condition is resolved, validated, or formally reassessed.**

## NO-GO

The evidence demonstrates that the product should not be released in its current state.

Examples include:

* Critical security failure.
* Unauthorized access.
* Unacceptable privacy or data exposure.
* Material product failure.
* Critical release requirement not satisfied.
* Product unsuitable for the intended release stage.

**Decision: Do not release. Significant remediation or reassessment is required.**

---

# The Key Distinction

Use this rule:

**GO = Proceed**

**CONDITIONAL GO = Proceed with defined conditions**

**HOLD = Do not proceed yet**

**NO-GO = Do not release in the current state**

Ask:

> **Has the organization approved proceeding under controlled conditions, or is a required condition still preventing approval?**

If the condition prevents approval:

**HOLD**

If approval has been granted with controlled, documented conditions:

**CONDITIONAL GO**

---

# Part 7 — Release Decision Authority

The Project Manager coordinates the readiness assessment, reviews the evidence, identifies risks, and makes or facilitates the release recommendation.

The PM should not assume personal authority to approve a release unless that authority has been explicitly assigned.

The formal decision authority depends on the organization's governance model.

Examples may include:

* Product Owner.
* Executive Sponsor.
* Business Owner.
* Steering Committee.
* Change-approval authority.
* Release board.
* Governance authority.
* Other formally designated decision-maker.

Document:

**PM Assessment → PM Recommendation → Authorized Decision → Conditions / Actions → Owner → Follow-Up**

The PM recommendation and final authorized decision should be recorded separately when they differ.

---

# Release Decision Record

Use:

| Decision Element          | Assessment |
| ------------------------- | ---------- |
| PM Recommendation         |            |
| Decision Authority        |            |
| Final Authorized Decision |            |
| Strongest Evidence        |            |
| Open Risks                |            |
| Open Defects              |            |
| Conditions                |            |
| Required Actions          |            |
| Action Owner              |            |
| Decision Date             |            |
| Next Review Point         |            |

---

# Part 8 — Deployment Readiness

After the release decision, determine whether the product is ready to be deployed.

Deployment readiness should consider:

## Environment

* Correct environment available.
* Required configuration completed.
* Required dependencies available.

## Access & Security

* Authentication configured.
* Authorization configured where required.
* Secrets protected.
* Security validation completed as required.

## Data & Content

* Required policy content available.
* Approved content loaded.
* Appropriate metadata present.
* Version/status checks completed.

## Monitoring

* KPI monitoring available.
* Error monitoring available.
* Feedback mechanism available.
* Escalation path established.

## Operations

* Support owner identified.
* Incident process defined.
* Documentation available.
* User communication prepared where required.

## Rollback

* Rollback trigger defined.
* Rollback owner defined.
* Recovery method documented.
* Validation process defined.

---

# Deployment Readiness Table

| Deployment Condition      | Required? | Actual Status | Evidence Reference | Owner |
| ------------------------- | --------- | ------------- | ------------------ | ----- |
| Environment Ready         |           |               |                    |       |
| Configuration Ready       |           |               |                    |       |
| Security Controls         |           |               |                    |       |
| Data / Policy Content     |           |               |                    |       |
| Monitoring                |           |               |                    |       |
| Support                   |           |               |                    |       |
| Rollback                  |           |               |                    |       |
| Operational Documentation |           |               |                    |       |

---

# Part 9 — Deployment Approach

Select a deployment approach appropriate to the product and risk.

## Direct Deployment

Move the approved release into the intended environment.

Useful when:

* Risk is low.
* Readiness is strong.
* Rollback is straightforward.

## Pilot

Release to a limited group before broader deployment.

Useful when:

* User feedback is important.
* Risk needs to be controlled.
* Production evidence is still limited.

## Phased Deployment

Expand access in stages.

Useful when:

* The product serves multiple groups.
* Risk increases with scale.
* Operational monitoring is required.

## Blue-Green Deployment

Maintain separate environments to support controlled switching and rollback.

Useful when:

* Infrastructure supports it.
* Availability is important.
* Rapid rollback is required.

### PM Decision

Select one approach and explain:

**Approach → Reason → Risk → Mitigation**

---

# Part 10 — Deployment Decision

The deployment decision is separate from the release decision.

Use:

## DEPLOY

The approved release meets the deployment-readiness conditions.

**Decision: Deploy.**

## HOLD DEPLOYMENT

The release may be approved, but a deployment condition remains unresolved.

Examples:

* Production access controls are incomplete.
* Production security validation is outstanding.
* Required monitoring is not configured.
* Deployment dependencies are incomplete.
* Production configuration is not ready.

**Decision: Do not deploy yet. Resolve and validate the condition first.**

## ROLLBACK

The deployment has created an unacceptable condition requiring recovery to a previous known-good state.

Examples:

* Critical production defect.
* Security failure.
* Material data exposure.
* Severe performance degradation.
* Unacceptable user impact.

**Decision: Recover using the defined rollback procedure and validate the recovered state.**

---

# Important Relationship

The following combinations are possible:

### Release GO + Deploy

The product is approved and ready to deploy.

### Release GO + Hold Deployment

The product is approved, but a deployment-specific condition remains unresolved.

### Release Conditional Go + Deploy

The product is approved to proceed under defined conditions and deployment readiness has also been satisfied.

### Release Conditional Go + Hold Deployment

The product has conditional approval, but a separate deployment condition is not yet satisfied.

### Release Hold

The product has not been approved to proceed.

Deployment should not occur.

### Release No-Go

The product should not be released.

Deployment should not occur.

---

# Part 11 — Deployment Execution Plan

Document the deployment sequence.

A typical sequence may include:

1. Confirm release approval.
2. Confirm deployment authority.
3. Confirm deployment conditions.
4. Confirm production environment.
5. Confirm required configuration and secrets.
6. Deploy the approved version.
7. Verify application availability.
8. Run post-deployment validation.
9. Begin stabilization monitoring.
10. Communicate deployment status.
11. Escalate incidents when required.

The exact sequence should reflect your product and environment.

---

# Part 12 — Post-Deployment Validation

Define at least **5 post-deployment checks**.

Examples:

* Application loads successfully.
* Users can submit a supported question.
* Relevant policy information is retrieved.
* Response is grounded and cited appropriately.
* Unsupported questions are handled correctly.
* Required access restrictions operate correctly.
* Monitoring is receiving expected data.
* Response time remains acceptable.

Use:

| Check        | Expected Result | Actual Result | Status | Evidence Reference |
| ------------ | --------------- | ------------- | ------ | ------------------ |
| Validation 1 |                 |               |        |                    |
| Validation 2 |                 |               |        |                    |
| Validation 3 |                 |               |        |                    |
| Validation 4 |                 |               |        |                    |
| Validation 5 |                 |               |        |                    |

---

# Part 13 — Rollback Plan

A rollback plan defines how the team will return to a known-good state when deployment creates unacceptable risk.

Define:

## Rollback Trigger

What condition causes rollback consideration?

Examples:

* Critical security issue.
* Material data exposure.
* Severe product failure.
* Unacceptable performance.
* Major business impact.

## Decision Owner

Who has authority to initiate rollback?

## Recovery State

What previous version or known-good state will be restored?

## Rollback Method

How will the recovery occur?

## Recovery Validation

How will you verify that the recovered state is functioning?

## Communication

Who must be informed?

Use:

**Trigger → Decision → Recovery → Validation → Communication**

---

# Part 14 — Operational Readiness

Deployment is not the end of the PM responsibility.

Confirm:

* Support ownership.
* Incident escalation.
* User feedback process.
* KPI monitoring.
* Issue triage.
* Documentation.
* Change management.
* Governance review.
* Continuous-improvement process.

The team should know what happens when something goes wrong after deployment.

---

# Part 15 — Early Stabilization Monitoring

Define at least **3 areas to monitor immediately after deployment**.

Examples:

* Response accuracy.
* Hallucination or unsupported-response behavior.
* Response latency.
* Retrieval quality.
* User feedback.
* Error rates.
* Access-control events.
* Security events.
* Policy content issues.

For each monitoring area, identify:

**Metric → Target → Threshold → Owner → Action**

---

# Stabilization Monitoring Table

| Monitoring Area | KPI / Measure | Target | Threshold | Owner | Action |
| --------------- | ------------- | -----: | --------: | ----- | ------ |
|                 |               |        |           |       |        |
|                 |               |        |           |       |        |
|                 |               |        |           |       |        |

---

# Part 16 — Complete the Release & Deployment Readiness Record

Use the following student-ready template to document your final assessment.

## 1. Product Information

**Project Name:**
[Enter project name]

**Product Name:**
[Enter product name]

**Release Version:**
[Enter version or release identifier]

**Release Stage:**
[Prototype / Pilot / MVP / Production / Other]

**Assessment Date:**
[Enter date]

**Project Manager:**
[Enter name or role]

---

## 2. Release Criteria Assessment

Document whether the product satisfies the criteria required for the intended release stage.

| Release Criterion   | Required Result | Actual Result | Status | Evidence Reference |
| ------------------- | --------------- | ------------- | ------ | ------------------ |
| Requirements        |                 |               |        |                    |
| Acceptance Criteria |                 |               |        |                    |
| AI Evaluation       |                 |               |        |                    |
| Security            |                 |               |        |                    |
| UAT                 |                 |               |        |                    |
| Critical Defects    |                 |               |        |                    |
| Monitoring          |                 |               |        |                    |
| Support             |                 |               |        |                    |
| Rollback            |                 |               |        |                    |
| Governance          |                 |               |        |                    |

### Release Criteria Summary

**What criteria are satisfied?**

[Enter assessment]

**What criteria remain unresolved?**

[Enter assessment]

**What evidence supports the assessment?**

[Enter evidence references]

---

## 3. AI Quality Assessment

| Measure                      | Target | Actual | Status | Interpretation | Evidence Reference |
| ---------------------------- | -----: | -----: | ------ | -------------- | ------------------ |
| Retrieval Accuracy           |        |        |        |                |                    |
| Answer Accuracy              |        |        |        |                |                    |
| Hallucination Rate           |        |        |        |                |                    |
| Citation Correctness         |        |        |        |                |                    |
| Unsupported-Question Refusal |        |        |        |                |                    |
| Response Latency             |        |        |        |                |                    |

### AI Quality Assessment

**What is performing well?**

[Enter assessment]

**What requires attention?**

[Enter assessment]

**What is the release impact?**

[Enter assessment]

---

## 4. Security & Governance Assessment

| Control / Requirement         | Status | Risk / Impact | Evidence Reference | Required Action |
| ----------------------------- | ------ | ------------- | ------------------ | --------------- |
| Authentication                |        |               |                    |                 |
| Authorization                 |        |               |                    |                 |
| Role-Based Access             |        |               |                    |                 |
| Confidential Data Protection  |        |               |                    |                 |
| Privacy                       |        |               |                    |                 |
| Policy Authority / Versioning |        |               |                    |                 |
| Governance Ownership          |        |               |                    |                 |
| Human Escalation              |        |               |                    |                 |
| Security Validation           |        |               |                    |                 |

### Security & Governance Summary

**Are there any unresolved critical security or authorization issues?**

[Yes / No]

**If yes, describe them and explain the release impact.**

[Enter assessment]

---

## 5. Open Defects & Risks

| ID | Issue / Risk | Type | Severity | Impact | Owner | Must Fix / Can Defer | Release Impact |
| -- | ------------ | ---- | -------- | ------ | ----- | -------------------- | -------------- |
|    |              |      |          |        |       |                      |                |
|    |              |      |          |        |       |                      |                |
|    |              |      |          |        |       |                      |                |
|    |              |      |          |        |       |                      |                |

### Highest-Priority Issue

**Issue / Risk:**

[Enter issue]

**Why is it the highest priority?**

[Enter reasoning]

**Required action:**

[Enter action]

---

## 6. PM Release Recommendation

Select one:

**☐ GO**

**☐ CONDITIONAL GO**

**☐ HOLD**

**☐ NO-GO**

### Recommendation

[Select and explain your recommendation.]

### Strongest Evidence

[Identify the most important evidence supporting your recommendation.]

### Primary Risks

[Identify the most significant remaining risks.]

### Required Actions

[Identify required corrective actions or conditions.]

### Action Owner(s)

[Identify owner(s).]

### Next Review Point

[Enter date, milestone, or decision point.]

---

## 7. Release Decision Authority

**PM Recommendation:**
[Go / Conditional Go / Hold / No-Go]

**Authorized Decision-Maker:**
[Product Owner / Executive Sponsor / Business Owner / Steering Committee / Other]

**Authorized Decision:**
[Go / Conditional Go / Hold / No-Go]

**Decision Date:**
[Enter date]

### Conditions or Decision Notes

[Document the authorized decision and any conditions.]

Remember:

**The PM recommendation and the authorized final decision may be different.**

---

## 8. Deployment Readiness Assessment

Release approval does not automatically mean the product is ready to deploy.

| Deployment Condition                      | Required? | Actual Status | Evidence Reference | Owner |
| ----------------------------------------- | --------- | ------------- | ------------------ | ----- |
| Environment Ready                         |           |               |                    |       |
| Configuration Ready                       |           |               |                    |       |
| Required Secrets / Credentials Configured |           |               |                    |       |
| Security Controls Ready                   |           |               |                    |       |
| Data / Policy Content Ready               |           |               |                    |       |
| Monitoring Ready                          |           |               |                    |       |
| Support Ready                             |           |               |                    |       |
| Rollback Ready                            |           |               |                    |       |
| Operational Documentation Ready           |           |               |                    |       |

### Deployment Readiness Summary

**Is the product ready to deploy?**

[Yes / No]

**What evidence supports this decision?**

[Enter evidence]

**What deployment conditions remain unresolved?**

[Enter conditions]

---

## 9. Deployment Approach

Select the approach used for this release:

**☐ Direct Deployment**

**☐ Pilot**

**☐ Phased Deployment**

**☐ Blue-Green Deployment**

**☐ Other**

### Why was this approach selected?

[Explain]

### Key Deployment Risk

[Identify the primary deployment risk.]

### Risk Mitigation

[Explain how the risk will be managed.]

---

## 10. Deployment Decision

Select one:

**☐ DEPLOY**

**☐ HOLD DEPLOYMENT**

**☐ ROLLBACK**

### Deployment Decision

[Explain the decision.]

### Decision Authority

[Enter authorized deployment decision-maker.]

### Conditions

[Document any conditions.]

---

## 11. Post-Deployment Validation

Define at least **5 validation checks**.

| Validation Check              | Expected Result | Actual Result | Status | Evidence Reference |
| ----------------------------- | --------------- | ------------- | ------ | ------------------ |
| Application availability      |                 |               |        |                    |
| Supported user scenario       |                 |               |        |                    |
| Retrieval / response behavior |                 |               |        |                    |
| Citation / evidence behavior  |                 |               |        |                    |
| Unsupported-question handling |                 |               |        |                    |

Add additional checks where appropriate.

---

## 12. Rollback Plan

### Rollback Trigger

What condition would cause rollback consideration?

[Enter condition]

### Rollback Decision Owner

[Enter role or name]

### Recovery State

What known-good version or state will be restored?

[Enter version or state]

### Rollback Method

How will the rollback be performed?

[Describe method]

### Recovery Validation

How will you confirm that the recovered state is functioning?

[Describe validation]

### Communication

Who must be informed?

[Identify stakeholders]

### Rollback Sequence

**Trigger → Decision → Recovery → Validation → Communication**

---

## 13. Operational Readiness

| Operational Area    | Status | Owner | Evidence Reference |
| ------------------- | ------ | ----- | ------------------ |
| Product Support     |        |       |                    |
| Technical Support   |        |       |                    |
| Incident Escalation |        |       |                    |
| User Feedback       |        |       |                    |
| KPI Monitoring      |        |       |                    |
| Issue Triage        |        |       |                    |
| Governance Review   |        |       |                    |
| Documentation       |        |       |                    |

### Operational Readiness Summary

[Describe whether the product can be supported after deployment.]

---

## 14. Stabilization Monitoring

Define at least **3 areas to monitor immediately after deployment**.

| Monitoring Area | KPI / Measure | Target | Threshold | Owner | Action |
| --------------- | ------------- | -----: | --------: | ----- | ------ |
|                 |               |        |           |       |        |
|                 |               |        |           |       |        |
|                 |               |        |           |       |        |

### Stabilization Plan

**How frequently will the product be reviewed during the initial stabilization period?**

[Enter cadence]

**What would trigger escalation?**

[Enter conditions]

---

## 15. Final Release & Deployment Summary

### Release

**PM Recommendation:**
[Go / Conditional Go / Hold / No-Go]

**Authorized Decision:**
[Go / Conditional Go / Hold / No-Go]

### Deployment

**Deployment Decision:**
[Deploy / Hold Deployment / Rollback]

### Key Risk

[Enter highest remaining risk.]

### Required Action

[Enter immediate action.]

### Owner

[Enter owner.]

### Next Review Point

[Enter date or milestone.]

---

## 16. PM Decision Statement

Complete the following:

> **Based on the available evidence, I recommend [decision] because [evidence/reasoning]. The primary risk is [risk], which will be addressed by [action] owned by [owner]. The decision will be reviewed at [review point].**

---

# Part 17 — Technical Build-Along

The technical deployment activity is optional.

All students complete the PM release and deployment analysis.

No advanced software engineering is required for the PM portion.

Students completing the technical Build-Along may use the PolicyAssist implementation to understand how deployment decisions relate to:

* Application configuration.
* Environment variables.
* Secrets.
* Data and policy content.
* Deployment platforms.
* Application validation.
* Monitoring.
* Rollback.

The purpose is to understand deployment from a PM perspective.

**The PM manages readiness, risk, ownership, evidence, and decisions.**

---

# Part 18 — PM Decisions

Make at least **three PM decisions** during this milestone.

Examples:

* Should the product receive a Go, Conditional Go, Hold, or No-Go recommendation?
* Which open issue has the greatest release impact?
* Is a condition acceptable for a limited release?
* Should deployment proceed?
* What must be validated before deployment?
* What deployment approach is appropriate?
* What should trigger rollback?
* Who should make the final release or rollback decision?

For each decision, use:

**Evidence → Risk / Impact → Decision → Action → Owner**

---

# Common Release & Deployment Mistakes

Avoid:

### Mistake 1 — Treating deployment as the release decision

Deployment is execution.

Release is approval.

### Mistake 2 — Using Conditional Go to bypass critical risk

A serious unresolved security, authorization, privacy, or safety issue should not be disguised as a manageable condition.

### Mistake 3 — Treating Hold as No-Go

A Hold means the decision cannot proceed yet.

It does not necessarily mean the product should never be released.

### Mistake 4 — Deploying because testing passed

Testing is one input into the release decision.

### Mistake 5 — Ignoring rollback

A production deployment without a recovery strategy increases operational risk.

### Mistake 6 — Forgetting post-deployment validation

The product must be verified after deployment.

### Mistake 7 — Assuming the PM personally authorizes release

The PM coordinates and recommends unless formal decision authority has been assigned.

---

# Milestone Completion Standard

Milestone 10 is complete when you have:

* Reviewed M9 testing and UAT evidence.
* Defined release criteria.
* Reviewed AI quality evidence.
* Reviewed security and governance conditions.
* Reviewed open risks and defects.
* Distinguished release from deployment.
* Applied the four-way release decision framework.
* Identified release decision authority.
* Documented a PM release recommendation.
* Assessed deployment readiness separately.
* Selected a deployment approach.
* Defined the deployment decision.
* Defined at least 5 post-deployment validation checks.
* Defined a rollback plan.
* Defined operational readiness.
* Defined early stabilization monitoring.
* Completed the Release & Deployment Readiness Record.
* Made at least 3 PM decisions.
* Completed the final checkpoint.

---

# Final PM Checkpoint

Answer:

> **Is the product approved for release, and is it actually ready to be deployed into the intended environment?**

Then answer:

> **What evidence supports each decision, who has authority to make the final decision, and what conditions must be satisfied before deployment?**

Your response should connect:

**Testing → UAT → AI Quality → Security → Release Decision → Deployment Readiness → Deployment → Validation → Monitoring**

---

# PM Perspective

Release is a governance decision.

Deployment is an execution decision.

The Project Manager's responsibility is to ensure that both decisions are supported by:

**Evidence → Risk Assessment → Clear Ownership → Appropriate Authority → Controlled Action**

A product should not be deployed simply because it works.

It should be deployed when:

* The intended release conditions are satisfied.
* The remaining risks are understood and acceptable.
* Required controls are implemented and validated.
* The authorized decision-maker has approved the release.
* The deployment environment is ready.
* Rollback and monitoring are in place.

The next milestone will use KPI evidence to determine whether the product is delivering the intended performance and business value after release.

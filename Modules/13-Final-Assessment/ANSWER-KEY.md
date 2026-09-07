# Module 13: Final Assessment — Answer Key

## Purpose

This document contains the recommended answers, rationale, and scoring guidance for the Module 13 Final Assessment.

It is intended for instructor use, self-review, or assessment grading.

---

# Scenario 1: The AI Solution Is Popular

## Correct Answer

**C. Define and validate the business problem and desired outcomes.**

## Rationale

Technology should support a validated business need.

Before selecting a model, platform, or implementation approach, the PM should understand:

* The business problem
* Current-state process
* Stakeholders
* Desired outcomes
* AI suitability
* Success measures

## Full-Credit Response

The learner identifies problem validation as the first step and explains that the organization should not adopt AI simply because competitors are using it.

---

# Scenario 2: Conflicting Policy Documents

## Correct Answer

**D. Hold the conflicting information for authority resolution.**

## Rationale

A newer document is not automatically authoritative.

The project must establish:

* Which document is approved.
* Who owns the policy.
* Which version is authoritative.
* Which version is active.
* Whether the newer document has completed the required approval process.

If authority cannot be established, the conflicting information should not automatically be used.

## Full-Credit Response

The learner recognizes that authority and approval take precedence over simply selecting the newest document.

---

# Scenario 3: The Model Performs Well

## Correct Decision

**Do not immediately approve production release.**

## Rationale

The technical metrics meet their thresholds, but UAT has identified a meaningful business problem.

The evaluation dataset may not adequately represent real user language.

The PM should:

1. Investigate the terminology mismatch.
2. Determine how frequently the issue occurs.
3. Review retrieval performance for those terms.
4. Expand the evaluation dataset.
5. Evaluate the business impact.
6. Determine whether the issue affects important user groups.
7. Correct the underlying issue.
8. Retest.
9. Reassess release readiness.

## Key Principle

**Technical KPI performance does not automatically establish business readiness.**

## Full-Credit Response

The learner identifies the disconnect between technical evaluation and real-world user performance and recommends investigation, expanded evaluation, corrective action, and retesting.

---

# Scenario 4: The Deadline Pressure

## Correct Decision

**Hold / No-Go.**

## Rationale

Critical production-readiness activities remain incomplete:

* Security testing
* UAT
* AI evaluation
* Monitoring
* Rollback validation

Launching before these activities are completed exposes the organization to unacceptable uncertainty.

The PM should communicate the risks and establish the conditions required for release.

## Full-Credit Response

The learner rejects schedule pressure as a sufficient reason to bypass production-readiness requirements.

---

# Scenario 5: The Requirement Is Too Vague

## Correct Response

The PM should convert the vague statement into measurable requirements.

For example:

**Fast** should have a defined response-time target.

**Accurate** should have a defined accuracy metric, measurement method, and threshold.

The PM should establish:

* Definition
* Measurement method
* Target
* Threshold
* Acceptance criteria
* Test method

## Example

Instead of:

> "The AI should be fast."

Use:

> "The system should return an answer within 10 seconds for at least 95% of valid requests under defined test conditions."

The exact threshold may vary by project, but it must be measurable and agreed upon.

---

# Scenario 6: The Vendor Makes A Claim

## Correct Response

The PM should challenge the claim and request evidence.

The PM should ask:

* What does "99% accuracy" mean?
* What dataset was used?
* How large was the dataset?
* What types of questions were tested?
* What was the evaluation methodology?
* What were the test conditions?
* Was the dataset representative of the organization's use case?
* Were edge cases included?
* How was accuracy calculated?

## Key Principle

**A vendor claim is not equivalent to project evidence.**

## Full-Credit Response

The learner does not automatically accept the vendor's percentage and instead requests evidence that can be evaluated against the organization's requirements.

---

# Scenario 7: Scope Expansion

## Correct Response

The PM should evaluate the change rather than automatically approving or rejecting it.

Consider:

* Business value
* Strategic importance
* Priority
* Resources
* Schedule
* Dependencies
* Risk
* Technical complexity
* MVP impact
* Existing commitments

The requested capabilities may be:

* Added to the current release.
* Moved to a future release.
* Added to the backlog.
* Rejected if they do not support the project's objectives.

## Full-Credit Response

The learner demonstrates structured change control and recognizes the impact of scope changes on schedule, resources, risk, and product priorities.

---

# Scenario 8: Security Risk

## Correct Decision

**Treat the issue as a serious security risk and investigate before release.**

## Rationale

The fact that the issue occurred during testing does not make it acceptable.

Potential unauthorized access can result in:

* Data exposure
* Privacy violations
* Compliance problems
* Loss of user trust
* Organizational damage

The PM should:

1. Escalate the issue.
2. Determine affected data and users.
3. Identify the root cause.
4. Coordinate remediation.
5. Confirm access controls.
6. Retest.
7. Document the risk and resolution.
8. Reassess release readiness.

## Full-Credit Response

The learner treats unauthorized access as a release-impacting risk rather than dismissing it because it occurred in testing.

---

# Scenario 9: Poor Data Quality

## Correct Decision

**Hold or proceed only with clearly defined conditions.**

## Rationale

Large quantities of data do not guarantee data readiness.

The project must establish:

* Authority
* Ownership
* Approval
* Versioning
* Metadata
* Quality
* Access controls

Conflicting or unapproved information should not automatically be used by the AI system.

## Key Principle

**Data volume is not the same as data quality or data readiness.**

---

# Scenario 10: UAT Failure

## Correct Answer

**B. UAT findings**

## Rationale

UAT evaluates whether the product actually supports the intended business process and users.

Technical testing can confirm that the system functions according to technical specifications.

It does not necessarily prove that users can successfully accomplish the intended business task.

## Full-Credit Response

The learner identifies UAT as important business evidence while recognizing that technical testing and UAT serve different purposes.

---

# Scenario 11: The PM Must Choose

## Correct Decision

**Go**, assuming all organizational release criteria have been satisfied.

## Rationale

The project shows:

* Requirements complete
* Data ready
* Evaluation targets achieved
* Security approved
* UAT substantially passed
* No critical defects
* No high defects
* Monitoring ready
* Rollback tested
* Business approval complete

The available evidence supports production readiness.

## Important Qualification

The learner should recognize that a Go decision is appropriate only if the stated criteria represent the organization's actual release requirements and no additional release blockers exist.

---

# Scenario 12: The Final Judgment

## Correct Decision

**Do not automatically approve the release.**

## Rationale

The project has unresolved business and governance concerns.

The PM should:

1. Investigate user-trust concerns.
2. Analyze refusal behavior.
3. Expand evaluation coverage.
4. Determine whether important scenarios were excluded from testing.
5. Investigate the governance concern.
6. Assess business impact.
7. Define corrective actions.
8. Retest where appropriate.
9. Reassess release readiness.
10. Make an evidence-based Go, Hold, or No-Go decision.

## Key Principle

Meeting technical KPIs does not automatically mean the project is ready for production.

---

# Final Assessment Exercise

## Expected Decision

The strongest recommendation is generally:

**Hold / Do Not Proceed To Production Yet.**

The learner may recommend **Proceed With Conditions** only if the response clearly establishes specific, credible conditions that must be satisfied before launch.

## Evidence Missing

A strong response should identify:

* Complete AI evaluation results
* Edge-case evaluation
* Security review results
* UAT results
* Production monitoring readiness
* Rollback validation
* Defect status
* Governance approvals
* Business readiness
* Operational readiness

## Major Risks

Potential risks include:

* Poor performance on important edge cases
* Security vulnerabilities
* Unvalidated AI quality
* Poor user acceptance
* Inadequate monitoring
* Failed rollback
* Unresolved defects
* Governance gaps
* Schedule-driven release
* Business impact from incorrect AI behavior

## Stakeholders

The learner should consider involving appropriate stakeholders such as:

* Product/business owner
* Project sponsor
* Technical team
* AI/ML specialists
* Data owners
* Information Security
* Legal/Compliance where appropriate
* Business users
* UAT representatives
* Operations/support
* Governance or risk representatives

## Required Pre-Release Activities

A strong answer should identify activities such as:

1. Complete AI evaluation.
2. Investigate and address edge-case failures.
3. Complete security review/testing.
4. Complete UAT.
5. Resolve critical and high-severity defects.
6. Complete monitoring.
7. Validate rollback.
8. Confirm governance approvals.
9. Confirm operational readiness.
10. Reassess release criteria.

## Edge Cases

Important edge cases should not simply be ignored because they are less common.

The PM should determine:

* Business impact
* Frequency
* Severity
* User population affected
* Whether the edge case represents a required business scenario

The cases should then be:

* Corrected
* Added to evaluation
* Added to the backlog
* Explicitly excluded with documented rationale
* Or treated as release blockers when appropriate

## Final Recommendation

A strong final recommendation would be:

> **Hold the production release until the outstanding evaluation, security, UAT, monitoring, rollback, and governance requirements are completed and the edge-case failures are adequately addressed or formally accepted.**

The launch date should not override evidence-based release criteria.

---

# Final Assessment Scoring Guidance

## Business Problem & Outcomes — 10%

### Full Credit

Identifies the underlying business objective and connects project decisions to business value.

### Partial Credit

Recognizes the business problem but does not consistently connect it to decisions.

### Weak Response

Focuses primarily on technology or schedule.

---

## Requirements & Scope — 10%

### Full Credit

Demonstrates measurable requirements, acceptance criteria, prioritization, and structured scope management.

### Partial Credit

Identifies requirements but does not consistently make them measurable.

### Weak Response

Accepts vague requirements or uncontrolled scope changes.

---

## Stakeholder Management — 10%

### Full Credit

Identifies relevant stakeholders, competing interests, decision authority, and communication needs.

### Partial Credit

Identifies stakeholders without explaining their role.

### Weak Response

Treats leadership or development as the only stakeholder group.

---

## AI Technology Understanding — 10%

### Full Credit

Demonstrates sufficient understanding to evaluate architecture, dependencies, limitations, and technical claims.

### Partial Credit

Understands major AI concepts but struggles to connect them to project decisions.

### Weak Response

Accepts technical claims without evidence.

---

## Data & Knowledge Governance — 10%

### Full Credit

Recognizes authority, ownership, approval, quality, versioning, metadata, and access requirements.

### Partial Credit

Recognizes general data-quality concerns.

### Weak Response

Equates data volume with readiness.

---

## AI Evaluation & Quality — 15%

### Full Credit

Understands metrics, evaluation datasets, thresholds, edge cases, hallucination, grounding, citations, and evidence.

### Partial Credit

Recognizes the need for evaluation but provides limited analysis.

### Weak Response

Assumes technical KPIs automatically prove business readiness.

---

## Risk, Security & Governance — 15%

### Full Credit

Identifies significant AI risks, evaluates impact, recommends controls, and understands governance responsibilities.

### Partial Credit

Identifies obvious risks but provides limited mitigation.

### Weak Response

Treats security or governance as issues that can automatically be addressed after launch.

---

## Testing, UAT & Release — 10%

### Full Credit

Clearly distinguishes testing, evaluation, UAT, pilot, and release readiness.

### Partial Credit

Understands the concepts but does not connect them to release decisions.

### Weak Response

Treats successful technical testing as sufficient for release.

---

## Monitoring & Continuous Improvement — 5%

### Full Credit

Recognizes monitoring, thresholds, feedback, incidents, and continuous improvement.

### Partial Credit

Recognizes monitoring but provides limited detail.

### Weak Response

Treats monitoring as optional or solely a technical responsibility.

---

## PM Judgment & Decision-Making — 5%

### Full Credit

Makes defensible decisions based on evidence, risk, business objectives, stakeholder impact, and readiness.

### Partial Credit

Makes reasonable decisions but provides limited evidence.

### Weak Response

Bases decisions primarily on schedule, leadership pressure, or technical claims.

---

# Recommended Final Assessment Standard

**80% or higher = Pass**

**90–100% = Strong Demonstration Of AI PM Competency**

**80–89% = Competent**

**70–79% = Requires Additional Review**

**Below 70% = Reassessment Recommended**

---

# Final Assessment Principle

The strongest AI Project Managers do not simply ask:

> "Can we launch?"

They ask:

> **"Do we have sufficient evidence that we should launch?"**

That distinction is central to AI Project Management.

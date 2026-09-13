# Milestone 9: Testing & User Acceptance Testing (UAT)

## PM Objective

Validate that the Artificial Intelligence (AI) product meets its agreed requirements, acceptance criteria, and intended user needs well enough to move toward release.

## Hands-On Objective

Use the requirements, acceptance criteria, risks, AI evaluation results, and security findings from earlier milestones to conduct structured testing and User Acceptance Testing (UAT).

In earlier milestones, you evaluated specific areas of the product:

* Milestone 6: Data and retrieval
* Milestone 7: AI response and citation quality
* Milestone 8: Security and governance

In this milestone, you bring those findings together and answer:

> **Does the product meet the requirements well enough for its intended users to accept it?**

You are not repeating every earlier test.

You are using the evidence already collected to validate the product as a whole.

---

# Section 1: Review What Must Be Accepted

Return to your Milestone 3 requirements and Milestone 4 backlog.

Identify the requirements that are included in the Minimum Viable Product (MVP).

For each selected requirement, identify its acceptance criteria.

Use:

| Requirement ID | Requirement | MVP? | Acceptance Criteria | Source Milestone |
| -------------- | ----------- | ---- | ------------------- | ---------------- |
|                |             |      |                     |                  |
|                |             |      |                     |                  |
|                |             |      |                     |                  |
|                |             |      |                     |                  |
|                |             |      |                     |                  |

Focus your testing on requirements that are important to the intended product outcome.

---

# Section 2: Build the Test Plan

Create a small set of representative tests that cover the most important MVP requirements.

Create at least **six test scenarios**.

Your scenarios should include a mixture of:

* A core user task
* A requirement involving AI behavior
* A requirement involving citation or evidence
* A requirement involving error or unsupported behavior
* A requirement involving user experience
* A requirement involving a business or operational outcome

Use previous milestone results where appropriate rather than repeating the same test unnecessarily.

Record:

| Test ID | Requirement ID | Test Scenario | Expected Result | Acceptance Criteria | Evidence Reference |
| ------- | -------------- | ------------- | --------------- | ------------------- | ------------------ |
|         |                |               |                 |                     |                    |
|         |                |               |                 |                     |                    |
|         |                |               |                 |                     |                    |
|         |                |               |                 |                     |                    |
|         |                |               |                 |                     |                    |
|         |                |               |                 |                     |                    |

### Evidence Reference

Use this field to identify the proof you will use to evaluate the test.

Examples:

* Screenshot
* Captured response
* Test record
* Prior milestone result
* UAT observation
* Defect record
* Other documented evidence

---

# Section 3: Execute Functional and Integration Tests

Run the applicable test scenarios.

A functional test asks:

> **Does the product perform the required function?**

An integration test asks:

> **Do the connected parts of the product work together as expected?**

For example, an employee may:

1. Enter a policy question
2. Receive a response
3. Review supporting information
4. Use the answer to complete the intended task

Record:

| Test ID | Actual Result | Pass/Fail | Evidence Reference | Issue ID |
| ------- | ------------- | --------- | ------------------ | -------- |
|         |               |           |                    |          |
|         |               |           |                    |          |
|         |               |           |                    |          |
|         |               |           |                    |          |
|         |               |           |                    |          |
|         |               |           |                    |          |

Use the **Evidence Reference** to identify the proof supporting your result.

Use the **Issue ID** only when a defect, gap, or other concern is identified.

---

# Section 4: Apply Consistent Test Pass/Fail Rules

Use these rules for each test.

### Pass

A test passes when the actual result meets the defined acceptance criteria for that scenario.

### Fail

A test fails when the actual result does not meet one or more required acceptance criteria.

### Not Testable

Use **Not Testable** when the capability cannot be tested in the current application or environment.

Do not convert Not Testable into Pass.

Document why the test could not be performed and identify the required future condition.

### Test-Level Rule

A test receives an overall **Pass** only when all required acceptance criteria for that scenario are met.

One passing element does not cancel a failed mandatory criterion.

When a test is Not Testable, record the reason and the Evidence Reference for the limitation when available.

---

# Section 5: Evaluate Defects and Gaps

When a test fails, determine whether the result represents:

**Defect:** The product does not behave as required.

**Requirement Gap:** The requirement or acceptance criteria are incomplete or unclear.

**Data Issue:** The underlying data or source information is incorrect, incomplete, or outdated.

**Process Issue:** The product may work, but a business or operational process is missing or ineffective.

**Enhancement:** The product works as required, but a future improvement may provide additional value.

Classify each issue:

| Issue ID | Test ID | Issue | Type | Business Impact | Recommended Action | Evidence Reference |
| -------- | ------- | ----- | ---- | --------------- | ------------------ | ------------------ |
|          |         |       |      |                 |                    |                    |
|          |         |       |      |                 |                    |                    |
|          |         |       |      |                 |                    |                    |

The Evidence Reference should identify the proof supporting the issue classification.

---

# Section 6: Assign Defect Severity

Use four simple severity levels.

### Critical

The issue creates unacceptable risk or prevents a critical business function from being safely used.

Examples:

* Unauthorized information exposure
* Materially incorrect policy guidance affecting a critical decision
* Critical MVP function cannot be used
* A required control is bypassed

### High

The issue significantly affects a key requirement or user task but does not create immediate critical risk.

### Medium

The issue affects functionality, usability, or efficiency but the primary business task can still be completed.

### Low

The issue has limited business impact and does not materially prevent successful use.

Record:

| Issue ID | Severity | Reason | Must Be Fixed Before Release? | Evidence Reference |
| -------- | -------- | ------ | ----------------------------- | ------------------ |
|          |          |        |                               |                    |
|          |          |        |                               |                    |
|          |          |        |                               |                    |

Severity should be based on **business and user impact**, not simply how difficult an issue is to fix.

---

# Section 7: Conduct User Acceptance Testing

User Acceptance Testing (UAT) evaluates the product from the perspective of the people who are expected to use or benefit from it.

For this Build-Along, assume representative business users such as employees, Human Resources (HR), or another appropriate user group for your project.

Select at least **three user scenarios**.

For each scenario, define:

* The user's goal
* What the user is expected to do
* What a successful outcome looks like
* Whether the user would consider the result acceptable

Use:

| UAT ID | User Type | User Goal | Scenario | Expected Outcome | Actual Outcome | Acceptance Result | Evidence Reference |
| ------ | --------- | --------- | -------- | ---------------- | -------------- | ----------------- | ------------------ |
| UAT01  |           |           |          |                  |                | Pass/Fail         |                    |
| UAT02  |           |           |          |                  |                | Pass/Fail         |                    |
| UAT03  |           |           |          |                  |                | Pass/Fail         |                    |

The focus is not whether the system is technically impressive.

The focus is whether the intended user can accomplish the intended task successfully.

---

# Section 8: Evaluate UAT Acceptance

For each UAT scenario, ask:

### Task Completion

Could the user complete the intended task?

### Expected Outcome

Did the product produce the expected result?

### Usability

Could the user reasonably understand and use the result?

### Confidence

Would the user have reasonable confidence in using the result?

### Business Value

Does the product actually help the user accomplish the intended business outcome?

Record:

| UAT ID | Task Completed? | Expected Outcome Met? | Usable? | User Accepts? | Acceptance Result | Evidence Reference |
| ------ | --------------- | --------------------- | ------- | ------------- | ----------------- | ------------------ |
| UAT01  |                 |                       |         |               | Pass/Fail         |                    |
| UAT02  |                 |                       |         |               | Pass/Fail         |                    |
| UAT03  |                 |                       |         |               | Pass/Fail         |                    |

### UAT Pass/Fail Rule

**Pass:** The intended user can complete the required task, the expected outcome is achieved, and the user accepts the result.

**Fail:** The intended user cannot complete the required task, the expected outcome is not achieved, or the user does not accept the result.

---

# Section 9: Review Earlier AI Quality Evidence

Do not repeat all Milestone 7 testing.

Instead, review the results already collected.

Use your Milestone 7 findings to determine:

* Whether response quality met its target
* Whether unsupported-response results created a release concern
* Whether citation quality met its target
* Whether any critical AI quality issue remains unresolved

Record the key findings:

| Area                      | Previous Result | Target | Current Status | Release Impact | Evidence Reference |
| ------------------------- | --------------: | -----: | -------------- | -------------- | ------------------ |
| Response Accuracy         |                 |        |                |                |                    |
| Unsupported Response Rate |                 |        |                |                |                    |
| Citation Accuracy         |                 |        |                |                |                    |
| Citation Support          |                 |        |                |                |                    |

You are carrying forward evidence, not recreating the entire evaluation.

---

# Section 10: Review Security and Governance Evidence

Use your Milestone 8 results.

Identify:

* Critical security findings
* Production readiness gaps
* Required governance controls
* Open security or governance conditions

Determine whether any outstanding issue affects the product's ability to move forward.

Use:

| Area              | Finding | Current Status | Production Requirement? | Release Impact | Evidence Reference |
| ----------------- | ------- | -------------- | ----------------------- | -------------- | ------------------ |
| Access            |         |                |                         |                |                    |
| Data Protection   |         |                |                         |                |                    |
| Privacy/Logging   |         |                |                         |                |                    |
| Policy Governance |         |                |                         |                |                    |
| Auditability      |         |                |                         |                |                    |

Remember that a control that is not implemented in the student prototype may be a **production condition** rather than a failed prototype test.

---

# Section 11: Review Requirements Traceability

Trace each critical MVP requirement to its test evidence.

Use:

**Requirement → Acceptance Criteria → Test → Result → Evidence → Release Decision**

Complete:

| Requirement ID | Requirement | Acceptance Criteria | Test ID | Test Result | Evidence Reference | Release Impact |
| -------------- | ----------- | ------------------- | ------- | ----------- | ------------------ | -------------- |
|                |             |                     |         |             |                    |                |
|                |             |                     |         |             |                    |                |
|                |             |                     |         |             |                    |                |
|                |             |                     |         |             |                    |                |
|                |             |                     |         |             |                    |                |

The Evidence Reference should point to the same evidence used to support the related test result.

This creates a basic **requirements traceability** record.

It allows you to demonstrate not only that testing occurred, but that testing was connected to what the product was required to deliver.

---

# Section 12: Identify Open Issues

Before recommending release, identify all unresolved issues that could affect the decision.

Separate:

**Must Fix Before Release**

and

**Can Be Deferred**

Use:

| Issue ID | Issue | Severity | Must Fix Before Release? | Owner | Next Action | Evidence Reference |
| -------- | ----- | -------- | ------------------------ | ----- | ----------- | ------------------ |
|          |       |          |                          |       |             |                    |
|          |       |          |                          |       |             |                    |
|          |       |          |                          |       |             |                    |

Do not defer an issue simply because fixing it is inconvenient.

Base the decision on business impact, risk, user impact, and release requirements.

---

# Section 13: Make the UAT Decision

Based on the UAT evidence, determine whether the intended user needs have been met.

Choose one:

### Accepted

The intended users can complete the required tasks and the product meets the agreed acceptance criteria.

### Accepted with Conditions

The intended users can use the product, but specific issues or conditions must be addressed before or during release.

### Not Accepted

The product does not meet important user or business expectations and requires corrective action before it can proceed.

Document:

**UAT Decision:**
[Accepted / Accepted with Conditions / Not Accepted]

**Evidence Reference(s):**
[Evidence supporting the decision]

**Open Issues:**
[Important unresolved issues]

**Required Actions:**
[Actions needed]

---

# Section 14: Make the Release Recommendation

Combine your testing, UAT, AI evaluation, security, governance, and requirements evidence.

Choose one:

### Go

The product meets its defined acceptance criteria, no unresolved critical issues prevent release, and the remaining risks are acceptable.

### Hold

More evidence, testing, remediation, or stakeholder review is required before release.

### No-Go

The product does not meet critical requirements or has unresolved risks that make release unacceptable.

Document:

**Recommendation:**
[Go / Hold / No-Go]

**Evidence Reference(s):**
[Key evidence supporting the recommendation]

**Critical Issues:**
[Unresolved critical or high-impact issues]

**Conditions:**
[Required actions before release]

**Decision Owner:**
[Role responsible]

---

# Section 15: Define Exit Criteria

Create a short list of conditions that must be satisfied before release.

Your exit criteria should cover the most important areas:

* Critical MVP requirements
* Acceptance criteria
* UAT acceptance
* AI quality
* Security
* Governance
* Critical defects
* Required documentation

Record:

| Exit Criterion                          | Required? | Status | Evidence Reference |
| --------------------------------------- | --------- | ------ | ------------------ |
| Critical MVP requirements met           | Yes       |        |                    |
| UAT accepted                            | Yes       |        |                    |
| No unresolved critical defect           | Yes       |        |                    |
| AI quality requirements met             | Yes       |        |                    |
| Critical security requirements met      | Yes       |        |                    |
| Required governance controls identified | Yes       |        |                    |
| Release conditions documented           | Yes       |        |                    |

Use the Evidence Reference to identify the evidence supporting each exit criterion.

---

# Evidence Reference Standard

Use **Evidence Reference** consistently throughout this milestone.

An Evidence Reference should identify where the supporting proof can be found.

Examples include:

* Test ID
* Screenshot
* Captured response
* UAT observation
* Prior milestone result
* Defect ID
* Document or artifact
* Other recorded evidence

The purpose is traceability.

A reviewer should be able to move from:

**Requirement → Test → Result → Evidence → Decision**

without having to rely on memory or assumption.

---

# Deliverable: Testing & UAT Results Record

Create a **Testing & User Acceptance Testing Results Record** containing:

* At least six representative test scenarios
* Expected results and acceptance criteria
* Actual test results
* Test-level Pass/Fail results
* Evidence References for test results
* Defects and gaps
* Defect severity
* At least three UAT scenarios
* UAT results
* Evidence References for UAT results
* Requirements traceability
* Results carried forward from Milestone 7
* Results carried forward from Milestone 8
* Evidence References for carried-forward results
* Open issues
* Must-Fix versus Deferred decisions
* UAT decision
* Release recommendation: Go, Hold, or No-Go
* Release exit criteria
* Evidence supporting the decision

---

# PM Checkpoint

Before moving forward, you should be able to answer:

> **Does the product meet its agreed requirements and intended user needs well enough to move toward release?**

You should also be able to explain:

* The difference between functional testing and UAT
* How acceptance criteria are used during testing
* How to determine whether a test passes or fails
* How to distinguish defects from enhancements
* How to prioritize defects by business impact
* How UAT differs from technical testing
* How earlier AI evaluation and security findings should carry into release decisions
* How requirements traceability connects requirements to evidence
* How Evidence References support test and release decisions
* Which issues must be fixed before release
* What conditions can be deferred
* Why UAT acceptance does not automatically mean production readiness
* How the evidence supports your Go, Hold, or No-Go recommendation

---

# PM Perspective

**Testing provides evidence. UAT provides user acceptance. The PM uses both to make a release decision.**

You are not asking whether every possible problem has been eliminated.

You are asking:

**Did we build what we agreed to build?**

**Can the intended user accomplish the intended task?**

**Are the remaining risks acceptable?**

**Can we trace the decision back to evidence?**

**Is there enough evidence to move forward?**

The progression is:

**Requirement → Acceptance Criteria → Test → Evidence → Defect/Gaps → UAT → Exit Criteria → Release Recommendation**

The next milestone will focus on **Release & Deployment**, where you will turn the testing and UAT evidence into a controlled release decision and deployment plan.

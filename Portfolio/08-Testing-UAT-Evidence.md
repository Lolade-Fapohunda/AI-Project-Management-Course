# 08: Testing, UAT & Pilot Evidence

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Evidence Area:** Testing, User Acceptance Testing (UAT) & Pilot

---

# Purpose

This artifact demonstrates how PolicyAssist was prepared for functional testing, AI quality validation, User Acceptance Testing (UAT), and controlled pilot use.

The objective is to establish whether the product is:

* Functionally complete.
* Safe.
* Usable.
* Reliable.
* Acceptable to business users.
* Ready to progress toward production.

---

# Testing Strategy

Testing is organized across multiple levels.

```text
Requirements
    ↓
Functional Testing
    ↓
Negative Testing
    ↓
Edge-Case Testing
    ↓
Security Validation
    ↓
Regression Testing
    ↓
AI Evaluation
    ↓
UAT
    ↓
Pilot
    ↓
Release Decision
```

Each stage provides different evidence.

---

# Testing Vs. Evaluation Vs. UAT

| Activity      | Primary Question                                                       |
| ------------- | ---------------------------------------------------------------------- |
| Testing       | Does the system behave according to requirements?                      |
| AI Evaluation | How well does the AI perform?                                          |
| UAT           | Can business users accept the product for its intended use?            |
| Pilot         | Does the product work successfully in a controlled real-world setting? |

A successful technical test does not automatically mean UAT should pass.

---

# Test Objectives

Testing must demonstrate that PolicyAssist can:

* Accept policy questions.
* Retrieve relevant policy information.
* Exclude ineligible policies.
* Generate grounded responses.
* Display appropriate citations.
* Refuse unsupported questions.
* Handle false premises.
* Handle mixed questions.
* Handle multi-policy questions.
* Enforce access controls.
* Meet performance requirements.
* Recover appropriately from failures.

---

# Functional Testing

Functional testing validates required product behavior.

Examples include:

| Test Area            | Expected Behavior                                             |
| -------------------- | ------------------------------------------------------------- |
| Question Submission  | User can submit a question                                    |
| Policy Retrieval     | Relevant eligible evidence is retrieved                       |
| Authority Validation | Ineligible sources are excluded                               |
| Response Generation  | Response reflects retrieved evidence                          |
| Citation             | Supporting source is displayed when appropriate               |
| Unsupported Question | System refuses or identifies insufficient evidence            |
| False Premise        | Unsupported assumption is not accepted as fact                |
| Mixed Question       | Supported and unsupported portions handled separately         |
| Multi-Policy         | Relevant evidence from multiple policies is handled correctly |
| Refresh              | Updated policy information can be reprocessed                 |

---

# Negative Testing

Negative testing verifies that the system fails safely.

Examples:

### Unsupported Question

**Input:** Question requiring information not present in the knowledge base.

**Expected:** No fabricated answer.

### Ineligible Policy

**Input:** Question where the only matching document is superseded.

**Expected:** Superseded policy is not treated as authoritative.

### Conflicting Policy

**Input:** Two sources contain conflicting requirements with unresolved authority.

**Expected:** No automatic selection.

### Unauthorized Request

**Input:** User requests restricted information.

**Expected:** Access controls prevent disclosure.

---

# Edge-Case Testing

Edge cases test conditions that may not appear during normal use.

Examples include:

* Very short questions.
* Very long questions.
* Multiple questions in one request.
* Questions spanning multiple policies.
* Questions containing false assumptions.
* Questions with ambiguous terminology.
* Missing policy evidence.
* Conflicting policy metadata.
* Duplicate documents.
* Scanned documents.
* Policy changes during operation.

The objective is to identify behavior that normal happy-path testing may not reveal.

---

# Security Testing

Security validation should cover:

* Authentication.
* Authorization.
* Restricted information.
* Data leakage.
* Prompt injection.
* Unsafe requests.
* Logging.
* Access boundaries.
* Failure behavior.

Security testing is performed by appropriate technical and security stakeholders.

The Project Manager's role is to:

* Define security expectations.
* Coordinate testing.
* Track findings.
* Assign ownership.
* Monitor remediation.
* Require evidence.
* Apply release gates.

---

# Regression Testing

AI systems can change behavior when components change.

Regression testing should be triggered by changes to:

* Model.
* Embedding model.
* Retrieval configuration.
* Prompt.
* Policy data.
* Chunking.
* Application logic.
* Security controls.
* User experience.

Previously passing scenarios should be retested when affected functionality changes.

---

# Defect Management

Testing defects should be documented and managed through a controlled lifecycle.

```text id="6r3l8x"
Identify
   ↓
Log
   ↓
Classify
   ↓
Prioritize
   ↓
Assign
   ↓
Remediate
   ↓
Retest
   ↓
Close / Escalate
```

---

# Defect Severity

## Critical

Examples:

* Unauthorized disclosure.
* Critical security breach.
* Fabricated critical policy information.
* Severe business or compliance impact.

**Release:** No-Go.

## High

Examples:

* Incorrect policy answer.
* Incorrect citation.
* Active policy not retrieved.
* Major grounding failure.
* Significant multi-policy failure.

**Release:** Fix before production unless formally accepted through appropriate governance.

## Medium

Examples:

* Confusing response.
* Minor functional inconsistency.
* Usability issue.

## Low

Examples:

* Cosmetic formatting.
* Minor wording problem.

Severity should be based on **business impact**, not technical difficulty.

---

# UAT Strategy

UAT determines whether representative business users can accept PolicyAssist for its intended business purpose.

UAT should include:

* Realistic questions.
* Representative users.
* Expected outcomes.
* Acceptance criteria.
* Defect recording.
* Business approval.

---

# UAT Scenarios

The project defined ten core UAT scenarios.

| ID     | Scenario                      | Expected Result                  |
| ------ | ----------------------------- | -------------------------------- |
| UAT-01 | Remote Work                   | Correct approved policy answer   |
| UAT-02 | Attendance                    | Correct approved policy answer   |
| UAT-03 | Expense Reimbursement         | Correct approved policy answer   |
| UAT-04 | Information Security          | Correct approved policy answer   |
| UAT-05 | Code Of Conduct               | Correct approved policy answer   |
| UAT-06 | Unsupported Vacation Question | Safe refusal                     |
| UAT-07 | False Premise                 | Unsupported premise not accepted |
| UAT-08 | Multi-Policy Question         | Evidence correctly combined      |
| UAT-09 | Superseded / Draft Policy     | Ineligible source excluded       |
| UAT-10 | Conflicting Authority         | Human resolution required        |

---

# UAT Acceptance Criteria

UAT should satisfy:

* 100% of critical scenarios executed.
* 100% of critical UAT failures resolved or formally dispositioned.
* All required policy categories tested.
* User satisfaction ≥ 85%.
* No unresolved critical security defect.
* No unresolved critical business defect.

---

# UAT Evidence

Each UAT case should record:

| Field           | Purpose              |
| --------------- | -------------------- |
| UAT ID          | Unique identifier    |
| User / Role     | Participant          |
| Scenario        | Business scenario    |
| Question        | User input           |
| Expected Result | Business expectation |
| Actual Result   | Observed behavior    |
| Pass / Fail     | Outcome              |
| Defect ID       | Related issue        |
| Comments        | User feedback        |
| Approval        | Business acceptance  |

---

# UAT Business Acceptance

Technical completion does not equal business acceptance.

The business must determine whether:

* Responses are understandable.
* Information is useful.
* Citations provide confidence.
* Unsupported questions are handled appropriately.
* Users can complete the intended task.
* The system fits the business workflow.

---

# Pilot Strategy

Pilot deployment should occur after sufficient UAT evidence exists.

The pilot should be:

* Controlled.
* Limited in scope.
* Time-bound.
* Monitored.
* Supported by clear success criteria.
* Capable of rollback.

The pilot is not a substitute for testing.

It is an additional source of real-world evidence.

---

# Pilot Objectives

The pilot should determine:

* Whether users can successfully use the product.
* Whether responses meet expectations.
* Whether users trust the evidence.
* Whether unexpected failure patterns emerge.
* Whether performance remains acceptable.
* Whether monitoring detects problems.
* Whether support and escalation processes work.

---

# Pilot Success Criteria

The project should target:

| Metric                               | Target |
| ------------------------------------ | -----: |
| User Satisfaction                    |  ≥ 85% |
| Critical Security Incidents          |      0 |
| Critical Defects                     |      0 |
| Unsupported Questions Safely Handled |   100% |
| Citation Correctness                 |   100% |
| Monitoring Coverage                  |   100% |

Additional product-specific evaluation targets remain applicable.

---

# Pilot Feedback

Feedback should be separated into:

### Defects

The system does not behave according to an established requirement.

### Enhancement Requests

The user wants functionality that is outside the current requirements.

### Usability Feedback

The functionality works but is difficult or confusing to use.

### Business Feedback

The product may not fully fit the intended business workflow.

This distinction prevents every user comment from becoming a technical defect.

---

# Pilot Exit Criteria

The pilot should not be considered successful merely because users participated.

Exit criteria should include:

* Required pilot scenarios completed.
* No critical security incidents.
* No unresolved critical defects.
* User satisfaction meets target.
* Citation behavior meets target.
* Unsupported questions handled safely.
* Monitoring functioning.
* Significant feedback reviewed.
* Required corrective actions identified.
* Sponsor/business approval obtained.

---

# Testing Evidence

The project should maintain evidence including:

* Test cases.
* Test results.
* UAT records.
* Defect records.
* Evaluation results.
* Security findings.
* Performance results.
* Pilot feedback.
* Retest results.
* Approvals.

Evidence should be traceable to requirements.

---

# Requirements Traceability

Testing should connect back to requirements.

Example:

| Requirement         | Test          | Result                | Evidence           |
| ------------------- | ------------- | --------------------- | ------------------ |
| Policy Retrieval    | TEST-RET-001  | Pending / Pass / Fail | Test Result        |
| Grounding           | TEST-AI-001   | Pending / Pass / Fail | Evaluation         |
| Citation            | TEST-AI-002   | Pending / Pass / Fail | Evaluation         |
| Unsupported Refusal | TEST-AI-003   | Pending / Pass / Fail | Evaluation         |
| Authorization       | TEST-SEC-001  | Pending               | Security Evidence  |
| Performance         | TEST-PERF-001 | Pending               | Performance Report |

This provides evidence that requirements were actually validated.

---

# Current Prototype Testing Evidence

Initial prototype testing has demonstrated:

* Policy ingestion.
* Semantic retrieval.
* Policy eligibility filtering.
* Grounded responses.
* Citation handling.
* Unsupported-question refusal.
* False-premise handling.
* Mixed-question handling.
* Multiple-policy ingestion.
* User interaction.

These results demonstrate initial functional feasibility.

They do not constitute complete UAT or production testing.

---

# Known Testing Gap

The project identified weaker performance on multi-policy questions.

This must be treated as a testing and evaluation issue rather than ignored because single-policy questions perform well.

Required actions include:

1. Add representative multi-policy cases.
2. Identify failure patterns.
3. Determine root cause.
4. Create defects where appropriate.
5. Remediate.
6. Retest.
7. Run regression evaluation.
8. Document results.

---

# Current Testing Status

| Area                         | Status                         |
| ---------------------------- | ------------------------------ |
| Prototype Functional Testing | Initial testing completed      |
| Negative Testing             | Initial scenarios demonstrated |
| Edge-Case Testing            | Requires Formal Validation     |
| Security Testing             | Pending                        |
| Regression Testing           | Pending Formal Baseline        |
| AI Evaluation                | Formal evaluation pending      |
| UAT                          | Pending                        |
| Pilot                        | Pending                        |
| Final Test Evidence          | Pending                        |

---

# Testing & UAT Release Gate

Production readiness requires:

* [ ] 100% critical functional requirements tested.
* [ ] 100% MVP must-have functionality tested.
* [ ] 0 unresolved critical functional defects.
* [ ] Negative scenarios pass safely.
* [ ] Critical edge cases tested.
* [ ] Authorization controls validated.
* [ ] 0 critical security findings.
* [ ] 0 unauthorized access.
* [ ] 0 critical data leakage.
* [ ] Regression-triggering changes tested.
* [ ] Performance target validated.
* [ ] Critical UAT scenarios completed.
* [ ] Critical UAT failures resolved or dispositioned.
* [ ] User satisfaction ≥ 85%.
* [ ] Pilot success criteria met.
* [ ] Monitoring operational.
* [ ] Evidence documented and approved.

---

# PM Decision

The Project Manager should not interpret:

> "The application works."

as:

> "Testing is complete."

A production decision requires evidence across:

* Functional behavior.
* AI quality.
* Security.
* UAT.
* Performance.
* Pilot results.
* Defect status.

---

# Current Testing Decision

**Decision:** Continue testing and validation.

**Production Position:** HOLD.

The project has demonstrated initial functional feasibility but has not completed the evidence required for production acceptance.

---

# Conditions To Remove HOLD

1. Complete formal test execution.
2. Complete security validation.
3. Complete the formal AI evaluation.
4. Resolve significant multi-policy failures.
5. Complete UAT.
6. Complete controlled pilot.
7. Validate performance.
8. Resolve or formally disposition release-blocking defects.
9. Confirm monitoring readiness.
10. Document approvals.

---

# Portfolio Evidence

This artifact demonstrates the ability to:

* Build an AI testing strategy.
* Distinguish testing from evaluation and UAT.
* Design negative and edge-case testing.
* Manage security testing at the PM level.
* Manage defects.
* Define severity.
* Plan UAT.
* Define business acceptance.
* Plan controlled pilot deployment.
* Separate defects from enhancements and feedback.
* Establish measurable exit criteria.
* Connect testing evidence to requirements.
* Use testing evidence in release decisions.

---

# Key PM Judgment

The most important testing decision was to treat **business acceptance as separate from technical functionality**.

A system can technically work while still failing to meet:

* Business expectations.
* Security requirements.
* AI quality thresholds.
* Usability requirements.
* UAT expectations.

Therefore, testing, evaluation, UAT, and pilot evidence must be considered together before production release.

---

# Final Testing Principle

> **Testing demonstrates behavior, evaluation measures AI quality, UAT establishes business acceptance, and pilot evidence demonstrates controlled real-world readiness.**

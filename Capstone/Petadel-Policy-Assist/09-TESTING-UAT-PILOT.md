# 09: Testing, UAT & Pilot

## Purpose

This document defines how Petadel PolicyAssist AI will be tested, validated by users, and evaluated during a controlled pilot.

Testing answers:

> **Does the system behave as expected?**

Evaluation answers:

> **How well does the AI perform?**

User Acceptance Testing (UAT) answers:

> **Does the solution meet the business user's needs?**

Pilot testing answers:

> **Can the solution operate successfully with a controlled group of real users?**

The Project Manager coordinates these activities and ensures that release decisions are based on documented evidence.

---

## 1. Testing Objective

Testing must determine whether PolicyAssist:

* Performs required functions.
* Retrieves appropriate policy information.
* Produces grounded responses.
* Handles unsupported questions safely.
* Applies access controls.
* Handles edge cases.
* Meets performance requirements.
* Provides correct citations.
* Supports real user workflows.
* Is ready for controlled adoption.

---

## 2. Testing Vs. Evaluation Vs. UAT

| Activity      | Primary Question                                                  | Owner                  |
| ------------- | ----------------------------------------------------------------- | ---------------------- |
| Testing       | Does the system work as designed?                                 | Technical Team         |
| AI Evaluation | How well does the AI perform?                                     | AI/Technical Team + PM |
| UAT           | Does it meet business needs?                                      | Business Users         |
| Pilot         | Does it work successfully in a controlled real-world environment? | PM + Business Owner    |

These activities are complementary and should not be treated as interchangeable.

---

## 3. Testing Strategy

The testing strategy should be risk-based.

Higher-risk capabilities require stronger validation.

### High-Risk Areas

* Policy authority
* Policy versioning
* Access control
* AI-generated answers
* Hallucination
* Citations
* Unsupported questions
* Security
* Data leakage
* Performance
* Human escalation

---

## 4. Test Levels

Testing should occur at appropriate levels.

### Component Testing

Validates individual components.

Examples:

* Document ingestion
* Metadata validation
* Retrieval
* Citation logic

### Integration Testing

Validates interactions between components.

Example:

```text
Document
→ Ingestion
→ Embedding
→ Vector Database
→ Retrieval
→ LLM
→ Grounding
→ Citation
→ User Response
```

### System Testing

Validates the complete PolicyAssist application.

### User Acceptance Testing

Validates the product against business expectations.

### Pilot Testing

Validates the solution with a controlled group of users.

---

## 5. Functional Testing

Functional testing verifies that required functions work.

Examples:

* User submits a question.
* Policy is retrieved.
* Response is generated.
* Source is displayed.
* Unsupported question is refused.
* User can submit another question.
* Authorized users can access permitted information.
* Unauthorized access is blocked.

### Acceptance Criteria

* **100% of critical functional requirements have documented test coverage.**
* **100% of MVP Must-Have functionality is tested before MVP acceptance.**
* **0 unresolved critical functional defects at release.**

---

## 6. Negative Testing

Negative testing verifies that the system behaves safely when conditions are invalid or unsupported.

Examples:

* Policy does not exist.
* Policy is draft.
* Policy is superseded.
* Policy authority is unclear.
* User is unauthorized.
* Question is outside scope.
* Evidence is insufficient.
* User provides a false premise.

### Expected Behavior

PolicyAssist should not invent an answer simply because a question was asked.

### Acceptance Criterion

**100% of defined negative test scenarios must produce the expected safe behavior.**

---

## 7. Edge-Case Testing

Edge cases test unusual or boundary conditions.

Examples:

* Very short question
* Very long question
* Ambiguous wording
* Multiple questions in one request
* Multiple policy areas
* Similar policy titles
* Conflicting policies
* Missing metadata
* Unreadable document
* No matching evidence

### Acceptance Criterion

**100% of critical defined edge cases must have documented expected behavior and test results before production release.**

---

## 8. Security Testing

Security testing validates that appropriate security controls work as intended.

Testing should address:

* Authentication
* Authorization
* Access restrictions
* Data leakage
* Sensitive information exposure
* Prompt injection
* Malicious document content
* Logging
* Administrative access

### PM Responsibility

The PM coordinates security testing with qualified security personnel.

The PM does not need to personally perform offensive security testing.

### Acceptance Criteria

* Authentication controls validated = **100%**
* Authorization controls validated = **100%**
* Critical security findings = **0**
* Unauthorized policy access = **0**
* Critical data leakage findings = **0**

---

## 9. Regression Testing

Regression testing determines whether changes broke existing functionality.

Regression testing should be considered after changes to:

* LLM
* Embedding model
* Prompt
* Retrieval threshold
* Chunking
* Citation logic
* Policy data
* Access controls
* Application logic

### Acceptance Criterion

**100% of defined regression-triggering changes must have documented regression testing before release approval.**

---

## 10. Performance Testing

Performance testing validates whether PolicyAssist meets the response-time requirement.

### Measurement

Response time is measured from:

> **Question submission → Complete response displayed**

### MVP Acceptance Criteria

* At least **95%** of representative requests complete within **10 seconds**.
* **100%** complete within **15 seconds**.
* At least **30 representative requests** are measured.
* Tests include direct, paraphrased, multi-policy, unsupported, and refusal-required questions.
* Every request exceeding 15 seconds is recorded as a performance failure.

### Evidence

| Measure              | Result |
| -------------------- | ------ |
| Number of Requests   |        |
| Average              |        |
| Median               |        |
| 95th Percentile      |        |
| Maximum              |        |
| Requests >10 Seconds |        |
| Requests >15 Seconds |        |
| Environment          |        |
| Model Version        |        |
| Result               |        |

---

## 11. Defect Management

Every significant testing failure should be documented.

### Defect Fields

| Field             | Description               |
| ----------------- | ------------------------- |
| Defect ID         | Unique identifier         |
| Description       | What failed               |
| Test Case         | Related test              |
| Severity          | Business/technical impact |
| Priority          | Urgency                   |
| Environment       | Where failure occurred    |
| Owner             | Responsible person        |
| Root Cause        | Cause                     |
| Corrective Action | Required fix              |
| Retest Result     | Pass/Fail                 |
| Status            | Open/Closed               |

---

## 12. Defect Severity

### Critical

Examples:

* Security breach
* Unauthorized access
* Fabricated policy information
* Critical data leakage
* System failure affecting safe operation

**Release Impact: No-Go**

### High

Examples:

* Incorrect policy answer
* Incorrect citation
* Active policy not retrieved
* Major UAT failure
* Significant security weakness

**Release Impact: Must be resolved or formally dispositioned before production**

### Medium

Examples:

* Confusing response
* Minor functional problem
* Usability issue

### Low

Examples:

* Cosmetic issue
* Minor formatting issue

---

## 13. Defect Lifecycle

```text
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
Fix
   ↓
Retest
   ↓
Regression Test
   ↓
Close
```

A defect should not be closed merely because a developer states that it was fixed.

Evidence of successful retesting is required.

---

## 14. User Acceptance Testing

UAT determines whether the solution meets business expectations.

UAT users should represent the intended user population.

### UAT Objectives

Users should validate:

* Correct answers
* Useful responses
* Appropriate citations
* Safe refusals
* Ease of use
* Appropriate escalation
* Expected workflows
* Business relevance

---

## 15. UAT Participants

Participants may include:

* Business owner
* Policy owners
* Representative employees
* Human Resources
* Finance
* Information Security
* Operations
* Project Manager
* Other approved stakeholders

Participants should understand what they are expected to validate.

---

## 16. UAT Acceptance Criteria

UAT should have measurable criteria.

Examples:

* **100% of critical UAT scenarios executed.**
* **100% of critical UAT failures resolved or formally dispositioned before production.**
* **100% of required policy categories tested.**
* User satisfaction target ≥ **85%**.
* No unresolved critical security issue.
* No unresolved critical business defect.

---

## 17. PolicyAssist UAT Scenarios

The following scenarios provide the minimum UAT baseline.

| ID     | Scenario                      | Expected Result                        |
| ------ | ----------------------------- | -------------------------------------- |
| UAT-01 | Remote Work                   | Correct remote-work policy response    |
| UAT-02 | Attendance                    | Correct attendance response            |
| UAT-03 | Expense                       | Correct reimbursement response         |
| UAT-04 | Information Security          | Correct security-policy response       |
| UAT-05 | Code Of Conduct               | Correct conduct response               |
| UAT-06 | Unsupported Vacation Question | Safe refusal                           |
| UAT-07 | False Premise                 | Does not accept unsupported claim      |
| UAT-08 | Multi-Policy Question         | Correctly combines applicable evidence |
| UAT-09 | Superseded/Draft Policy       | Does not use ineligible policy         |
| UAT-10 | Conflicting Authority         | Holds/escalates rather than guessing   |

---

## 18. UAT Scenario Structure

Each UAT scenario should include:

| Field              | Description             |
| ------------------ | ----------------------- |
| Scenario ID        | Unique identifier       |
| Business Objective | What is being validated |
| User Role          | Intended user           |
| Input              | User action/question    |
| Expected Result    | Required outcome        |
| Actual Result      | Observed outcome        |
| Evidence           | Supporting evidence     |
| Pass/Fail          | Result                  |
| Defect ID          | Related defect          |
| UAT Owner          | Responsible participant |

---

## 19. UAT Failure Handling

A failed UAT scenario should trigger:

1. Defect documentation.
2. Severity assessment.
3. Root-cause analysis.
4. Corrective action.
5. Retesting.
6. Regression testing where appropriate.
7. UAT confirmation.

### PM Rule

> **A failed critical UAT scenario is a release blocker until resolved or formally approved through governance.**

---

## 20. Pilot Testing

A pilot introduces the product to a limited group before broader release.

### Pilot Objectives

The pilot should validate:

* Real-world usability
* Business value
* User trust
* Response quality
* Operational readiness
* Support requirements
* Monitoring
* Feedback processes

---

## 21. Pilot Population

The pilot should use a controlled user group.

Consider:

* Representative departments
* Different user roles
* Expected usage patterns
* Accessibility needs
* Policy usage frequency

The pilot should be large enough to produce useful evidence but controlled enough to manage risk.

---

## 22. Pilot Success Criteria

Example pilot targets:

| Measure                              | Target |
| ------------------------------------ | -----: |
| User Satisfaction                    |   ≥85% |
| Critical Security Incidents          |      0 |
| Critical Defects                     |      0 |
| Unsupported Questions Safely Handled |   100% |
| Citation Correctness                 |   100% |
| Required Monitoring Coverage         |   100% |
| Pilot UAT Completion                 |   100% |

---

## 23. Pilot Feedback

Feedback should be classified.

### Positive Feedback

Indicates strengths.

### Improvement Feedback

Indicates potential product improvements.

### Defect

Indicates failure against an expected requirement.

### Risk

Indicates potential future harm or failure.

Feedback should not automatically become a defect.

---

## 24. Pilot Monitoring

During the pilot, monitor:

* Response time
* Accuracy indicators
* Refusal behavior
* Citation issues
* User satisfaction
* Escalations
* Security events
* Defects
* Policy changes
* Usage patterns

Material problems should trigger investigation.

---

## 25. Pilot Exit Criteria

The pilot should not end simply because the calendar period has expired.

Exit criteria should include:

* Required pilot scenarios completed.
* User feedback collected.
* Critical defects = 0.
* Critical security findings = 0.
* Major issues addressed.
* Performance reviewed.
* Monitoring functioning.
* Support process established.
* Business owner approval obtained.
* Production recommendation documented.

---

## 26. Test Evidence

Testing evidence may include:

* Test cases
* Test results
* Screenshots
* Logs
* Evaluation reports
* Defect records
* UAT sign-offs
* Security results
* Performance measurements
* Pilot feedback
* Pilot metrics

### Evidence Principle

> **No Evidence = Not Yet Accepted.**

---

## 27. Test Readiness Gate

Before formal testing begins, confirm:

* Requirements are defined.
* Acceptance criteria exist.
* Test data is available.
* Test environment is available.
* Expected results are documented.
* Test participants are identified.
* Defect process is established.

---

## 28. UAT Readiness Gate

Before UAT begins:

* MVP functionality is complete.
* Critical functional testing has passed.
* AI evaluation is complete enough for UAT.
* Required policies are validated.
* Test scenarios are approved.
* UAT users are identified.
* Defect process is ready.
* UAT acceptance criteria are documented.

---

## 29. Pilot Readiness Gate

Before pilot launch:

* UAT is complete.
* Critical defects are resolved.
* Security validation is complete.
* Data governance is validated.
* Monitoring is operational.
* Support process exists.
* Escalation process exists.
* Rollback procedure exists.
* Pilot users are identified.
* Pilot success criteria are approved.

---

## 30. Release Readiness Relationship

Testing, evaluation, UAT, and pilot results all contribute to release readiness.

```text
Testing
   ↓
AI Evaluation
   ↓
Security Validation
   ↓
UAT
   ↓
Pilot
   ↓
Release Decision
```

Failure at a critical gate may stop progression.

---

## 31. Practical Exercise 9: Plan Testing, UAT & Pilot

### Scenario

PolicyAssist has completed development.

The team reports:

* Functional testing is 95% complete.
* AI evaluation meets the accuracy targets.
* Citation correctness is 100%.
* One High-severity defect remains open.
* Authorization testing is incomplete.
* UAT has not started.
* Monitoring is partially implemented.
* Leadership wants to begin the pilot tomorrow.

### Your Task

As the Project Manager:

1. Determine whether the system is ready for UAT.
2. Determine whether it is ready for pilot.
3. Identify missing evidence.
4. Identify release blockers.
5. Define UAT acceptance criteria.
6. Define pilot success criteria.
7. Determine required security validation.
8. Define defect handling.
9. Determine the appropriate PM decision.

### PM Decision

Choose:

* **Proceed**
* **Proceed With Conditions**
* **Hold**

Explain which conditions must be satisfied before progression.

---

## 32. Artifact / Output

Complete:

**Testing, UAT & Pilot Plan**

The artifact should contain:

* Testing strategy
* Test levels
* Functional tests
* Negative tests
* Edge cases
* Security testing
* Regression testing
* Performance testing
* Defect process
* UAT plan
* UAT scenarios
* UAT acceptance criteria
* Pilot plan
* Pilot success criteria
* Pilot monitoring
* Exit criteria
* Evidence requirements
* Release readiness decision

---

## 33. PM Decision

The Project Manager should not allow schedule pressure to replace validation.

A system that is technically functional may still be:

* Unsafe
* Untrusted
* Poorly governed
* Unusable
* Incomplete
* Not ready for production

### Decision Principle

> **Testing proves behavior. Evaluation measures AI quality. UAT proves business acceptance. Pilot testing validates controlled real-world use.**

---

## 34. Decision / Reflection

Ask:

> **"If the project team tells me the product is ready, what evidence would I need to independently support that decision?"**

Your answer should include testing, evaluation, security, UAT, pilot, defects, monitoring, and release criteria.

---

## Competency Check

You should now be able to:

* Explain testing, evaluation, UAT, and pilot differences.
* Build a risk-based testing strategy.
* Define functional, negative, edge-case, and regression testing.
* Understand security testing at the PM level.
* Define measurable performance testing.
* Establish defect severity and release impact.
* Design UAT scenarios.
* Define measurable UAT acceptance criteria.
* Design a controlled pilot.
* Define pilot success and exit criteria.
* Require evidence before accepting results.
* Identify testing and UAT release blockers.
* Make evidence-based testing and readiness decisions.

---

## Key Takeaways

* Testing is necessary but not sufficient for AI release.
* AI evaluation measures AI quality.
* Negative testing is essential for preventing unsafe answers.
* Security testing must validate access and data protections.
* Regression testing protects previously validated behavior.
* UAT validates business acceptance.
* Pilot testing validates controlled real-world use.
* Critical defects and security findings can block release.
* Performance must be measured.
* User feedback should be distinguished from defects.
* Every major testing decision should have evidence.
* **No Evidence = Not Yet Accepted.**

---

## Connection To Capstone

This document provides the testing, UAT, and pilot framework for Petadel PolicyAssist AI.

It directly supports:

* `03-REQUIREMENTS.md`
* `04-PRODUCT-BACKLOG.md`
* `05-ARCHITECTURE.md`
* `06-DATA-GOVERNANCE.md`
* `07-EVALUATION-PLAN.md`
* `08-RISK-SECURITY-GOVERNANCE.md`
* `10-RELEASE-DEPLOYMENT.md`
* `11-MONITORING-CONTINUOUS-IMPROVEMENT.md`
* `13-RISK-REGISTER.md`
* `14-TRACEABILITY.md`
* `16-FINAL-GO-HOLD-NO-GO.md`

Testing, evaluation, UAT, and pilot results provide the evidence required for the final release decision.

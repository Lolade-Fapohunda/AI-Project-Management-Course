# Milestone 8: Security & Governance

## PM Objective

Determine whether the Artificial Intelligence (AI) product protects information, enforces appropriate access, follows defined governance requirements, and operates safely within its intended use.

## Hands-On Objective

Evaluate PolicyAssist from a Product Management (PM) perspective by testing the security and governance behaviors supported by the current application and identifying the controls required for a production-ready AI product.

In Milestone 7, you evaluated **response and citation quality**.

In this milestone, you will evaluate whether PolicyAssist can provide useful AI assistance **without creating unacceptable security, privacy, access, or governance risks**.

Your primary question is:

> **Can PolicyAssist provide useful assistance while protecting information and operating within defined security and governance requirements?**

---

# What You Can Test vs. What You Will Assess

Not every production security control is implemented in the student starter application.

You should **test what the current application supports** and **define or assess what a production product would require**.

### You Can Test in the Current Application

You can test:

* Supported policy questions
* Unsupported questions
* Refusal or escalation behavior
* Whether the AI invents unsupported information
* Whether available policy content appears appropriate for employee use
* Whether policy versions and status information are identifiable
* Whether responses expose information outside the intended policy content
* Basic data and source-handling risks observable through the application

### You Will Assess as a PM

You will define or assess production requirements for:

* Authentication
* Role-based access control
* Unauthorized-user testing
* Confidential information protection
* Privacy controls
* Logging and retention
* Auditability
* Policy ownership
* Change control
* Governance ownership
* Production security testing

> **Do not claim that a control has been tested when the current application does not implement that control.**

When a capability is not implemented, identify it as a **production requirement, future test, risk, or governance recommendation**.

---

# Section 1: Identify Users and Access Levels

Start by identifying who may use PolicyAssist.

Consider:

* Employees
* Human Resources (HR)
* Information Technology (IT)
* Policy owners
* Administrators

Determine what each user should be able to access.

| User Type     | Example Use             | Information They Should Access                   | Access Level |
| ------------- | ----------------------- | ------------------------------------------------ | ------------ |
| Employee      | General policy question | Employee-approved policy information             |              |
| HR            | Policy support          | Applicable HR and employee policy information    |              |
| IT            | System administration   | Technical/system information appropriate to role |              |
| Policy Owner  | Policy management       | Policies they are responsible for                |              |
| Administrator | System administration   | Administrative information required for the role |              |

Do not assume that every user should have the same access.

---

# Section 2: Define Access Requirements

For each user type, identify:

* What they should be allowed to see
* What they should not be allowed to see
* Why the restriction exists
* What should happen when access is denied

Complete:

| User Type | Allowed Information | Restricted Information | Reason for Restriction | Expected Denial Behavior |
| --------- | ------------------- | ---------------------- | ---------------------- | ------------------------ |
|           |                     |                        |                        |                          |
|           |                     |                        |                        |                          |
|           |                     |                        |                        |                          |
|           |                     |                        |                        |                          |

### Important

The current student starter may not contain authentication or role-based permissions.

When those controls are not implemented, document them as **production requirements** rather than treating them as tested controls.

---

# Section 3: Test Current Application Security Behavior

Run **three security-related tests** using the current PolicyAssist application.

Include:

1. A supported policy question
2. An unsupported question
3. A question that helps determine whether the system provides information outside the available policy content

The unsupported-question test will also allow you to evaluate whether the system refuses or escalates appropriately. Do not create a separate unsupported-question test for this milestone.

For each test, record:

| Test ID | Question | Expected Behavior | Actual Result | Security/Governance Observation |
| ------- | -------- | ----------------- | ------------- | ------------------------------- |
| S01     |          |                   |               |                                 |
| S02     |          |                   |               |                                 |
| S03     |          |                   |               |                                 |

The purpose of these tests is to observe what the current application actually does.

Do not infer that a security control exists simply because the application does not appear to expose a problem during a small test.

---

# Section 4: Evaluate the Unsupported-Question Result

Use the unsupported-question test from Section 3.

Evaluate whether the system:

* Avoids inventing information
* Clearly communicates its limitation
* Provides an appropriate response
* Escalates when required

Record:

| Test ID | Expected Behavior | Actual Behavior | Unsupported Information? | Appropriate Escalation? | Pass/Fail |
| ------- | ----------------- | --------------- | ------------------------ | ----------------------- | --------- |
| S02     |                   |                 |                          |                         |           |

### Pass/Fail Rule

**Pass:** The system does not invent an answer and follows the expected refusal or escalation behavior.

**Fail:** The system provides unsupported guidance or fails to follow the expected refusal or escalation behavior.

This is the same test already performed in Section 3. You are analyzing its security and governance implications here, not running another test.

---

# Section 5: Assess Unauthorized Access as a Production Requirement

The current student application may not provide authentication or role-based access controls.

Do not attempt to demonstrate a security control that does not exist.

Instead, define how an unauthorized-access test **should** work once those controls are implemented.

Create at least **one future unauthorized-access test scenario**.

Example:

> An employee attempts to access information classified as restricted to Human Resources.

Document:

| Future Test | User Type | Restricted Request | Expected Behavior | Why It Matters |
| ----------- | --------- | ------------------ | ----------------- | -------------- |
|             |           |                    |                   |                |

### Production Pass/Fail Rule

**Pass:** An unauthorized user is prevented from receiving restricted information.

**Fail:** Restricted information is disclosed or the access control can be bypassed.

**Target: 0 authorization issues.**

This is a **defined future test** unless the version of PolicyAssist you are using includes working access controls.

---

# Section 6: Assess Data Protection

Identify the types of information PolicyAssist may process.

Examples include:

* Policy documents
* Employee-facing information
* Internal organizational information
* Access or authorization information
* Administrative or technical information

Classify each type as:

* Public
* Internal
* Restricted
* Confidential

Record:

| Information Type | Classification | Who Should Access It? | Protection Needed | Risk if Exposed |
| ---------------- | -------------- | --------------------- | ----------------- | --------------- |
|                  |                |                       |                   |                 |
|                  |                |                       |                   |                 |
|                  |                |                       |                   |                 |

Ask:

> **What is the impact if this information is exposed to the wrong user?**

Focus on business impact rather than assuming that all information has the same sensitivity.

---

# Section 7: Assess Privacy and Logging

Consider what information could be collected through:

* User questions
* AI responses
* Feedback
* Application logs
* Monitoring
* Error information

Determine:

* What information needs to be collected?
* What information should not be collected unnecessarily?
* Who should have access to logs?
* How long should information be retained?
* Could logs expose sensitive information?

Complete:

| Area              | What Should Be Collected? | What Should Be Protected or Limited? | Recommended Control |
| ----------------- | ------------------------- | ------------------------------------ | ------------------- |
| User Questions    |                           |                                      |                     |
| Responses         |                           |                                      |                     |
| Feedback          |                           |                                      |                     |
| Logs              |                           |                                      |                     |
| Error Information |                           |                                      |                     |

> **Do not assume that collecting more information automatically improves the product.**

The goal is to collect what is necessary for security, support, monitoring, and improvement while limiting unnecessary exposure.

---

# Section 8: Evaluate Policy Governance

PolicyAssist depends on authoritative policy information.

Determine how the production product should handle:

* Policy ownership
* Approval status
* Versioning
* Effective dates
* Review dates
* Outdated policies
* Duplicate policies
* Conflicting policies

Use:

| Governance Area     | Requirement | Current State | Gap | Recommended Control |
| ------------------- | ----------- | ------------- | --- | ------------------- |
| Policy Owner        |             |               |     |                     |
| Approval Status     |             |               |     |                     |
| Version             |             |               |     |                     |
| Effective Date      |             |               |     |                     |
| Review Date         |             |               |     |                     |
| Outdated Content    |             |               |     |                     |
| Conflicting Content |             |               |     |                     |

Ask:

> **Who is accountable for ensuring that the AI uses an authoritative and current policy?**

---

# Section 9: Evaluate AI Governance

Identify the controls needed to keep PolicyAssist within its intended purpose.

Consider:

* Defined product scope
* Approved information sources
* Human escalation
* Quality evaluation
* Access controls
* Monitoring
* Feedback
* Incident management
* Change control
* Regression testing
* Policy review
* Governance ownership

Determine at least **three governance controls** that PolicyAssist should have.

| Governance Control | Purpose | Owner | Evidence of Control | Current or Future? |
| ------------------ | ------- | ----- | ------------------- | ------------------ |
|                    |         |       |                     |                    |
|                    |         |       |                     |                    |
|                    |         |       |                     |                    |

Use **Current** when the control is already implemented and observable.

Use **Future** when it is required for the production product but is not currently implemented.

---

# Section 10: Evaluate Auditability

Auditability means being able to understand and investigate important product activity when needed.

Consider whether a production PolicyAssist environment should allow the team to determine:

* What changed
* When it changed
* Who approved the change
* Which policy version was active
* Which application or model version was used
* When a quality issue was identified
* What action was taken

Identify at least **two areas where auditability matters**.

| Area | What Should Be Traceable? | Why It Matters | Current or Future Requirement? |
| ---- | ------------------------- | -------------- | ------------------------------ |
|      |                           |                |                                |
|      |                           |                |                                |

Do not claim auditability has been tested unless the current application actually provides the necessary capability.

---

# Section 11: Identify Security and Governance Gaps

Review your findings and identify at least **three gaps**.

A gap exists when the current product or process does not adequately meet the required security or governance expectation.

Examples include:

* No authentication
* No role-based access control
* No authorization enforcement
* Weak access rules
* Outdated policy content
* Missing policy ownership
* No clear escalation process
* Excessive logging
* Insufficient auditability
* No change-control process
* No defined governance owner

Document:

| Gap | Risk | Impact | Current Control | Recommended Control | Priority |
| --- | ---- | ------ | --------------- | ------------------- | -------- |
|     |      |        |                 |                     |          |
|     |      |        |                 |                     |          |
|     |      |        |                 |                     |          |

---

# Section 12: Prioritize Security and Governance Risks

Not every risk has the same urgency.

Prioritize your identified risks based on:

* Potential user impact
* Business impact
* Security impact
* Likelihood
* Regulatory or compliance impact
* Ability to detect the issue
* Ability to prevent the issue

Identify the **top three risks** that require PM attention.

| Risk | Impact | Priority | Why It Matters | Immediate Action Needed? |
| ---- | ------ | -------- | -------------- | ------------------------ |
|      |        |          |                |                          |
|      |        |          |                |                          |
|      |        |          |                |                          |

---

# Section 13: Define Security Regression Tests

Security testing should continue after initial implementation.

Create at least **three future regression tests**.

At least one should address access or authorization.

Examples:

* Authorized user receives permitted information
* Unauthorized user is denied restricted information
* Unsupported question does not produce fabricated guidance
* Current policy version is used
* Restricted information does not appear in an employee response

Use:

| Test ID | Scenario | Expected Result | Why It Should Be Repeated |
| ------- | -------- | --------------- | ------------------------- |
|         |          |                 |                           |
|         |          |                 |                           |
|         |          |                 |                           |

These become part of the product's ongoing test strategy.

---

# Section 14: Make PM Decisions

Based on your assessment, identify at least **three PM decisions or recommendations**.

Examples include:

* Require authentication before production release
* Implement role-based access control
* Block unauthorized requests
* Require policy ownership and version information
* Establish a policy review process
* Require human escalation for unsupported questions
* Limit unnecessary logging
* Add audit controls
* Establish an AI governance owner
* Require security testing before deployment
* Add authorization scenarios to regression testing

Record:

| PM Decision | Evidence | Business Reason | Risk Addressed | Owner |
| ----------- | -------- | --------------- | -------------- | ----- |
|             |          |                 |                |       |
|             |          |                 |                |       |
|             |          |                 |                |       |

---

# Section 15: Determine Security and Governance Readiness

Use the results of your security and governance assessment to determine whether PolicyAssist is ready to move to the next stage of the Build-Along.

Remember that the student application is a learning prototype. Some controls required for a real production system may not be implemented in the current application.

Do not automatically classify the prototype as Not Ready simply because a production control has not yet been implemented.

Distinguish between:

**Prototype Readiness:** Is the current application safe enough to continue testing and validation within the scope of this Build-Along?

**Production Readiness:** Would the product have the required controls to be safely released to real users?

### Ready

Select **Ready** when:

* The security and governance behaviors that can be tested in the current application meet their defined expectations.
* No tested critical security or governance failure remains unresolved.
* The evidence is sufficient to continue to the next stage of the Build-Along.
* Any controls that are not implemented are documented as future production requirements rather than treated as failed tests.

### Ready with Conditions

Select **Ready with Conditions** when:

* The current prototype can continue through learning or validation.
* One or more production controls are not yet implemented.
* Specific security or governance actions must be completed before a real production release.
* No current tested failure requires an immediate stop.

Examples may include:

* Authentication not yet implemented
* Role-based access control not yet implemented
* Production audit logging not yet implemented
* Formal retention controls not yet implemented
* Additional security testing required before production

### Not Ready

Select **Not Ready** when:

* A tested critical security or governance control fails.
* The current application demonstrates a serious unresolved risk.
* The evidence indicates that continuing validation would be inappropriate.
* A known issue creates unacceptable risk even within the intended prototype or validation scope.

Examples may include:

* The system provides materially unsupported policy guidance when it should refuse or escalate.
* A tested security control allows unauthorized information to be exposed.
* A critical governance requirement has no viable control or owner and prevents safe progression.

Document:

**Decision:**
[Ready / Ready with Conditions / Not Ready]

**Prototype Status:**
[Ready to Continue / Requires Corrective Action / Stop]

**Production Readiness Gaps:**
[List controls that must be implemented before production]

**Evidence:**
[Key findings from your assessment]

**Critical Risks:**
[Most important unresolved risks]

**Required Actions:**
[Actions needed]

**Decision Owner:**
[Role responsible]

---

# Security and Governance Pass/Fail Rules

Use these rules consistently.

## Current Application Behavior

**Pass:** The current application behaves as expected for the security or governance behavior being tested.

**Fail:** The current application behaves differently from the defined expected behavior.

## Authorization

When authorization controls exist:

**Pass:** Users can access only information they are authorized to receive.

**Fail:** Any unauthorized information is disclosed.

**Target: 0 authorization issues.**

When authorization controls do not yet exist:

Record the control as **Not Implemented**, not Pass or Fail.

## Confidential Data Exposure

**Pass:** No confidential information is exposed to an unauthorized user or unnecessary system process.

**Fail:** Any confirmed unauthorized exposure occurs.

**Target: 0 exposures.**

If the current application does not process confidential information or lacks a mechanism to test this control, record it as **Not Tested** and identify it as a production requirement.

## Policy Authority

**Pass:** Approved and authoritative policy information is identified as the source of truth.

**Fail:** An unapproved, outdated, or unauthorized source is treated as authoritative.

## Version Control

**Pass:** The applicable approved policy version can be identified.

**Fail:** An outdated or incorrect version can be treated as the current source.

## Unsupported Guidance

**Pass:** The system refuses or escalates when sufficient evidence is unavailable.

**Fail:** The system provides unsupported guidance.

## Governance

**Pass:** Required ownership, approval, review, and change controls are defined with appropriate accountability.

**Fail:** A critical governance requirement has no defined owner or control.

## Auditability

**Pass:** Required product activity can be traced when investigation is necessary.

**Fail:** Critical activity cannot be reasonably traced.

When the capability is not implemented in the student starter, record it as **Not Implemented** rather than Pass or Fail.

---

# Critical Failure Rule

A critical failure requires corrective action regardless of the number of other checks that pass.

Treat the following as critical:

* Unauthorized information disclosure in a control that is actually being tested
* Bypassed authorization control in an implemented access-control test
* Confidential information exposure
* Unsupported material policy guidance
* Use of an unauthorized policy source as authoritative
* Inability to identify the applicable policy version when required for a decision
* Missing governance control that creates an immediate and material risk within the current validation scope

A production control that is **not implemented in the student starter is not automatically a critical failure**.

Record it as a **production readiness gap** and identify the required future control or test.

---

# Deliverable: Security & Governance Assessment

Create a **Security & Governance Assessment** containing:

* User and access analysis
* Access requirements
* Three security-related tests performed in the current application
* Results of the unsupported-question test
* Production unauthorized-access test scenario
* Data classification assessment
* Privacy and logging assessment
* Policy governance assessment
* AI governance controls
* Auditability assessment
* At least three security or governance gaps
* Top three prioritized risks
* At least three PM decisions or recommendations
* Current application Pass/Fail results where applicable
* Not Implemented or Not Tested items where appropriate
* At least three future security regression tests
* Any critical failures
* Prototype readiness decision
* Production readiness gaps
* Evidence supporting the decision

---

# PM Checkpoint

Before moving forward, you should be able to answer:

> **Can PolicyAssist provide useful AI assistance while protecting information and operating within defined security and governance requirements?**

You should also be able to explain:

* What security behaviors you can actually test in the current application
* Which security controls are production requirements rather than current application tests
* Who should have access to different information
* How unauthorized access should be tested once access controls are implemented
* Why authorization failures are zero-tolerance issues
* How confidential information should be protected
* Why unnecessary data collection and logging can create risk
* Why policy ownership and version control matter
* How AI governance keeps the product within its intended purpose
* What auditability means for an AI product
* Which security and governance gaps require corrective action
* Why a prototype can be ready for continued validation while still not being ready for production
* What evidence supports your readiness decision

---

# PM Perspective

**Security and governance are product requirements, not assumptions.**

A product can be technically functional and still be unacceptable if it exposes information, uses unauthorized policy content, bypasses access controls, or operates without appropriate governance.

As a PM, you must distinguish between:

**What the product does today**

and

**What the production product must be able to do safely.**

You must also distinguish between:

**Ready to Continue**

and

**Ready for Production**

Those are not necessarily the same decision.

The progression is:

**Access Requirements → Current-State Testing → Security & Governance Gaps → Required Controls → Regression Tests → Risk Assessment → Readiness Decision**

The next milestone will focus on **Testing & User Acceptance Testing (UAT)**, where you will determine whether the product meets its requirements and is ready to be validated by its intended users.

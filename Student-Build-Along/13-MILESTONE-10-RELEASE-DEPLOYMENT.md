# Milestone 10: Release & Deployment

## PM Objective

Determine whether the Artificial Intelligence (AI) product is ready to move from testing and User Acceptance Testing (UAT) into a controlled release and deployment process.

## Hands-On Objective

Use the evidence from previous milestones to make a **release decision**, assess **deployment readiness**, define **deployment validation**, and establish a **rollback and stabilization plan**.

In Milestone 9, you evaluated:

* Requirements and acceptance criteria
* Functional and integration testing
* User Acceptance Testing
* Open defects
* AI quality results
* Security and governance findings
* Release exit criteria

In this milestone, you will turn those findings into a controlled release and deployment approach.

Your primary questions are:

> **Is the product ready to be released?**

and

> **Is the deployment ready to occur safely?**

These are related decisions, but they are not the same decision.

---

# Release vs. Deployment

A **release decision** determines whether the product is approved to move forward into the release process.

A **deployment decision** determines whether the approved release should actually be deployed into the target environment at a specific time and under specific conditions.

A product can be approved for release while deployment is still on hold.

### PolicyAssist Example

Suppose the PolicyAssist Minimum Viable Product (MVP) has:

* Passed required functional and integration testing
* Passed User Acceptance Testing (UAT)
* Met the defined AI quality targets
* Met the current release criteria

The **Release Decision is Go**.

However, suppose role-based access control required for production users has not yet been implemented or validated.

The **Deployment Decision is Hold Deployment** until that production security condition is satisfied.

After the control is implemented and successfully validated, the deployment decision can be reconsidered.

The progression is:

**Testing/UAT Passed → Release: Go → Production Condition Outstanding → Deployment: Hold → Condition Resolved and Validated → Deployment: Deploy**

This distinction is an important Product Management (PM) decision.

---

# Section 1: Review Release Evidence

Start with the evidence from Milestone 9.

Review:

* Test results
* UAT results
* Open defects
* AI evaluation results
* Security and governance findings
* Requirements traceability
* Exit criteria
* Production readiness conditions

Do not repeat earlier testing.

Carry forward the evidence you already collected.

Record the key findings:

| Area         | Previous Result | Current Status | Release Impact | Evidence Reference |
| ------------ | --------------- | -------------- | -------------- | ------------------ |
| Requirements |                 |                |                |                    |
| Testing      |                 |                |                |                    |
| UAT          |                 |                |                |                    |
| AI Quality   |                 |                |                |                    |
| Security     |                 |                |                |                    |
| Governance   |                 |                |                |                    |
| Open Defects |                 |                |                |                    |

---

# Section 2: Define Release Readiness Criteria

A release-readiness criterion is a condition that should be satisfied before the product is approved for release.

Create at least **eight release criteria**.

Your criteria should address:

* Critical requirements
* Acceptance criteria
* UAT
* AI quality
* Security
* Governance
* Critical defects
* Required documentation

Use:

| Release Criterion | Required? | Status | Evidence Reference | Outstanding Issue | Owner |
| ----------------- | --------- | ------ | ------------------ | ----------------- | ----- |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |
|                   | Yes       |        |                    |                   |       |

For **Status**, use:

* Met
* Partially Met
* Not Met
* Not Applicable

Do not mark a criterion **Met** without supporting evidence.

---

# Section 3: Review Open Defects and Risks

Review the issues identified during testing and UAT.

Determine which issues:

* Must be fixed before release
* Can be accepted as known limitations
* Can be deferred to a future release
* Require monitoring after release

Use:

| Issue ID | Issue | Severity | Release Impact | Decision | Owner | Required Action | Evidence Reference |
| -------- | ----- | -------- | -------------- | -------- | ----- | --------------- | ------------------ |
|          |       |          |                |          |       |                 |                    |
|          |       |          |                |          |       |                 |                    |
|          |       |          |                |          |       |                 |                    |

A release does not necessarily require zero open issues.

It does require an explicit decision about every issue that could affect release.

---

# Section 4: Confirm Business and User Acceptance

Review the UAT decision from Milestone 9.

Confirm:

* Intended user tasks were successfully tested
* Critical acceptance criteria were met
* Open user-impacting issues are understood
* Any conditions attached to acceptance are documented

Record:

| Acceptance Area     | Status | Evidence Reference | Release Impact |
| ------------------- | ------ | ------------------ | -------------- |
| User Tasks          |        |                    |                |
| Acceptance Criteria |        |                    |                |
| User Feedback       |        |                    |                |
| UAT Conditions      |        |                    |                |

A product should not be considered ready simply because technical tests passed.

User acceptance is part of release readiness.

---

# Section 5: Confirm AI Quality and Security Conditions

Carry forward the results from Milestones 7 and 8.

Review only the conditions that could affect release.

| Area                | Requirement or Condition | Status | Release Impact | Evidence Reference |
| ------------------- | ------------------------ | ------ | -------------- | ------------------ |
| AI Response Quality |                          |        |                |                    |
| Citation Quality    |                          |        |                |                    |
| Security            |                          |        |                |                    |
| Authorization       |                          |        |                |                    |
| Governance          |                          |        |                |                    |

Do not repeat the complete evaluations from earlier milestones.

Use the evidence already collected.

---

# Section 6: Make the Release Decision

Based on the release-readiness criteria, testing, UAT, AI quality, security, governance, defects, and risks, make a **release decision**.

Choose one:

### Go

The product meets its defined release criteria and is approved to move into the deployment process.

### Hold

The product requires additional evidence, remediation, stakeholder review, or other conditions before the release can be approved.

### No-Go

The product does not meet critical requirements or has unresolved risks that make releasing it unacceptable.

Document:

**Release Decision:**
[Go / Hold / No-Go]

**Evidence Reference(s):**
[Key evidence supporting the release decision]

**Critical Conditions:**
[Conditions that influenced the release decision]

**Open Risks:**
[Remaining risks]

**Required Actions:**
[Actions needed]

**Decision Owner:**
[Role responsible]

> **A Release: Go decision does not automatically mean Deployment: Go.**

---

# Section 7: Assess Deployment Readiness

A product can be approved for release and still not be ready to deploy.

Evaluate whether the deployment process is ready.

Consider:

* Deployment steps are defined
* Required configuration is available
* Required environment variables or secrets are configured appropriately
* Required data or policy content is available
* Dependencies are available
* The deployment owner is identified
* The deployment sequence is understood
* A validation check is defined
* Rollback is defined

Record:

| Deployment Requirement | Status | Evidence Reference | Owner | Required Action |
| ---------------------- | ------ | ------------------ | ----- | --------------- |
| Deployment Steps       |        |                    |       |                 |
| Configuration          |        |                    |       |                 |
| Data/Policy Content    |        |                    |       |                 |
| Dependencies           |        |                    |       |                 |
| Deployment Owner       |        |                    |       |                 |
| Validation Check       |        |                    |       |                 |
| Rollback Readiness     |        |                    |       |                 |

---

# Section 8: Choose the Deployment Approach

Choose a deployment approach appropriate to the product.

Examples include:

### Direct Release

The approved version is deployed directly to the target environment.

### Phased Release

The product is introduced in stages to reduce risk and gather early feedback.

### Pilot

A limited group of intended users validates the product before broader deployment.

### Blue-Green Deployment

Two environments are maintained so traffic can be shifted between the current and new versions.

You do not need to implement every deployment method.

Choose the approach most appropriate for your project and explain why.

Document:

**Selected Approach:**
[Your choice]

**Why It Fits the Product:**
[Your reasoning]

**Primary Risk:**
[Your concern]

**Control or Mitigation:**
[How the risk will be managed]

---

# Section 9: Make the Deployment Decision

Now make a separate **deployment decision**.

Choose one:

### Deploy

The approved release is ready to be deployed because the deployment environment, dependencies, configuration, validation, rollback, and operational conditions are ready.

### Hold Deployment

The release is approved, but one or more deployment conditions must be completed before deployment occurs.

### Rollback

Use this decision only after deployment when the release has created an unacceptable issue and the rollback criteria have been met.

Document:

**Deployment Decision:**
[Deploy / Hold Deployment / Rollback]

**Evidence Reference(s):**
[Key evidence supporting the deployment decision]

**Deployment Conditions:**
[Conditions that must be met]

**Deployment Owner:**
[Role responsible]

---

# Section 10: Define Deployment Validation

After deployment, the team should confirm that the product is operating as expected.

Define at least **five post-deployment validation checks**.

Examples:

* Application is accessible
* Users can submit a question
* A supported policy question produces an expected response
* Citations appear correctly
* Response time is within the defined target
* No critical errors appear
* Monitoring is functioning
* Feedback or escalation mechanisms work

Record:

| Validation Check | Expected Result | Evidence Reference | Pass/Fail |
| ---------------- | --------------- | ------------------ | --------- |
|                  |                 |                    |           |
|                  |                 |                    |           |
|                  |                 |                    |           |
|                  |                 |                    |           |
|                  |                 |                    |           |

Do not assume that a successful deployment means the product is operating correctly.

The deployment must be validated.

---

# Section 11: Define the Rollback Plan

Rollback is the process of returning to a previously stable version or state when a release creates an unacceptable problem.

Your rollback plan should define:

* What conditions trigger rollback
* Who can authorize rollback
* What version or state will be restored
* How rollback will be performed
* How the team will confirm recovery
* How users and stakeholders will be informed

Create your rollback plan:

| Rollback Element          | Decision |
| ------------------------- | -------- |
| Rollback Trigger          |          |
| Rollback Decision Owner   |          |
| Version/State to Restore  |          |
| Rollback Method           |          |
| Recovery Validation       |          |
| Stakeholder Communication |          |

### Example Rollback Triggers

Consider triggers such as:

* Critical security failure
* Unauthorized information exposure
* Materially incorrect AI responses
* Major application failure
* Severe performance degradation
* Critical deployment configuration failure

Connect each trigger to a meaningful business or user impact.

---

# Section 12: Assess Operational Readiness

Release is not the end of the product lifecycle.

Determine whether the team is prepared to operate and support the product after deployment.

Consider:

* Support ownership
* Incident escalation
* Monitoring
* User feedback
* Known issues
* Documentation
* Issue triage
* Change management
* AI quality monitoring

Record:

| Operational Area    | Ready? | Gap | Owner | Required Action | Evidence Reference |
| ------------------- | ------ | --- | ----- | --------------- | ------------------ |
| Support Ownership   |        |     |       |                 |                    |
| Incident Escalation |        |     |       |                 |                    |
| Monitoring          |        |     |       |                 |                    |
| User Feedback       |        |     |       |                 |                    |
| Documentation       |        |     |       |                 |                    |
| Issue Triage        |        |     |       |                 |                    |
| Change Management   |        |     |       |                 |                    |

---

# Section 13: Define Release and Deployment Criteria

Use the evidence collected throughout the Build-Along.

## Release Go

Use **Go** when:

* Required release criteria are met
* UAT has been accepted
* No unresolved critical issue prevents release
* Remaining risks are acceptable

## Release Hold

Use **Hold** when:

* More evidence is needed
* A required condition is incomplete
* Additional remediation is needed
* Stakeholder review or approval is outstanding

## Release No-Go

Use **No-Go** when:

* A critical requirement is not met
* A critical security or authorization issue remains unresolved
* A critical defect prevents safe use
* UAT does not support release

## Deployment Go

Use **Deploy** when:

* The release has been approved
* The target environment is ready
* Required configuration is available
* Dependencies are available
* Deployment ownership is clear
* Validation is defined
* Rollback is ready
* Required operational conditions are satisfied

## Deployment Hold

Use **Hold Deployment** when:

* The release is approved
* One or more deployment conditions remain incomplete
* The product can safely wait for those conditions to be resolved

## Rollback

Use **Rollback** when:

* The deployed release has triggered a defined rollback condition
* The impact is unacceptable
* Returning to a stable version or state is the approved recovery action

---

# Section 14: Create the Release and Deployment Readiness Record

Create a consolidated record that clearly separates **release readiness** from **deployment readiness**.

| Readiness Area         | Release Status | Deployment Status | Evidence Reference | Outstanding Issue | Owner | Required Action |
| ---------------------- | -------------- | ----------------- | ------------------ | ----------------- | ----- | --------------- |
| Requirements           |                |                   |                    |                   |       |                 |
| UAT                    |                |                   |                    |                   |       |                 |
| AI Quality             |                |                   |                    |                   |       |                 |
| Security               |                |                   |                    |                   |       |                 |
| Governance             |                |                   |                    |                   |       |                 |
| Deployment Environment |                |                   |                    |                   |       |                 |
| Configuration          |                |                   |                    |                   |       |                 |
| Rollback               |                |                   |                    |                   |       |                 |
| Operations             |                |                   |                    |                   |       |                 |
| Business Approval      |                |                   |                    |                   |       |                 |

This record becomes the basis for both decisions.

---

# Section 15: Technical Build-Along Deployment

If you are following the PolicyAssist technical Build-Along, use the deployment instructions provided for your current project environment.

Your responsibilities as a PM are to:

* Confirm the release candidate is the version that was tested
* Confirm required configuration is available
* Confirm deployment ownership
* Confirm post-deployment validation
* Confirm rollback readiness
* Record deployment evidence
* Record any issues discovered after deployment

You are not expected to become a deployment engineer.

The objective is to understand and manage the release process.

If a deployment capability is not available in your environment, document the production requirement and the process that would be used rather than claiming that deployment was completed.

---

# Section 16: Define Early Stabilization

The first period after deployment requires focused monitoring.

Define at least **three things that should be monitored immediately after deployment**.

Examples:

* Application availability
* Response time
* AI response quality
* Unsupported response rate
* Citation behavior
* Error rate
* User feedback
* Escalation volume

Use:

| Monitoring Area | What Will Be Monitored? | Expected Condition | Action if Condition Is Not Met | Evidence Reference |
| --------------- | ----------------------- | ------------------ | ------------------------------ | ------------------ |
|                 |                         |                    |                                |                    |
|                 |                         |                    |                                |                    |
|                 |                         |                    |                                |                    |

This creates a bridge to the Key Performance Indicator (KPI), dashboard, monitoring, and continuous-improvement work in later milestones.

---

# Deliverable: Release & Deployment Readiness Record

Create a **Release & Deployment Readiness Record** containing:

* Review of prior milestone evidence
* Release-readiness criteria
* Open defect and risk decisions
* UAT acceptance status
* AI quality conditions
* Security and governance conditions
* Release decision: Go, Hold, or No-Go
* Deployment-readiness assessment
* Selected deployment approach
* Deployment decision: Deploy, Hold Deployment, or Rollback where applicable
* At least five post-deployment validation checks
* Rollback plan
* Operational readiness assessment
* Consolidated release and deployment readiness record
* Early stabilization monitoring plan
* Evidence References supporting major decisions

---

# PM Checkpoint

Before moving forward, you should be able to answer:

> **Is the product approved for release, is the deployment ready to occur, and what will we do if something goes wrong?**

You should also be able to explain:

* The difference between a release decision and a deployment decision
* How testing and UAT evidence inform release readiness
* Which issues must be resolved before release
* Which risks may be accepted or deferred
* What makes a deployment-ready environment
* Why deployment validation is necessary
* What a rollback plan should contain
* When a rollback should be triggered
* Why operational readiness matters
* How Go, Hold, and No-Go decisions differ
* Why a Release: Go decision can still result in Deployment: Hold
* Why a successful deployment does not automatically mean the product is operationally stable
* What should be monitored immediately after deployment

---

# PM Perspective

**Release is an approval decision. Deployment is an execution decision.**

A product may be approved for release while deployment remains on hold because an environment, configuration, staffing, security, rollback, or operational condition is not ready.

The PM uses evidence from requirements, testing, UAT, AI evaluation, security, governance, deployment readiness, and operational planning to make both decisions.

The progression is:

**Test Results → UAT → Release Criteria → Release Decision → Deployment Readiness → Deployment Decision → Validation → Stabilization**

The next milestone will focus on **KPIs & Dashboard**, where you will measure whether the project is being delivered effectively and whether the AI product is achieving its intended performance and business outcomes.

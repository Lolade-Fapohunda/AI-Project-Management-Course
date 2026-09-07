# Module 10: Release & Deployment Management

## Purpose

Reaching the end of development does not automatically mean an AI product is ready for production.

Release and deployment management ensures that an AI product moves into production in a controlled, approved, and measurable way.

The AI Project Manager must coordinate:

* Release readiness
* Deployment planning
* Approvals
* Dependencies
* Change management
* Communication
* Training
* Operational readiness
* Rollback planning
* Production support

The PM does not need to perform the technical deployment.

The PM must ensure that the organization is prepared for the product to be deployed and supported.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain the difference between release and deployment.
* Define release readiness criteria.
* Develop a release plan.
* Identify deployment dependencies.
* Manage production readiness.
* Coordinate stakeholder approvals.
* Understand change-management requirements.
* Plan user communication and training.
* Define rollback requirements.
* Manage deployment risks.
* Coordinate go-live activities.
* Establish post-release support.
* Make evidence-based Go, Hold, or No-Go decisions.

---

## Release Vs. Deployment

Release and deployment are related but different.

### Release

A release is the controlled decision to make a product version available for use.

### Deployment

Deployment is the technical process of moving the product into the target environment.

A product may be technically deployed without being officially released.

For example:

> The application is installed in production, but users cannot access it until the business approves the release.

The PM should understand both concepts.

---

## Release Readiness

Before approving a release, the PM should confirm that required conditions have been satisfied.

These may include:

* Requirements completed
* Acceptance criteria met
* AI evaluation completed
* Security validation completed
* UAT completed
* Critical defects resolved
* High-severity defects addressed or formally accepted
* Data validated
* Access controls confirmed
* Monitoring available
* Support process established
* Rollback plan available
* Required approvals obtained

Release readiness should be evidence-based.

---

## Release Criteria

Release criteria define the minimum conditions required for deployment.

Example:

| Criteria          | Requirement                   |
| ----------------- | ----------------------------- |
| UAT               | Completed                     |
| Critical Defects  | 0 Open                        |
| High Defects      | Resolved or formally accepted |
| Security          | Approved                      |
| Data Readiness    | Approved                      |
| AI Evaluation     | Meets agreed thresholds       |
| Monitoring        | Operational                   |
| Support           | Ready                         |
| Rollback          | Tested/validated              |
| Business Approval | Obtained                      |

The exact criteria will vary by project.

---

## Release Decision

The PM should distinguish between:

### Go

The product meets release requirements and can proceed.

### Go With Conditions

The product may proceed with documented limitations, controls, or approved exceptions.

### Hold

The product requires additional work or evidence before release.

### No-Go

The product should not be released because the risks or deficiencies are unacceptable.

The decision should be documented.

---

## Deployment Strategy

Different deployment strategies can reduce risk.

### Big Bang

The entire user population receives the product at once.

**Advantage:**

* Simple deployment structure.

**Risk:**

* A problem can affect the entire organization.

---

### Phased Deployment

Users receive the product in groups.

Example:

**Group 1 → Group 2 → Group 3 → Full Deployment**

This allows the team to learn from earlier groups.

---

### Pilot To Production

A successful pilot may transition into broader production deployment.

This approach uses real-world evidence before expanding the user population.

---

### Canary Deployment

A small percentage of users or traffic receives the new version before broader deployment.

This can help identify problems early.

The PM does not need to configure the technical mechanism but should understand the risk-management purpose.

---

## Deployment Dependencies

A release may depend on other systems or activities.

Examples:

* Identity management
* Databases
* APIs
* Network access
* Infrastructure
* Data pipelines
* Security approvals
* Vendor services
* User training
* Support teams

The PM should identify dependencies early.

A deployment can fail even when the application itself works correctly.

---

## Change Management

Production changes should be controlled.

A change-management process may require:

1. Change Request
2. Impact Assessment
3. Risk Assessment
4. Approval
5. Implementation
6. Validation
7. Monitoring
8. Closure

Changes should be traceable.

For AI systems, changes may include:

* Model changes
* Prompt changes
* Retrieval changes
* Knowledge-base changes
* Application changes
* Access-control changes
* Configuration changes

A seemingly small AI change can affect system behavior.

---

## Model And Knowledge Changes

AI systems may change without traditional application code being changed.

For example:

> A knowledge document is replaced with a newer version.

This may change the AI's answers.

Similarly:

> A model version is changed.

This may affect accuracy, latency, or behavior.

The PM should therefore treat important model and knowledge changes as controlled changes rather than informal updates.

---

## Production Readiness

Production readiness means the organization is prepared to operate the system, not simply deploy it.

The PM should confirm:

### Technical Readiness

* Infrastructure ready
* Integrations working
* Configuration complete
* Monitoring operational

### Business Readiness

* Users identified
* Processes defined
* Training completed
* Support available

### Governance Readiness

* Approvals obtained
* Ownership established
* Risks documented
* Policies established

### Operational Readiness

* Incident process defined
* Support process established
* Escalation paths available
* Rollback plan available

---

## User Communication

Users should understand what is changing.

Communication may include:

* What the product does
* Who can use it
* When it becomes available
* How to access it
* What users should and should not do
* Known limitations
* How to report problems
* How to request support

AI products may require additional communication about:

* AI limitations
* Appropriate use
* Human review
* Accuracy expectations
* Sensitive information

---

## User Training

Training should focus on how users should use the product responsibly.

Training may include:

* Product functionality
* Appropriate use
* Prohibited use
* AI limitations
* Security responsibilities
* Data handling
* Escalation procedures
* Feedback mechanisms

Training should be proportionate to the product's complexity and risk.

---

## Rollback

Every significant release should have a rollback strategy.

Rollback answers:

> "What happens if the release causes unacceptable problems?"

A basic rollback process is:

**Detect Problem**

↓

**Stop Release / Disable**

↓

**Restore Previous Approved Version**

↓

**Investigate**

↓

**Correct**

↓

**Retest**

↓

**Re-Approve**

↓

**Redeploy**

Rollback planning should occur before deployment, not after an incident.

---

## Go-Live Planning

A go-live plan coordinates activities immediately before and during deployment.

A basic plan may include:

| Activity           | Owner          | Timing           | Status |
| ------------------ | -------------- | ---------------- | ------ |
| Final Approval     | Business Owner | Before Go-Live   |        |
| Backup             | Technical Team | Before Go-Live   |        |
| Deployment         | Technical Team | Go-Live          |        |
| Validation         | Technical Team | After Deployment |        |
| User Communication | PM             | Go-Live          |        |
| Monitoring         | Operations     | Go-Live          |        |
| Support            | Service Team   | Go-Live          |        |

The PM coordinates the overall activity.

---

## Go-Live Command Structure

For important releases, a defined command structure can improve coordination.

Participants may include:

* Project Manager
* Product Owner
* Technical Lead
* Security Lead
* Business Lead
* Operations
* Support
* Vendor representatives

Each participant should understand their responsibilities and escalation authority.

---

## Hypercare

Hypercare is an intensified support period immediately following a major release.

During hypercare, teams may monitor:

* Errors
* User issues
* Performance
* AI quality
* Security events
* Support volume
* Unexpected behavior

The PM should establish:

* Duration
* Owners
* Escalation process
* Reporting frequency
* Exit criteria

Hypercare should eventually transition into normal operational support.

---

## Release Communication

A release should have a communication plan.

Stakeholders may need:

### Before Release

* What is changing?
* Why is it changing?
* When will it happen?
* What preparation is required?

### During Release

* Current status
* Issues
* Deployment progress
* Go/No-Go status

### After Release

* Release completed
* Known issues
* Support instructions
* Monitoring status
* Next steps

Clear communication reduces confusion during high-pressure releases.

---

## Release Risks

Common release risks include:

* Incomplete testing
* Unresolved defects
* Security findings
* Missing approvals
* Failed dependencies
* Poor user readiness
* Insufficient monitoring
* Inadequate rollback
* Vendor failure
* Unexpected AI behavior

The PM should ensure release risks are actively tracked.

---

## Release Evidence

A release decision should be supported by evidence.

The PM should be able to show:

* Test results
* Evaluation results
* UAT results
* Security results
* Defect status
* Risk status
* Data readiness
* Approval records
* Monitoring readiness
* Rollback readiness

The statement:

> "Everything looks good."

is not sufficient release evidence.

---

## Practical Exercise 10: Build A Release And Deployment Plan

### Scenario

An AI product has completed development, evaluation, and UAT.

Leadership wants to release the product to the entire organization on Monday.

You discover:

* UAT passed.
* AI evaluation meets the agreed thresholds.
* One high-severity defect remains open.
* Security approval is complete.
* Monitoring is configured.
* User training is only partially complete.
* The rollback plan exists but has not been validated.
* A critical third-party integration will be updated the same weekend.
* Business leadership has not formally documented the release decision.

### Part 1: Assess Release Readiness

Evaluate each readiness area:

* Testing
* AI evaluation
* Security
* Defects
* Training
* Monitoring
* Dependencies
* Rollback
* Governance

Classify each as:

* Ready
* At Risk
* Not Ready

### Part 2: Identify Release Risks

Identify at least **six risks**.

For each risk, define:

* Risk
* Impact
* Likelihood
* Mitigation
* Owner

### Part 3: Build The Release Plan

Define:

* Deployment approach
* Go-live activities
* Stakeholder responsibilities
* Communication
* Training
* Monitoring
* Support
* Hypercare
* Rollback

### Part 4: Define Release Gates

Create the conditions that must be satisfied before:

**Go-Live Approval**

and

**Production Deployment**

### Part 5: PM Decision

Determine whether the project should:

* **Go**
* **Go With Conditions**
* **Hold**
* **No-Go**

Support your decision using:

1. Evidence
2. Defects
3. Risks
4. Dependencies
5. Governance
6. Operational readiness

---

## PM Decision

Leadership says:

> "We already told everyone Monday is the launch date. We cannot move it."

You determine that:

* A high-severity defect remains open.
* The rollback plan has not been validated.
* A critical integration is changing immediately before launch.
* User training is incomplete.
* Formal release approval has not been documented.

As the AI Project Manager, determine whether the release should proceed.

Your decision should address:

* Business impact
* Technical readiness
* User readiness
* Risk
* Rollback capability
* Governance
* Schedule pressure

### Key Principle

> **A committed date is not the same as release readiness.**

The PM must protect the product and organization even when schedule pressure exists.

---

## Artifact / Output

Create a **Release & Deployment Plan** containing:

* Release scope
* Release criteria
* Deployment strategy
* Dependencies
* Change-management process
* Production readiness assessment
* Communication plan
* Training plan
* Go-live plan
* Rollback plan
* Hypercare plan
* Support model
* Release risks
* Approval requirements
* Go/Hold/No-Go criteria

The artifact should demonstrate that you can coordinate a controlled AI product release.

---

## Decision / Reflection

Answer the following:

1. What is the difference between release and deployment?
2. Why should release criteria be defined before deployment?
3. Why can a technically working product still be unready for production?
4. Why should AI-related changes be controlled?
5. Why is rollback planning important?
6. What makes an organization operationally ready?
7. Why is user training part of release readiness?
8. What is hypercare?
9. Why should production dependencies be identified before deployment?
10. Why should schedule pressure not override release readiness?

---

## Key Takeaways

* Release and deployment are related but different activities.
* Release decisions should be based on defined readiness criteria.
* Production readiness includes technical, business, governance, and operational readiness.
* AI changes can affect system behavior even when traditional application code does not change.
* Model, prompt, retrieval, and knowledge changes should be appropriately controlled.
* Deployment dependencies can create significant release risk.
* Users need appropriate communication and training.
* Rollback should be planned before deployment.
* Go-live requires coordinated ownership and communication.
* Hypercare provides intensified support after major releases.
* Release evidence should include testing, evaluation, security, UAT, risks, approvals, monitoring, and rollback readiness.
* Schedule commitments do not automatically justify releasing an unready product.
* The PM is responsible for coordinating release readiness and facilitating an evidence-based decision.

---

## Connection To Capstone

The release and deployment principles from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will apply these principles to:

* Production readiness
* Release criteria
* Deployment planning
* Stakeholder approvals
* User communication
* Training
* Monitoring
* Rollback
* Hypercare
* Release risk management
* Go/Hold/No-Go decisions

The technical deployment itself is treated as a technical execution activity. The PM's responsibility is to coordinate readiness, dependencies, approvals, communication, risk, and release decisions.

---

**Next: Module 11 — Monitoring & Continuous Improvement.**

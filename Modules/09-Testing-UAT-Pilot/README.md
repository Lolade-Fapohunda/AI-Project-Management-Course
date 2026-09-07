# Module 9: Testing, UAT & Pilot

## Purpose

An AI system can meet technical requirements and still fail to meet business needs.

Testing, User Acceptance Testing (UAT), and pilot activities provide the evidence needed to determine whether an AI product is ready for real users.

The AI Project Manager is responsible for coordinating this process and ensuring that:

* Requirements are tested.
* AI behavior is evaluated.
* Security requirements are validated.
* Users confirm business usability.
* Defects are documented and resolved.
* Pilot objectives are measurable.
* Release decisions are supported by evidence.

The PM does not need to perform every technical test.

The PM must ensure the right testing occurs, the results are documented, and unresolved issues are appropriately managed.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain the purpose of testing in AI projects.
* Distinguish functional testing from AI evaluation and UAT.
* Define a testing strategy.
* Develop test scenarios from requirements and acceptance criteria.
* Understand positive, negative, edge-case, and security testing.
* Create and manage a defect log.
* Define User Acceptance Testing (UAT).
* Develop UAT scenarios and acceptance criteria.
* Understand pilot planning.
* Define pilot objectives and success criteria.
* Manage pilot risks and feedback.
* Determine whether a system is ready to progress from testing to pilot.
* Make evidence-based Go, Hold, or No-Go decisions.

---

## Testing In AI Projects

Testing determines whether the product behaves as expected.

AI projects require multiple forms of testing because there are multiple layers of potential failure.

A system can:

* Function technically but provide incorrect answers.
* Produce accurate answers but expose unauthorized information.
* Pass technical testing but fail user acceptance.
* Perform well in development but poorly under realistic usage.

Testing should therefore occur throughout the lifecycle rather than only immediately before release.

---

## Testing Vs. Evaluation Vs. UAT

These activities have different purposes.

### Testing

Determines whether the system meets defined technical and functional requirements.

Example:

> Does the application prevent an unauthorized user from accessing restricted information?

### Evaluation

Measures the quality of AI behavior.

Example:

> How accurately does the AI answer questions across the approved evaluation dataset?

### User Acceptance Testing

Determines whether the product meets real business-user needs.

Example:

> Can employees use the system effectively to complete the task it was designed to support?

A mature AI project requires all three.

---

## Testing Strategy

A testing strategy defines how the project will validate the product.

The PM should establish:

* What will be tested.
* What will not be tested.
* Who is responsible.
* When testing occurs.
* What environments will be used.
* What data will be used.
* What constitutes a pass.
* How defects will be managed.
* What findings block progression.

Testing should trace back to requirements.

---

## Test Levels

AI products may require testing at multiple levels.

### Unit Testing

Tests individual components.

Example:

> Does a document-processing function correctly process a document?

### Integration Testing

Tests whether components work together.

Example:

> Does retrieval correctly provide information to the AI model?

### System Testing

Tests the complete application.

Example:

> Can a user submit a question and receive an appropriate response?

### AI Evaluation

Measures AI behavior and quality.

Example:

> Does the system provide grounded and accurate responses?

### UAT

Validates the product from the business-user perspective.

Example:

> Can employees successfully use the system for their intended business tasks?

The PM should understand the purpose of each level without needing to perform every technical test personally.

---

## Functional Testing

Functional testing verifies that required features work correctly.

Examples:

* User login
* Search
* Document retrieval
* Response generation
* Citation display
* Feedback submission
* Escalation
* Administrative functions

Functional testing should be linked to requirements and acceptance criteria.

---

## Negative Testing

Negative testing determines how the system behaves when something unexpected or invalid occurs.

Examples:

* Invalid login
* Unsupported question
* Missing information
* Invalid document
* Unauthorized request
* Incorrect input
* System dependency unavailable

A strong AI system should fail safely rather than simply fail unpredictably.

---

## Edge-Case Testing

Edge cases test unusual conditions.

Examples:

* Very long questions
* Ambiguous questions
* Multiple questions in one request
* Conflicting information
* Rare terminology
* Empty input
* Extremely large documents
* Unexpected user behavior

Edge cases are important because AI systems may behave differently outside normal scenarios.

---

## Security Testing

Security testing validates whether security requirements and controls work as intended.

Potential areas include:

* Authentication
* Authorization
* Access control
* Sensitive information
* Data leakage
* Prompt injection
* Logging
* Session security
* Third-party integrations

The PM should coordinate security testing with qualified technical stakeholders.

The PM should not attempt to perform offensive security testing without appropriate authorization and expertise.

---

## Regression Testing

Regression testing determines whether a change has unintentionally broken existing functionality.

AI projects require particular attention to regression because changes to:

* Models
* Prompts
* Retrieval
* Documents
* Application logic
* Configuration

may change system behavior.

For example:

> A retrieval improvement may increase performance for one category while causing another category to decline.

Therefore, important evaluation and test cases should be repeated after significant changes.

---

## Defect Management

A defect is a condition in which the system does not meet an expected requirement or behavior.

A basic defect record may contain:

| Field                  | Purpose                             |
| ---------------------- | ----------------------------------- |
| **Defect ID**          | Unique identifier                   |
| **Description**        | What went wrong                     |
| **Severity**           | Business/technical impact           |
| **Priority**           | How urgently it should be addressed |
| **Environment**        | Where it occurred                   |
| **Steps To Reproduce** | How the issue occurred              |
| **Expected Result**    | What should happen                  |
| **Actual Result**      | What happened                       |
| **Owner**              | Person/team responsible             |
| **Status**             | Current state                       |
| **Resolution**         | How it was addressed                |
| **Retest Result**      | Whether the fix worked              |

---

## Severity Vs. Priority

Severity and priority are not the same.

### Severity

How serious is the problem?

### Priority

How urgently should the problem be addressed?

For example:

A cosmetic issue may have:

* Low severity
* Low priority

A security vulnerability may have:

* Critical severity
* Immediate priority

A PM should ensure that the team does not confuse the two.

---

## Defect Lifecycle

A typical defect lifecycle is:

**Identified**

↓

**Logged**

↓

**Triaged**

↓

**Assigned**

↓

**Fixed**

↓

**Retested**

↓

**Closed**

If the fix does not work:

**Retest Failed**

↓

**Reopened**

↓

**Returned To Development**

Defects should not be considered resolved simply because a developer says the issue was fixed.

---

## UAT

User Acceptance Testing determines whether the system is acceptable to its intended business users.

UAT should answer:

> "Does this product actually meet the business need?"

UAT is not simply another technical test.

Users should evaluate realistic business scenarios.

---

## UAT Participants

UAT participants should represent the intended user population.

Depending on the project, this may include:

* Business users
* Subject Matter Experts (SMEs)
* Managers
* Operational staff
* Product owners
* Process owners

The PM should ensure that appropriate users participate rather than relying only on the development team.

---

## UAT Scenarios

UAT scenarios should be based on real business activities.

A UAT scenario should define:

* Scenario ID
* User role
* Business objective
* Starting conditions
* User action
* Expected result
* Acceptance criteria
* Actual result
* Pass/Fail
* Comments

Good UAT scenarios should reflect how users will actually use the product.

---

## UAT Acceptance Criteria

UAT acceptance criteria should be measurable.

Weak:

> "The system is easy to use."

Stronger:

> "At least 85% of participating users can complete the defined task without assistance."

The PM should avoid relying solely on subjective statements.

---

## UAT Defects

UAT may identify issues that technical testing does not.

Examples:

* Users cannot find important functionality.
* AI responses are technically correct but difficult to understand.
* Workflow does not match business processes.
* Users cannot interpret citations.
* Users do not understand when they should escalate to a human.

UAT findings should be treated as legitimate project evidence.

---

## Pilot Testing

A pilot introduces the product to a limited group of real users before broader deployment.

A pilot reduces the risk of launching an unproven product to the entire organization.

A pilot should have:

* Defined population
* Defined duration
* Defined objectives
* Defined success criteria
* Defined monitoring
* Support process
* Feedback mechanism
* Escalation process
* Exit criteria

---

## Pilot Objectives

A pilot should answer specific questions.

Examples:

* Can users complete the intended tasks?
* Does the system perform under realistic usage?
* Are users satisfied?
* Are AI quality targets maintained?
* Are support requests manageable?
* Are security controls working?
* Are unexpected behaviors occurring?

A pilot should not simply be:

> "Let's let people try it."

It should be a controlled learning activity.

---

## Pilot Success Criteria

Pilot success criteria should be measurable.

Example:

| Measure                     |       Target |
| --------------------------- | -----------: |
| User Satisfaction           |        ≥ 85% |
| Answer Accuracy             |        ≥ 90% |
| Response Latency            | ≤ 10 seconds |
| Critical Security Incidents |            0 |
| Critical Defects            |            0 |
| UAT Acceptance              |        ≥ 90% |

Targets should be defined before the pilot whenever possible.

---

## Pilot Risks

Common pilot risks include:

* Insufficient user participation
* Poor user training
* Unexpected AI behavior
* Security incidents
* Excessive support demand
* Poor data quality
* Performance degradation
* Negative user feedback
* Scope expansion

The PM should monitor pilot risks and establish escalation criteria.

---

## Pilot Feedback

Feedback should be collected systematically.

Sources may include:

* Surveys
* Interviews
* User observations
* Support requests
* Defect reports
* Usage metrics
* AI evaluation results

The PM should distinguish between:

**Preference**

and

**Evidence Of A Product Problem**

Not every negative opinion represents a defect.

---

## Pilot Exit Criteria

The pilot should have clear exit criteria.

Possible outcomes include:

### Proceed

The product meets the required criteria and can move toward broader deployment.

### Proceed With Conditions

The product can continue with specific limitations or corrective actions.

### Extend Pilot

More evidence is needed before making a decision.

### Hold

The product has unresolved issues that prevent progression.

### No-Go

The product should not proceed because risks or failures are unacceptable.

---

## Testing Evidence

The PM should maintain evidence showing:

* What was tested.
* What passed.
* What failed.
* What defects were identified.
* Which defects remain open.
* What UAT users reported.
* What pilot results showed.
* Whether acceptance criteria were met.
* What risks remain.
* What approvals were obtained.

The PM should be able to defend the release recommendation using evidence rather than opinions.

---

## Practical Exercise 9: Plan Testing, UAT & Pilot

### Scenario

An AI knowledge assistant has completed development.

The technical team reports:

> "All major features are working."

The project is scheduled for a 100-user pilot in two weeks.

You discover:

* Functional testing is mostly complete.
* AI evaluation has been performed but several edge cases failed.
* Two high-severity defects remain open.
* Security testing has not been completed.
* UAT participants have not yet been selected.
* No formal pilot success criteria exist.
* Leadership wants to maintain the planned pilot date.

### Part 1: Build The Testing Strategy

Define:

* Testing levels
* Test categories
* Owners
* Test evidence
* Pass criteria
* Defect management process

### Part 2: Define UAT

Create at least **six UAT scenarios**.

For each scenario, define:

* User role
* Business objective
* User action
* Expected result
* Acceptance criteria

### Part 3: Define Defect Priorities

Determine how you would handle:

* Two high-severity defects
* Failed edge cases
* An unresolved usability issue
* A cosmetic issue

Explain which issues should block the pilot.

### Part 4: Build The Pilot Plan

Define:

* Pilot population
* Duration
* Objectives
* Success criteria
* Monitoring
* Support process
* Feedback process
* Escalation process
* Exit criteria

### Part 5: PM Decision

Leadership wants to maintain the pilot date.

Determine whether the project should:

* **Proceed**
* **Proceed With Conditions**
* **Extend Pilot Preparation**
* **Hold**
* **No-Go**

Support your decision using:

1. Testing evidence
2. Defects
3. Security
4. UAT readiness
5. Pilot readiness
6. Risk
7. Required actions

---

## PM Decision

Leadership says:

> "We only have two weeks left. We can fix the remaining issues during the pilot."

You determine that:

* Security testing is incomplete.
* Two high-severity defects remain.
* UAT has not occurred.
* Pilot success criteria are undefined.

As the AI Project Manager, determine whether the pilot should proceed.

Your decision should address:

* Whether the product is sufficiently validated.
* Whether the remaining defects are acceptable.
* Whether security readiness has been established.
* Whether users have validated the product.
* Whether the pilot has measurable objectives.
* What evidence is still required.

### Key Principle

> **A pilot is not a substitute for required validation.**

A pilot should reduce uncertainty, not become an excuse to bypass testing and governance.

---

## Artifact / Output

Create a **Testing, UAT & Pilot Plan** containing:

* Testing strategy
* Test levels
* Test categories
* Test ownership
* Test evidence
* Defect management process
* Severity and priority definitions
* UAT plan
* UAT scenarios
* UAT acceptance criteria
* Pilot objectives
* Pilot population
* Pilot success criteria
* Pilot monitoring
* Feedback process
* Escalation process
* Pilot exit criteria
* Go/Hold/No-Go criteria

The artifact should demonstrate that you can coordinate validation of an AI product before broader deployment.

---

## Decision / Reflection

Answer the following:

1. Why are testing, evaluation, and UAT different?
2. Why should testing trace back to requirements?
3. Why is negative testing important for AI systems?
4. Why are edge cases important?
5. Why should security testing be completed before an appropriate pilot?
6. What is the difference between severity and priority?
7. Why should UAT involve real business users?
8. Why should pilot success criteria be defined before the pilot?
9. When should a high-severity defect prevent progression?
10. Why should a pilot reduce uncertainty rather than bypass validation?

---

## Key Takeaways

* AI projects require multiple forms of testing.
* Testing, evaluation, and UAT serve different purposes.
* Testing should trace back to requirements and acceptance criteria.
* Negative testing identifies unsafe or unexpected behavior.
* Edge-case testing helps expose weaknesses outside normal scenarios.
* Security testing should be coordinated with qualified technical stakeholders.
* Regression testing is important after AI-related changes.
* Defects should be documented, prioritized, assigned, fixed, and retested.
* Severity describes impact; priority describes urgency.
* UAT validates the product from the business-user perspective.
* UAT should use realistic business scenarios.
* Pilot programs should have defined objectives and measurable success criteria.
* Pilot feedback should be collected systematically.
* Pilot exit criteria should be established before the pilot begins.
* A pilot should not be used to bypass required security, testing, or governance activities.
* Release decisions should be based on evidence.

---

## Connection To Capstone

The testing, UAT, and pilot principles from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will apply these principles to:

* Functional testing
* AI evaluation
* Security validation
* UAT scenarios
* Defect management
* Pilot planning
* User feedback
* Acceptance criteria
* Go/Hold/No-Go decisions

The capstone will use realistic policy-related UAT scenarios to determine whether the product meets business, AI quality, security, and usability requirements.

---

## Competency Check

Before moving to Module 10, confirm that you can:

* [ ] Explain the difference between testing, evaluation, and UAT.
* [ ] Develop an AI testing strategy.
* [ ] Connect tests to requirements and acceptance criteria.
* [ ] Define functional, negative, edge-case, and security testing.
* [ ] Explain regression testing.
* [ ] Create and manage a defect record.
* [ ] Distinguish severity from priority.
* [ ] Define UAT participants and responsibilities.
* [ ] Create realistic UAT scenarios.
* [ ] Define measurable UAT acceptance criteria.
* [ ] Develop a controlled pilot plan.
* [ ] Define pilot objectives and success criteria.
* [ ] Establish pilot exit criteria.
* [ ] Manage pilot feedback and escalation.
* [ ] Determine whether unresolved issues should block progression.
* [ ] Make a **Proceed, Proceed With Conditions, Extend Pilot Preparation, Hold, or No-Go** decision using evidence.
* [ ] Complete the **Testing, UAT & Pilot Plan**.

**Module Complete When:** You can coordinate testing, User Acceptance Testing, and pilot activities and determine whether an AI product has sufficient evidence to progress toward broader deployment.

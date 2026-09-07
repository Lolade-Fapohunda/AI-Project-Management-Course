# Module 3: Business Analysis & Requirements

## Purpose

Once the business problem and desired outcomes are understood, the project manager must translate that understanding into clear, measurable, and actionable requirements.

Requirements establish what the solution must accomplish and provide the foundation for planning, development, testing, acceptance, and release decisions.

For AI projects, requirements must address not only what the system does, but also how accurately, securely, reliably, and responsibly it must operate.

## Learning Objectives

By the end of this module, you should be able to:

* Distinguish business, functional, and non-functional requirements
* Write clear user stories
* Write measurable acceptance criteria
* Identify AI-specific requirements
* Prioritize requirements
* Establish requirements traceability
* Identify ambiguity and gaps
* Evaluate requirements from a project-management perspective

## PM Responsibilities

The project manager does not need to personally write every technical requirement.

However, the PM must ensure that requirements are:

* Clear
* Complete
* Consistent
* Testable
* Traceable
* Prioritized
* Approved
* Aligned with business outcomes

The PM should also ensure that requirements do not become a collection of disconnected technical requests.

Every major requirement should have a reason for existing.

## Key Terminology

### Business Requirement

A business requirement describes what the organization needs to achieve.

Example:

> Reduce the average time required to complete a customer-service request by 30%.

A business requirement focuses on the desired business outcome.

### Functional Requirement

A functional requirement describes what the solution must do.

Example:

> The system shall allow users to search customer records using a customer identification number.

Functional requirements describe system behavior.

### Non-Functional Requirement

A non-functional requirement describes how the system must perform.

Examples include:

* Performance
* Availability
* Security
* Scalability
* Usability
* Reliability
* Accessibility

Example:

> The system shall return a response within five seconds for at least 95% of requests.

## User Story

A user story describes a capability from the perspective of the person who needs it.

A common format is:

> As a [user], I want [capability], so that [benefit].

Example:

> As a customer service representative, I want to quickly locate a customer record so that I can resolve customer requests faster.

A good user story identifies:

* Who needs something
* What they need
* Why they need it

## Acceptance Criteria

Acceptance criteria define what must be true for a requirement or user story to be considered complete.

Example:

**User Story**

> As a customer service representative, I want to search for a customer record so that I can resolve requests faster.

**Acceptance Criteria**

* The user can search using a valid customer identification number.
* The system displays the matching customer record.
* The system returns no unrelated customer records.
* Invalid identification numbers produce an appropriate message.
* The search result is returned within the defined performance target.

Acceptance criteria should be specific enough that the team can determine whether the requirement has been satisfied.

## Business Analysis

Business analysis connects business needs to solution requirements.

The process generally involves:

**Business Need → Problem → Outcome → Requirement → Acceptance Criteria → Validation**

The project manager should continually ask:

> What business problem does this requirement solve?

If there is no clear answer, the requirement may need to be challenged.

## From Business Need To Requirement

Consider this business need:

> Customers are waiting too long for support.

A weak requirement might be:

> Build an AI chatbot.

This specifies a solution without defining the actual business need.

A stronger progression would be:

**Business Need**

Reduce customer wait time.

**Business Outcome**

Reduce average wait time by 30%.

**Functional Requirement**

The solution shall provide customers with automated responses to supported questions.

**Non-Functional Requirement**

The solution shall provide an initial response within five seconds for at least 95% of supported requests.

**Acceptance Criteria**

The defined response-time target must be demonstrated during testing.

This creates traceability from business need to implementation.

## Functional Vs. Non-Functional Requirements

AI projects require both.

### Functional Requirements

Examples:

* Search information
* Classify requests
* Generate responses
* Route requests
* Record feedback
* Escalate requests
* Authenticate users

### Non-Functional Requirements

Examples:

* Response time
* Accuracy
* Availability
* Security
* Reliability
* Accessibility
* Scalability
* Auditability

A project may have all required functions and still fail because it is too slow, inaccurate, insecure, or difficult to use.

## AI-Specific Requirements

AI introduces requirements that traditional applications may not have.

Examples include:

### Accuracy

> The system shall achieve at least 90% answer accuracy on the approved evaluation dataset.

### Hallucination Control

> The system shall not present unsupported information as factual.

### Grounding

> Responses shall be based on approved source information.

### Citation

> The system shall identify the source supporting an answer when applicable.

### Confidence Handling

> The system shall identify situations where sufficient evidence is unavailable.

### Human Escalation

> The system shall provide a defined escalation path when the AI cannot reliably answer a request.

### Access Control

> The system shall restrict information according to the user's authorized access level.

These requirements help define how the AI should behave, not simply what features it should contain.

## Requirements Prioritization

Not every requirement has equal importance.

A common prioritization framework is **MoSCoW**:

* **Must Have** — required for the solution to be viable
* **Should Have** — important but not immediately critical
* **Could Have** — desirable if resources permit
* **Won't Have** — intentionally excluded from the current release

Prioritization should consider:

* Business value
* Risk
* Regulatory requirements
* User impact
* Dependencies
* Cost
* Technical feasibility
* Schedule

The PM should make tradeoffs visible rather than allowing every stakeholder to label everything as "high priority."

## Requirements Traceability

Requirements traceability connects requirements to the reason they exist and the evidence that they were satisfied.

A basic traceability chain is:

**Business Outcome → Requirement → User Story → Acceptance Criteria → Test → Result**

Example:

| Business Outcome       | Requirement                | User Story           | Acceptance Criteria                           | Test          |
| ---------------------- | -------------------------- | -------------------- | --------------------------------------------- | ------------- |
| Reduce processing time | Automated request handling | User submits request | Supported request receives automated response | Response test |

Traceability helps answer:

* Why does this requirement exist?
* Who requested it?
* What business outcome does it support?
* How will it be tested?
* Was it actually delivered?

## Requirement Quality

A strong requirement should be:

### Clear

The requirement should have one reasonable interpretation.

### Specific

Avoid vague terms such as:

* Fast
* Easy
* User-friendly
* Accurate
* Secure

Unless they are defined measurably.

### Testable

The team must be able to determine whether the requirement has been met.

### Traceable

The requirement should connect to a business need or outcome.

### Feasible

The requirement must be achievable within the project's constraints.

### Approved

The appropriate stakeholders must agree that the requirement represents the intended need.

## Common Requirements Problems

### Solution Bias

Starting with:

> "The system must use AI."

Instead of:

> "What business outcome requires this capability?"

### Ambiguous Language

Example:

> "The system should respond quickly."

Better:

> "The system shall return a response within ten seconds for at least 95% of supported requests."

### Missing Acceptance Criteria

A requirement without acceptance criteria can create disagreements later.

### Scope Creep

New requirements continually enter the project without evaluating their effect on:

* Schedule
* Cost
* Resources
* Risk
* Dependencies

### Conflicting Requirements

Two stakeholders may request incompatible behavior.

The PM must surface and resolve the conflict rather than allowing the development team to decide silently.

## Practical Exercise 3: Build The Requirements

### Scenario

A company is considering an AI Customer Support Assistant.

The current customer-support process has several problems:

* Customers wait too long for responses.
* Support staff answer many repetitive questions.
* Information is stored across several approved sources.
* Some questions require human judgment.
* Leadership wants to improve response speed without reducing answer quality.

The project sponsor asks you to define the initial requirements.

You are the project manager.

### Part 1: Identify The Requirements

Create:

* Three business requirements
* Four functional requirements
* Four non-functional requirements
* Three AI-specific requirements

### Part 2: Write User Stories

Write three user stories.

Each story must include:

* User
* Need
* Business benefit

### Part 3: Write Acceptance Criteria

Write at least three acceptance criteria for one of your user stories.

Your acceptance criteria must be measurable or objectively testable.

### Part 4: Prioritize

Using MoSCoW, classify your requirements as:

* Must Have
* Should Have
* Could Have
* Won't Have

Explain one prioritization decision.

### Part 5: Identify The Risk

Identify one requirement-related risk.

Explain:

* Risk
* Impact
* Likelihood
* Mitigation
* Owner

### Part 6: Build Traceability

Create a simple traceability chain:

**Business Outcome → Requirement → User Story → Acceptance Criteria → Test**

## PM Decision

The sponsor says:

> "Just make the system as accurate as possible."

As the project manager, should you accept this as a requirement?

No.

"Accurate as possible" is not measurable.

The PM should work with stakeholders to define:

* What accuracy means
* How accuracy will be measured
* What dataset will be used
* What minimum threshold is acceptable
* What happens when the system cannot provide a reliable answer

The PM's responsibility is to turn vague expectations into measurable requirements.

## Artifact / Output

Create an:

**AI Project Requirements Specification**

Your document should contain:

* Business Requirements
* Functional Requirements
* Non-Functional Requirements
* AI-Specific Requirements
* User Stories
* Acceptance Criteria
* Prioritization
* Requirement Risks
* Requirements Traceability

## Decision / Reflection

Consider the following:

> A requirement can be technically achievable but still be a poor requirement.

Explain why.

Consider:

* Business value
* User need
* Risk
* Measurability
* Feasibility
* Testability

## Key Takeaways

* Requirements translate business needs into actionable expectations.
* Business requirements describe outcomes.
* Functional requirements describe what the solution does.
* Non-functional requirements describe how the solution must perform.
* AI projects require additional requirements around accuracy, grounding, hallucination, security, access, and human escalation.
* Acceptance criteria make requirements testable.
* Prioritization controls scope.
* Traceability connects business outcomes to testing.
* A strong PM challenges vague requirements rather than simply documenting them.

## Connection To Capstone

The requirements techniques from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will take the project's previously established problem and desired outcomes and translate them into formal business, functional, non-functional, and AI-specific requirements.

You will also create user stories, acceptance criteria, prioritization, and requirements traceability for the project.

# Milestone 3 — Requirements

## Objective

In this milestone, you will translate the validated business problem and stakeholder needs into clear, measurable requirements for the AI product.

The goal is not simply to create a list of features.

The goal is to define **what the product must do, how well it must perform, how success will be measured, and what conditions must be satisfied for the product to be acceptable.**

You will apply Project Management (PM) thinking to:

**Stakeholder Need → Business Value → Product Requirement → Measure → Acceptance Criteria**

---

# What You Will Do

You will:

1. Review the problem and stakeholder needs established in Milestone 2.
2. Translate those needs into product requirements.
3. Define functional and non-functional requirements.
4. Define AI-specific requirements.
5. Define security and access requirements.
6. Establish measurable targets.
7. Write acceptance criteria.
8. Identify requirement risks and dependencies.
9. Prioritize the requirements.
10. Make a PM recommendation about what must be true for the product to succeed.

---

# Why Requirements Matter

An AI product can fail even when the technology works.

For example:

* The AI may answer questions but use the wrong information.
* The product may provide answers without citations.
* The response may be too slow.
* Unsupported questions may receive invented answers.
* Unauthorized users may receive restricted information.
* The product may perform well technically but fail to solve the original business problem.

Requirements prevent these gaps by defining what success means before the team builds and tests the product.

A strong requirement should help the team answer:

> **What must be true for the product to meet the business need?**

---

# Part 1 — Review the Stakeholder Needs

Review the stakeholder analysis from Milestone 2.

Identify the most important needs for:

* Employees.
* Human Resources.
* Information Technology.
* Security and governance stakeholders.
* Project or product leadership.

For each important need, ask:

* What problem does this need address?
* Why does it matter?
* What would success look like?
* What risk exists if the need is not addressed?

---

# Part 2 — Define Product Requirements

Create at least **8 requirements** for PolicyAssist.

Your requirements should include a mix of:

* Functional requirements.
* Non-functional requirements.
* AI-specific requirements.
* Security and access requirements.

Do not make every requirement a feature.

A requirement can define:

* Behavior.
* Quality.
* Performance.
* Security.
* Governance.
* Reliability.
* User experience.
* Business outcome.

---

# Requirement Categories

## Functional Requirements

Functional requirements describe what the product must do.

Examples:

* The system shall retrieve relevant policy information.
* The system shall display supporting citations.
* The system shall identify unsupported questions.
* The system shall provide a human escalation path when sufficient evidence is unavailable.

## Non-Functional Requirements

Non-functional requirements describe how well the product must operate.

Examples:

* Response time.
* Reliability.
* Usability.
* Availability.
* Performance.

Example:

> PolicyAssist should return a response within **10 seconds** under the defined test conditions.

## AI-Specific Requirements

AI-specific requirements define expected AI behavior.

Examples:

* Retrieve authoritative information.
* Ground responses in retrieved evidence.
* Avoid unsupported claims.
* Handle unsupported questions appropriately.
* Maintain defined answer-quality targets.

## Security and Access Requirements

These requirements define who can access information and under what conditions.

Examples:

* Users must only receive information they are authorized to access.
* Confidential information must not be exposed to unauthorized users.
* Authorization issues must be zero.
* Access controls must be validated before production deployment.

---

# Part 3 — Make Requirements Measurable

Avoid vague requirements.

### Weak

> The AI should be accurate.

### Stronger

> PolicyAssist should achieve at least **90% answer accuracy** against the approved evaluation set.

### Weak

> The system should be fast.

### Stronger

> PolicyAssist should return a response within **10 seconds** under the defined performance test conditions.

### Weak

> The system should be secure.

### Stronger

> Unauthorized users must not retrieve restricted policy information, and authorization issues must remain at **0**.

The requirement should make success measurable.

---

# Part 4 — Define Acceptance Criteria

For each major requirement, define acceptance criteria.

Acceptance criteria describe the conditions that must be satisfied for the requirement to be considered complete.

Example:

### Requirement

PolicyAssist shall provide grounded responses supported by authoritative policy information.

### Acceptance Criteria

* The response is based on retrieved policy evidence.
* The policy source is identified.
* A citation is provided when applicable.
* Unsupported information is not presented as fact.
* The expected response behavior passes the defined evaluation test.

Use acceptance criteria that can be tested.

---

# Part 5 — Define Measures

For your major requirements, identify the measure that will determine whether the requirement is satisfied.

Examples include:

| Requirement Area      | Example Measure              |
| --------------------- | ---------------------------- |
| Search efficiency     | Policy search-time reduction |
| Retrieval             | Retrieval accuracy           |
| Answer quality        | Answer accuracy              |
| Hallucination         | Hallucination rate           |
| Citations             | Citation correctness         |
| Unsupported questions | Appropriate refusal rate     |
| Performance           | Response latency             |
| User experience       | User satisfaction            |
| Security              | Authorization issues         |
| Confidentiality       | Confidential data exposure   |

Use measurable evidence whenever possible.

---

# Part 6 — PolicyAssist Success Targets

Use the established PolicyAssist targets.

| Measure                      |      Target | Direction        |
| ---------------------------- | ----------: | ---------------- |
| Policy Search-Time Reduction |        ≥50% | Higher is better |
| Retrieval Accuracy           |        ≥90% | Higher is better |
| Answer Accuracy              |        ≥90% | Higher is better |
| Hallucination Rate           |         <2% | Lower is better  |
| Citation Correctness         |        100% | Higher is better |
| Unsupported-Question Refusal |        100% | Higher is better |
| Response Latency             | ≤10 seconds | Lower is better  |
| User Satisfaction            |        ≥85% | Higher is better |
| Critical Security Incidents  |           0 | Lower is better  |

These targets establish measurable expectations.

Later milestones will evaluate whether the product actually achieves them.

---

# Part 7 — Identify Risks and Dependencies

Requirements can introduce dependencies and risks.

For each major requirement, consider:

* What must exist for this requirement to work?
* What could prevent it from being satisfied?
* Which team or stakeholder owns the dependency?
* What happens if the requirement is missed?

Examples:

### Retrieval Accuracy

Potential dependency:

* High-quality authoritative policy documents.

Potential risk:

* Duplicate or outdated documents may reduce retrieval quality.

### Citation Correctness

Potential dependency:

* Accurate document metadata and source mapping.

Potential risk:

* The system may cite an incorrect or unrelated source.

### Authorization

Potential dependency:

* Identity and access-control mechanisms.

Potential risk:

* Unauthorized users may retrieve restricted information.

---

# Part 8 — Prioritize Requirements

Not every requirement has the same priority.

Use:

* **Must**
* **Should**
* **Could**
* **Deferred / Out of Scope**

Prioritize based on:

* Business value.
* User impact.
* Risk.
* Regulatory or governance importance.
* Technical dependency.
* MVP necessity.

Security and authorization requirements should receive appropriate priority because a security failure can prevent safe deployment.

---

# Part 9 — Requirements Review

Create a requirements table.

| ID   | Requirement | Type | Measure | Acceptance Criteria | Priority | Risk / Dependency |
| ---- | ----------- | ---- | ------- | ------------------- | -------- | ----------------- |
| R-01 |             |      |         |                     |          |                   |
| R-02 |             |      |         |                     |          |                   |
| R-03 |             |      |         |                     |          |                   |
| R-04 |             |      |         |                     |          |                   |
| R-05 |             |      |         |                     |          |                   |
| R-06 |             |      |         |                     |          |                   |
| R-07 |             |      |         |                     |          |                   |
| R-08 |             |      |         |                     |          |                   |

Add additional rows when needed.

---

# Part 10 — PM Decisions

Make at least **three PM decisions** based on your requirements.

Examples:

* Which requirement is essential to the MVP?
* Which requirement creates the highest risk?
* Which requirement depends on another capability?
* Which requirement must be validated before release?
* Which requirement can be deferred?

For each decision, explain:

**Requirement → Evidence → Risk/Impact → Decision**

---

# Requirements Quality Check

Review each requirement.

Ask:

### Is it clear?

Can the team understand what is expected?

### Is it measurable?

Can you determine whether it was achieved?

### Is it testable?

Can evidence be collected?

### Is it relevant?

Does it support the business problem?

### Is ownership clear?

Does someone own the requirement or acceptance decision?

### Is the requirement realistic?

Can it be achieved within the defined scope, constraints, and resources?

---

# Common Requirement Problems

Avoid:

### Vague language

"Easy to use."

Instead define how usability will be evaluated.

### Unmeasurable language

"Highly accurate."

Instead define the accuracy target.

### Feature-only thinking

A list of features does not define product quality.

### Missing acceptance criteria

Without acceptance criteria, the team may disagree about what "complete" means.

### Missing security requirements

Security should be defined as a requirement, not discovered only after development.

### Requirements disconnected from business value

Every major requirement should support a user need, business objective, risk-control objective, or product-quality objective.

---

# Deliverable

Complete a **PolicyAssist Requirements Record** containing:

1. At least 8 requirements.
2. Requirement category/type.
3. Measure.
4. Acceptance criteria.
5. Priority.
6. Risks or dependencies.
7. At least three PM requirement decisions.

---

# Checkpoint

Before moving forward, answer:

> **What must be true for PolicyAssist to solve the original business problem safely and effectively?**

Your answer should connect:

**Business Need → Requirement → Measure → Acceptance Criteria**

---

# PM Perspective

A Project Manager does not simply collect requirements.

The PM helps the team determine:

**What matters → Why it matters → How success will be measured → How it will be accepted → What risk exists if it fails**

Good requirements create the foundation for:

**Backlog → MVP → Architecture → Evaluation → Testing → Release**

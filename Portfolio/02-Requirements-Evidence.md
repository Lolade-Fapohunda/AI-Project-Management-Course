# 02: Requirements Evidence

## Purpose

This artifact demonstrates how the Petadel PolicyAssist AI business problem was translated into measurable, testable, and traceable requirements.

The requirements establish what the product must accomplish, how it should behave, what constraints apply, and how acceptance will be determined.

The requirements also provide the foundation for:

**Product Backlog → Acceptance Criteria → Testing → Evaluation → UAT → Release Decision**

---

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Requirement Type:** AI Product Requirements

---

## Business Need

Employees need a faster and more reliable way to locate and interpret approved internal policy information.

The solution must reduce reliance on manual searching while preventing the AI from presenting outdated, unauthorized, conflicting, or unsupported information as fact.

---

## Requirement Management Approach

The project separates requirements into several categories:

* Business Requirements
* Functional Requirements
* Non-Functional Requirements
* AI-Specific Requirements
* Data Requirements
* Policy Authority Requirements
* Security Requirements
* Evaluation Requirements
* Testing Requirements
* UAT Requirements
* Release Requirements
* Monitoring Requirements

This separation allows different types of expectations to be managed and validated appropriately.

---

# Business Requirements

| ID     | Business Requirement                                                                                 | Priority  |
| ------ | ---------------------------------------------------------------------------------------------------- | --------- |
| BR-001 | Employees must have a faster method for locating relevant internal policy information.               | Must Have |
| BR-002 | The system must provide information grounded in approved organizational policies.                    | Must Have |
| BR-003 | The system must reduce the risk of employees relying on outdated or unauthorized policy information. | Must Have |
| BR-004 | The system must identify and use authoritative policy versions.                                      | Must Have |
| BR-005 | The system must safely handle questions that cannot be answered from approved policy information.    | Must Have |
| BR-006 | The system must protect policy information according to applicable access restrictions.              | Must Have |
| BR-007 | The system must provide sufficient evidence to support AI-generated policy responses.                | Must Have |
| BR-008 | The system must support measurable evaluation of AI response quality.                                | Must Have |
| BR-009 | The solution must provide a controlled path from MVP to production readiness.                        | Must Have |

---

# Functional Requirements

| ID     | Functional Requirement                                                                                          | Priority    |
| ------ | --------------------------------------------------------------------------------------------------------------- | ----------- |
| FR-001 | The system shall allow a user to submit a policy-related question.                                              | Must Have   |
| FR-002 | The system shall process approved policy documents for retrieval.                                               | Must Have   |
| FR-003 | The system shall retrieve policy content relevant to the user's question.                                       | Must Have   |
| FR-004 | The system shall validate policy eligibility before using retrieved information.                                | Must Have   |
| FR-005 | The system shall use only eligible policy information for grounded responses.                                   | Must Have   |
| FR-006 | The system shall generate a response based on retrieved evidence.                                               | Must Have   |
| FR-007 | The system shall provide a supporting citation when the retrieved evidence substantively supports the response. | Must Have   |
| FR-008 | The system shall not present an unsupported document as evidence for an answer.                                 | Must Have   |
| FR-009 | The system shall safely refuse questions when sufficient approved evidence is unavailable.                      | Must Have   |
| FR-010 | The system shall identify unsupported portions of mixed questions.                                              | Must Have   |
| FR-011 | The system shall answer supported portions of mixed questions when sufficient evidence exists.                  | Must Have   |
| FR-012 | The system shall not invent information for unsupported portions of a question.                                 | Must Have   |
| FR-013 | The system shall prevent draft or superseded policies from being treated as active authoritative knowledge.     | Must Have   |
| FR-014 | The system shall support policy metadata required for eligibility validation.                                   | Must Have   |
| FR-015 | The system shall support human escalation for unresolved policy-authority conflicts.                            | Must Have   |
| FR-016 | The system shall allow the policy knowledge base to be refreshed when approved source information changes.      | Should Have |
| FR-017 | The system shall support user feedback or escalation when an answer requires review.                            | Should Have |

---

# Non-Functional Requirements

| ID      | Requirement                  | Target                                                                 |
| ------- | ---------------------------- | ---------------------------------------------------------------------- |
| NFR-001 | Response Performance         | ≤ 10 seconds under defined representative conditions                   |
| NFR-002 | Retrieval Accuracy           | ≥ 90%                                                                  |
| NFR-003 | Answer Accuracy              | ≥ 90%                                                                  |
| NFR-004 | Hallucination Rate           | < 2%                                                                   |
| NFR-005 | Citation Correctness         | 100%                                                                   |
| NFR-006 | Unsupported-Question Refusal | 100%                                                                   |
| NFR-007 | Critical Security Incidents  | 0                                                                      |
| NFR-008 | Unauthorized Policy Access   | 0                                                                      |
| NFR-009 | User Satisfaction            | ≥ 85%                                                                  |
| NFR-010 | Availability                 | Defined according to production operating requirements                 |
| NFR-011 | Maintainability              | Policy and model changes must follow controlled change processes       |
| NFR-012 | Auditability                 | Material project, governance, and release decisions must be documented |

---

# AI-Specific Requirements

## Grounding

AI responses must be grounded in retrieved evidence.

The language model must not be treated as the authoritative source of organizational policy.

---

## Hallucination Control

The system must not invent policy requirements, benefits, restrictions, deadlines, or other organizational information.

If sufficient evidence does not exist, the system must refuse or identify the limitation.

---

## Unsupported Questions

For questions outside the available approved policy knowledge:

**Expected Behavior:**

> The system should clearly indicate that it does not have sufficient approved information to provide an answer.

The system must not fabricate an answer merely to satisfy the user.

---

## False-Premise Questions

The system must recognize questions that contain unsupported assumptions.

For example:

> "How many weeks of paid vacation does every employee receive?"

If no approved policy establishes that premise, the system must not accept the assumption as fact.

---

## Mixed Questions

Mixed questions must be evaluated component by component.

For example:

> "How many days can I work remotely, and how many vacation days do I receive?"

If remote-work information exists but vacation information does not, the system may answer the supported portion while identifying the unsupported portion.

It must not fabricate the missing information.

---

## Citation Requirement

A citation may only be presented when the cited evidence substantively supports the response.

The requirement is:

> **Citation Presence ≠ Citation Correctness**

A citation that exists but does not support the answer is considered a quality defect.

---

# Data Requirements

Production-eligible policy information must have required metadata.

At minimum:

* Policy ID
* Policy name
* Policy owner
* Version
* Effective date
* Status
* Approval status
* Document type
* Applicable audience
* Required access classification where applicable

---

# Policy Authority Requirements

PolicyAssist must use only authoritative policy information.

The governing rule is:

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

The system must not automatically treat every document in the repository as authoritative.

---

## Policy Status

Policy information may have statuses including:

* Draft
* Pending Approval
* Active
* Superseded
* Archived
* Expired
* Unverified

Only information meeting the defined eligibility requirements may be used as active AI knowledge.

---

## Version Control

The project must distinguish current versions from historical versions.

Example:

**Version 3.0 — Active**

**Version 2.0 — Superseded**

Version 3.0 is eligible.

Version 2.0 is not eligible for active policy retrieval.

---

# Authority Conflict Requirements

If two policy sources conflict, PolicyAssist must not automatically select the document that appears more relevant.

The project must establish:

1. Policy ownership.
2. Approval status.
3. Effective date.
4. Version.
5. Active status.
6. Source-of-truth designation.

If authority still cannot be established:

> **Hold the information and escalate for human resolution.**

---

# Security Requirements

| ID      | Requirement                                                                                   |
| ------- | --------------------------------------------------------------------------------------------- |
| SEC-001 | Users must only access information they are authorized to access.                             |
| SEC-002 | The system must prevent unauthorized disclosure of restricted policy information.             |
| SEC-003 | The system must prevent critical data leakage.                                                |
| SEC-004 | Security-sensitive behavior must be validated before production release.                      |
| SEC-005 | Security findings must be tracked and dispositioned.                                          |
| SEC-006 | Critical security findings must block production release until resolved or formally governed. |

---

# Evaluation Requirements

The project must establish a structured evaluation dataset.

The minimum evaluation dataset is:

**30 cases**

Evaluation categories include:

* Direct questions.
* Paraphrased questions.
* Unsupported questions.
* False-premise questions.
* Mixed questions.
* Multi-policy questions.
* Authority/version questions.
* Performance and edge cases.

Evaluation must measure:

* Retrieval accuracy.
* Answer accuracy.
* Grounding.
* Hallucination.
* Citation correctness.
* Unsupported-question refusal.
* Performance.

---

# Testing Requirements

Testing must include:

* Functional testing.
* Negative testing.
* Edge-case testing.
* Security validation.
* Regression testing.
* AI evaluation.
* UAT.

Testing must demonstrate coverage of critical requirements.

---

# UAT Requirements

User Acceptance Testing must confirm that the product meets business expectations.

Critical UAT scenarios include:

* Policy retrieval.
* Remote-work questions.
* Attendance questions.
* Expense questions.
* Information-security questions.
* Code-of-conduct questions.
* Unsupported questions.
* False-premise questions.
* Multi-policy questions.
* Superseded or draft policies.
* Conflicting authority.

---

# Release Requirements

Production release requires evidence that mandatory readiness gates have been satisfied.

The release decision must consider:

* Requirements.
* Data readiness.
* AI quality.
* Security.
* Governance.
* Testing.
* UAT.
* Performance.
* Monitoring.
* Rollback.
* Risks.
* Defects.
* Approvals.

A working prototype alone is not sufficient for production approval.

---

# Monitoring Requirements

After release, the project must monitor:

* Retrieval quality.
* Answer quality.
* Hallucination.
* Citation correctness.
* Response latency.
* User satisfaction.
* Security incidents.
* Policy changes.
* Data changes.
* Model changes.
* User feedback.
* Business outcomes.

Material changes must trigger appropriate evaluation, testing, approval, and release processes.

---

# Requirement Acceptance Model

Requirements are not considered complete simply because functionality has been implemented.

Acceptance follows:

**Requirement**

↓

**Acceptance Criteria**

↓

**Implementation**

↓

**Test / Evaluation**

↓

**Evidence**

↓

**Acceptance Decision**

---

# Requirement Traceability

The project maintains traceability across the delivery lifecycle:

| Requirement Area        | Backlog | Test / Evaluation | UAT | Release |
| ----------------------- | ------- | ----------------- | --- | ------- |
| Business Outcomes       | ✓       | ✓                 | ✓   | ✓       |
| Functional Requirements | ✓       | ✓                 | ✓   | ✓       |
| AI Quality              | ✓       | ✓                 | ✓   | ✓       |
| Data Governance         | ✓       | ✓                 | ✓   | ✓       |
| Security                | ✓       | ✓                 | ✓   | ✓       |
| Policy Authority        | ✓       | ✓                 | ✓   | ✓       |
| Performance             | ✓       | ✓                 | ✓   | ✓       |
| Monitoring              | ✓       | ✓                 | ✓   | ✓       |

The detailed traceability artifact provides the requirement-to-evidence relationship.

---

# MoSCoW Prioritization

Requirements were prioritized using **MoSCoW**:

### Must Have

Required for the MVP or critical to safe operation.

Examples:

* Policy retrieval.
* Authority validation.
* Grounded responses.
* Citation correctness.
* Unsupported-question refusal.
* Security controls.
* Critical performance requirements.

### Should Have

Important capabilities that improve the product but may not block the initial MVP.

Examples:

* Enhanced feedback.
* Additional administrative functionality.
* Expanded knowledge-management capabilities.

### Could Have

Useful improvements that can be considered after core requirements are satisfied.

### Won't Have

Capabilities deliberately excluded from the current scope.

This protects the project from uncontrolled scope expansion.

---

# Requirement Change Control

Requirements may change when:

* Business priorities change.
* New risks are identified.
* Security requirements change.
* Policy governance changes.
* Evaluation reveals unexpected behavior.
* Technical constraints emerge.
* Users identify material gaps.

Changes must be:

1. Identified.
2. Documented.
3. Assessed for impact.
4. Reviewed by appropriate stakeholders.
5. Approved.
6. Updated in affected artifacts.
7. Tested.
8. Traced through the delivery lifecycle.

---

# PM Requirements Quality Check

Before accepting a requirement, the Project Manager should confirm:

* [ ] The requirement addresses a defined business need.
* [ ] The requirement is specific.
* [ ] The requirement is measurable.
* [ ] The requirement is testable.
* [ ] The requirement has an identified priority.
* [ ] The requirement has appropriate acceptance criteria.
* [ ] Dependencies are understood.
* [ ] Security implications are considered.
* [ ] Data implications are considered.
* [ ] AI-specific risks are considered.
* [ ] The requirement is traceable.
* [ ] Stakeholders understand the requirement.

---

# Key PM Judgment

One of the most important requirement decisions in PolicyAssist was refusing to define the system simply as:

> "An AI chatbot that answers employee questions."

That requirement would be too vague.

The project instead defines expectations around:

* What information may be used.
* Which sources are authoritative.
* How answers must be grounded.
* When citations may be displayed.
* When the system must refuse.
* How security is enforced.
* How quality is measured.
* How acceptance is determined.
* When production release is permitted.

This converts an ambiguous AI idea into a manageable product requirement framework.

---

# Current Requirements Position

**Status: Defined / Continuing Reconciliation**

The major requirement categories have been established.

The remaining project-management activity is to maintain alignment between:

**Requirements**

→

**Product Backlog**

→

**Acceptance Criteria**

→

**Testing & Evaluation**

→

**UAT**

→

**Release Decision**

---

# Portfolio Evidence

This artifact demonstrates the ability to:

* Translate business needs into requirements.
* Manage AI-specific requirements.
* Establish measurable quality expectations.
* Define data and authority requirements.
* Incorporate security into requirements.
* Establish acceptance criteria.
* Prioritize scope.
* Maintain traceability.
* Manage requirement changes.
* Connect requirements to release decisions.

---

## Evidence Principle

> **A requirement is not complete because it has been written. It is complete when its acceptance criteria have been satisfied and the evidence supports acceptance.**

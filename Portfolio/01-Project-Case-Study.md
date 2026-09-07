# 01: Project Case Study

## Project

**Petadel PolicyAssist AI**

**Organization:** Petadel Technology Services (PTS)

**Project Type:** Internal Generative AI Knowledge Assistant

**Role:** AI Project Manager

**Project Focus:** AI Product Planning, Delivery, Governance, Evaluation, and Release Readiness

---

## Project Overview

Petadel Technology Services identified an opportunity to improve how employees locate and interpret internal policies.

The organization maintained a large collection of policy documents across different formats and potential versions. Employees could encounter outdated documents, duplicate information, conflicting policies, incomplete metadata, and information with different access requirements.

The proposed solution was **Petadel PolicyAssist AI**, an internal AI knowledge assistant designed to help employees locate approved policy information and receive responses grounded in authoritative sources.

The project required more than selecting an AI model. It required establishing the business requirements, product scope, data governance, AI quality standards, security controls, testing strategy, release criteria, and ongoing monitoring model necessary to operate the solution responsibly.

---

## Business Problem

Employees may spend unnecessary time searching for policy information and determining whether the information they find is current and authoritative.

The underlying problem is not simply document search.

It includes:

* Difficulty locating relevant policies.
* Multiple copies of the same information.
* Outdated policy versions.
* Draft and unapproved documents.
* Conflicting policy statements.
* Missing ownership information.
* Inconsistent metadata.
* Scanned documents requiring additional processing.
* Access restrictions.
* Dependence on human assistance to resolve uncertainty.

These conditions create both operational inefficiency and business risk.

---

## Business Objective

The objective was to design and manage an AI solution capable of helping employees retrieve approved internal policy information more efficiently while maintaining appropriate controls over accuracy, authority, security, and access.

The solution was expected to:

* Retrieve relevant policy information.
* Use authoritative and active policy sources.
* Generate grounded responses.
* Provide appropriate supporting citations.
* Refuse unsupported questions.
* Handle false-premise questions safely.
* Handle mixed questions without inventing unsupported information.
* Respect access restrictions.
* Escalate unresolved policy-authority conflicts.

---

## Project Management Challenge

The central project-management challenge was balancing:

**Business Value**

with

**AI Reliability**

**Data Governance**

**Security**

**User Experience**

**Project Schedule**

**Release Risk**

Leadership wanted the solution delivered quickly.

However, accelerating implementation by simply ingesting all available documents would introduce significant risks.

The project therefore established a principle:

> **The fastest path to a working AI system is not necessarily the fastest path to a reliable AI product.**

---

## PM Approach

The project was managed across the AI product lifecycle:

**Initiation**

↓

**Discovery**

↓

**Requirements**

↓

**Agile Planning**

↓

**Architecture**

↓

**Data Governance**

↓

**AI Evaluation**

↓

**Risk & Security**

↓

**Testing & UAT**

↓

**Release**

↓

**Monitoring**

↓

**Continuous Improvement**

Each stage established evidence and decision criteria for the next.

---

## Requirements Management

The project translated the business problem into structured requirements covering:

* Business outcomes.
* Functional behavior.
* Non-functional requirements.
* AI-specific behavior.
* Data readiness.
* Policy authority.
* Security.
* Evaluation.
* Testing.
* UAT.
* Release.
* Monitoring.

Requirements were connected to acceptance criteria and traceability.

This ensured that project decisions could be evaluated against defined expectations rather than subjective opinions.

---

## Product Planning

The product backlog contains:

**10 Epics**

**58 User Stories**

**3 Releases**

The epics cover:

1. Security & Access
2. Policy Knowledge Base / Ingestion
3. Policy Retrieval
4. AI Response / Grounding
5. User Experience
6. Performance & Reliability
7. Human Escalation & Feedback
8. Administration / Governance
9. Evaluation / Testing
10. Monitoring / Continuous Improvement

The MVP was deliberately focused on the core policy-question journey rather than attempting to solve every organizational knowledge problem.

---

## AI Architecture

The solution uses a Retrieval-Augmented Generation (RAG) architecture.

### Architecture Flow

**Policy Documents**

↓

**Document Processing**

↓

**Chunking**

↓

**Embeddings**

↓

**Vector Database**

↓

**Retrieval**

↓

**Eligibility Validation**

↓

**Large Language Model**

↓

**Grounding**

↓

**Application-Controlled Citation**

↓

**Streamlit Interface**

The architecture separates retrieval and policy eligibility decisions from the model's language-generation role.

This reduces the risk of allowing the language model to determine which policy information is authoritative.

---

## Data Governance Decision

One of the most important project decisions was establishing a formal eligibility rule for policy information.

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

Information that does not satisfy the required criteria is not automatically treated as valid AI knowledge.

This includes:

* Draft policies.
* Superseded policies.
* Unverified information.
* Documents with unresolved authority.
* Documents missing required metadata.

When authority cannot be established, the project requires human resolution.

---

## AI Response Controls

The project established several response controls.

### Supported Question

If sufficient authoritative evidence exists:

**Answer + Supporting Citation**

### Unsupported Question

If sufficient evidence does not exist:

**Safe Refusal + No Unsupported Citation**

### Conflicting Policy Authority

If sources conflict and authority cannot be established:

**Do Not Guess → Escalate For Human Resolution**

### Mixed Question

Each component of the question is evaluated independently.

Supported information may be answered.

Unsupported information must not be invented.

---

## AI Quality Management

The project established measurable quality targets.

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |
| Critical Security Incidents  |            0 |
| User Satisfaction            |        ≥ 85% |

A minimum structured evaluation dataset of **30 cases** was established.

Evaluation categories include:

* Direct questions.
* Paraphrased questions.
* Unsupported questions.
* False premises.
* Mixed questions.
* Multi-policy questions.
* Authority and version scenarios.
* Performance and edge cases.

---

## Security & Governance

Security was treated as a release gate rather than a post-launch improvement.

Key considerations included:

* Authentication.
* Authorization.
* Confidential information.
* Personally Identifiable Information (PII).
* Data leakage.
* Prompt injection.
* Unauthorized policy retrieval.
* Human oversight.
* Policy authority.
* Governance approval.
* Incident management.

Critical security failures are release blockers.

---

## Testing & UAT

The project separates:

**Testing**

from

**AI Evaluation**

from

**User Acceptance Testing**

Testing covers functional, negative, edge-case, security, and regression scenarios.

UAT covers real user scenarios involving:

* Policy retrieval.
* Unsupported questions.
* False premises.
* Multi-policy questions.
* Superseded policies.
* Draft policies.
* Conflicting policy authority.
* Access-sensitive information.

This prevents technical functionality from being mistaken for business acceptance.

---

## Release Management

The project established formal release gates.

A production release requires evidence across:

* Requirements.
* MVP functionality.
* Data readiness.
* AI quality.
* Security.
* Governance.
* Testing.
* UAT.
* Performance.
* Monitoring.
* Rollback.
* Risk.
* Defects.

The deployment strategy uses a controlled pilot followed by phased expansion.

---

## Prototype Outcome

The PolicyAssist prototype successfully demonstrated the core AI workflow.

Demonstrated capabilities include:

* Multi-policy ingestion.
* Semantic retrieval.
* Policy eligibility controls.
* Grounded responses.
* Source citation handling.
* Unsupported-question refusal.
* False-premise handling.
* Mixed-question handling.
* Local AI execution.

The prototype therefore demonstrated technical feasibility.

However, technical feasibility was not treated as equivalent to production readiness.

---

## Current Project Decision

# HOLD

The project is currently classified as **HOLD**.

The prototype has been demonstrated, but additional evidence is required before production release.

Remaining areas include:

* Formal AI evaluation.
* UAT.
* Pilot validation.
* Production security validation.
* Monitoring readiness.
* Rollback validation.
* Governance approval.
* Final evidence review.

---

## Why HOLD Is The Correct PM Decision

A Project Manager should not approve production simply because:

> "The AI works."

The release decision must consider whether the complete product is:

* Reliable.
* Secure.
* Governed.
* Tested.
* Accepted.
* Monitored.
* Recoverable.
* Supported by evidence.

The current HOLD decision demonstrates evidence-based project governance rather than schedule-driven release approval.

---

## Key PM Decisions

The project demonstrates the following decisions:

| Decision                                         | PM Rationale                                               |
| ------------------------------------------------ | ---------------------------------------------------------- |
| Use RAG architecture                             | Enables retrieval of controlled organizational knowledge   |
| Require authoritative active policies            | Reduces outdated and conflicting information               |
| Do not automatically resolve authority conflicts | Prevents AI from making governance decisions               |
| Control citations through the application        | Prevents unsupported model-generated citations             |
| Refuse unsupported questions                     | Reduces hallucination risk                                 |
| Evaluate mixed questions independently           | Prevents unsupported portions from being presented as fact |
| Establish measurable AI thresholds               | Creates objective release criteria                         |
| Require a structured evaluation dataset          | Provides repeatable evidence                               |
| Treat security as a release gate                 | Protects organizational information                        |
| Separate UAT from AI evaluation                  | Confirms both technical and business acceptance            |
| Require rollback capability                      | Provides controlled recovery                               |
| Establish monitoring                             | Supports responsible post-release management               |

---

## Professional Competencies Demonstrated

This case study demonstrates competency in:

* AI project initiation.
* Business analysis.
* Requirements management.
* Agile product planning.
* AI technology assessment.
* Data governance.
* AI evaluation.
* Risk management.
* Security governance.
* Testing.
* UAT.
* Release management.
* Monitoring.
* Stakeholder decision-making.
* Evidence-based project governance.

---

## Project Management Lessons

### 1. AI Is Not Just A Technology Project

AI introduces additional considerations around uncertainty, evaluation, data quality, grounding, hallucination, and changing behavior.

### 2. Data Readiness Is A Project Dependency

A large document collection does not automatically constitute usable AI knowledge.

### 3. Authority Must Be Explicit

The AI should not determine organizational policy authority through similarity or probability.

### 4. Evaluation Must Be Measurable

Statements such as "the AI works well" are insufficient for release decisions.

### 5. Security Must Be Designed Into The Product

Unauthorized access or information disclosure can make an otherwise functional system unacceptable.

### 6. A Working Prototype Is Not A Production Product

Production readiness requires evidence across multiple dimensions.

### 7. PM Judgment Is Critical

The Project Manager must be willing to recommend **HOLD** when evidence does not support release—even when stakeholders want to launch.

---

## Evidence

Detailed supporting artifacts are maintained in the capstone project:

* Project Overview
* Project Charter
* Requirements
* Product Backlog
* Architecture
* Data Governance
* Evaluation Plan
* Risk, Security & Governance
* Testing, UAT & Pilot
* Release & Deployment
* Monitoring & Continuous Improvement
* Decision Log
* Risk Register
* Traceability
* Executive Summary
* Final Go / Hold / No-Go Decision

---

## Final Case Study Statement

Petadel PolicyAssist AI demonstrates an AI Project Management approach that connects:

**Business Need**

↓

**Requirements**

↓

**Product Planning**

↓

**AI Architecture**

↓

**Data Governance**

↓

**Evaluation**

↓

**Security**

↓

**Testing & UAT**

↓

**Release Readiness**

↓

**Monitoring**

The project demonstrates that successful AI Project Management is not simply about getting an AI system to produce an answer.

It is about ensuring that the product produces the **right answer, from the right information, for the right user, under the right controls—and that there is sufficient evidence to justify the decision to release it.**

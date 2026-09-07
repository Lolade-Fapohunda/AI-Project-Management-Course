# Project Overview

## Project Name

**Petadel PolicyAssist AI**

## Organization

**Petadel Technology Services (PTS)**

## Project Type

Artificial Intelligence (AI) Project

## Project Purpose

Petadel PolicyAssist AI is an AI-powered policy assistance solution designed to help employees quickly locate and understand authoritative company policies.

The solution uses approved policy documents as its knowledge source and provides grounded responses based on the applicable policy information.

---

## Business Problem

Employees currently experience difficulty locating and understanding company policies.

Policy information may be:

* Difficult to locate
* Distributed across multiple documents
* Available in different versions
* Difficult to interpret
* Potentially inconsistent across sources

This creates unnecessary search time and increases the risk that employees rely on outdated, incorrect, or unauthorized policy information.

---

## Business Objective

The project aims to provide employees with a reliable and efficient way to retrieve policy information while ensuring that responses are grounded in authoritative and active policy sources.

---

## Initial Success Targets

The project establishes the following initial targets:

| Measure                      |                 Target |
| ---------------------------- | ---------------------: |
| Policy search time           | Reduce by at least 50% |
| Response latency             |           ≤ 10 seconds |
| Retrieval accuracy           |                  ≥ 90% |
| Answer accuracy              |                  ≥ 90% |
| Hallucination rate           |                   < 2% |
| Citation correctness         |                   100% |
| Unsupported-question refusal |                   100% |
| Critical security incidents  |                      0 |
| User satisfaction            |                  ≥ 85% |

These targets must be validated through appropriate evaluation, testing, and User Acceptance Testing (UAT).

---

## Core Project Principle

PolicyAssist must use only authoritative, active policy information.

### Data Readiness Rule

A policy is eligible for retrieval only when:

**Active + Authoritative + Approved + Required Metadata Present = Eligible**

Policies that are:

* Draft
* Superseded
* Unverified
* Conflicting
* Missing required metadata

must not be automatically used as authoritative policy evidence.

---

## Authority Conflict Rule

If multiple policy documents conflict and the authoritative version cannot be established, PolicyAssist must not automatically select one.

The issue must be flagged for resolution by the appropriate policy owner or authorized governance authority.

---

## Core User Experience

A user should be able to:

1. Enter a policy-related question.
2. Submit the question.
3. Receive a grounded response when sufficient evidence exists.
4. See the supporting policy source when the evidence substantively supports the answer.
5. Receive an appropriate refusal when sufficient authoritative evidence is unavailable.

---

## Citation Rule

PolicyAssist must display a source citation only when the retrieved policy evidence substantively supports the response.

If the available evidence does not support an answer:

* The system should not invent information.
* The system should not present an unrelated document as evidence.
* The system should not imply that unsupported information came from an authoritative policy.

---

## Mixed Questions

When a user asks a question containing both supported and unsupported components, PolicyAssist should evaluate each component independently.

The system should:

* Answer the supported portion.
* Identify the unsupported portion.
* Provide citations for supported information.
* Avoid inventing an answer to unsupported portions.

---

## High-Level Solution Architecture

```text
Policy Documents
       ↓
Document Processing
       ↓
Chunking
       ↓
Embeddings
       ↓
Vector Database
       ↓
Semantic Retrieval
       ↓
Large Language Model (LLM)
       ↓
Grounding & Citation
       ↓
PolicyAssist User Interface
```

---

## Technology Stack

| Technology            | Role                                     |
| --------------------- | ---------------------------------------- |
| Python                | Programming language                     |
| Streamlit             | Application and user interface framework |
| Sentence Transformers | Embedding framework/library              |
| all-MiniLM-L6-v2      | Embedding model                          |
| ChromaDB              | Vector database                          |
| Ollama                | Local AI runtime                         |
| Llama 3.2 3B          | Large Language Model (LLM)               |

The Project Manager does not need to implement every technical component but must understand the role, dependencies, risks, and project implications of each component.

---

## Project Lifecycle

The project follows the complete AI project lifecycle:

**Initiation → Discovery → Requirements → Planning → Architecture → Build → Evaluation → Security & Governance → UAT → Release → Monitoring → Continuous Improvement**

---

## Product Backlog

The project contains **10 epics and 58 user stories**.

### Epics

1. Security & Access
2. Policy Knowledge Base/Ingestion
3. Policy Retrieval
4. AI Response/Grounding
5. User Experience
6. Performance & Reliability
7. Human Escalation & Feedback
8. Administration/Governance
9. Evaluation/Testing
10. Monitoring/Continuous Improvement

---

## Release Structure

The backlog is organized into three major releases:

### Release 1 — Foundation

Establish the core data, security, knowledge, retrieval, and technical foundation.

### Release 2 — MVP Product

Deliver the minimum viable user experience and core AI policy-assistance capabilities.

### Release 3 — Production Readiness

Complete evaluation, security, governance, UAT, monitoring, operational readiness, and release controls.

---

## Project Management Focus

The Project Manager is responsible for ensuring that the project:

* Solves the intended business problem.
* Maintains clear scope.
* Meets defined requirements.
* Has appropriate stakeholder involvement.
* Uses reliable and authorized data.
* Produces measurable AI quality.
* Manages risks and security.
* Meets UAT expectations.
* Has sufficient release evidence.
* Includes monitoring and operational ownership.
* Supports evidence-based Go, Hold, or No-Go decisions.

---

## Definition Of Success

PolicyAssist is successful only when both the technology and the project outcomes are successful.

A working AI application alone does not constitute project success.

Success requires:

**Business Value + Requirements + Data Readiness + AI Quality + Security + Governance + User Acceptance + Operational Readiness**

---

## Capstone Role

This project serves as the practical capstone for the AI Project Management Course.

The learner will use the project to demonstrate the ability to lead an AI initiative from business problem through production and continuous improvement.

The final capstone portfolio will contain the major Project Management artifacts, decisions, evaluations, and recommendations developed throughout the course.

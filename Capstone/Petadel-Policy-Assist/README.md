# Petadel PolicyAssist AI

## Capstone Overview

**Project:** Petadel PolicyAssist AI

**Organization:** Petadel Technology Services (PTS)

**Project Type:** Internal Generative AI Policy Knowledge Assistant

**Course:** AI Project Management Course

**Primary Role:** AI Project Manager

---

## 1. Business Problem

Employees may have difficulty locating, identifying, and interpreting the correct internal policy information because organizational policies can exist across multiple documents, versions, repositories, and formats.

The project addresses:

* Policy discovery.
* Outdated policy versions.
* Duplicate or conflicting information.
* Unclear policy authority.
* Scanned or difficult-to-search documents.
* Access-control concerns.
* Increased dependency on human assistance.

---

## 2. Business Objective

The objective of PolicyAssist is to provide employees with a faster and more reliable way to locate approved internal policy information while maintaining appropriate governance, security, accuracy, and source traceability.

---

## 3. Success Targets

The project establishes the following targets:

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |
| User Satisfaction            |        ≥ 85% |
| Critical Security Incidents  |            0 |

These targets require documented evaluation evidence before production acceptance.

---

## 4. Core Product Principle

PolicyAssist must use eligible policy information as the source for responses.

The system follows:

**Retrieve → Ground → Answer → Cite**

When sufficient authoritative evidence does not exist:

**Do Not Invent → Refuse or Escalate**

The application must not treat the language model as an independent source of company policy.

---

## 5. Core Governance Rule

PolicyAssist may use a policy as authoritative evidence only when the policy is:

**Active + Authoritative + Approved + Required Metadata Present = Eligible**

The system must not automatically rely on:

* Draft policies.
* Superseded policies.
* Unverified policies.
* Policies with missing required metadata.
* Unresolved conflicting policies.

---

## 6. Product Lifecycle

The capstone follows the complete project lifecycle:

**Initiation → Discovery → Requirements → Planning → Architecture → Build → Evaluation → Security and Governance → UAT → Release → Monitoring → Continuous Improvement**

The Project Manager maintains alignment between these phases.

---

## 7. Product Backlog

The PolicyAssist backlog contains:

**10 Epics**

**58 User Stories**

**3 Releases**

### Epics

1. Security & Access
2. Policy Knowledge Base and Ingestion
3. Policy Retrieval
4. Response and Grounding
5. User Experience
6. Performance and Reliability
7. Human Escalation and Feedback
8. Administration and Governance
9. Evaluation and Testing
10. Monitoring and Continuous Improvement

### Releases

**Release 1: Foundation**

Establish the secure and governed policy knowledge foundation.

**Release 2: MVP Product**

Deliver the core employee policy-assistance experience.

**Release 3: Production Readiness**

Validate quality, security, governance, UAT, monitoring, reliability, and release readiness.

---

## 8. Technical Architecture

The current prototype architecture is:

**Policy Documents → Document Processing → Chunking → Embeddings → ChromaDB → Semantic Retrieval → Response Generation → Grounding and Citation → Streamlit Application**

The current response-generation configuration supports two environments:

**Deployed configuration:**

**Google Gen AI → Gemini 2.5 Flash**

**Local development fallback:**

**Ollama → Llama 3.2 3B**

The application checks for `GEMINI_API_KEY`. When the key is available, the application uses Gemini 2.5 Flash. When the key is not available, the application falls back to the local Ollama runtime and Llama 3.2 3B.

### Technology Roles

| Technology            | Role                                                         |
| --------------------- | ------------------------------------------------------------ |
| Python                | Programming language                                         |
| Streamlit             | Application and user interface                               |
| Sentence Transformers | Embedding framework                                          |
| `all-MiniLM-L6-v2`    | Embedding model                                              |
| ChromaDB              | Vector database                                              |
| Google Gen AI         | Cloud model integration                                      |
| Gemini 2.5 Flash      | Primary response-generation model for deployed configuration |
| Ollama                | Local model runtime                                          |
| Llama 3.2 3B          | Local response-generation fallback                           |

The Project Manager does not need to become an AI engineer but must understand what each major component does and what dependencies and risks it introduces.

---

## 9. Project Deliverables

The capstone produces the following project artifacts:

1. Project Overview
2. Project Charter
3. Requirements Specification
4. Product Backlog and Release Plan
5. AI Architecture and Technology Assessment
6. Data Readiness and Knowledge Governance Assessment
7. AI Evaluation and Quality Plan
8. AI Risk, Security and Governance Plan
9. Testing, UAT and Pilot Plan
10. Release and Deployment Plan
11. Monitoring and Continuous Improvement Plan
12. Decision Log
13. Risk Register
14. Requirements Traceability
15. Executive Project Summary
16. Final Go, Hold, or No-Go Recommendation
17. Final Presentation

---

## 10. Project Manager Responsibilities

The Project Manager is responsible for:

* Business alignment.
* Requirements.
* Scope.
* Stakeholder management.
* Product planning.
* Risk management.
* Data governance coordination.
* Evaluation planning.
* Security and governance coordination.
* Testing and UAT.
* Release readiness.
* Monitoring.
* Decision management.
* Executive communication.

---

## 11. Production Readiness

A working prototype does not automatically qualify for production release.

Production readiness requires evidence covering:

* Requirements.
* Data readiness.
* Evaluation.
* Security.
* Governance.
* Testing.
* UAT.
* Performance.
* Monitoring.
* Rollback.
* Risk.
* Defect status.
* Stakeholder approval.

The current project position is:

**HOLD**

The prototype works, but additional production-readiness evidence is required before a production Go decision.

---

## 12. Project Management Principle

The purpose of the capstone is not simply to demonstrate that an application can generate responses.

The purpose is to demonstrate that a Project Manager can determine:

* What should be built.
* Why it should be built.
* How requirements should be defined.
* How success should be measured.
* What risks must be controlled.
* What evidence is required.
* When the project is ready to proceed.

---

## 13. Portfolio Relationship

The Capstone contains the detailed project documentation.

The Portfolio presents the strongest evidence from the Capstone in a professional format.

The Course Modules provide the concepts, frameworks, and templates used to complete the project.

The relationship is:

**Course Learning → Capstone Application → Project Evidence → Professional Portfolio**

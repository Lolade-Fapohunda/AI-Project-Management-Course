# Petadel PolicyAssist AI

## Capstone Project

**Organization:** Petadel Technology Services (PTS)
**Project:** Petadel PolicyAssist AI
**Project Type:** Generative AI Policy Assistant
**Course:** AI Project Management Course

---

# 1. Project Overview

Petadel PolicyAssist AI is a Generative AI solution designed to help employees quickly locate and understand company policies.

The solution uses approved policy documents as its knowledge source and retrieves relevant policy information to generate grounded responses.

The project demonstrates how an AI Project Manager manages an AI product from initiation through production monitoring and continuous improvement.

---

# 2. Business Problem

Employees currently spend significant time searching through policy documents to locate relevant information.

Challenges include:

* Large numbers of policy documents.
* Difficult document search.
* Outdated or superseded documents.
* Duplicate policy information.
* Conflicting versions.
* Unclear policy authority.
* Scanned or difficult-to-search documents.
* Difficulty determining which policy applies.
* Risk of employees receiving incorrect or outdated information.

---

# 3. Business Objective

The objective of PolicyAssist is to:

* Reduce employee policy search time.
* Improve access to relevant policy information.
* Use authoritative and active policy sources.
* Provide grounded responses.
* Provide accurate source citations.
* Prevent unsupported policy guidance.
* Support appropriate access controls.
* Establish measurable AI quality.
* Provide monitoring and continuous improvement after release.

---

# 4. Initial Success Targets

The project establishes the following initial targets:

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Policy search-time reduction |        ≥ 50% |
| Retrieval accuracy           |        ≥ 90% |
| Answer accuracy              |        ≥ 90% |
| Hallucination rate           |         < 2% |
| Citation correctness         |         100% |
| Unsupported-question refusal |         100% |
| Response latency             | ≤ 10 seconds |
| User satisfaction            |        ≥ 85% |
| Critical security incidents  |            0 |

These are project targets and must be validated through appropriate evaluation, testing, UAT, and production evidence.

---

# 5. Core Governance Rule

PolicyAssist may use a policy as authoritative evidence only when the policy is:

**Active + Authoritative + Approved + Required Metadata Present = Eligible**

The system must not automatically rely on:

* Draft policies.
* Superseded policies.
* Unverified policies.
* Policies with missing required metadata.
* Policies with unresolved authority conflicts.

If authority cannot be established, the issue must be escalated for human resolution.

---

# 6. AI Response Principle

PolicyAssist must ground responses in retrieved policy evidence.

The AI model is not considered an independent source of company policy.

When sufficient evidence exists:

**Retrieve → Ground → Answer → Cite**

When sufficient authoritative evidence does not exist:

**Do Not Invent → Refuse or Escalate**

For mixed questions, supported and unsupported portions must be evaluated independently.

---

# 7. Product Lifecycle

The capstone follows the complete AI project lifecycle:

**Initiation → Discovery → Requirements → Planning → Architecture → Build → Evaluation → Security/Governance → UAT → Release → Monitoring → Continuous Improvement**

The Project Manager is responsible for maintaining alignment between these phases.

---

# 8. Product Backlog

The PolicyAssist backlog contains:

* **10 Epics**
* **58 User Stories**
* **3 Releases**

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

### Releases

**Release 1 — Foundation**

Establish the secure and governed policy knowledge foundation.

**Release 2 — MVP Product**

Deliver the core employee policy-assistance experience.

**Release 3 — Production Readiness**

Validate quality, security, governance, UAT, monitoring, reliability, and release readiness.

---

# 9. Technical Architecture

The conceptual architecture is:

**Policy Documents → Chunking → Embeddings → Vector Database → Retrieval → Large Language Model → Grounding/Citation → User Interface**

### Technology Roles

| Technology            | Role                                     |
| --------------------- | ---------------------------------------- |
| Python                | Programming language                     |
| Streamlit             | Application and user-interface framework |
| Sentence Transformers | Embedding framework/library              |
| all-MiniLM-L6-v2      | Embedding model                          |
| ChromaDB              | Vector database                          |
| Ollama                | Local AI runtime                         |
| Llama 3.2 3B          | Large Language Model (LLM)               |

The Project Manager does not need to become an AI engineer but must understand what each component does, why it exists, and what risks or dependencies it introduces.

---

# 10. Project Deliverables

The capstone produces the following project artifacts:

1. Project Overview
2. Project Charter
3. Requirements Specification
4. Product Backlog & Release Plan
5. AI Architecture & Technology Assessment
6. Data Readiness & Knowledge Governance Assessment
7. AI Evaluation & Quality Plan
8. AI Risk, Security & Governance Plan
9. Testing, UAT & Pilot Plan
10. Release & Deployment Plan
11. Monitoring & Continuous Improvement Plan
12. Decision Log
13. Risk Register
14. Requirements Traceability
15. Executive Project Summary
16. Final Go/Hold/No-Go Recommendation
17. Final Presentation

---

# 11. Project Manager Responsibilities

The AI Project Manager is responsible for:

* Defining and protecting the business objective.
* Managing stakeholders.
* Translating business needs into requirements.
* Managing scope and priorities.
* Coordinating technical teams.
* Challenging unsupported technical claims.
* Managing AI-specific risks.
* Ensuring data readiness.
* Establishing evaluation criteria.
* Coordinating testing and UAT.
* Managing release readiness.
* Maintaining traceability.
* Managing decisions and risks.
* Monitoring production performance.
* Driving continuous improvement.

The Project Manager does not need to build every technical component personally.

The PM's responsibility is to ensure the product is **valuable, controlled, measurable, secure, usable, and ready for release.**

---

# 12. Definition Of Success

PolicyAssist is successful only when the project demonstrates more than a functioning AI application.

Success requires evidence that:

* The business problem is addressed.
* Requirements are satisfied.
* Policy data is ready.
* Authoritative sources are controlled.
* AI responses are grounded.
* Citations are accurate.
* Unsupported questions are handled appropriately.
* Security requirements are satisfied.
* Evaluation targets are measured.
* Testing is complete.
* UAT is successful.
* Critical and high-severity issues are appropriately addressed.
* Monitoring is ready.
* Rollback is available.
* Stakeholders support the release decision.

---

# 13. Capstone Decision Framework

The final release decision uses three possible outcomes:

### GO

The solution satisfies required release criteria and can proceed to production.

### PROCEED WITH CONDITIONS

The solution may proceed only when clearly defined conditions, controls, or follow-up actions are established and approved.

### HOLD / NO-GO

The solution must not proceed because required evidence, controls, quality, security, governance, or business acceptance is insufficient.

The Project Manager must base the decision on evidence rather than schedule pressure or technical optimism.

---

# 14. Portfolio Purpose

The completed PolicyAssist project forms the practical portfolio component of the AI Project Management Course.

The portfolio demonstrates the ability to manage an AI project across:

**Business → People → Requirements → Technology → Data → AI Quality → Risk → Testing → Release → Operations**

The goal is to demonstrate **AI Project Management capability**, not simply software development capability.

---

# 15. Capstone Navigation

The numbered documents contain the detailed project artifacts:

* `01-PROJECT-OVERVIEW.md`
* `02-PROJECT-CHARTER.md`
* `03-REQUIREMENTS.md`
* `04-PRODUCT-BACKLOG.md`
* `05-ARCHITECTURE.md`
* `06-DATA-GOVERNANCE.md`
* `07-EVALUATION-PLAN.md`
* `08-RISK-SECURITY-GOVERNANCE.md`
* `09-TEST-UAT-PILOT.md`
* `10-RELEASE-DEPLOYMENT.md`
* `11-MONITORING-CONTINUOUS-IMPROVEMENT.md`
* `12-DECISION-LOG.md`
* `13-RISK-REGISTER.md`
* `14-TRACEABILITY.md`
* `15-EXECUTIVE-SUMMARY.md`
* `16-FINAL-GO-HOLD-NO-GO.md`

This README provides the overall context; the numbered documents provide the detailed project evidence.

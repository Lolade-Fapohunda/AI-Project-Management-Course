# Module 12: Capstone & Portfolio

## Purpose

The capstone brings together the AI Project Management skills developed throughout the course.

You will manage an AI product from project initiation through evaluation, governance, release planning, and continuous improvement.

The course uses **Petadel PolicyAssist AI** as the reference capstone project.

You may use the Petadel PolicyAssist AI reference project or apply the same Project Management framework to your own AI product or use case.

The project simulates a real enterprise AI initiative in which an organization needs a reliable way to locate, understand, and use approved internal policies.

The objective is not to demonstrate that you can build an AI system by yourself.

The objective is to demonstrate that you can **manage an AI project successfully**.

You will use the knowledge, decisions, artifacts, and frameworks developed throughout the course to create a complete AI project portfolio.

---

## Learning Objectives

By the end of this module, you will be able to:

* Apply the AI Project Management lifecycle end-to-end.
* Define an AI business problem and desired outcomes.
* Identify and manage stakeholders.
* Develop business and functional requirements.
* Prioritize an AI product backlog.
* Evaluate AI technology and architecture decisions.
* Assess data readiness and knowledge governance.
* Define AI evaluation criteria and quality thresholds.
* Manage AI risk, security, and governance.
* Plan testing, UAT, and pilot activities.
* Develop release and deployment plans.
* Establish monitoring and continuous improvement processes.
* Make evidence-based Go, Hold, or No-Go decisions.
* Build a professional AI Project Management portfolio.
* Explain project decisions to technical and non-technical stakeholders.

---

## Capstone Reference Project: Petadel PolicyAssist AI

### Organization

**Petadel Technology Services (PTS)**

### Project

**Petadel PolicyAssist AI**

### Business Problem

Employees currently experience difficulty locating and understanding internal company policies.

Policy information may be distributed across multiple documents and sources.

This creates problems such as:

* Long search times
* Difficulty identifying the correct policy
* Outdated information
* Conflicting versions
* Unclear policy ownership
* Inconsistent interpretation
* Increased reliance on manual assistance

PTS wants to explore an AI-powered solution that can help employees find and understand approved policy information.

If you are using your own AI product or use case for the capstone, replace the Petadel-specific project information with the corresponding information for your project while following the same Project Management framework.

---

## Business Objective

The objective of PolicyAssist AI is to provide employees with a reliable way to locate and understand approved internal policies while maintaining appropriate security, governance, and access controls.

The project must prioritize:

* Accuracy
* Grounding
* Authority
* Security
* Usability
* Traceability
* Governance

For your own AI product or use case, define equivalent business objectives and priorities appropriate to your project.

---

## Initial Success Targets

The Petadel reference project establishes the following target measures:

| Measure                      |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |
| User Satisfaction            |        ≥ 85% |
| Critical Security Incidents  |            0 |

These are project targets.

They must be validated through evidence rather than assumed to have been achieved.

If you are using your own AI product or use case, establish measurable targets appropriate to your project.

---

## Capstone Lifecycle

You will manage the project through the following lifecycle:

**Initiation**

↓

**Discovery**

↓

**Requirements**

↓

**Planning**

↓

**Architecture**

↓

**Build**

↓

**Evaluation**

↓

**Security & Governance**

↓

**UAT**

↓

**Pilot**

↓

**Release**

↓

**Monitoring**

↓

**Continuous Improvement**

Each stage should produce evidence and decisions that support the next stage.

---

## Capstone Rule

The capstone should demonstrate **decision-making**, not simply document creation.

For every major project decision, consider:

1. **What is the evidence?**
2. **What is the business impact?**
3. **What is the risk?**
4. **Who are the stakeholders?**
5. **What alternatives exist?**
6. **What decision should be made?**
7. **What action follows?**

---

# Capstone Phase 1: Initiation

## Objective

Establish why the project exists and whether it should proceed.

### Activities

Define:

* Business problem
* Business need
* Desired outcomes
* Initial scope
* Major stakeholders
* Initial risks
* AI opportunity
* Project assumptions
* Constraints

### PM Decision

Determine:

> **Should the organization investigate an AI solution for this problem?**

Do not assume AI is automatically the correct solution.

---

## Artifact

Create a **Project Charter** containing:

* Project name
* Business problem
* Business objective
* Project goals
* Scope
* Out-of-scope items
* Stakeholders
* Assumptions
* Constraints
* Initial risks
* Success measures
* PM decision

---

# Capstone Phase 2: Discovery & Stakeholders

## Objective

Understand the current state and determine what stakeholders actually need.

### Activities

Analyze:

* Current process
* Existing pain points
* Root causes
* Stakeholder groups
* Stakeholder objectives
* Conflicting priorities
* Desired business outcomes

For the Petadel reference project, consider:

* Employees
* Managers
* Human Resources
* Finance
* Information Security
* Legal/Compliance
* Policy Owners
* IT
* Executive Leadership

For your own project, identify the stakeholder groups relevant to your product or use case.

### PM Decision

Determine:

> **What problem should the AI product actually solve?**

---

## Artifact

Create a **Stakeholder & Discovery Plan** containing:

* Current-state analysis
* Problem statement
* Root-cause analysis
* Stakeholder register
* Stakeholder analysis
* Discovery questions
* Business outcomes
* AI suitability assessment

---

# Capstone Phase 3: Requirements

## Objective

Translate the business problem into measurable product requirements.

### Activities

Define:

* Business requirements
* Functional requirements
* Non-functional requirements
* AI-specific requirements
* User stories
* Acceptance criteria
* Traceability
* Priorities

### Example Requirement

> The system must provide answers supported by approved policy evidence.

### Example Acceptance Criterion

> Given a policy-related question, the system must retrieve and use only an authoritative and active version of the applicable policy.

For your own project, create requirements and acceptance criteria appropriate to your product or use case.

---

## Artifact

Create a **Requirements Specification** containing:

* Business requirements
* Functional requirements
* Non-functional requirements
* AI requirements
* User stories
* Acceptance criteria
* Prioritization
* Requirements traceability matrix

---

# Capstone Phase 4: Agile Product Planning

## Objective

Translate requirements into an executable product backlog and release plan.

### Activities

Define:

* Epics
* User stories
* Acceptance criteria
* Dependencies
* Priorities
* MVP scope
* Releases
* Definition of Ready
* Definition of Done

---

## Petadel PolicyAssist Product Backlog

For the Petadel reference project, the capstone uses the following backlog structure:

### EP-01: Security & Access

### EP-02: Policy Knowledge Base/Ingestion

### EP-03: Policy Retrieval

### EP-04: AI Response/Grounding

### EP-05: User Experience

### EP-06: Performance & Reliability

### EP-07: Human Escalation & Feedback

### EP-08: Administration/Governance

### EP-09: Evaluation/Testing

### EP-10: Monitoring/Continuous Improvement

The Petadel reference backlog contains **58 user stories** distributed across these ten epics.

If you are using your own project, create a backlog structure appropriate to your product and apply the same prioritization and release-planning principles.

---

## Releases

For the Petadel reference project, the backlog is organized into:

### Release 1: Foundation

Establish the core technical and governance foundation.

### Release 2: MVP Product

Deliver the core employee-facing PolicyAssist experience.

### Release 3: Production Readiness

Complete evaluation, security, UAT, monitoring, governance, and operational readiness.

For your own project, define releases appropriate to the scope, risk, and business objectives.

---

## Artifact

Create a **Product Backlog & Release Plan** containing:

* Epics
* User stories
* Priorities
* Dependencies
* MVP scope
* Release structure
* Acceptance criteria
* Definition of Ready
* Definition of Done

---

# Capstone Phase 5: AI Technology & Architecture

## Objective

Evaluate the technical architecture from an AI Project Manager perspective.

### Petadel PolicyAssist Architecture

The Petadel reference architecture is:

**Documents**

↓

**Chunking**

↓

**Embedding Model**

↓

**Vector Database**

↓

**Retrieval**

↓

**Large Language Model**

↓

**Grounding / Citation**

↓

**Streamlit Application**

For your own project, document and evaluate the architecture relevant to your product or use case.

---

## Technology Roles

For the Petadel reference project:

| Technology                | Role                                     |
| ------------------------- | ---------------------------------------- |
| **Python**                | Programming language                     |
| **Streamlit**             | Application and user-interface framework |
| **Sentence Transformers** | Embedding framework/library              |
| **all-MiniLM-L6-v2**      | Embedding model                          |
| **ChromaDB**              | Vector database                          |
| **Ollama**                | Local AI runtime                         |
| **Llama 3.2 3B**          | Large language model                     |

The PM should be able to explain what each component does and identify its project dependencies and risks.

For your own project, document the technologies, roles, dependencies, and risks relevant to your solution.

---

## PM Responsibilities

Evaluate:

* Architecture dependencies
* Model selection
* Data flow
* Retrieval design
* Grounding
* Performance
* Scalability considerations
* Security considerations
* Operational dependencies
* Technical risks

The PM does not need to engineer the architecture.

The PM must be able to challenge technical assumptions and understand their project impact.

---

## Artifact

Create an **AI Architecture & Technology Assessment** containing:

* Architecture diagram
* Technology roles
* Technical dependencies
* Technology risks
* Key assumptions
* Performance considerations
* Security considerations
* PM recommendations

---

# Capstone Phase 6: Data & Knowledge Management

## Objective

Determine whether the policy information is trustworthy and ready for AI use.

For your own project, apply the same data-readiness and knowledge-governance principles to the information used by your AI solution.

### Core Governance Rule

> **PolicyAssist may retrieve and use only the authoritative, active version of a policy.**

If authority cannot be established, the system must not automatically choose between conflicting versions.

The issue must be flagged for human resolution.

For your own project, establish an equivalent source-authority and conflict-handling rule appropriate to your data.

---

## Data Readiness Rule

For the Petadel reference project, information is eligible for retrieval only when:

**Active + Authoritative + Approved + Required Metadata Present**

Information that is:

* Superseded
* Draft
* Unverified
* Conflicting

is not eligible for retrieval.

---

## Required Metadata

For the Petadel reference project, policy information should include appropriate metadata such as:

* Policy ID
* Policy name
* Owner
* Effective date
* Version
* Status
* Applicability
* Document type
* Approval information

For your own project, define the metadata required to establish authority, quality, status, and appropriate use.

---

## Artifact

Create a **Data Readiness & Knowledge Governance Assessment** containing:

* Data inventory
* Data owners
* Authority rules
* Versioning rules
* Metadata requirements
* Data-quality criteria
* Conflict-handling process
* Access requirements
* Ingestion requirements
* Data risks
* Readiness decision

---

## PM Decision

Determine whether the project knowledge base or data sources are:

* **Ready**
* **Ready With Conditions**
* **Hold**

Support the decision with evidence.

---

# Capstone Phase 7: AI Evaluation & Quality

## Objective

Determine whether the AI solution produces acceptable AI behavior.

### Evaluation Categories

For the Petadel reference project, the evaluation dataset should include:

* Happy-path questions
* Paraphrased questions
* Unsupported questions
* False-premise questions
* Multi-part questions
* Multi-policy questions
* Edge cases
* Citation cases
* Performance cases
* Security-sensitive cases

For your own project, define evaluation categories appropriate to your AI system.

---

## Evaluation Targets

For the Petadel reference project:

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |

For your own project, define measurable evaluation targets appropriate to your use case.

---

## Citation Rule

PolicyAssist should display a source citation only when the retrieved evidence substantively supports the answer.

If sufficient evidence cannot be established:

* Do not invent an answer.
* Do not present an unrelated document as supporting evidence.
* Refuse or appropriately escalate.

For your own project, define equivalent evidence and response-grounding rules where applicable.

---

## Artifact

Create an **AI Evaluation & Quality Report** containing:

* Evaluation dataset
* Evaluation categories
* Metrics
* Thresholds
* Results
* Failed cases
* Defect severity
* Root-cause analysis
* Corrective actions
* Retesting results
* Quality decision

---

## PM Decision

Determine whether the AI quality results support:

* **Go**
* **Proceed With Conditions**
* **Hold**
* **No-Go**

---

# Capstone Phase 8: Risk, Security & Governance

## Objective

Determine whether the AI solution can operate within acceptable organizational risk.

### Risk Areas

Evaluate:

* Unauthorized access
* Sensitive information
* Data leakage
* Prompt injection
* Incorrect AI responses
* Hallucination
* Model misuse
* Third-party dependencies
* Privacy
* Compliance
* Operational failure

---

## Governance Requirements

Define:

* Product ownership
* Data ownership
* Security ownership
* Risk ownership
* Approval authority
* Release authority
* Incident ownership
* Human escalation

---

## Artifact

Create an **AI Risk, Security & Governance Plan** containing:

* Risk register
* Risk scoring
* Controls
* Residual risk
* Access requirements
* Security requirements
* Governance roles
* RACI
* Human oversight
* Incident process
* Risk acceptance
* Governance gates

---

## PM Decision

Determine whether remaining risks are:

* Acceptable
* Mitigated
* Require formal acceptance
* Release-blocking

---

# Capstone Phase 9: Testing, UAT & Pilot

## Objective

Determine whether the AI solution is ready for real users.

### UAT Scenarios

For the Petadel reference project, create realistic UAT scenarios covering:

* Remote work
* Attendance
* Expense reimbursement
* Information security
* Code of conduct
* Unsupported questions
* False premises
* Multi-policy questions
* Superseded/draft policies
* Conflicting authority

For your own project, create UAT scenarios that reflect real user tasks and risks.

---

## UAT Acceptance

UAT should determine whether users can:

* Find relevant information.
* Understand the response.
* Verify supporting evidence.
* Recognize limitations.
* Escalate when necessary.
* Complete intended business tasks.

---

## Pilot

Define:

* Pilot population
* Duration
* Objectives
* Success criteria
* Monitoring
* Support
* Feedback
* Escalation
* Exit criteria

---

## Artifact

Create a **Testing, UAT & Pilot Plan** containing:

* Test strategy
* Test cases
* Defect log
* UAT scenarios
* UAT acceptance criteria
* Pilot plan
* Pilot success criteria
* Feedback process
* Exit criteria
* Go/Hold/No-Go criteria

---

## PM Decision

Determine whether the AI solution is ready to proceed from validation into broader deployment.

---

# Capstone Phase 10: Release & Deployment

## Objective

Determine whether the product and organization are ready for production.

### Release Readiness

Confirm:

* Evaluation complete
* UAT complete
* Security approved
* Data ready
*

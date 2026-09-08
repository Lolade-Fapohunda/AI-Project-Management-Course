# Portfolio: Petadel PolicyAssist AI

## Portfolio Purpose

This portfolio presents the completed project-management work for **Petadel PolicyAssist AI**, an AI-powered internal policy knowledge assistant developed as the capstone project for the AI Project Management Course.

The portfolio demonstrates the ability to manage an AI project from business problem identification through requirements, planning, architecture, data governance, evaluation, risk management, testing, release readiness, and continuous improvement.

The portfolio is designed as a **professional evidence package**, not a duplicate copy of the detailed capstone documentation.

---

## Project

**Project:** Petadel PolicyAssist AI

**Organization:** Petadel Technology Services (PTS)

**Project Type:** Internal Generative AI Knowledge Assistant

**Project Management Focus:** AI Project Management

**Primary Business Problem:**

Employees may have difficulty locating, identifying, and interpreting the correct internal policy information because organizational policies can exist across multiple documents, versions, repositories, and formats.

This creates:

* Increased policy-search time.
* Inconsistent interpretation.
* Risk of using outdated information.
* Risk of conflicting information.
* Difficulty identifying authoritative policies.
* Security and access-control concerns.
* Increased dependency on human assistance.

---

## Business Objective

The objective of PolicyAssist AI is to provide employees with a faster and more reliable way to locate approved internal policy information while ensuring that responses are grounded in authoritative sources.

The system is designed to:

* Retrieve relevant policy information.
* Use only eligible policy sources.
* Identify authoritative and active policy versions.
* Provide grounded responses.
* Display appropriate citations.
* Refuse unsupported questions rather than invent information.
* Respect access restrictions.
* Escalate unresolved authority or policy issues when necessary.

---

## Initial Success Targets

The project established measurable quality targets:

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

These targets require documented evaluation evidence before production acceptance.

---

## Portfolio Evidence

The portfolio demonstrates competency across the complete AI project lifecycle.

### 1. Business & Project Initiation

Evidence demonstrates the ability to:

* Define the business problem.
* Establish business objectives.
* Identify project scope.
* Define stakeholders.
* Establish assumptions and constraints.
* Define success criteria.
* Establish project governance.

**Primary Evidence:**

`01-Project-Case-Study.md`

---

### 2. Requirements & Scope

Evidence demonstrates the ability to:

* Define business requirements.
* Define functional requirements.
* Define non-functional requirements.
* Define AI-specific requirements.
* Define security requirements.
* Define data requirements.
* Define evaluation requirements.
* Establish acceptance criteria.
* Prioritize requirements.
* Maintain traceability.

**Primary Evidence:**

`02-Requirements-Evidence.md`

---

### 3. Agile Product Planning

Evidence demonstrates the ability to:

* Define epics.
* Develop user stories.
* Establish acceptance criteria.
* Prioritize work.
* Define the Minimum Viable Product (MVP).
* Manage dependencies.
* Establish release boundaries.
* Control scope.

The project backlog contains:

**10 Epics**

**58 User Stories**

**3 Releases**

**Primary Evidence:**

`03-Product-Planning-Evidence.md`

---

### 4. Architecture & Technology

Evidence demonstrates the ability to understand and manage an AI technology architecture without requiring the Project Manager to become an AI engineer.

The PolicyAssist architecture includes:

**Policy Documents**

↓

**Document Processing**

↓

**Chunking**

↓

**Embeddings**

↓

**ChromaDB**

↓

**Semantic Retrieval**

↓

**Gemini 2.5 Flash**

↓

**Grounded Response**

↓

**Citation**

↓

**Streamlit Application**

The application also supports Ollama with Llama 3.2 3B as a local development fallback.

Key technologies include:

* Python
* Streamlit
* Sentence Transformers
* `all-MiniLM-L6-v2`
* ChromaDB
* Google Gen AI
* Gemini 2.5 Flash
* Ollama
* Llama 3.2 3B

The Project Manager does not need to become an AI engineer but must understand the role, dependency, and risk associated with each major component.

**Primary Evidence:**

`04-AI-Architecture-Decision.md`

---

### 5. Data & Knowledge Governance

The project establishes a formal policy-data governance model.

The governing eligibility rule is:

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

The project also establishes that:

* Draft policies are not automatically eligible.
* Superseded policies are not automatically eligible.
* Unverified policies are not automatically eligible.
* Conflicting policies are not automatically selected.
* Policy ownership must be established.
* Version information must be maintained.
* Effective dates must be validated.
* Required metadata must be present.
* Access restrictions must be enforced.
* Material policy changes must be documented.

If authority cannot be established, the information is held for human resolution.

**Primary Evidence:**

`05-Data-Governance-Decision.md`

---

### 6. AI Evaluation & Quality

The project separates technical testing from AI evaluation.

Evaluation covers:

* Retrieval accuracy.
* Answer accuracy.
* Grounding.
* Hallucination.
* Citation correctness.
* Unsupported questions.
* False-premise questions.
* Paraphrased questions.
* Mixed questions.
* Multi-policy questions.
* Authority and version scenarios.
* Performance.

A minimum structured evaluation dataset of **30 cases** was established.

The project does not consider the system successful merely because the application produces responses.

Acceptance requires measurable evidence.

**Primary Evidence:**

`06-AI-Evaluation-Results.md`

---

### 7. Risk, Security & Governance

The project treats security and governance as release considerations.

Key risks include:

* Unauthorized policy access.
* Data leakage.
* Incorrect policy responses.
* Hallucination.
* Incorrect citations.
* Unsupported answers.
* Prompt injection.
* Policy authority conflicts.
* Outdated information.
* Vendor risk.
* Inadequate human oversight.

Critical security failures are release blockers.

**Primary Evidence:**

`07-Risk-Security-Decision.md`

---

### 8. Testing, UAT & Pilot

The project establishes separate processes for:

* Functional testing.
* Negative testing.
* Edge-case testing.
* Security validation.
* Regression testing.
* AI evaluation.
* User Acceptance Testing (UAT).
* Pilot testing.

The UAT framework includes scenarios covering:

* Remote work.
* Attendance.
* Expense reimbursement.
* Information security.
* Code of conduct.
* Unsupported questions.
* False premises.
* Multi-policy questions.
* Superseded or draft policies.
* Conflicting authority.

**Primary Evidence:**

`08-Testing-UAT-Evidence.md`

---

### 9. Release & Deployment

The project establishes formal release readiness criteria.

Release decisions consider:

* Requirements completion.
* MVP readiness.
* Data readiness.
* AI quality.
* Security.
* Governance.
* Testing.
* UAT.
* Performance.
* Monitoring.
* Rollback capability.
* Risk.
* Defect status.
* Evidence.

The deployment strategy uses a controlled pilot followed by phased expansion.

Rollback is treated as a required production capability.

**Primary Evidence:**

`09-Release-Readiness-Decision.md`

---

### 10. Monitoring & Continuous Improvement

The project establishes an ongoing production-management process.

The improvement lifecycle is:

**Monitor**

↓

**Identify Problem**

↓

**Create Backlog Item**

↓

**Prioritize**

↓

**Develop**

↓

**Test**

↓

**Evaluate**

↓

**UAT**

↓

**Release**

↓

**Monitor**

Monitoring includes:

* Retrieval performance.
* Answer accuracy.
* Hallucination.
* Citation correctness.
* Response latency.
* User satisfaction.
* Security incidents.
* Knowledge changes.
* Data changes.
* Model changes.
* User feedback.
* Business outcomes.

**Primary Evidence:**

`10-Monitoring-Strategy.md`

---

## Decision Management

The project maintains formal decision management rather than relying on undocumented assumptions.

Important project decisions include:

* Use of Retrieval-Augmented Generation (RAG).
* Authoritative active policy requirement.
* No automatic resolution of conflicting authority.
* Application-controlled citations.
* Unsupported-question refusal.
* Independent evaluation of mixed questions.
* Measurable quality thresholds.
* Minimum evaluation dataset.
* Response-time requirement.
* Controlled pilot.
* Rollback capability.
* Human escalation.
* Security as a release gate.
* UAT as a separate quality gate.
* Evidence as an acceptance requirement.

Detailed decision records remain part of the Capstone documentation.

**Primary Evidence:**

`11-Final-PM-Decision.md`

---

## Risk Management

The project maintains a formal risk management process covering:

* Data risks.
* AI quality risks.
* Security risks.
* Governance risks.
* Operational risks.
* Release risks.
* Vendor risks.
* User adoption risks.

Risk management includes:

* Likelihood.
* Impact.
* Risk score.
* Response strategy.
* Risk ownership.
* Status.
* Controls.
* Escalation.
* Residual risk.
* Release implications.

Detailed risk records remain part of the Capstone documentation.

**Primary Evidence:**

`07-Risk-Security-Decision.md`

---

## Requirements Traceability

The project maintains traceability between requirements, backlog items, acceptance criteria, testing, evaluation, and release decisions.

The objective is to demonstrate:

> **Requirement → Implementation → Acceptance Criteria → Test/Evaluation Evidence → Release Decision**

This provides evidence that project decisions are connected to defined business and product requirements.

**Primary Evidence:**

`02-Requirements-Evidence.md`

---

## Final Release Decision

The current project position is:

# HOLD

The prototype demonstration has been completed successfully.

However, production release requires additional evidence and validation, including:

* Formal evaluation.
* UAT completion.
* Pilot validation.
* Production security validation.
* Monitoring readiness.
* Rollback validation.
* Governance approval.
* Final evidence review.

The HOLD decision demonstrates an important AI Project Management principle:

> **A working prototype is not automatically a production-ready AI product.**

The project should proceed toward release only after the remaining mandatory gates have been satisfied.

**Primary Evidence:**

`11-Final-PM-Decision.md`

---

## Portfolio Presentation

The portfolio should demonstrate the following professional capabilities:

### Business Judgment

Ability to determine whether an AI solution addresses a meaningful business problem.

### Requirements Management

Ability to convert business needs into measurable project requirements.

### Agile Planning

Ability to manage epics, user stories, acceptance criteria, prioritization, MVP scope, and releases.

### AI Technology Understanding

Ability to understand AI architecture, dependencies, limitations, and technical risks at the Project Manager level.

### Data Governance

Ability to determine whether information is fit for use.

### AI Evaluation

Ability to define measurable quality criteria and interpret evaluation evidence.

### Risk & Security

Ability to identify project risks and establish appropriate controls.

### Testing & UAT

Ability to distinguish technical testing, AI evaluation, and user acceptance.

### Release Management

Ability to make evidence-based Go, Hold, or No-Go decisions.

### Monitoring

Ability to manage the product after release and establish continuous improvement.

### Executive Communication

Ability to communicate complex project information in a business-oriented manner.

---

## Professional Evidence Standard

Portfolio evidence should answer five questions:

1. **What was the problem?**
2. **What decision was made?**
3. **Why was the decision made?**
4. **What evidence supported the decision?**
5. **What was the resulting project action or outcome?**

The portfolio should prioritize demonstrated judgment over documentation volume.

---

## Relationship To Capstone Documentation

The detailed Capstone documentation remains the project's working source of truth.

The Portfolio serves as the professional presentation layer.

### Capstone

Contains detailed project-management documentation, requirements, decisions, registers, plans, and governance artifacts.

### Portfolio

Presents the strongest evidence demonstrating AI Project Management competency.

### Course Modules

Teach the concepts and methods used to create the project artifacts.

This creates the relationship:

**Course Learning**

↓

**Capstone Application**

↓

**Project Evidence**

↓

**Professional Portfolio**

---

## Portfolio Evidence Map

| Competency            | Primary Evidence           |
| --------------------- | -------------------------- |
| Project Initiation    | Project Case Study         |
| Business Requirements | Requirements Evidence      |
| Agile Planning        | Product Planning Evidence  |
| Architecture          | AI Architecture Decision   |
| Data Governance       | Data Governance Decision   |
| AI Evaluation         | AI Evaluation Results      |
| Risk & Security       | Risk & Security Decision   |
| Testing & UAT         | Testing & UAT Evidence     |
| Release Management    | Release Readiness Decision |
| Monitoring            | Monitoring Strategy        |
| Decision Management   | Final PM Decision          |
| Risk Management       | Risk & Security Decision   |
| Traceability          | Requirements Evidence      |
| Executive Judgment    | Final PM Decision          |

---

## Portfolio Quality Standard

Before the portfolio is considered complete, confirm that:

* [ ] All major project-management competencies are represented.
* [ ] Evidence is based on actual project work.
* [ ] Portfolio artifacts are consistent with the Capstone.
* [ ] Requirements match the backlog.
* [ ] Backlog items are traceable to requirements.
* [ ] Evaluation targets are consistent across artifacts.
* [ ] Data-governance rules are consistent.
* [ ] Security requirements are consistent.
* [ ] UAT criteria are consistent.
* [ ] Release criteria are consistent.
* [ ] Monitoring thresholds are consistent.
* [ ] Decision records support major project decisions.
* [ ] Risk records reflect the current project position.
* [ ] The final release decision is supported by evidence.
* [ ] No unsupported claims of production readiness are made.
* [ ] No unnecessary duplication exists between Portfolio and Capstone documentation.
* [ ] All Portfolio artifacts are presentation-ready.

---

## Final Portfolio Principle

The portfolio should demonstrate that the Project Manager can manage an AI project using **evidence, structured decision-making, measurable requirements, governance, and business judgment**.

The goal is not simply to demonstrate that the application works.

The goal is to demonstrate that the Project Manager knows:

> **What should be built, why it should be built, how success will be measured, what risks must be controlled, what evidence is required, and when the project is ready to proceed.**

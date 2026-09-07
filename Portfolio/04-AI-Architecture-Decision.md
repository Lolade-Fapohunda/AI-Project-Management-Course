# 04: AI Architecture Decision

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Architecture Pattern:** Retrieval-Augmented Generation (RAG)
**Decision Type:** Architecture & Technology Assessment

---

## Purpose

This artifact documents the architectural decisions made for PolicyAssist AI and demonstrates how the Project Manager evaluated technical choices against business requirements, AI quality, security, data governance, performance, and project constraints.

The objective was not to design the system as an engineer.

The objective was to ensure that the selected architecture could support the product requirements and that its risks were understood and managed.

---

# Business Requirement Driving The Architecture

PolicyAssist must allow employees to ask natural-language questions about internal policies and receive responses supported by approved policy information.

The architecture therefore must support:

* Policy ingestion.
* Semantic search.
* Policy authority validation.
* Relevant evidence retrieval.
* Grounded response generation.
* Citation.
* Unsupported-question refusal.
* Access controls.
* Performance within the defined target.
* Evaluation and monitoring.

---

# Architecture Overview

The selected architecture follows a Retrieval-Augmented Generation pattern.

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
Eligibility / Authority Validation
       ↓
Relevant Policy Evidence
       ↓
Large Language Model
       ↓
Grounded Response
       ↓
Application-Controlled Citation
       ↓
Streamlit User Interface
```

The architecture separates **knowledge retrieval** from **response generation**.

This is important because the model should not be treated as the authoritative source of company policy.

---

# Architecture Components

| Component              | Role                                                    |
| ---------------------- | ------------------------------------------------------- |
| Policy Documents       | Source knowledge                                        |
| Document Processing    | Extracts and prepares content                           |
| Chunking               | Divides documents into retrievable sections             |
| Embedding Model        | Converts text into numerical representations            |
| Vector Database        | Stores searchable representations                       |
| Retrieval Layer        | Finds potentially relevant evidence                     |
| Eligibility Validation | Determines whether retrieved policy content may be used |
| Large Language Model   | Generates the response                                  |
| Grounding Layer        | Constrains response to retrieved evidence               |
| Citation Layer         | Identifies supporting policy evidence                   |
| User Interface         | Allows employees to interact with the system            |

---

# Technology Assessment

The prototype uses a local technology stack.

| Technology                | Role                                     |
| ------------------------- | ---------------------------------------- |
| **Python**                | Programming language                     |
| **Streamlit**             | Application and user-interface framework |
| **Sentence Transformers** | Embedding framework/library              |
| **all-MiniLM-L6-v2**      | Embedding model                          |
| **ChromaDB**              | Vector database                          |
| **Ollama**                | Local AI runtime                         |
| **Llama 3.2 3B**          | Large Language Model                     |

The important PM consideration is understanding the role of each component rather than treating the technology stack as a list of interchangeable products.

---

# Why Retrieval-Augmented Generation

A general-purpose language model may contain broad knowledge, but PolicyAssist requires responses based on organizational policy documents.

RAG provides a controlled approach:

**Question**

↓

**Retrieve Relevant Policy Evidence**

↓

**Provide Evidence To Model**

↓

**Generate Response Based On Evidence**

This reduces reliance on the model's general knowledge for organization-specific policy questions.

---

# Architecture Decision

### Decision

Use a Retrieval-Augmented Generation architecture for the PolicyAssist MVP.

### Rationale

RAG supports the project's requirement to:

* Search internal policy content.
* Retrieve relevant evidence.
* Ground responses.
* Provide citations.
* Update knowledge without retraining the language model for every policy change.
* Separate organizational knowledge from general model knowledge.

---

# Authority Validation

Retrieval alone is not sufficient.

A document may be semantically relevant but still be:

* Draft.
* Superseded.
* Unverified.
* Unauthorized.
* Conflicting with another source.

PolicyAssist therefore applies an eligibility rule.

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

If authority cannot be established, the system should not automatically select one source over another.

---

# Retrieval Flow

The intended retrieval process is:

```text
User Question
     ↓
Semantic Search
     ↓
Candidate Policy Sections
     ↓
Eligibility Validation
     ↓
Relevant Eligible Evidence
     ↓
Response Generation
```

The separation between **retrieval** and **eligibility validation** is an important governance control.

---

# Retrieval Distance

The prototype uses a retrieval-distance threshold to reduce irrelevant results.

Current prototype threshold:

**MAX_DISTANCE = 1.20**

Retrieved content exceeding the configured threshold is not treated as sufficiently relevant evidence.

The threshold is an implementation parameter and must be validated through evaluation rather than assumed to be optimal.

---

# Grounding

The architecture requires the model to generate responses from retrieved evidence.

The model should not independently determine which policy documents are authoritative.

The application controls:

* Which documents are eligible.
* Which evidence is provided.
* Which citations are displayed.

This reduces the risk of the model inventing or selecting unsupported policy information.

---

# Citation Architecture

Citations are controlled by the application rather than generated freely by the language model.

The system should display a source only when the retrieved evidence substantively supports the answer.

### Required Behavior

**Evidence supports answer**

→ Answer + supporting citation

**Evidence does not support answer**

→ Refusal or limitation + no misleading citation

**Authority cannot be established**

→ Do not use conflicting source + escalate

This prevents a document from being presented as evidence merely because it was retrieved.

---

# Unsupported Questions

The architecture must support safe refusal.

Example:

> "How many vacation days do employees receive?"

If the approved knowledge base does not contain sufficient evidence, PolicyAssist should not invent a vacation policy.

The expected behavior is to explain that sufficient approved information is unavailable.

This is an architectural requirement because the application must distinguish between:

* Evidence available.
* Evidence unavailable.
* Evidence conflicting.
* Evidence unauthorized.

---

# False-Premise Handling

The system must also handle questions containing incorrect assumptions.

For example:

> "Why does PTS give fathers 20 weeks of paid leave?"

If the approved policy evidence does not establish that claim, the system should not accept the premise as fact.

The response should correct or decline the unsupported premise rather than fabricate supporting information.

---

# Mixed Questions

Some questions contain multiple independent requests.

Example:

> "How much parental leave do I receive, and how many vacation days do I receive?"

If parental leave information exists but vacation information does not, the system should not treat the entire question as supported.

The expected behavior is:

* Answer the supported portion.
* Identify the unsupported portion.
* Cite evidence for the supported portion.
* Avoid inventing the unsupported portion.

This requirement affects retrieval, prompting, response handling, and evaluation.

---

# Security Architecture Considerations

The architecture must recognize that retrieval relevance and authorization are different controls.

A document may be:

* Active.
* Authoritative.
* Approved.
* Relevant.

but still restricted to certain users.

Therefore:

> **Retrieval eligibility does not automatically mean user access eligibility.**

Authorization must be evaluated before restricted information is disclosed.

---

# Performance Requirement

PolicyAssist has a response-latency target of:

**≤ 10 seconds**

The measurement begins when the user submits the question and ends when the complete response is displayed.

The measurement includes:

* Request processing.
* Embedding.
* Retrieval.
* Eligibility validation.
* LLM generation.
* Grounding.
* Citation handling.
* Response display.

---

# MVP Performance Acceptance

For representative MVP testing:

* At least **95%** of representative policy questions should complete within **10 seconds**.
* **100%** should complete within **15 seconds**.
* At least **30 representative evaluation questions** should be measured.
* The dataset should include:

  * Direct questions.
  * Paraphrased questions.
  * Multi-policy questions.
  * Unsupported questions.
  * Refusal-required questions.

Any response exceeding the maximum threshold must be documented and analyzed.

---

# Production Performance

Production readiness requires stronger evidence.

The production-equivalent environment should demonstrate:

* At least 95% of representative requests within 10 seconds.
* No response exceeding the approved maximum threshold unless formally accepted.
* Realistic workload conditions.
* Performance monitoring.
* Performance failure analysis.
* Identified ownership for performance remediation.

---

# Architecture Dependencies

Key dependencies include:

| Dependency          | Architectural Impact                 |
| ------------------- | ------------------------------------ |
| Policy Documents    | Required for retrieval               |
| Metadata            | Required for eligibility             |
| Embedding Model     | Required for semantic search         |
| Vector Database     | Required for retrieval               |
| LLM Runtime         | Required for response generation     |
| Security Controls   | Required for authorized access       |
| Evaluation Dataset  | Required for architecture validation |
| Monitoring          | Required for production operation    |
| Rollback Capability | Required for controlled changes      |

---

# Architecture Risks

## Retrieval Risk

The system retrieves irrelevant evidence.

**Impact:** Incorrect or incomplete responses.

## Authority Risk

The system retrieves an outdated or conflicting policy.

**Impact:** Incorrect organizational guidance.

## Model Risk

The LLM adds unsupported information.

**Impact:** Hallucination and loss of trust.

## Citation Risk

The displayed source does not actually support the response.

**Impact:** False confidence.

## Security Risk

Restricted information is disclosed.

**Impact:** Potential privacy, security, compliance, and business risk.

## Performance Risk

The response exceeds the required latency.

**Impact:** Poor user experience and reduced adoption.

## Dependency Risk

A component change affects retrieval or response quality.

**Impact:** Regression and release instability.

---

# Architecture Decision Records

Major architecture decisions should be documented rather than existing only in technical discussions.

Each decision should include:

* Decision ID.
* Decision.
* Context.
* Options considered.
* Selected option.
* Rationale.
* Risks.
* Dependencies.
* Evidence.
* Approval.
* Review date.

---

# Key Architecture Decisions

| ID      | Decision                                                      |
| ------- | ------------------------------------------------------------- |
| ADR-001 | Use RAG for policy knowledge retrieval                        |
| ADR-002 | Use application-controlled policy eligibility                 |
| ADR-003 | Do not automatically resolve authority conflicts              |
| ADR-004 | Use application-controlled citations                          |
| ADR-005 | Require safe refusal when evidence is insufficient            |
| ADR-006 | Evaluate mixed questions independently                        |
| ADR-007 | Use measurable response-latency requirements                  |
| ADR-008 | Validate architecture through a structured evaluation dataset |

---

# Architecture Change Management

Architecture changes must be evaluated for downstream effects.

A change to one component may affect:

* Data ingestion.
* Retrieval.
* Prompting.
* AI quality.
* Security.
* Performance.
* Evaluation.
* UAT.
* Monitoring.
* Release readiness.

For example, changing the embedding model may require:

1. Re-indexing.
2. Retrieval testing.
3. Evaluation.
4. Regression testing.
5. Performance testing.
6. UAT where user behavior is affected.
7. Release approval.

---

# MVP Architecture Acceptance Gate

The architecture should not be considered ready merely because the application launches.

The architecture must demonstrate:

* [ ] Required policy data can be ingested.
* [ ] Eligible policy content can be identified.
* [ ] Semantic retrieval works.
* [ ] Irrelevant retrieval is controlled.
* [ ] Authority rules are enforced.
* [ ] Responses are grounded.
* [ ] Citations are substantively correct.
* [ ] Unsupported questions are handled safely.
* [ ] Mixed questions are handled correctly.
* [ ] Access controls are validated.
* [ ] Performance meets the MVP threshold.
* [ ] Architecture risks are documented.
* [ ] Evaluation evidence is available.

---

# Current Prototype Evidence

The PolicyAssist prototype has demonstrated the core architecture.

Demonstrated capabilities include:

* Multiple policy documents ingested.
* Policy metadata used for eligibility.
* Semantic retrieval functioning.
* Local embedding generation.
* Vector database retrieval.
* Local LLM response generation.
* Grounded response behavior.
* Citation handling.
* Unsupported-question refusal.
* False-premise handling.
* Mixed-question handling.
* Refresh/re-ingestion workflow.
* User interaction through Streamlit.
* Enter-to-submit functionality.

The prototype demonstrates technical feasibility.

It does **not** by itself establish production readiness.

---

# Architecture Evidence Status

| Area                        | Current Position |
| --------------------------- | ---------------- |
| Core Architecture           | Demonstrated     |
| Local AI Runtime            | Demonstrated     |
| Embeddings                  | Demonstrated     |
| Vector Retrieval            | Demonstrated     |
| Policy Eligibility          | Demonstrated     |
| Grounding                   | Demonstrated     |
| Citation Controls           | Demonstrated     |
| Unsupported Refusal         | Demonstrated     |
| Mixed Questions             | Demonstrated     |
| Formal Evaluation           | Pending          |
| Full Security Validation    | Pending          |
| UAT                         | Pending          |
| Pilot                       | Pending          |
| Production Monitoring       | Pending          |
| Rollback Validation         | Pending          |
| Final Architecture Approval | Pending          |

---

# PM Architecture Quality Check

Before approving an architecture, the Project Manager should be able to answer:

* Does the architecture support the business objective?
* Are technical components clearly understood?
* Are dependencies documented?
* Are AI-specific risks identified?
* Is authoritative knowledge separated from model knowledge?
* Are security controls considered?
* Is performance measurable?
* Can the architecture be evaluated?
* Can changes be regression-tested?
* Is there a rollback strategy?
* Is there sufficient evidence for the architecture decision?

---

# Portfolio Evidence

The architecture decision demonstrates that the Project Manager did not simply select technology because it was available.

The architecture was evaluated against:

* Business requirements.
* AI behavior.
* Data governance.
* Security.
* Performance.
* Evaluation.
* User experience.
* Change management.
* Production readiness.

The technical architecture therefore supports the broader project-management framework rather than operating independently from it.

---

# PM Judgment

The most important architecture decision was to prevent the language model from becoming the source of truth.

PolicyAssist uses the following principle:

> **The knowledge source establishes organizational truth; the AI model interprets and communicates that information.**

This distinction reduces the risk of treating model-generated knowledge as organizational policy.

---

# Current Architecture Decision

**Decision:** Proceed with the selected RAG architecture for continued MVP evaluation and validation.

**Production Decision:** Not yet approved.

The architecture has demonstrated technical feasibility, but production approval remains dependent on formal evaluation, security validation, UAT, pilot evidence, monitoring readiness, rollback validation, governance approval, and the final release decision.

---

# Final Evidence Principle

> **A working architecture is evidence of technical feasibility — not evidence of production readiness.**

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

The objective was to ensure that the selected architecture supports the product requirements and that its risks are understood and managed.

---

# Business Requirement Driving the Architecture

PolicyAssist must allow employees to ask natural-language questions about internal policies and receive responses supported by approved policy information.

The architecture therefore must support:

* Policy ingestion
* Semantic search
* Policy authority validation
* Relevant evidence retrieval
* Grounded response generation
* Citation
* Unsupported-question refusal
* Access controls
* Performance within the defined target
* Evaluation and monitoring

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
ChromaDB
       ↓
Semantic Retrieval
       ↓
Eligibility / Authority Validation
       ↓
Relevant Policy Evidence
       ↓
Response Generation
       ↓
Grounding
       ↓
Application-Controlled Citation
       ↓
Streamlit User Interface
```

The architecture separates knowledge retrieval from response generation.

The language model is not treated as the authoritative source of company policy.

---

# Technology Assessment

| Technology            | Role                           | Current Configuration  |
| --------------------- | ------------------------------ | ---------------------- |
| Python                | Application language           | Python                 |
| Streamlit             | Application and user interface | Streamlit              |
| Sentence Transformers | Embedding framework            | Sentence Transformers  |
| `all-MiniLM-L6-v2`    | Embedding model                | `all-MiniLM-L6-v2`     |
| ChromaDB              | Vector database                | ChromaDB               |
| Google Gen AI         | Cloud model integration        | Deployed configuration |
| Gemini 2.5 Flash      | Response generation            | Deployed configuration |
| Ollama                | Local model runtime            | Local fallback         |
| Llama 3.2 3B          | Response generation            | Local fallback         |

---

# Deployment and Local Development

The deployed application uses:

**Google Gen AI → Gemini 2.5 Flash**

When the Gemini API key is available, the application uses Gemini 2.5 Flash for response generation.

For local development and fallback operation, the application supports:

**Ollama → Llama 3.2 3B**

Both configurations use the same core retrieval, grounding, and citation workflow.

The model/runtime configuration is therefore an architecture and dependency decision, not simply an implementation detail.

---

# Why Retrieval-Augmented Generation

A general-purpose language model may contain broad knowledge, but PolicyAssist requires responses based on organizational policy documents.

RAG provides a controlled approach:

```text
User Question
      ↓
Retrieve Relevant Policy Evidence
      ↓
Validate Eligible Evidence
      ↓
Provide Evidence to Model
      ↓
Generate Response
      ↓
Display Supporting Source
```

This reduces reliance on the model's general knowledge for organization-specific policy questions.

---

# Architecture Decision

## Decision

Use a Retrieval-Augmented Generation architecture for the PolicyAssist Minimum Viable Product (MVP).

## Rationale

RAG supports the project's requirement to:

* Search internal policy content
* Retrieve relevant evidence
* Ground responses
* Provide citations
* Update policy knowledge without retraining the language model for every policy change
* Separate organizational knowledge from general model knowledge

---

# Authority Validation

Retrieval alone is not sufficient.

A document may be semantically relevant but still be:

* Draft
* Superseded
* Unverified
* Unauthorized
* Conflicting with another source

PolicyAssist therefore applies the following eligibility principle:

> Active + Authoritative + Approved + Required Metadata Present = Eligible

If authority cannot be established, the system should not automatically select one source over another.

---

# Grounding

The architecture requires the generated response to be supported by retrieved policy evidence.

The application controls:

* Which documents are eligible
* Which evidence is retrieved
* Which evidence is provided to the model
* Which citations are displayed

This reduces the risk of unsupported policy statements.

---

# Citation Architecture

Citations are controlled by the application rather than generated freely by the language model.

Expected behavior:

| Evidence Condition              | Expected Response                        |
| ------------------------------- | ---------------------------------------- |
| Evidence supports answer        | Answer + supporting citation             |
| Evidence is insufficient        | Refusal or limitation                    |
| Authority cannot be established | Do not use conflicting source + escalate |

A document should not be presented as authoritative simply because it was retrieved.

---

# Unsupported Questions

The architecture must support safe refusal.

If the approved knowledge base does not contain sufficient evidence, PolicyAssist should not invent an answer.

The system should communicate that sufficient approved information is unavailable.

This distinguishes:

* Evidence available
* Evidence unavailable
* Evidence conflicting
* Evidence unauthorized

---

# Mixed Questions

Some questions contain multiple policy requests.

For example:

> How much parental leave do I receive, and how many vacation days do I receive?

If evidence exists for one portion but not the other, the system should:

* Answer the supported portion
* Identify the unsupported portion
* Cite evidence for the supported portion
* Avoid inventing the unsupported portion

---

# Security Architecture Considerations

Retrieval relevance and authorization are separate controls.

A document may be active, authoritative, approved, and relevant while still being restricted to certain users.

Therefore:

> Retrieval eligibility does not automatically mean user access eligibility.

Production implementation must evaluate authorization before restricted information is disclosed.

Security considerations include:

* Authentication
* Authorization
* Role-based access
* Document access controls
* Sensitive information protection
* Audit logging
* Unauthorized-access testing

---

# Performance Requirement

PolicyAssist has a response-latency target of:

**≤ 10 seconds**

Measurement should include:

* Request processing
* Embedding
* Retrieval
* Eligibility validation
* Model generation
* Grounding
* Citation handling
* Response display

The target must be formally validated using representative test conditions.

---

# Architecture Risks

## Retrieval Risk

The system retrieves irrelevant or incomplete evidence.

**Impact:** Incorrect or incomplete responses.

## Authority Risk

The system retrieves an outdated or conflicting policy.

**Impact:** Incorrect organizational guidance.

## Model Risk

The language model adds unsupported information.

**Impact:** Hallucination and loss of trust.

## Citation Risk

The displayed source does not actually support the response.

**Impact:** False confidence.

## Security Risk

Restricted information is disclosed.

**Impact:** Privacy, security, compliance, and business risk.

## Performance Risk

The response exceeds the required latency.

**Impact:** Poor user experience and reduced adoption.

## Dependency Risk

A model or technology component changes behavior or availability.

**Impact:** Regression, quality changes, or release instability.

---

# Architecture Dependencies

| Dependency            | Architectural Impact                    |
| --------------------- | --------------------------------------- |
| Policy Documents      | Required for retrieval                  |
| Policy Metadata       | Required for eligibility                |
| Embedding Model       | Required for semantic search            |
| ChromaDB              | Required for vector retrieval           |
| Gemini 2.5 Flash      | Deployed response-generation dependency |
| Ollama / Llama 3.2 3B | Local fallback dependency               |
| Security Controls     | Required for authorized access          |
| Evaluation Dataset    | Required for architecture validation    |
| Monitoring            | Required for production operation       |
| Rollback Capability   | Required for controlled changes         |

---

# Evaluation Requirements

Architecture acceptance depends on evidence from evaluation.

Key evaluation areas include:

* Retrieval accuracy
* Response accuracy
* Grounding
* Citation correctness
* Unsupported questions
* Multi-policy questions
* Hallucination rate
* Response latency
* Security behavior

The project includes quality targets for:

* Retrieval accuracy: **90%**
* Hallucination rate: **less than 2%**
* Response latency: **10 seconds or less**

These targets must be formally validated before production approval.

---

# MVP Architecture

The current architecture is appropriate for prototype and MVP evaluation.

The prototype demonstrates:

* Document ingestion
* Embedding generation
* Vector retrieval
* Policy eligibility
* Response generation
* Grounding
* Citation
* User interaction

The prototype demonstrates technical feasibility.

---

# Production Readiness

A functioning prototype does not automatically qualify as production-ready.

Production readiness requires evidence for:

* Accuracy
* Security
* Governance
* Performance
* Testing
* User acceptance
* Monitoring
* Risk management
* Rollback

The Project Manager should not approve production release based solely on successful technical demonstration.

---

# Architecture Change Management

Architecture changes should be assessed when they affect:

* Model selection
* Retrieval strategy
* Data sources
* Security
* Access control
* Performance
* Hosting
* Cost
* Compliance
* User experience

A model or runtime change should trigger appropriate impact assessment, testing, evaluation, and release review.

---

# PM Architecture Review Questions

The Project Manager should ask:

1. Does the architecture support the business objective?
2. What data does the system use?
3. Is the data authoritative?
4. How is relevant evidence retrieved?
5. How does the system prevent unsupported answers?
6. Which model generates the response?
7. What happens if the deployed model is unavailable?
8. How is user access controlled?
9. How is performance measured?
10. How is AI quality evaluated?
11. How are policy updates handled?
12. What evidence is required before production release?
13. How are architecture changes governed?

---

# Current Architecture Decision

**Decision:** Proceed with the selected RAG architecture for continued MVP evaluation and validation.

**Production Decision:** Not approved.

The architecture has demonstrated technical feasibility, but production approval remains dependent on formal evaluation, security validation, UAT, pilot evidence, monitoring readiness, rollback validation, governance approval, and the final release decision.

---

# PM Decision

## HOLD

The PolicyAssist prototype demonstrates the core architecture and provides a working end-to-end workflow.

However, production approval remains on hold until the required evidence and release gates are completed.

The Project Manager should not convert the decision from HOLD to GO solely because the prototype is functional.

---

# Final Architecture Principle

> The knowledge source establishes organizational truth; the AI model interprets and communicates that information.

A working AI architecture is evidence of technical feasibility, not proof of production readiness.

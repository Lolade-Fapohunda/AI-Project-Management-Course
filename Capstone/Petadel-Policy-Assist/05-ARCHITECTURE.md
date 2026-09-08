# Petadel PolicyAssist AI

# AI Architecture & Technology Assessment

## 1. Purpose

This document defines the architecture for Petadel PolicyAssist AI and explains how the major application components support the business and project requirements.

The purpose is to provide the Project Manager with enough architectural understanding to manage dependencies, risks, quality, security, governance, testing, and release decisions.

The Project Manager is not expected to implement the architecture but must understand the purpose and risk associated with each major component.

---

# 2. Business Problem

Employees may have difficulty locating and interpreting the correct internal policy information.

The project addresses:

* Policy discovery.
* Multiple policy versions.
* Outdated information.
* Conflicting policy information.
* Unclear policy authority.
* Document search limitations.
* Access-control concerns.
* Dependence on human assistance.

---

# 3. Architecture Objective

The architecture must support a policy-assistance workflow in which the system:

1. Receives a policy question.
2. Identifies relevant policy information.
3. Retrieves eligible policy evidence.
4. Uses the retrieved evidence to generate a response.
5. Provides an appropriate source.
6. Refuses unsupported information rather than inventing an answer.
7. Supports appropriate security and governance controls.

---

# 4. High-Level Architecture

```text
Policy Documents
       ↓
Document Processing
       ↓
Metadata Validation
       ↓
Policy Eligibility Check
       ↓
Chunking
       ↓
Embeddings
       ↓
ChromaDB
       ↓
Semantic Retrieval
       ↓
Evidence Validation
       ↓
Response Generation
       ↓
Grounded Response
       ↓
Citation
       ↓
Streamlit Application
       ↓
User
```

---

# 5. Architecture Components

## 5.1 Policy Documents

Policy documents provide the source information used by the application.

Policy documents must contain sufficient information to establish:

* Policy ID
* Policy name
* Version
* Status
* Effective date
* Policy owner
* Approval information when available

---

## 5.2 Document Processing

The application reads approved policy documents and extracts their contents.

The document-processing stage prepares the information for validation, chunking, embedding, and retrieval.

---

## 5.3 Policy Eligibility

A policy is eligible for retrieval when it meets the required conditions:

**Active + Authoritative + Approved + Required Metadata Present = Eligible**

The application validates required policy metadata and status before policy information is treated as eligible.

---

## 5.4 Chunking

Policy documents are divided into smaller sections so that relevant portions can be retrieved when a user asks a question.

The purpose of chunking is to improve the ability to locate relevant policy content.

---

## 5.5 Embeddings

The application uses Sentence Transformers with:

`all-MiniLM-L6-v2`

The embedding model converts policy content and user questions into numerical representations that can be compared for semantic similarity.

---

## 5.6 Vector Database

The application uses:

**ChromaDB**

ChromaDB stores the policy embeddings and associated metadata used during retrieval.

---

## 5.7 Semantic Retrieval

The retrieval process compares the user's question with the stored policy information.

The current prototype uses a maximum retrieval distance of:

**1.20**

This is a configuration value.

It is not proof that retrieval accuracy is 90 percent or higher.

Retrieval quality must be demonstrated through evaluation.

---

# 6. Response Generation

The current application supports two response-generation configurations.

## 6.1 Deployed Configuration

When `GEMINI_API_KEY` is available, the application uses:

**Google Gen AI**

with:

**Gemini 2.5 Flash**

The current application configuration identifies `gemini-2.5-flash` as the Gemini model.

---

## 6.2 Local Development Configuration

When the Gemini API key is not available, the application can use:

**Ollama**

with:

**Llama 3.2 3B**

The application identifies `llama3.2:3b` as the local model and uses Ollama for local response generation.

---

## 6.3 Runtime Decision

The current runtime behavior is:

```text
GEMINI_API_KEY Available
        ↓
Gemini 2.5 Flash
```

If the key is not available:

```text
GEMINI_API_KEY Not Available
        ↓
Ollama
        ↓
Llama 3.2 3B
```

This allows the deployed application to use Gemini while retaining a local development option.

---

# 7. Grounding

The response-generation model receives the policy evidence selected by the application.

The model is instructed to answer using the supplied policy evidence.

The model is not treated as the source of company policy.

The basic flow is:

```text
User Question
       ↓
Policy Retrieval
       ↓
Eligible Evidence
       ↓
Response Generation
       ↓
Grounded Response
```

---

# 8. Unsupported Questions

If sufficient authoritative evidence does not exist, the system should not present an unsupported answer as policy information.

The expected behavior is:

```text
Question
   ↓
Insufficient Evidence
   ↓
Limitation or Refusal
   ↓
No Unsupported Policy Claim
```

---

# 9. Citation

Citations must correspond to the policy evidence supporting the response.

The application should not present a document as a supporting source merely because it was retrieved.

The project target is:

**Citation Correctness = 100%**

Unsupported citations should be treated as a quality failure.

---

# 10. Mixed Questions

Users may ask multiple questions in one request.

Example:

> How much parental leave do I receive and how many vacation days do I receive?

If evidence supports only one part of the question, the system should:

* Answer the supported portion.
* Identify the unsupported portion.
* Avoid inventing information.
* Provide the supporting source for the supported answer.

---

# 11. Policy Authority

Policy authority is a core control.

Eligible policies should be:

* Active.
* Authoritative.
* Approved.
* Complete with required metadata.

The system should not automatically select one document when two authoritative documents conflict and the correct authority cannot be established.

The conflict should be referred for human resolution.

---

# 12. Security Architecture

Security requirements include:

* Authentication.
* Authorization.
* Access control.
* Protection of sensitive information.
* Appropriate logging.
* Protection of policy information.

The production solution must ensure that users can access only information they are authorized to access.

---

# 13. Architecture Interfaces

| Interface                      | Input                        | Output                    | Key Risk                     |
| ------------------------------ | ---------------------------- | ------------------------- | ---------------------------- |
| User to Application            | Question                     | Request                   | Unauthorized access          |
| Application to Embedding Model | Text                         | Embedding                 | Poor representation          |
| Application to ChromaDB        | Query embedding              | Candidate policy sections | Poor retrieval               |
| ChromaDB to Application        | Policy evidence and metadata | Candidate evidence        | Incorrect or ineligible data |
| Application to Response Model  | Approved evidence and prompt | Candidate response        | Unsupported claims           |
| Response Model to Application  | Generated response           | Candidate answer          | Hallucination                |
| Application to User            | Answer and source            | User experience           | Incorrect information        |
| Policy Source to Ingestion     | Policy document              | Indexed content           | Outdated or incomplete data  |

---

# 14. Technology Stack

| Technology            | Role                                           |
| --------------------- | ---------------------------------------------- |
| Python                | Programming language                           |
| Streamlit             | Application and user interface                 |
| Sentence Transformers | Embedding framework                            |
| `all-MiniLM-L6-v2`    | Embedding model                                |
| ChromaDB              | Vector database                                |
| Google Gen AI         | Cloud model integration                        |
| Gemini 2.5 Flash      | Response generation for deployed configuration |
| Ollama                | Local model runtime                            |
| Llama 3.2 3B          | Local response-generation fallback             |

---

# 15. Technical Dependencies

Major dependencies include:

* Policy documents.
* Policy metadata.
* Embedding model.
* ChromaDB.
* Response-generation model.
* Streamlit.
* Authentication and authorization.
* Evaluation dataset.
* Monitoring.
* Application configuration.

Dependencies should be tracked when failure could affect:

* Scope.
* Schedule.
* Cost.
* Quality.
* Security.
* Release readiness.

---

# 16. Technical Risks

| Risk                      | Severity    | PM Response                            |
| ------------------------- | ----------- | -------------------------------------- |
| Poor document quality     | High        | Establish data-readiness controls      |
| Incorrect policy metadata | High        | Validate required metadata             |
| Conflicting policies      | High        | Hold for authority resolution          |
| Poor retrieval accuracy   | High        | Evaluate retrieval performance         |
| Unsupported responses     | Critical    | Enforce grounding and refusal controls |
| Incorrect citations       | High        | Validate citation correctness          |
| Model limitations         | Medium/High | Evaluate against approved dataset      |
| Slow response time        | Medium      | Measure latency                        |
| Unauthorized access       | Critical    | Validate access controls               |
| Vector database failure   | Medium/High | Define recovery approach               |
| Model or runtime failure  | Medium      | Maintain approved fallback approach    |
| Uncontrolled model change | High        | Apply change control                   |
| Knowledge-base changes    | High        | Revalidate changed policy information  |

---

# 17. MVP Architecture

The MVP must support the minimum employee journey:

```text
Authorized User
       ↓
Ask Policy Question
       ↓
Retrieve Eligible Policy
       ↓
Generate Grounded Response
       ↓
Display Supporting Source
       ↓
User Can Provide Feedback
```

The MVP should include:

* Approved policy ingestion.
* Required policy metadata.
* Active and authority controls.
* Semantic retrieval.
* Grounded responses.
* Evidence-based citations.
* Unsupported-question handling.
* Basic security controls.
* Basic feedback and escalation.
* Core evaluation.
* Core testing.
* MVP UAT.

---

# 18. MVP Does Not Equal Production Readiness

The MVP does not need to provide every operational capability required for production.

Production readiness additionally requires:

* Production-scale performance validation.
* Comprehensive monitoring.
* Full security validation.
* Complete governance controls.
* Full regression testing.
* Reliability validation.
* Tested rollback.
* Production deployment controls.
* Long-term improvement processes.

---

# 19. Evaluation Acceptance Criteria

The project establishes the following targets:

| Measure                      |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |
| Critical Security Findings   |            0 |
| User Satisfaction            |        ≥ 85% |

These are project targets.

They must be supported by documented evidence before production acceptance.

---

# 20. Performance

Response time should be measured from:

> **The moment the user submits a policy question to the moment the complete PolicyAssist response is displayed.**

The measurement should include:

* Question processing.
* Embedding generation.
* Vector retrieval.
* Policy eligibility validation.
* Response generation.
* Grounding.
* Citation processing.
* Final response display.

The project target is:

**Response Latency ≤ 10 seconds**

Performance must be measured rather than judged by user perception.

---

# 21. Production Architecture Considerations

Production planning should address:

### Scalability

Can the system support the expected number of users and policy documents?

### Reliability

What happens when a major component becomes unavailable?

### Performance

Can the system consistently meet the response-time target?

### Security

Can production authentication and authorization requirements be enforced?

### Governance

Can policy changes be controlled and audited?

### Monitoring

Can quality, security, performance, and business outcomes be monitored?

### Recovery

Can the system be restored to an approved state?

### Change Management

Can changes to the application, embedding model, response-generation model, and policy knowledge base be controlled?

---

# 22. Current Architecture Decisions

| Decision                | Current Selection                      | Reason                                          |
| ----------------------- | -------------------------------------- | ----------------------------------------------- |
| Architecture Pattern    | Retrieval-Augmented Generation         | Grounds responses in retrieved policy evidence  |
| Embedding Model         | `all-MiniLM-L6-v2`                     | Supports semantic retrieval                     |
| Vector Database         | ChromaDB                               | Supports vector retrieval                       |
| Deployed Response Model | Gemini 2.5 Flash                       | Current cloud response-generation configuration |
| Local Response Model    | Llama 3.2 3B through Ollama            | Supports local development                      |
| UI                      | Streamlit                              | Supports the working prototype                  |
| Policy Source of Truth  | Active, authoritative, approved policy | Prevents unsupported policy use                 |
| Retrieval Threshold     | Maximum distance 1.20                  | Current prototype configuration                 |
| Citation Control        | Application-controlled                 | Supports evidence-based citations               |
| Response-Time Target    | ≤10 seconds                            | Provides measurable performance requirement     |

The application confirms the current Gemini and Ollama model configuration.

These decisions remain subject to evaluation evidence and change control.

---

# 23. Architecture Assumptions

Current assumptions include:

1. Approved policy documents can be obtained.
2. Policy owners can establish authority.
3. Required policy metadata can be maintained.
4. Users can be authenticated.
5. Authorization rules can be established.
6. The selected response-generation environment can support prototype requirements.
7. Evaluation data can be created and maintained.
8. Policy changes can be identified and controlled.
9. Technical stakeholders can provide architecture evidence.
10. Security requirements can be validated before production.
11. Representative performance testing can be performed.

Each assumption should be validated before it becomes a production dependency.

---

# 24. Architecture Constraints

Known constraints include:

* The current project is a prototype.
* Production-scale infrastructure is outside the initial prototype scope.
* The Project Manager is not expected to implement advanced infrastructure or MLOps.
* Security testing is evaluated at the Project Manager and design level within the course.
* Production security and authorization require additional validation.
* Performance results from a prototype must not automatically be treated as proof of production-scale performance.
* Model selection may change based on evaluation, cost, availability, security, or project requirements.

---

# 25. Architecture Traceability

| Requirement Area      | Architecture Response                              |
| --------------------- | -------------------------------------------------- |
| Policy retrieval      | Embeddings and ChromaDB                            |
| Grounded responses    | Retrieved evidence and response-generation model   |
| Citation              | Application-controlled evidence mapping            |
| Authority             | Policy metadata and eligibility validation         |
| Versioning            | Policy metadata and status controls                |
| Unsupported questions | Evidence sufficiency and refusal logic             |
| Security              | Authentication, authorization, and access controls |
| Performance           | Response-time measurement                          |
| Quality               | Evaluation dataset and defined metrics             |
| UAT                   | Testable user journeys                             |
| Monitoring            | Metrics, logs, alerts, and feedback                |
| Rollback              | Controlled restoration to an approved state        |

---

# 26. Architecture Change Control

Architecture changes must be evaluated when they could affect:

* Business requirements.
* Security.
* Data governance.
* Quality.
* Performance.
* Cost.
* Schedule.
* Scope.
* Testing.
* UAT.
* Release readiness.

A material architecture change should trigger:

1. Change request.
2. Impact assessment.
3. Risk assessment.
4. Stakeholder review.
5. Architecture decision update.
6. Documentation update.
7. Testing.
8. Approval.

---

# 27. Architecture Evidence

Architecture approval must be evidence-based.

Acceptable evidence includes:

* Architecture diagrams.
* Technical design documentation.
* Evaluation results.
* Performance results.
* Security assessment.
* Data-readiness assessment.
* Test results.
* UAT results.
* Dependency analysis.
* Risk assessment.
* Architecture decision records.

### PM Rule

> **No Evidence = Not Yet Accepted.**

---

# 28. PM Architecture Review Questions

Before approving the architecture, the Project Manager should ask:

1. Does the architecture support the business problem?
2. Does each major requirement map to an architecture capability?
3. Where is policy authority validated?
4. How is policy versioning controlled?
5. What happens when policies conflict?
6. How does retrieval work?
7. How is retrieval quality measured?
8. How does the system prevent unsupported answers?
9. How are citations validated?
10. What happens if the response-generation model produces an unsupported response?
11. What security controls protect policy information?
12. What happens if ChromaDB becomes unavailable?
13. What happens if the response-generation model becomes unavailable?
14. What happens when policies change?
15. What happens when the model changes?
16. What evidence demonstrates that the architecture works?
17. What technical dependencies could affect the schedule?
18. What architecture changes require reapproval?
19. Which capabilities are MVP versus production-only?
20. How is response time measured?
21. What happens when response-time thresholds are exceeded?
22. Is the architecture ready to proceed to the next project gate?

---

# 29. PM Decision

The architecture should proceed only when sufficient evidence exists that it can support the required business, quality, security, performance, and governance objectives.

Possible decisions:

### Proceed

Architecture is sufficiently understood, risks are controlled, and required evidence is available.

### Proceed With Conditions

Architecture is acceptable for the current phase, but specific conditions must be completed before the next gate.

### Hold

Critical information, evidence, security controls, governance decisions, performance validation, or technical validation are missing.

---

# 30. Final Architecture Position

The current architecture supports a working prototype.

The current application uses:

**Python → Streamlit → Sentence Transformers → all-MiniLM-L6-v2 → ChromaDB → Semantic Retrieval → Gemini 2.5 Flash → Grounded Response → Citation**

The application also supports:

**Ollama → Llama 3.2 3B**

as a local development fallback.

The architecture should not be considered production-ready solely because the prototype works.

Production acceptance requires documented evidence for:

* Quality.
* Security.
* Performance.
* UAT.
* Governance.
* Monitoring.
* Rollback.
* Reliability.
* Final release approval.

**Current Project Decision: HOLD**

---

# 31. Key Takeaways

* The Project Manager does not need to be the engineer but must understand the architecture.
* Architecture decisions must connect to business requirements.
* Retrieval should occur before response generation.
* The response-generation model is not the policy source of truth.
* Policy authority and versioning must be controlled outside the model.
* Unsupported questions must not produce fabricated policy information.
* Citations must be evidence-based.
* Security must be designed into the architecture.
* Performance must be measured.
* MVP architecture and production architecture are not necessarily identical.
* Technical dependencies and risks must be actively managed.
* Material architecture decisions should be documented.
* Architecture must be traceable to requirements.
* Technical claims must be supported by evidence.
* **No Evidence = Not Yet Accepted.**

---

# 32. Connection To Capstone

This architecture assessment supports the remaining Petadel PolicyAssist AI capstone work, including:

* Requirements.
* Product backlog.
* Data governance.
* Evaluation.
* Risk and security.
* Testing and UAT.
* Release readiness.
* Monitoring.
* Decision management.
* Requirements traceability.

The architecture is therefore a project-management artifact that connects the business requirements to the technical solution, quality controls, governance requirements, testing, and release decisions.

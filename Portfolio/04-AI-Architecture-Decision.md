# AI Architecture Decision

## 1. Purpose

This document records the architecture decision for the Petadel PolicyAssist AI capstone.

The purpose is to document how the solution retrieves policy information, generates responses, supports source citation, and manages the technical considerations that affect project delivery.

This document focuses on the Project Manager's role in understanding and governing the architecture rather than implementing the software.

## 2. Business Problem

Petadel Technology Services (PTS) employees may have difficulty locating and understanding current company policies.

The solution needs to retrieve relevant information from approved policy documents and provide responses that are grounded in those documents.

The architecture must support:

* Policy retrieval
* Source grounding
* Citation
* Policy authority
* Version awareness
* Response generation
* Unsupported-question handling
* Performance
* Security
* Future scalability

## 3. Architecture Approach

The PolicyAssist prototype uses a Retrieval-Augmented Generation (RAG) approach.

The primary flow is:

**Policy Documents → Document Processing → Chunking → Embeddings → ChromaDB → Semantic Retrieval → Response Generation → Grounding and Citation → Streamlit Interface**

The architecture separates information retrieval from response generation.

This separation helps reduce the risk of generating responses that are not supported by the available policy evidence.

## 4. Architecture Components

### Policy Documents

Approved policy documents provide the source information used by the system.

Policy metadata includes information such as:

* Policy ID
* Policy name
* Policy category
* Policy owner
* Effective date
* Version
* Status
* Applicability
* Document type

### Document Processing

Policy documents are loaded and prepared for retrieval.

The processing stage supports the creation of searchable content from the approved policy documents.

### Chunking

Documents are divided into smaller sections to improve retrieval of relevant policy evidence.

### Embeddings

The application uses Sentence Transformers with:

`all-MiniLM-L6-v2`

The model converts policy text into vector embeddings that can be compared based on semantic similarity.

### ChromaDB

ChromaDB is used as the vector database for storing and retrieving document embeddings.

### Semantic Retrieval

When a user submits a question, the system searches the policy knowledge base for relevant evidence.

The retrieval process is intended to identify the most relevant policy content before response generation occurs.

### Response Generation

The response-generation layer converts retrieved evidence into a user-facing answer.

The current application supports two model configurations.

## 5. Deployed Model Configuration

The deployed application uses:

**Google Gen AI → Gemini 2.5 Flash**

When the Gemini API key is available, the application uses Gemini 2.5 Flash to generate the response from the retrieved policy evidence.

This is the configuration used for the deployed Streamlit application.

## 6. Local Model Configuration

For local development, the application supports:

**Ollama → Llama 3.2 3B**

This provides a local response-generation option when a Gemini API key is not available.

The local configuration supports development and testing without requiring the deployed Gemini configuration.

## 7. Architecture Decision

The architecture decision is to use a retrieval-based approach with a separate response-generation layer.

The selected technology stack is:

| Component               | Technology                  |
| ----------------------- | --------------------------- |
| Application language    | Python                      |
| User interface          | Streamlit                   |
| Embeddings              | Sentence Transformers       |
| Embedding model         | `all-MiniLM-L6-v2`          |
| Vector database         | ChromaDB                    |
| Deployed response model | Gemini 2.5 Flash            |
| Local response model    | Llama 3.2 3B through Ollama |

This approach provides a practical prototype architecture while keeping the system simple enough to evaluate and demonstrate.

## 8. Why RAG Was Selected

Retrieval-Augmented Generation was selected because PolicyAssist needs to answer questions using organizational policy evidence rather than relying solely on a general-purpose language model.

The approach supports:

* Evidence-based responses
* Source citation
* Policy-specific retrieval
* Reduced dependence on model memory
* Better traceability
* Easier policy document updates

The architecture does not eliminate hallucination risk. Evaluation and governance remain necessary.

## 9. Grounding

Grounding requires the generated response to be supported by retrieved policy evidence.

If sufficient evidence is not available, the system should not invent a policy answer.

The project therefore treats unsupported questions as an important evaluation and governance scenario.

## 10. Citation

PolicyAssist is designed to identify the policy evidence supporting the response.

Citation improves:

* Transparency
* User confidence
* Verification
* Auditability
* Policy traceability

A response without sufficient supporting evidence should not be treated as authoritative policy guidance.

## 11. Unsupported Questions

The architecture must account for questions that cannot be answered from the available policy documents.

Expected behavior includes communicating that the available evidence does not establish an answer rather than generating unsupported policy guidance.

This is an important control against hallucination.

## 12. Mixed Questions

Questions may contain multiple policy topics.

For example, a question could involve:

* PTO
* Sick leave
* Parental leave
* Manager approval

The system must retrieve relevant evidence across applicable policies and avoid combining unrelated policy requirements incorrectly.

Multi-policy questions remain an important evaluation scenario.

## 13. Policy Authority

The system must prioritize authoritative policy documents.

Policy authority should consider:

* Policy status
* Effective date
* Version
* Policy owner
* Applicability

Superseded policy versions should not be presented as current guidance when an approved active version exists.

## 14. Security and Access

A production implementation must ensure that users only receive information they are authorized to access.

Security considerations include:

* Authentication
* Authorization
* Role-based access
* Document access controls
* Sensitive information protection
* Audit logging
* Unauthorized access testing

Security is a release requirement rather than an optional enhancement.

## 15. Performance

The project includes a target response latency of:

**10 seconds or less**

Performance should be evaluated across:

* Retrieval time
* Embedding operations
* Model response time
* End-to-end response time

The target must be validated using representative test conditions before production approval.

## 16. Architecture Risks

Key architecture risks include:

### Retrieval Failure

The system may retrieve incomplete or incorrect evidence.

### Hallucination

The model may generate information that is not supported by the retrieved evidence.

### Outdated Policy

An outdated document may be retrieved if authority and version controls are not correctly implemented.

### Multi-Policy Complexity

Questions involving multiple policies may produce incomplete or incorrectly combined answers.

### Model Dependency

The deployed configuration depends on an external generative AI service.

### Security

Insufficient access controls could expose policy information to unauthorized users.

### Performance

Response time may increase as document volume, retrieval complexity, or model processing requirements increase.

## 17. Evaluation Requirements

Architecture acceptance depends on evidence from the evaluation process.

Key evaluation areas include:

* Retrieval accuracy
* Response accuracy
* Grounding
* Citation
* Unsupported questions
* Multi-policy questions
* Hallucination rate
* Response latency

The project includes quality targets, including:

* Retrieval accuracy target: 90%
* Hallucination rate target: less than 2%
* Response latency target: 10 seconds or less

These targets must be formally validated before production readiness can be approved.

## 18. MVP Architecture

The current architecture is appropriate for a prototype or Minimum Viable Product (MVP).

The MVP demonstrates:

* Document ingestion
* Embedding generation
* Vector retrieval
* Response generation
* Grounding
* Citation
* User interaction

The prototype demonstrates the core workflow needed to evaluate the product concept.

## 19. MVP Does Not Equal Production Readiness

A functioning prototype does not automatically qualify as production-ready.

Production readiness requires evidence that the solution meets agreed requirements for:

* Accuracy
* Security
* Governance
* Performance
* Testing
* User acceptance
* Monitoring
* Risk management

The Project Manager should not approve production release based solely on successful technical demonstration.

## 20. Production Architecture Considerations

Before production release, the architecture should be evaluated for:

* Scalable document processing
* Centralized document storage
* Enterprise identity integration
* Role-based access control
* Secure API management
* Monitoring
* Logging
* Model availability
* Failure handling
* Backup and recovery
* Version control
* Auditability
* Cost management

These considerations are outside the minimum prototype scope but are relevant to production planning.

## 21. Current Architecture Decision

The current architecture is **accepted for prototype evaluation**.

It is not yet accepted as a production architecture.

The distinction is important because the project currently has a working prototype but still requires formal evidence for production readiness.

## 22. Architecture Traceability

The architecture supports the following project requirements:

| Requirement                         | Architecture Support                         |
| ----------------------------------- | -------------------------------------------- |
| Retrieve policy information         | Semantic retrieval                           |
| Use approved policy evidence        | Policy metadata and authority controls       |
| Ground responses                    | Retrieved policy context                     |
| Provide supporting sources          | Citation                                     |
| Support relevant document retrieval | Embeddings and ChromaDB                      |
| Generate user-facing responses      | Gemini 2.5 Flash or local Llama 3.2 3B       |
| Manage unsupported questions        | Evidence-based response controls             |
| Support evaluation                  | Retrieval and response evaluation            |
| Support performance targets         | End-to-end latency measurement               |
| Support security requirements       | Access-control and governance considerations |

## 23. Architecture Change Control

Architecture changes should be documented when they affect:

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

Changes should be evaluated for impact on requirements, risks, testing, and release readiness.

## 24. Project Manager Architecture Review Questions

A Project Manager should ask:

1. What data does the system use?
2. Is the data authoritative?
3. How is relevant evidence retrieved?
4. How does the system prevent unsupported answers?
5. Which model generates the response?
6. What happens if the model is unavailable?
7. How is user access controlled?
8. How is performance measured?
9. How is AI quality evaluated?
10. What evidence is required before production release?
11. How are policy updates handled?
12. How are architecture changes governed?

## 25. PM Decision

**Decision: HOLD**

The PolicyAssist prototype demonstrates the core architecture and provides a working end-to-end workflow.

However, production approval remains on hold until the required evidence and release gates are completed.

The Project Manager should not convert the decision from HOLD to GO solely because the prototype is functional.

## 26. Final Architecture Position

The selected architecture is appropriate for the current prototype and evaluation stage.

The deployed configuration uses **Gemini 2.5 Flash** for response generation.

The local configuration supports **Ollama with Llama 3.2 3B**.

The architecture provides a practical foundation for PolicyAssist while recognizing that additional controls and validation are required before production deployment.

## 27. Key Takeaways

The architecture demonstrates that an AI Project Manager does not need to build the AI system personally but must understand enough to manage:

* Architecture decisions
* Technical dependencies
* Data
* AI models
* Retrieval
* Security
* Evaluation
* Performance
* Risks
* Release readiness

The central project management principle is:

**A working AI prototype is evidence of technical feasibility, not proof of production readiness.**

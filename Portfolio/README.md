# Petadel PolicyAssist AI Portfolio

## Portfolio Overview

This portfolio demonstrates the project management work completed for the Petadel PolicyAssist AI capstone.

The portfolio focuses on the decisions, evidence, controls, and project management practices required to lead an AI product from problem definition through release readiness and continuous improvement.

The portfolio is designed to demonstrate practical AI Project Management capability rather than software engineering capability.

## Project

**Petadel PolicyAssist AI**

Petadel PolicyAssist AI is a policy assistance solution designed to help employees locate and understand authoritative company policies.

The solution retrieves relevant policy information from approved policy documents and provides grounded responses with supporting sources.

## Portfolio Evidence Map

| Evidence Area                 | Portfolio Evidence                                                   |
| ----------------------------- | -------------------------------------------------------------------- |
| Project Case Study            | [01-Project-Case-Study.md](01-Project-Case-Study.md)                 |
| Requirements                  | [02-Requirements-Evidence.md](02-Requirements-Evidence.md)           |
| Product Planning              | [03-Product-Planning-Evidence.md](03-Product-Planning-Evidence.md)   |
| AI Architecture               | [04-AI-Architecture-Decision.md](04-AI-Architecture-Decision.md)     |
| Data Governance               | [05-Data-Governance-Decision.md](05-Data-Governance-Decision.md)     |
| AI Evaluation                 | [06-AI-Evaluation-Results.md](06-AI-Evaluation-Results.md)           |
| Risk, Security and Governance | [07-Risk-Security-Decision.md](07-Risk-Security-Decision.md)         |
| Testing and UAT               | [08-Testing-UAT-Evidence.md](08-Testing-UAT-Evidence.md)             |
| Release Readiness             | [09-Release-Readiness-Decision.md](09-Release-Readiness-Decision.md) |
| Monitoring                    | [10-Monitoring-Strategy.md](10-Monitoring-Strategy.md)               |
| Final PM Decision             | [11-Final-PM-Decision.md](11-Final-PM-Decision.md)                   |

## Project Management Evidence

The portfolio demonstrates the ability to:

* Define a technology and AI business problem.
* Translate business needs into requirements.
* Build and manage a product backlog.
* Apply prioritization methods.
* Define acceptance criteria.
* Evaluate architecture decisions.
* Establish data governance requirements.
* Define AI evaluation criteria.
* Manage project and AI-specific risks.
* Address security and access requirements.
* Plan testing and User Acceptance Testing (UAT).
* Establish release readiness criteria.
* Define monitoring and continuous improvement practices.
* Make evidence-based Go, Hold, or No-Go decisions.

## AI Architecture

The PolicyAssist prototype uses a Retrieval-Augmented Generation (RAG) approach.

The primary architecture flow is:

**Policy Documents → Document Processing → Chunking → Embeddings → ChromaDB → Semantic Retrieval → Response Generation → Grounding and Citation → Streamlit Interface**

The deployed configuration uses:

* Google Gen AI
* Gemini 2.5 Flash

Local development can use:

* Ollama
* Llama 3.2 3B

Embeddings are generated using Sentence Transformers with `all-MiniLM-L6-v2`.

ChromaDB is used for vector storage and semantic retrieval.

The architecture documentation explains the technical decisions and their project management implications.

See [04-AI-Architecture-Decision.md](04-AI-Architecture-Decision.md).

## Data Governance

The project treats policy authority, versioning, document status, access, and source traceability as core governance requirements.

The system should prioritize authoritative and current policy documents and should not present unsupported information as official policy guidance.

See [05-Data-Governance-Decision.md](05-Data-Governance-Decision.md).

## AI Evaluation

The project includes an evaluation approach covering:

* Retrieval accuracy
* Response accuracy
* Grounding
* Citation
* Unsupported questions
* Multi-policy questions
* Response latency
* Hallucination risk

The project defines target quality thresholds, but formal production-readiness validation remains a required gate.

See [06-AI-Evaluation-Results.md](06-AI-Evaluation-Results.md).

## Risk, Security and Governance

The project identifies risks associated with:

* Incorrect responses
* Unsupported answers
* Outdated policies
* Unauthorized access
* Data exposure
* Incomplete evaluation
* Performance
* Model behavior
* Policy conflicts

Security and governance requirements are treated as release considerations rather than optional enhancements.

See [07-Risk-Security-Decision.md](07-Risk-Security-Decision.md).

## Testing and UAT

The testing approach separates:

1. Application testing
2. AI evaluation
3. User Acceptance Testing
4. Production-readiness validation

This separation helps ensure that a technically functioning prototype is not automatically treated as production-ready.

See [08-Testing-UAT-Evidence.md](08-Testing-UAT-Evidence.md).

## Release Readiness

Release readiness is based on evidence across:

* Requirements
* Testing
* AI evaluation
* Security
* Governance
* Performance
* User acceptance
* Monitoring
* Risk

See [09-Release-Readiness-Decision.md](09-Release-Readiness-Decision.md).

## Monitoring and Continuous Improvement

The monitoring strategy considers:

* Response quality
* Retrieval performance
* Latency
* Unsupported questions
* User feedback
* Policy changes
* Security events
* System availability

Monitoring is intended to support ongoing improvement after release.

See [10-Monitoring-Strategy.md](10-Monitoring-Strategy.md).

## Final Project Decision

### HOLD

The current project decision is **HOLD**.

The prototype demonstrates the core PolicyAssist workflow and is available as a working application.

However, a working prototype does not by itself establish production readiness.

Formal evidence and release gates must be completed before a production Go decision can be made.

See [11-Final-PM-Decision.md](11-Final-PM-Decision.md).

## Professional PM Perspective

The key project management lesson demonstrated by this capstone is that AI project success is not determined solely by whether the application works.

A Project Manager must evaluate:

* Business value
* Requirements
* Product scope
* Architecture
* Data
* AI quality
* Security
* Governance
* Testing
* User acceptance
* Release readiness
* Monitoring
* Risk
* Evidence

The final decision should be based on documented evidence and agreed acceptance criteria.

## Related Project Materials

The complete capstone documentation is available in:

`Capstone/Petadel-Policy-Assist/`

The working application is available in:

`PolicyAssist-App/`

The standalone application repository is:

`PolicyAssistAI`

The course provides the learning framework, while the capstone and portfolio demonstrate its practical application.

## Portfolio Outcome

This portfolio demonstrates an end-to-end approach to managing an AI-enabled technology product from initial problem definition through evaluation, governance, release readiness, and continuous improvement.

It is intended to provide evidence of practical AI Project Management capability for professional and career development.

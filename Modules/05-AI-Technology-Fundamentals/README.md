# Module 5: AI Technology Fundamentals

## Purpose

An AI Project Manager does not need to be an AI engineer.

However, an AI Project Manager must understand enough about AI technologies to:

* Communicate effectively with technical teams.
* Challenge unrealistic technical assumptions.
* Understand project dependencies.
* Identify technical risks.
* Translate technical constraints into project decisions.
* Evaluate whether proposed technology supports the business objective.

This module introduces the technical concepts an AI Project Manager needs to manage AI projects effectively.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain the major components of an AI system.
* Distinguish between AI, machine learning, generative AI, and large language models.
* Explain how data, models, applications, and infrastructure interact.
* Understand embeddings, vector databases, retrieval, and grounding.
* Understand the difference between a model and an AI application.
* Identify common AI technical dependencies and risks.
* Evaluate technical claims from a project-management perspective.
* Translate technical information into project decisions.

---

## What Is Artificial Intelligence?

Artificial Intelligence (AI) refers to technologies that allow computer systems to perform tasks that normally require aspects of human intelligence.

Examples include:

* Understanding language.
* Recognizing patterns.
* Classifying information.
* Generating text.
* Making predictions.
* Recommending actions.
* Analyzing images.

AI is a broad field.

Not every AI system works the same way.

---

## Machine Learning

Machine Learning (ML) is a subset of AI in which systems learn patterns from data rather than relying entirely on explicitly programmed rules.

For example:

A traditional system might use:

> If transaction amount > $10,000 → Flag transaction.

A machine-learning system may instead learn patterns from historical transactions and predict which transactions are likely to be suspicious.

### PM Considerations

The PM should understand:

* What data is required?
* How much data is available?
* Is the data reliable?
* How will performance be measured?
* What happens when the model is wrong?
* What business decision depends on the prediction?

---

## Generative AI

Generative AI refers to AI systems capable of generating new content.

Examples include:

* Text
* Images
* Audio
* Video
* Code

Large Language Models are a major category of generative AI systems.

Generative AI introduces additional project-management concerns because generated output may be:

* Incorrect
* Incomplete
* Inconsistent
* Biased
* Unsupported by evidence
* Sensitive or inappropriate

The PM must therefore plan for evaluation and governance, not simply functionality.

---

## Large Language Models

A Large Language Model (LLM) is an AI model trained on large amounts of text to understand and generate language.

LLMs can perform tasks such as:

* Answering questions.
* Summarizing information.
* Classifying text.
* Extracting information.
* Generating content.
* Transforming text.

However, an LLM does not automatically know an organization's current internal policies, procedures, or proprietary information.

That information must be provided through an appropriate architecture.

---

## AI Model Vs. AI Application

One of the most important concepts for an AI Project Manager is understanding that the **AI model is not the entire product**.

A model is one component.

An AI application may also require:

* User interface
* Authentication
* Data sources
* Document processing
* Retrieval
* Databases
* Business rules
* Security controls
* Monitoring
* Logging
* Evaluation
* Human escalation

Therefore:

> A powerful model does not automatically produce a successful AI product.

---

## AI Application Architecture

A simplified AI application may look like:

**User**

↓

**Application Interface**

↓

**Business Logic**

↓

**Data / Knowledge Retrieval**

↓

**AI Model**

↓

**Response Validation / Grounding**

↓

**User**

Each component introduces project dependencies and risks.

---

## Embeddings

An embedding is a numerical representation of information that captures semantic meaning.

Text with similar meanings can produce embeddings that are mathematically closer together.

For example:

> "How many vacation days do I receive?"

and

> "How much paid time off am I entitled to?"

use different words but may have similar meaning.

Embeddings allow systems to perform semantic search rather than relying only on exact keyword matches.

### PM Considerations

The PM should ask:

* What embedding model is being used?
* Why was it selected?
* Does it support the required language?
* How will embedding quality be evaluated?
* What happens when similar concepts are retrieved incorrectly?

The PM does not need to calculate the embedding vectors.

The PM needs to understand their role in the system.

---

## Vector Databases

A vector database stores numerical representations of information so that systems can efficiently search for semantically similar content.

A simplified process is:

**Document**

↓

**Text Chunk**

↓

**Embedding**

↓

**Vector Database**

↓

**Similarity Search**

↓

**Relevant Content**

Vector databases are commonly used in Retrieval-Augmented Generation systems.

---

## Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is an architecture that allows an AI system to retrieve relevant information before generating a response.

A simplified RAG workflow is:

**User Question**

↓

**Convert Question Into Search Representation**

↓

**Search Knowledge Base**

↓

**Retrieve Relevant Content**

↓

**Provide Retrieved Content To Model**

↓

**Generate Response**

↓

**Ground / Cite Response**

RAG can help an application answer questions using organization-specific information without requiring the model itself to contain all of that information.

---

## Grounding

Grounding means connecting an AI response to reliable information or evidence.

For example, instead of allowing a model to answer entirely from its learned patterns, the application can provide relevant approved source information and require the response to rely on that information.

Grounding is particularly important for:

* Policies
* Procedures
* Legal information
* Financial information
* Medical information
* Compliance information
* Internal organizational knowledge

### PM Question

The PM should ask:

> "What evidence supports this answer?"

rather than simply:

> "Does the AI sound correct?"

---

## Hallucination

An AI hallucination occurs when an AI system generates information that appears plausible but is unsupported or incorrect.

For a general chatbot, a hallucination may be inconvenient.

For an enterprise policy system, a hallucination could create serious business, legal, compliance, or employee-relations risk.

The PM must therefore establish:

* Hallucination targets.
* Evaluation methods.
* Refusal behavior.
* Source requirements.
* Escalation procedures.
* Acceptance criteria.

---

## Model Selection

Choosing an AI model is a project decision, not simply a technical decision.

Possible selection factors include:

* Accuracy
* Cost
* Speed
* Context capacity
* Privacy
* Security
* Deployment requirements
* Language support
* Hardware requirements
* Licensing
* Availability
* Maintainability

The "best" model is not necessarily the largest or newest model.

The correct model is the one that best satisfies the project's requirements and constraints.

---

## Local Vs. Cloud AI

AI systems can run in different environments.

### Local AI

The model runs within an organization's controlled environment.

Potential advantages:

* Greater control over data.
* Reduced dependence on external services.
* Potentially lower recurring API costs.
* Useful for sensitive information.

Potential challenges:

* Hardware requirements.
* Model management.
* Performance limitations.
* Maintenance responsibility.

### Cloud AI

The AI capabilities run through a cloud provider or external service.

Potential advantages:

* Scalability.
* Access to powerful infrastructure.
* Easier integration with managed services.
* Reduced infrastructure management.

Potential challenges:

* Cost.
* Data privacy.
* Vendor dependency.
* Compliance.
* Network dependency.

The PM should evaluate the business and project implications of both approaches.

---

## AI Technology Stack

An AI application may contain multiple technology layers.

| Layer                             | Purpose                                              |
| --------------------------------- | ---------------------------------------------------- |
| **Programming Language**          | Used to build application logic                      |
| **Application Framework**         | Provides application or user-interface functionality |
| **Embedding Framework / Library** | Generates semantic representations                   |
| **Embedding Model**               | Produces embeddings from data                        |
| **Vector Database**               | Stores and searches embeddings                       |
| **AI Runtime**                    | Runs or serves an AI model                           |
| **Large Language Model**          | Generates or processes language                      |
| **Application Logic**             | Controls how the components interact                 |

The PM should understand the **role** of each technology rather than memorizing technology names.

---

## Technical Dependencies

AI projects commonly contain dependencies such as:

**Data Availability**

↓

**Data Processing**

↓

**Embedding**

↓

**Knowledge Storage**

↓

**Retrieval**

↓

**AI Generation**

↓

**Evaluation**

↓

**User Acceptance**

If an earlier component is not ready, downstream work may be blocked.

The PM should maintain a dependency view throughout the project.

---

## Challenging Technical Claims

AI Project Managers should not accept technical claims without evidence.

Consider:

> "The model is highly accurate."

Ask:

* What does accurate mean?
* What dataset was used?
* What metric was measured?
* What was the sample size?
* What was the test methodology?
* What types of errors occurred?
* Does the result represent real users?
* What threshold defines acceptance?

Another example:

> "The retrieval system works."

A strong PM response is:

> "What retrieval accuracy did the evaluation demonstrate against the agreed test dataset?"

The goal is not to challenge engineers unnecessarily.

The goal is to replace assumptions with measurable evidence.

---

## Technical Risk Categories

Common AI technical risks include:

### Data Risk

Required information is incomplete, inaccurate, outdated, or inaccessible.

### Model Risk

The selected model does not meet performance requirements.

### Retrieval Risk

The system retrieves irrelevant or incomplete information.

### Grounding Risk

The response is not adequately supported by source information.

### Performance Risk

The system takes too long to respond.

### Integration Risk

AI components do not work correctly with the surrounding application.

### Scalability Risk

The solution performs well for a small test group but fails under larger usage.

### Security Risk

Sensitive information is exposed or accessed by unauthorized users.

---

## What The PM Needs To Know

The AI Project Manager should be able to answer:

* What does each major component do?
* Why is it needed?
* What does it depend on?
* What could fail?
* How will we know if it works?
* Who owns the component?
* What business requirement does it support?
* What happens if it fails?

The PM does **not** need to:

* Train complex models from scratch.
* Develop advanced machine-learning algorithms.
* Build production infrastructure.
* Perform advanced mathematical model optimization.

The PM needs enough technical understanding to manage the project responsibly.

---

## Practical Exercise 5: Evaluate An AI Technology Architecture

### Scenario

A company plans to build an internal AI knowledge assistant.

The proposed architecture is:

**Employees**

↓

**Web Application**

↓

**Document Search**

↓

**Vector Database**

↓

**Large Language Model**

↓

**Generated Answer**

Leadership claims:

> "Because we are using a powerful LLM, the system will automatically provide accurate answers."

The technical team also states:

> "The vector database guarantees that the correct information will always be retrieved."

The security team has not yet reviewed the architecture.

### Part 1: Explain The Architecture

Explain the purpose of each major component.

Identify what is missing from the proposed architecture.

### Part 2: Challenge The Claims

Evaluate the two leadership/technical claims.

For each claim, identify:

* What is assumed.
* What evidence is needed.
* What risk exists if the assumption is wrong.

### Part 3: Identify Dependencies

Identify at least **five technical or project dependencies**.

### Part 4: Identify Risks

Identify at least **five AI project risks**.

Classify each risk as:

* Data
* Model
* Retrieval
* Security
* Performance
* Integration
* Governance
* Other

### Part 5: Define Evidence

Identify the evidence you would require before approving the architecture for development.

### Part 6: PM Decision

Decide whether the project should:

* Proceed
* Proceed With Conditions
* Hold

Support your decision using:

1. **Evidence**
2. **Risks**
3. **Dependencies**
4. **Stakeholders**
5. **Required Actions**

---

## PM Decision

The technical lead tells you:

> "We don't need extensive evaluation yet. We can test everything after development is complete."

As the AI Project Manager, decide whether this approach is appropriate.

Consider:

* Cost of discovering problems late.
* Technical dependencies.
* Requirements.
* Security.
* Data quality.
* Model performance.
* User expectations.
* Release risk.

Your decision should explain **when evaluation should occur and why.**

---

## Artifact / Output

Create an **AI Technology Architecture Assessment** containing:

* System components
* Component responsibilities
* Dependencies
* Technical assumptions
* Risks
* Evidence requirements
* Security considerations
* Performance considerations
* Evaluation considerations
* PM recommendation

The artifact should demonstrate that you can manage an AI project without needing to become the technical implementer.

---

## Decision / Reflection

Answer the following:

1. Why is an AI model not the same thing as an AI product?
2. Why does the PM need to understand retrieval and grounding?
3. Why should technical claims be supported by measurable evidence?
4. What risks arise when technology is selected before requirements are understood?
5. When should technical evaluation begin?
6. What technical decisions should require business or security stakeholder involvement?

---

## Key Takeaways

* AI Project Managers need technical literacy, not necessarily engineering expertise.
* AI systems are made up of multiple interconnected components.
* A model is only one part of an AI product.
* Embeddings support semantic search.
* Vector databases support similarity-based retrieval.
* Retrieval-Augmented Generation allows AI systems to use external knowledge.
* Grounding connects AI responses to evidence.
* Hallucination is a significant AI project risk.
* Model selection should be based on requirements and constraints.
* Local and cloud architectures create different project risks and tradeoffs.
* Technical claims should be validated with evidence.
* Evaluation should begin early rather than waiting until the end of development.

---

## Connection To Capstone

The technical concepts from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will analyze and manage an architecture involving:

**Documents → Chunking → Embeddings → Vector Database → Retrieval → Large Language Model → Grounding / Citation → Application**

You will focus on understanding the purpose, dependencies, risks, evaluation requirements, and project-management implications of each component rather than becoming responsible for advanced AI engineering.

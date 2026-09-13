# Milestone 5 — AI Architecture

## PM Objective

Understand how the major components of an Artificial Intelligence (AI) solution work together and identify the project management decisions, dependencies, risks, and trade-offs associated with them.

You are not expected to become an AI engineer. Your goal is to understand the solution well enough to manage requirements, risks, quality, delivery, and stakeholder expectations.

## Hands-On Objective

Trace how an employee's question moves through PolicyAssist from the initial request to the final response.

By the end of this milestone, you should be able to explain the AI solution at a high level and identify what a Project Manager (PM) needs to manage at each stage.

---

## Section 1: Start With the User Request

Think about what happens when an employee asks:

> "How many paid time off days do I receive each year?"

The employee sees a simple question-and-answer experience, but several components work behind the scenes before the answer is produced.

Your task is to understand that flow.

A simplified PolicyAssist flow is:

**Employee Question → User Interface → Document Processing/Data → Embeddings → Vector Database → Retrieval → Large Language Model → Grounded Response → Citation → Employee**

Do not focus on writing code. Focus on understanding what each stage does and why it matters to the product.

---

## Section 2: Understand the Major Components

### 1. User Interface (UI)

The User Interface is the part of the product the employee interacts with.

For PolicyAssist, this is where the employee:

* Enters a policy question
* Submits the question
* Reviews the response
* Reviews supporting policy information or citations
* Receives an escalation when the system cannot provide a reliable answer

**PM consideration:** Is the experience clear, usable, and appropriate for the intended employee?

---

### 2. Policy Documents

Policy documents are the authoritative information the AI solution is expected to use.

Examples include:

* Employee leave policies
* Information security policies
* Remote work policies
* Code of conduct policies
* Expense policies

The Large Language Model (LLM) should not be treated as the source of truth. The approved policy content is the source of truth.

**PM consideration:** Are employees receiving information from the correct and current policy source?

---

### 3. Document Processing

Before policy information can be retrieved effectively, documents must be prepared for use by the AI system.

Document processing may include:

* Reading documents
* Extracting text
* Breaking content into smaller sections
* Preparing content for retrieval
* Preserving useful document information such as policy names or versions

**PM consideration:** Could errors during document processing cause information to be missing, incomplete, or difficult to retrieve?

---

### 4. Embeddings

An embedding is a numerical representation of text that captures aspects of its meaning.

Embeddings allow the system to compare a user's question with stored policy content based on semantic similarity rather than relying only on exact words.

For example, an employee might ask:

> "How much vacation time do I get?"

while the policy may use the term:

> "Paid Time Off."

The system can use semantic similarity to help connect the question with the relevant policy content.

**PM consideration:** Is the retrieval approach capable of finding relevant information when employees use different wording?

---

### 5. Vector Database

A vector database stores embeddings so that the system can efficiently search for content that is semantically similar to a user's question.

For PolicyAssist, the vector database supports the retrieval process by helping identify potentially relevant sections of policy documents.

**PM consideration:** Is the correct content stored, available, and retrievable?

---

### 6. Retrieval

Retrieval is the process of finding relevant policy content based on the employee's question.

For example:

**Employee question:**
"How many sick days do I get?"

**Retrieved content:**
The section of the approved leave policy describing sick leave.

Retrieval is critical because the quality of the final response depends heavily on whether the system finds the right evidence.

**PM consideration:** Is the system consistently retrieving the most relevant and authoritative information?

---

### 7. Large Language Model (LLM)

A Large Language Model (LLM) generates the natural-language response that the employee sees.

The LLM uses the retrieved information to formulate an answer.

The LLM should not be treated as an independent source of policy information.

**PM consideration:** Does the LLM produce an answer that is supported by the retrieved evidence rather than inventing information?

---

### 8. Grounding

Grounding means connecting the AI-generated response to trusted information provided by the system.

For PolicyAssist, the response should be grounded in approved policy content.

Grounding helps reduce unsupported or fabricated answers.

**PM consideration:** Can you demonstrate that responses are based on authoritative policy information?

---

### 9. Citations

Citations help the employee understand where the answer came from.

A citation may identify information such as:

* Policy name
* Policy version
* Relevant document
* Supporting policy section

Citations also provide an important quality and governance mechanism because they allow the response to be checked against its source.

**PM consideration:** Are citations present, accurate, and connected to the information used in the response?

---

## Section 3: Trace the End-to-End Flow

Choose a realistic PolicyAssist question and trace what happens from the employee's question to the final answer.

Complete the following:

| Stage                | What Happens? | PM Concern |
| -------------------- | ------------- | ---------- |
| User Question        |               |            |
| User Interface       |               |            |
| Document/Data        |               |            |
| Embeddings           |               |            |
| Vector Database      |               |            |
| Retrieval            |               |            |
| Large Language Model |               |            |
| Grounding            |               |            |
| Citation/Response    |               |            |

Your objective is not to describe technical implementation details.

Your objective is to understand the **product flow and management implications**.

---

## Section 4: Identify Dependencies

Architecture components do not operate independently.

Identify at least **three dependencies** in the PolicyAssist solution.

Consider questions such as:

* What must exist before retrieval can work?
* What happens if policy documents are not processed correctly?
* What happens if the vector database contains outdated information?
* What happens if retrieval returns irrelevant content?
* What happens if the LLM receives poor or incomplete evidence?
* What happens if citations do not match the information presented?

Document your dependencies using:

| Dependency | Components Involved | Why It Matters | Potential Impact |
| ---------- | ------------------- | -------------- | ---------------- |
|            |                     |                |                  |
|            |                     |                |                  |
|            |                     |                |                  |

---

## Section 5: Identify AI and Technical Risks

Identify at least **three risks** that could affect the PolicyAssist solution.

Include at least one risk related to AI response quality.

Consider:

* Incorrect retrieval
* Outdated policy content
* Hallucination or unsupported responses
* Missing citations
* Poor document processing
* Slow response times
* Security or authorization failures
* Incorrect policy version
* System availability
* Incomplete source content

For each risk, identify:

| Risk | Cause | Potential Impact | Mitigation | PM Decision Needed |
| ---- | ----- | ---------------- | ---------- | ------------------ |
|      |       |                  |            |                    |
|      |       |                  |            |                    |
|      |       |                  |            |                    |

---

## Section 6: Identify Architecture Trade-Offs

AI products often involve trade-offs rather than perfect solutions.

Consider at least **two** trade-offs.

Examples:

* Retrieval quality vs. response speed
* More retrieved content vs. more irrelevant content
* Simplicity vs. advanced functionality
* Automation vs. human escalation
* Broader access vs. tighter authorization
* Faster delivery vs. additional testing
* More AI functionality vs. greater governance risk

For each trade-off, document:

| Trade-Off | Option A | Option B | Business Impact | PM Decision |
| --------- | -------- | -------- | --------------- | ----------- |
|           |          |          |                 |             |
|           |          |          |                 |             |

---

## Section 7: Make a PM Architecture Decision

Choose at least **one architecture-related decision** that a PM would need to make.

Examples include:

* What information should be available to the AI?
* What sources are considered authoritative?
* What happens when retrieval confidence is low?
* When should the system escalate to Human Resources?
* What quality threshold must retrieval meet?
* What happens when a policy is outdated?
* What information should be included in citations?
* What security controls must be in place before release?

Document:

**Decision:**
[Your decision]

**Why it matters:**
[Business or user impact]

**Evidence needed:**
[What information would help you make or validate the decision]

**Risk if the decision is wrong:**
[Potential consequence]

---

## Section 8: Create Your AI Solution Architecture Summary

Create either:

1. A simple architecture diagram, or
2. A one-page architecture summary.

Your architecture should show the major flow:

**Employee → User Interface → Policy Content → Processing → Embeddings/Vector Database → Retrieval → Large Language Model → Grounded Response → Citation → Employee**

For each major component, document:

* Purpose
* PM concern
* Dependency
* Risk

Keep the architecture at a level appropriate for a Project Manager. You do not need to provide source code or detailed engineering specifications.

---

## Deliverable: AI Solution Architecture Summary

Submit an **AI Solution Architecture Summary** containing:

* End-to-end AI solution flow
* Major components and their purposes
* Component dependencies
* At least three technical or AI risks
* At least two architecture trade-offs
* At least one PM architecture decision
* Architecture diagram or one-page architecture summary
* PM concerns for each major component

---

## PM Checkpoint

Before moving forward, you should be able to answer:

> **How does PolicyAssist work at a high level, and what does the PM need to manage at each stage?**

You should also be able to explain:

* Why the policy documents are the source of truth
* What embeddings are used for
* Why a vector database is needed
* What retrieval does
* What role the Large Language Model plays
* Why grounding matters
* Why citations matter
* Where AI quality risks can occur
* Where security and authorization risks can occur
* What architecture decisions require PM involvement

---

## PM Perspective

**You do not need to build the AI architecture to manage it. You need to understand how the pieces connect, where value is created, where risk enters the system, and which decisions require PM attention.**

The progression is:

**Requirement → Product Capability → Architecture → Dependencies → Risks → PM Decisions**

The next milestone will focus on the data and retrieval layer, where the quality of the information available to the AI becomes critical to the quality of the final response.

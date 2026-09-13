# Milestone 6 — Data & Retrieval

## PM Objective

Understand how data quality, document authority, versioning, metadata, and retrieval affect the performance and trustworthiness of an Artificial Intelligence (AI) product.

## Hands-On Objective

Evaluate how PolicyAssist finds information and determine whether the information retrieved is relevant, authoritative, current, and appropriate for the employee's question.

---

## Section 1: Start With the Source of Truth

PolicyAssist is designed to answer questions using approved policy information.

The Large Language Model (LLM) is not the source of truth.

The policy content is the source of truth.

This creates an important Product Management (PM) question:

> **What information should the AI be allowed to use when answering an employee?**

Identify the policy sources available to your PolicyAssist application.

For each source, identify:

| Source | Policy Area | Authority | Current Version | Status |
| ------ | ----------- | --------- | --------------- | ------ |
|        |             |           |                 |        |
|        |             |           |                 |        |
|        |             |           |                 |        |

Consider:

* Who owns the policy?
* Is the source approved?
* Is it current?
* Is the version identifiable?
* Could another document conflict with it?
* Should the AI be allowed to use it?

---

## Section 2: Understand Document Authority

Not every document should be treated equally.

Consider these examples:

* An approved Human Resources policy
* An outdated policy
* An employee-created document
* A draft policy
* A duplicate policy
* An unofficial FAQ

If the AI retrieves an unofficial or outdated document, the response could appear reasonable while still being wrong.

Determine which sources should be considered authoritative for PolicyAssist.

Document:

**Authoritative source:**
[Your answer]

**Why it is authoritative:**
[Your answer]

**Sources that should not be treated as authoritative:**
[Your answer]

**Risk if an unauthorized source is used:**
[Your answer]

---

## Section 3: Evaluate Version and Status

Policy information can change.

A policy may have:

* A version number
* An effective date
* An approval status
* An expiration or review date
* An owner

Test at least **three policy sources** and record the information you can identify.

| Policy | Version | Effective Date | Status | Owner/Authority Identified? |
| ------ | ------- | -------------- | ------ | --------------------------- |
|        |         |                |        |                             |
|        |         |                |        |                             |
|        |         |                |        |                             |

Then answer:

> **What could happen if PolicyAssist retrieves an older version of a policy?**

Document the potential business and employee impact.

---

## Section 4: Test Retrieval

Now test how PolicyAssist retrieves information.

Ask at least **five questions**.

Use a mixture of questions, including:

1. A straightforward policy question
2. A question using different wording from the policy
3. A question requiring a specific policy detail
4. A question where multiple policies could appear relevant
5. A question the system should not be able to answer from the available policies

For each question, record:

| Question | Expected Policy/Source | Retrieved Information | Relevant? | Correct? | Citation Present? |
| -------- | ---------------------- | --------------------- | --------- | -------- | ----------------- |
|          |                        |                       |           |          |                   |
|          |                        |                       |           |          |                   |
|          |                        |                       |           |          |                   |
|          |                        |                       |           |          |                   |
|          |                        |                       |           |          |                   |

Do not evaluate only whether the application produced an answer.

Evaluate whether it found the **right evidence**.

---

## Section 5: Evaluate Retrieval Quality

For each test, ask:

### Relevance

Did the retrieved information actually relate to the employee's question?

### Authority

Did the information come from an approved source?

### Currency

Was the information from the correct and current version?

### Completeness

Did the retrieved information contain enough information to support the answer?

### Accuracy

Did the final answer correctly represent the retrieved information?

### Citation

Could the employee identify where the answer came from?

Record any problems you find.

| Test | Issue | Likely Cause | Business Impact |
| ---- | ----- | ------------ | --------------- |
|      |       |              |                 |
|      |       |              |                 |
|      |       |              |                 |

---

## Section 6: Look for Retrieval Failure

A retrieval failure occurs when the system does not retrieve the information needed to answer the question correctly.

Examples include:

* The relevant policy was not retrieved.
* An unrelated policy was retrieved.
* An outdated policy was retrieved.
* Multiple conflicting sources were retrieved.
* The retrieved content was incomplete.
* The correct policy was retrieved, but the response did not use it correctly.

Identify at least **two retrieval failures or weaknesses** from your testing.

For each one, document:

**What happened:**
[Your observation]

**Why it matters:**
[Business/user impact]

**Possible cause:**
[Your hypothesis]

**Recommended action:**
[Your recommendation]

---

## Section 7: Evaluate Metadata

Metadata is information that describes the source content.

Examples include:

* Policy name
* Policy identifier
* Version
* Effective date
* Status
* Department or owner
* Review date
* Access classification

Metadata can help the system and the people managing it determine which content should be retrieved and trusted.

Evaluate the available metadata for the policy sources you tested.

| Metadata Field | Present? | Reliable? | Why It Matters |
| -------------- | -------- | --------- | -------------- |
| Policy Name    |          |           |                |
| Policy ID      |          |           |                |
| Version        |          |           |                |
| Effective Date |          |           |                |
| Status         |          |           |                |
| Owner          |          |           |                |
| Review Date    |          |           |                |

Then answer:

> **Which missing or unreliable metadata could create the greatest risk for PolicyAssist?**

Explain why.

---

## Section 8: Consider Conflicting Information

Imagine two documents contain different answers to the same policy question.

For example:

* Document A says employees receive 20 days of Paid Time Off.
* Document B says employees receive 15 days.
* Both documents appear in the system.

The AI may retrieve the wrong document or combine information from both.

Determine how PolicyAssist should handle conflicting information.

Consider:

* Version
* Effective date
* Approval status
* Policy owner
* Document authority
* Human escalation

Document your decision:

**How should conflicting policy information be handled?**

[Your answer]

**What evidence should determine which source is authoritative?**

[Your answer]

**When should the AI escalate instead of answering?**

[Your answer]

---

## Section 9: Consider Access and Permissions

Not all information should necessarily be available to every employee.

Consider whether PolicyAssist could accidentally retrieve information that a user should not be authorized to access.

Identify at least **one authorization or access risk**.

Document:

| Risk | Who Could Be Affected? | Potential Impact | Required Control |
| ---- | ---------------------- | ---------------- | ---------------- |
|      |                        |                  |                  |

Remember:

> **A technically correct answer can still be an unacceptable product response if the user was not authorized to receive the information.**

---

## Section 10: Make PM Decisions

Based on your testing, identify at least **three PM decisions or recommendations**.

Examples include:

* Require current policy versions before ingestion.
* Require policy ownership and approval metadata.
* Remove outdated documents from the retrieval source.
* Improve retrieval testing.
* Add stronger citation requirements.
* Establish a policy review process.
* Require human escalation when authoritative evidence is unavailable.
* Add authorization controls.
* Improve document organization or metadata.

For each decision, document:

| Decision/Recommendation | Evidence | Business Reason | Risk Addressed | Expected Outcome |
| ----------------------- | -------- | --------------- | -------------- | ---------------- |
|                         |          |                 |                |                  |
|                         |          |                 |                |                  |
|                         |          |                 |                |                  |

---

## Deliverable: Data & Retrieval Assessment

Create a **Data & Retrieval Assessment** containing:

* Policy source inventory
* Authority assessment
* Version and status assessment
* Results from at least five retrieval tests
* Retrieval quality assessment
* At least two retrieval or data-quality issues
* Metadata assessment
* Conflicting-information assessment
* Access/authorization risk
* At least three PM decisions or recommendations

Your assessment should be based on **observed evidence from testing**, not assumptions about how the system should work.

---

## PM Checkpoint

Before moving forward, you should be able to answer:

> **How can poor data, outdated information, or incorrect retrieval affect the AI product, and what can the PM do about it?**

You should also be able to explain:

* Why the source of truth matters
* Why document authority matters
* Why versioning matters
* Why metadata matters
* How retrieval quality affects AI response quality
* How conflicting information can create risk
* Why authorization must be considered during retrieval
* When an AI product should answer versus escalate
* What evidence supports your recommended improvements

---

## PM Perspective

**AI quality begins before the AI generates an answer.**

If the system retrieves the wrong information, an impressive-looking response can still be wrong.

The progression is:

**Authoritative Data → Quality Data → Retrieval → Evidence → Grounded Response → User Trust**

Your role as a PM is to make sure the product is designed and evaluated around that entire chain, not just the final response.

The next milestone will focus on **AI evaluation**, where you will use evidence and measurable criteria to determine whether the product is performing well enough for its intended use.

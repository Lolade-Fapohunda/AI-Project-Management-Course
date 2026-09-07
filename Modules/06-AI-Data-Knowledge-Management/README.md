# Module 6: AI Data & Knowledge Management

## Purpose

Data is one of the most important components of an AI project.

An AI system can have a strong model and well-designed application, but poor, incomplete, outdated, or unauthorized data can still produce unreliable results.

This module teaches the AI Project Manager how to manage data readiness, knowledge sources, ownership, quality, authority, access, and governance.

The goal is not to make the PM a data engineer.

The goal is to ensure that the data supporting the AI product is **usable, trustworthy, governed, and fit for purpose**.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain why data quality affects AI project outcomes.
* Distinguish between structured and unstructured data.
* Evaluate data readiness before development.
* Identify data owners and sources of authority.
* Understand metadata and version control.
* Identify duplicate, outdated, conflicting, and incomplete information.
* Understand document ingestion and preprocessing.
* Explain chunking and embeddings at a project-management level.
* Identify data-access and privacy risks.
* Establish data-quality acceptance criteria.
* Make project decisions based on data readiness.

---

## Why Data Matters In AI Projects

AI systems depend on information.

If the underlying information is:

* Incorrect
* Incomplete
* Outdated
* Duplicated
* Conflicting
* Poorly structured
* Unauthorized
* Inaccessible

the AI system may produce unreliable results.

This creates an important PM principle:

> **AI quality cannot consistently exceed the quality and governance of the information supporting it.**

The PM must therefore treat data as a project dependency rather than an afterthought.

---

## Types Of AI Data

AI projects may use many types of data.

### Structured Data

Data organized into predictable fields and tables.

Examples:

* Customer records
* Transaction databases
* Employee records
* Inventory systems

### Unstructured Data

Information without a fixed tabular structure.

Examples:

* PDFs
* Documents
* Emails
* Images
* Audio
* Video
* Web pages

### Semi-Structured Data

Data that has some organizational structure but does not follow a traditional database table.

Examples:

* JSON
* XML
* Application logs
* Tagged documents

The type of data affects how it must be processed and managed.

---

## Data Readiness

Before AI development begins, the PM should determine whether the required data is ready.

A useful readiness assessment considers:

* Availability
* Accuracy
* Completeness
* Relevance
* Currency
* Authority
* Approval
* Accessibility
* Metadata
* Security
* Ownership

### Data Readiness Principle

A data source should not automatically be considered usable simply because it exists.

The PM must ask:

> "Is this information approved, reliable, current, authorized, and appropriate for this use case?"

---

## Data Ownership

Every important data source should have an identified owner.

The owner may be responsible for:

* Accuracy
* Approval
* Updates
* Version control
* Access decisions
* Retention
* Governance

Without ownership, the project may have no clear authority for resolving data problems.

---

## Source Of Truth

A source of truth is the authoritative source that should be relied upon for a particular piece of information.

Organizations frequently have multiple copies of the same information.

For example:

* A document repository contains Version 3.
* An employee has a saved copy of Version 2.
* An email contains language from Version 1.
* A shared folder contains an unapproved draft.

The existence of multiple documents does not mean they are equally authoritative.

The PM must establish which source controls.

---

## Authority And Versioning

AI knowledge systems must account for document status and version.

Possible statuses include:

* Draft
* Pending Approval
* Active
* Superseded
* Archived
* Expired
* Unverified

The project should establish rules for determining which information is eligible for use.

### Example

If Version 3 is approved and active while Version 2 is superseded:

**Version 3 → Eligible**

**Version 2 → Not Eligible**

The system should not simply select whichever document happens to be retrieved first.

---

## Conflicting Information

One of the most important data-governance problems is conflicting information.

Consider:

**Document A**

> Remote employees may work remotely three days per week.

**Document B**

> Remote employees may work remotely two days per week.

If the project cannot establish which document is authoritative, the AI system should not automatically choose one.

### PM Rule

> **When authority cannot be established, stop automatic selection and escalate for human resolution.**

This protects the project from turning unresolved organizational ambiguity into an incorrect AI answer.

---

## Metadata

Metadata is information that describes a data source.

For a document, useful metadata may include:

* Document ID
* Document name
* Owner
* Department
* Version
* Effective date
* Status
* Approval status
* Document type
* Audience
* Access classification

Metadata allows systems and project teams to understand what a document is and whether it should be used.

---

## Data Quality

Data quality can be evaluated across several dimensions.

| Dimension        | Question                                    |
| ---------------- | ------------------------------------------- |
| **Accuracy**     | Is the information correct?                 |
| **Completeness** | Is required information missing?            |
| **Consistency**  | Does information conflict across sources?   |
| **Currency**     | Is the information current?                 |
| **Relevance**    | Does it support the intended use case?      |
| **Validity**     | Does it meet required rules or formats?     |
| **Uniqueness**   | Are duplicate records or documents present? |

The PM should establish which dimensions matter most for the project.

---

## Duplicate Information

Duplicate information can create unexpected AI behavior.

For example, the same policy may exist:

* In a document repository.
* In a shared drive.
* In an email attachment.
* In an employee portal.
* In an outdated project folder.

If the system treats all copies as equally valid, retrieval may return conflicting information.

The solution is not necessarily to delete every duplicate.

Instead, the project should establish:

* Which repository is authoritative.
* Which documents are eligible.
* How duplicates are identified.
* How outdated copies are handled.

---

## Document Ingestion

Document ingestion is the process of bringing information into an AI system so that it can be processed and searched.

A simplified workflow is:

**Source Documents**

↓

**Document Validation**

↓

**Text Extraction**

↓

**Cleaning / Normalization**

↓

**Metadata Validation**

↓

**Chunking**

↓

**Embeddings**

↓

**Knowledge Store**

The exact implementation may vary.

The PM is responsible for ensuring the workflow supports the requirements.

---

## Scanned Documents

Some organizational documents are scanned images rather than machine-readable text.

A system may therefore require Optical Character Recognition (OCR) to extract usable text.

Potential OCR problems include:

* Missing text
* Incorrect characters
* Formatting errors
* Tables being misread
* Headers being lost
* Footnotes being omitted

The PM should include scanned-document handling in data-readiness and testing requirements when applicable.

---

## Chunking

Chunking divides large documents into smaller pieces that can be processed and retrieved more effectively.

For example:

**100-page document**

↓

**Sections**

↓

**Smaller text chunks**

↓

**Embeddings**

↓

**Searchable knowledge**

Poor chunking can create retrieval problems.

If chunks are too large:

* Retrieval may include excessive irrelevant information.

If chunks are too small:

* Important context may be separated.

The PM does not need to determine the mathematical optimization of chunk size but should ensure that chunking is evaluated as part of system quality.

---

## Embeddings And Semantic Search

Embeddings convert information into numerical representations that capture semantic relationships.

This allows a system to identify conceptually similar information even when the wording differs.

For example:

> "How long can an employee work remotely?"

may retrieve information from a document containing:

> "Employees may perform their duties from an approved remote location for up to three days per week."

The wording differs, but the meaning is related.

---

## Knowledge Base Governance

A knowledge base should have defined governance.

The PM should establish:

* Who owns the information.
* Who approves updates.
* How versions are tracked.
* How outdated content is removed or excluded.
* How conflicts are resolved.
* Who can access information.
* How changes are documented.
* How data quality is monitored.

Without governance, the knowledge base can become unreliable over time.

---

## Access And Data Security

Not every user should necessarily have access to every piece of information.

The PM should consider:

* User roles
* Authorization
* Confidential information
* Personally Identifiable Information (PII)
* Sensitive business information
* Department restrictions
* Data retention
* Audit requirements

A system should not retrieve information for a user simply because that information exists in the knowledge base.

### Key Principle

> **Retrieval eligibility and user access eligibility are separate controls.**

Information may be authoritative and active but still restricted to certain users.

---

## Data Lifecycle

Data should be managed throughout its lifecycle.

A simplified lifecycle is:

**Create**

↓

**Approve**

↓

**Store**

↓

**Use**

↓

**Update**

↓

**Supersede**

↓

**Archive / Retain**

The PM should determine which lifecycle events affect AI availability.

For example, when a policy becomes superseded, the system should no longer treat it as an authoritative active source.

---

## Data Change Management

Changes to source information can affect AI behavior.

A new version of a document may require:

* Validation
* Approval
* Re-ingestion
* Metadata updates
* Re-indexing
* Evaluation
* UAT
* Release approval

The PM should therefore connect data changes to the broader change-management process.

---

## Data Quality Acceptance Criteria

Data requirements should be measurable.

Weak:

> The knowledge base should contain good documents.

Better:

> All documents designated for production use must have an identified owner, approved status, current version, effective date, and required metadata before being made available to the AI system.

Good acceptance criteria make data readiness testable.

---

## Data Risks

Common AI data risks include:

### Outdated Data

The system uses information that is no longer current.

### Conflicting Data

Multiple sources contain different information.

### Missing Data

Required information is unavailable.

### Poor Extraction

Information is incorrectly extracted from source documents.

### Unauthorized Data

Information is used without appropriate authorization.

### Poor Metadata

The system cannot reliably determine the status or ownership of information.

### Duplicate Data

Multiple versions create retrieval ambiguity.

### Data Drift

The underlying information changes over time and the AI system is not updated accordingly.

---

## Practical Exercise 6: Evaluate AI Data Readiness

### Scenario

An organization wants to build an AI assistant using an internal knowledge repository.

The repository contains:

* 4,000 documents.
* Multiple copies of many documents.
* Draft documents.
* Archived documents.
* Current documents.
* Documents with missing owners.
* Documents with inconsistent version numbers.
* Several scanned PDFs.
* Documents containing confidential information.

Leadership says:

> "We already have thousands of documents, so the data is ready."

### Part 1: Define Readiness

Create a data-readiness checklist.

Identify the conditions that must be satisfied before information can be used by the AI system.

### Part 2: Identify Problems

Identify at least **eight data risks or quality problems** in the scenario.

For each, explain the potential impact on the AI project.

### Part 3: Establish Authority

Define how the project should determine which document is authoritative.

Include:

* Owner
* Approval
* Status
* Version
* Effective date
* Conflict resolution

### Part 4: Define Metadata

Identify the metadata that should be required for production documents.

### Part 5: Access Control

Identify at least three situations where a document may be authoritative but still should not be available to every user.

### Part 6: PM Decision

Decide whether the project should:

* Proceed
* Proceed With Conditions
* Hold

Support your decision using:

1. **Evidence**
2. **Data Risks**
3. **Dependencies**
4. **Stakeholders**
5. **Required Actions**

---

## PM Decision

The project sponsor says:

> "We cannot spend months cleaning the data. Just ingest everything and let the AI figure out which documents are correct."

As the AI Project Manager, decide how you would respond.

Your decision should address:

* Data quality
* Authority
* Security
* AI reliability
* Project schedule
* Business risk
* Minimum readiness criteria

Explain what data can proceed and what data should be placed on hold.

---

## Artifact / Output

Create a **Data Readiness & Knowledge Governance Assessment** containing:

* Data inventory
* Data owners
* Source-of-truth rules
* Required metadata
* Data-quality criteria
* Authority rules
* Versioning rules
* Access considerations
* Conflict-resolution process
* Data risks
* Readiness decision

The artifact should demonstrate that you can determine whether information is fit for use before allowing it to become part of an AI product.

---

## Decision / Reflection

Answer the following:

1. Why is having a large amount of data not the same as having good data?
2. Why is source authority important for AI systems?
3. What should happen when two sources conflict and authority cannot be established?
4. Why should metadata be treated as a project requirement?
5. How can outdated information affect AI responses?
6. Why should data access be considered separately from data quality?
7. When should a PM place data on hold rather than allowing it into the system?

---

## Key Takeaways

* Data readiness is a prerequisite for reliable AI.
* Data must be evaluated for accuracy, completeness, relevance, currency, and authority.
* Every important data source should have an owner.
* A source of truth must be established before conflicting information is used.
* Metadata helps determine whether information is valid and eligible.
* Draft, superseded, archived, or unverified information should not automatically become AI knowledge.
* Scanned documents may require additional processing such as OCR.
* Chunking and embeddings affect retrieval quality.
* Authoritative information may still require access restrictions.
* Data governance must continue throughout the AI product lifecycle.
* Conflicting information should be escalated rather than resolved through guesswork.
* Data-quality requirements should be measurable and testable.

---

## Connection To Capstone

The data and knowledge-management principles from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will establish:

* Policy ownership
* Authority
* Approval
* Versioning
* Effective dates
* Policy status
* Required metadata
* Retrieval eligibility
* Conflict handling
* Access considerations

The capstone will apply the principle:

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

If authority cannot be established, the policy should be held for human resolution rather than automatically used by the AI system.

## Module Completion Checklist

Before moving to Module 7, confirm that you can:

* [ ] Explain why data quality affects AI project outcomes.
* [ ] Assess whether data is ready for AI use.
* [ ] Identify data owners and authoritative sources.
* [ ] Evaluate document status, version, approval, and metadata.
* [ ] Identify duplicate, outdated, incomplete, and conflicting information.
* [ ] Explain document ingestion, chunking, and embeddings at a PM level.
* [ ] Identify data-access and security risks.
* [ ] Define measurable data-quality acceptance criteria.
* [ ] Make a **Proceed, Proceed With Conditions, or Hold** decision based on evidence.
* [ ] Complete the **Data Readiness & Knowledge Governance Assessment**.

**Module Complete When:** You can confidently determine whether information is trustworthy, governed, authorized, and ready to support an AI product.


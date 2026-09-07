# 05: Data Governance Decision

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Decision Area:** Data Readiness & Knowledge Governance

---

## Purpose

This artifact demonstrates how data was evaluated before being treated as usable AI knowledge.

The Project Manager's responsibility is not to clean every document personally.

The responsibility is to establish whether information is:

* Available
* Relevant
* Accurate
* Current
* Authoritative
* Approved
* Properly identified
* Secure
* Accessible to the appropriate users
* Suitable for the intended AI use

---

# Business Problem

PolicyAssist depends on internal policy documents to answer employee questions.

A large document collection does not automatically represent a reliable knowledge base.

Potential problems include:

* Multiple versions.
* Duplicate documents.
* Draft policies.
* Archived policies.
* Missing owners.
* Conflicting information.
* Missing metadata.
* Scanned documents.
* Restricted information.
* Outdated content.

If these problems are not controlled, the AI system may retrieve information that should not be used.

---

# Data Governance Principle

The project established the following eligibility rule:

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

A document that does not satisfy the required conditions should not automatically become AI knowledge.

---

# Data Lifecycle

Policy information is managed throughout its lifecycle.

```text
Create
  ↓
Review
  ↓
Approve
  ↓
Publish
  ↓
Use
  ↓
Update
  ↓
Supersede
  ↓
Archive / Retain
```

The AI system must respect the lifecycle status of the underlying information.

---

# Policy Data Inventory

The prototype knowledge base contains six policy documents.

| Policy                       | Owner                | Status | Version | Effective Date |
| ---------------------------- | -------------------- | ------ | ------- | -------------- |
| Employee Leave Policy        | Human Resources      | Active | 1.0     | 2026-01-01     |
| Remote Work Policy           | Human Resources      | Active | 1.0     | 2026-01-01     |
| Attendance Policy            | Human Resources      | Active | 1.0     | 2026-01-01     |
| Expense Reimbursement Policy | Finance              | Active | 1.0     | 2026-01-01     |
| Information Security Policy  | Information Security | Active | 1.0     | 2026-01-01     |
| Code Of Conduct Policy       | Human Resources      | Active | 1.0     | 2026-01-01     |

This inventory provides a controlled starting point for the prototype.

---

# Data Ownership

Each policy must have an accountable owner.

The owner is responsible for establishing or confirming:

* Accuracy.
* Approval.
* Current version.
* Effective date.
* Policy status.
* Authorized audience.
* Required updates.
* Resolution of policy questions.

The AI Project Manager should not independently declare a disputed policy to be authoritative.

---

# Source Of Truth

The project must establish the authoritative repository for each policy.

The existence of multiple copies does not mean every copy is equally valid.

For example:

```text
Approved Policy Repository
        ↓
Authoritative Version
        ↓
Eligible For AI Retrieval
```

while:

```text
Email Attachment
Shared Drive Copy
Personal Copy
Old Project Folder
        ↓
Requires Validation
```

A duplicate should not become authoritative simply because it is easier for the system to retrieve.

---

# Authority Rules

PolicyAssist must evaluate policy authority before using retrieved information.

A policy should be considered eligible only when the project can establish:

1. Identified owner.
2. Approved status.
3. Active status.
4. Valid version.
5. Effective date.
6. Required metadata.
7. Authoritative source.
8. Appropriate access classification.

---

# Policy Status

The system must distinguish between policy states.

| Status           | Retrieval Eligibility       |
| ---------------- | --------------------------- |
| Draft            | Not Eligible                |
| Pending Approval | Not Eligible                |
| Active           | Potentially Eligible        |
| Superseded       | Not Eligible                |
| Archived         | Not Eligible                |
| Expired          | Not Eligible                |
| Unverified       | Not Eligible                |
| Conflicting      | Not Eligible Until Resolved |

Active status alone does not automatically establish authority.

---

# Version Control

Each policy should have a clear version.

Example:

**Version 1.0 — Active**

**Version 2.0 — Active**

The project must know which version is currently authoritative.

When a new version replaces an older one:

```text
Old Version
    ↓
Superseded
    ↓
Excluded From Active Retrieval

New Version
    ↓
Approved + Active
    ↓
Eligible
```

---

# Effective Dates

Effective dates establish when a policy becomes applicable.

A document may exist in the repository but not yet be effective.

The project should therefore distinguish:

* Publication date.
* Approval date.
* Effective date.
* Supersession date.
* Archive date.

These dates may affect retrieval eligibility and response accuracy.

---

# Metadata Requirements

Production policy documents should contain required metadata.

Minimum fields include:

| Metadata              | Required |
| --------------------- | -------- |
| Policy ID             | Yes      |
| Policy Name           | Yes      |
| Owner                 | Yes      |
| Department            | Yes      |
| Version               | Yes      |
| Status                | Yes      |
| Effective Date        | Yes      |
| Approval Status       | Yes      |
| Document Type         | Yes      |
| Access Classification | Yes      |

Missing mandatory metadata should prevent production eligibility unless formally approved through governance.

---

# Data Quality Criteria

The project evaluates data across several dimensions.

### Accuracy

The policy content must represent the approved organizational requirement.

### Completeness

Required policy information must not be missing.

### Currency

The information must reflect the current approved policy.

### Consistency

The information must not conflict with the authoritative source.

### Relevance

The policy must support the intended AI use case.

### Validity

Metadata and document information must meet project rules.

### Uniqueness

Duplicate versions must be identified and dispositioned.

---

# Duplicate Data

Duplicate documents create retrieval risk.

For example, the same policy may exist in:

* An approved repository.
* A shared drive.
* An email attachment.
* A project folder.
* An employee portal.

The solution is not necessarily to delete every duplicate.

The project should determine:

* Which source is authoritative.
* Which copies are eligible.
* Which copies are outdated.
* Whether duplicates should be excluded.
* How duplicate status is documented.

---

# Conflicting Policies

Conflicting information creates a significant governance risk.

Example:

**Policy A**

> Employees may work remotely three days per week.

**Policy B**

> Employees may work remotely two days per week.

If the project cannot establish which policy is authoritative, PolicyAssist must not guess.

### Required Behavior

**Conflict Identified**

↓

**Automatic Selection Blocked**

↓

**Policy Owner / Governance Authority Reviews**

↓

**Conflict Resolved**

↓

**Approved Version Identified**

↓

**Knowledge Base Updated**

↓

**Revalidated**

This prevents unresolved organizational ambiguity from becoming an AI-generated answer.

---

# Scanned Documents

Some policy information may exist as scanned PDFs.

Scanned documents may require OCR before their content can be reliably processed.

Potential issues include:

* Incorrect characters.
* Missing text.
* Misread tables.
* Lost headings.
* Missing footnotes.
* Formatting errors.

The PM should require validation of extracted content before scanned documents are treated as reliable AI knowledge.

---

# Document Ingestion

The project follows a controlled ingestion process.

```text
Source Document
      ↓
Document Validation
      ↓
Metadata Validation
      ↓
Authority Validation
      ↓
Text Extraction
      ↓
Cleaning / Normalization
      ↓
Chunking
      ↓
Embeddings
      ↓
Knowledge Store
```

The ingestion process must not bypass authority and eligibility checks.

---

# Chunking

Documents are divided into smaller sections to support retrieval.

Poor chunking may:

* Separate important context.
* Return incomplete policy requirements.
* Include excessive irrelevant content.
* Reduce retrieval quality.

Chunking therefore becomes an evaluation consideration rather than simply a technical implementation detail.

---

# Embeddings

Embeddings represent text numerically so that semantically related information can be identified.

For PolicyAssist, embeddings support semantic retrieval of policy sections.

The PM does not need to design the mathematical model.

The PM does need to ensure that:

* The embedding approach supports the use case.
* Retrieval quality is evaluated.
* Changes are regression-tested.
* Model changes are documented.

---

# Access Governance

A policy can be authoritative and active while still being restricted.

Examples include:

1. A policy containing confidential employee information.
2. A policy restricted to a specific department.
3. A policy containing security-sensitive procedures.

Therefore:

> **Data quality and data access are separate controls.**

A document should not be exposed simply because it is relevant to the user's question.

---

# Security And Privacy

The project must consider:

* Authorization.
* Personally Identifiable Information (PII).
* Confidential information.
* Department restrictions.
* User roles.
* Retention.
* Audit requirements.
* Data exposure.

The system should apply authorization controls before displaying restricted policy information.

---

# Data Change Management

A material policy change can affect AI behavior.

A change may require:

1. Policy review.
2. Approval.
3. Metadata update.
4. Re-ingestion.
5. Re-indexing.
6. Retrieval testing.
7. AI evaluation.
8. Regression testing.
9. UAT where appropriate.
10. Release approval.

The Project Manager must connect policy changes to the overall change-management process.

---

# Data Readiness Acceptance Criteria

Before production, the project requires:

| Criterion                                              | Target |
| ------------------------------------------------------ | -----: |
| Eligible policies with required metadata               |   100% |
| Policies with validated authority and approval         |   100% |
| Draft policies available for retrieval                 |      0 |
| Superseded policies available for active retrieval     |      0 |
| Unverified policies available for retrieval            |      0 |
| Unresolved authority conflicts available for retrieval |      0 |
| Unauthorized policy access                             |      0 |
| Required data-readiness checks completed               |   100% |
| Material policy changes documented                     |   100% |
| Scanned documents validated                            |   100% |
| Duplicate documents dispositioned                      |   100% |

---

# Data Governance Release Gate

The data layer should not pass the production gate unless:

* [ ] All production policies have identified owners.
* [ ] Authority is established.
* [ ] Approval is confirmed.
* [ ] Current versions are identified.
* [ ] Effective dates are validated.
* [ ] Required metadata is present.
* [ ] Draft content is excluded.
* [ ] Superseded content is excluded.
* [ ] Unverified content is excluded.
* [ ] Conflicts are resolved.
* [ ] Scanned content is validated.
* [ ] Duplicates are dispositioned.
* [ ] Access restrictions are defined.
* [ ] Data changes are governed.
* [ ] Evidence is documented.

---

# Prototype Data Evidence

The prototype demonstrates a controlled data foundation.

The current policy library contains six active policy documents with metadata including:

* Policy ID.
* Policy name.
* Category.
* Owner.
* Effective date.
* Version.
* Status.
* Applicability.
* Document type.

The prototype also applies eligibility checks before policy content is used.

This demonstrates the intended governance model.

---

# Current Data Position

**Prototype Data Status:** Controlled and usable for continued MVP testing.

**Production Data Status:** Not yet approved.

Formal production readiness still requires validation of:

* Complete policy inventory.
* Authority.
* Approval.
* Versioning.
* Access controls.
* Duplicate disposition.
* Conflict handling.
* Scanned documents.
* Data-quality evidence.
* Governance approval.

---

# Data Governance Risks

| Risk                   | Potential Impact        | Required Response         |
| ---------------------- | ----------------------- | ------------------------- |
| Outdated Policy        | Incorrect response      | Exclude and update        |
| Conflicting Policy     | Incorrect guidance      | Human resolution          |
| Missing Owner          | No authority            | Assign owner              |
| Missing Metadata       | Eligibility uncertainty | Correct metadata          |
| Duplicate Policy       | Retrieval ambiguity     | Establish source of truth |
| Scanned Document Error | Incorrect extraction    | Validate OCR              |
| Unauthorized Data      | Security exposure       | Enforce access control    |
| Data Drift             | Increasing inaccuracy   | Monitor and revalidate    |

---

# PM Decision

The Project Manager should not accept the argument:

> "There are thousands of documents, so the data is ready."

Quantity is not readiness.

The correct PM question is:

> **"Can we demonstrate that the information is authoritative, approved, current, appropriately accessible, and fit for the intended AI use?"**

If the answer is no, the affected information should remain on hold.

---

# Portfolio Evidence

This artifact demonstrates the ability to:

* Assess AI data readiness.
* Establish data ownership.
* Define sources of truth.
* Control policy authority.
* Manage versions and status.
* Define required metadata.
* Identify data-quality risks.
* Govern document ingestion.
* Manage conflicting information.
* Separate data quality from access control.
* Establish measurable readiness criteria.
* Connect data changes to testing and release management.

---

# Key PM Judgment

The critical data-governance decision was to reject the assumption that **more documents automatically produce a better AI system**.

For PolicyAssist, the objective is not to ingest the maximum amount of information.

The objective is to make the **right information available under controlled conditions**.

---

# Final Data Governance Decision

**Decision:** Continue using the controlled policy dataset for MVP development and evaluation.

**Production Decision:** HOLD pending formal data-readiness evidence and governance approval.

Production data must satisfy:

> **Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

If authority cannot be established:

> **HOLD → Human Resolution → Validate → Re-ingest → Re-evaluate**

---

# Evidence Principle

> **Data is not production-ready because it exists. Data is production-ready when its quality, authority, access, governance, and eligibility can be demonstrated with evidence.**

# 06: Data Readiness & Knowledge Governance

## Purpose

This document defines how Petadel PolicyAssist AI will determine whether policy information is safe, authoritative, complete, and suitable for retrieval.

For an AI policy assistant, data governance is a core product requirement.

A technically functioning AI system can still provide incorrect answers if it retrieves:

* Outdated policies
* Draft policies
* Superseded policies
* Unapproved documents
* Duplicate documents
* Conflicting policies
* Incomplete documents
* Documents with missing metadata
* Information the user is not authorized to access

The Project Manager is responsible for ensuring that data governance requirements are defined, assigned, tested, and supported by evidence.

---

## 1. Data Governance Objective

The objective is to ensure that PolicyAssist retrieves and uses only policy information that is:

* Authoritative
* Active
* Approved
* Complete
* Properly identified
* Appropriate for the requesting user

### Core Governance Principle

> **The AI must never treat the most easily retrieved document as the source of truth.**

Authority must be established through governance rules and validated metadata.

---

## 2. Policy Data Lifecycle

Policy information follows a controlled lifecycle:

```text
Create
  ↓
Review
  ↓
Approve
  ↓
Publish
  ↓
Ingest
  ↓
Validate
  ↓
Retrieve
  ↓
Monitor
  ↓
Change / Replace
  ↓
Revalidate
  ↓
Archive / Supersede
```

A change to policy information may require re-ingestion, revalidation, evaluation, and approval.

---

## 3. Data Sources

Potential policy sources may include:

* Human Resources
* Finance
* Information Security
* Legal
* Compliance
* Operations
* Executive leadership
* Approved policy repositories
* Approved document-management systems

Not every document found in an organizational repository should automatically become eligible for retrieval.

---

## 4. Source Of Truth

Each policy must have an identified authoritative source.

The Project Manager should establish:

* Policy owner
* Authoritative repository
* Approval authority
* Effective date
* Version
* Status
* Applicability
* Document type

### Source Of Truth Rule

> **Only the approved authoritative source should be treated as the official source for policy responses.**

Copies, drafts, locally saved documents, emails, and unofficial versions should not automatically be treated as authoritative.

---

## 5. Policy Authority

Authority determines whether a policy can be trusted as an official source.

### Authority Questions

The project team should determine:

1. Who owns the policy?
2. Who approved it?
3. Where is the official version stored?
4. What is the current version?
5. When did it become effective?
6. Has it been superseded?
7. Does another authoritative document conflict with it?
8. Who has authority to resolve a conflict?

---

## 6. Data Readiness Rule

A policy is eligible for retrieval only when all mandatory criteria are satisfied.

```text
Active
+
Authoritative
+
Approved
+
Required Metadata Present
=
Eligible For Retrieval
```

### Mandatory Criteria

| Criterion             | Required |
| --------------------- | -------- |
| Policy ID             | Yes      |
| Policy name           | Yes      |
| Version               | Yes      |
| Status                | Yes      |
| Effective date        | Yes      |
| Policy owner          | Yes      |
| Authority established | Yes      |
| Approval established  | Yes      |

### Readiness Decision

| Result                            | Decision |
| --------------------------------- | -------- |
| All mandatory criteria pass       | Eligible |
| One or more criteria fail         | Hold     |
| Authority cannot be determined    | Hold     |
| Conflicting authoritative sources | Hold     |

### PM Rule

> **One mandatory data-readiness failure means the policy is not eligible for retrieval until the issue is resolved.**

---

## 7. Policy Status

Policy status must be explicitly maintained.

### Approved Active

Eligible for retrieval if all other requirements are satisfied.

### Draft

Not eligible for retrieval.

### Superseded

Not eligible for retrieval.

### Expired

Not eligible for retrieval unless formally reapproved and reactivated.

### Unverified

Not eligible for retrieval.

### Conflicting

Not eligible until authority is resolved.

---

## 8. Version Control

Every policy should have a unique version.

Example:

```text
Policy: Remote Work Policy
Version: 1.0
Effective Date: 2026-01-01
Status: Active
```

When a new version becomes effective:

1. New version is approved.
2. Previous version is identified as superseded.
3. Metadata is updated.
4. New version is ingested.
5. Retrieval eligibility is validated.
6. Evaluation is performed when required.
7. Previous version is removed from active retrieval.
8. Change is documented.

### Acceptance Criterion

**100% of active policies must have a valid version identifier and effective date.**

---

## 9. Metadata Requirements

Metadata allows PolicyAssist to determine whether information is eligible for retrieval.

### Required Metadata

| Metadata        | Purpose                         |
| --------------- | ------------------------------- |
| Policy ID       | Unique identification           |
| Policy name     | Human-readable identification   |
| Category        | Classification                  |
| Policy owner    | Accountability                  |
| Effective date  | Determines applicability        |
| Version         | Version control                 |
| Status          | Active/draft/superseded/etc.    |
| Applies to      | Audience                        |
| Document type   | Policy/procedure/guideline/etc. |
| Authority       | Establishes source legitimacy   |
| Approval status | Governance control              |

### Metadata Acceptance Criteria

* **100%** of eligible policies contain all mandatory metadata.
* **0** eligible policies may have missing Policy ID.
* **0** eligible policies may have missing version.
* **0** eligible policies may have missing status.
* **0** eligible policies may have missing effective date.
* **0** eligible policies may have missing policy owner.

---

## 10. Document Quality

Policy documents must be readable and usable by the ingestion process.

Data-quality checks should identify:

* Corrupted files
* Empty documents
* Missing pages
* Unreadable scans
* Duplicate content
* Incomplete content
* Incorrect encoding
* Missing metadata
* Formatting that prevents extraction

### Quality Rule

> **A document that cannot be reliably interpreted should not be treated as reliable AI knowledge.**

---

## 11. Scanned Documents

Some organizational policies may exist as scanned PDFs.

Scanned documents may require:

* Optical Character Recognition (OCR)
* Text extraction
* Manual validation
* Formatting validation

The PM should ensure that the team determines whether extracted text accurately represents the source document.

### Acceptance Criterion

**100% of scanned policy documents included in the knowledge base must pass text-extraction validation before becoming eligible for retrieval.**

---

## 12. Document Ingestion

The ingestion process should include:

```text
Document Received
      ↓
File Validation
      ↓
Metadata Validation
      ↓
Authority Validation
      ↓
Status Validation
      ↓
Approval Validation
      ↓
Text Extraction
      ↓
Content Validation
      ↓
Chunking
      ↓
Embedding
      ↓
Indexing
```

Only eligible content should enter the active retrieval population.

---

## 13. Chunking

Long policy documents must be divided into smaller sections before semantic retrieval.

Chunking should preserve sufficient context to prevent misleading results.

The team should evaluate:

* Chunk size
* Overlap
* Section boundaries
* Headings
* Policy identifiers
* Context preservation

### PM Responsibility

The PM does not need to determine the exact technical chunking algorithm.

The PM should ensure the team can demonstrate that the selected approach supports retrieval quality.

---

## 14. Embeddings

Embeddings convert policy content into numerical representations.

The current architecture uses:

**`all-MiniLM-L6-v2`**

Embeddings support semantic retrieval.

For example:

> "How much time can I take off after having a baby?"

may retrieve relevant parental-leave content even if the policy does not use exactly the same wording.

### PM Consideration

Changes to the embedding model may affect:

* Retrieval accuracy
* Existing indexes
* Evaluation results
* Performance
* Re-ingestion requirements

A model change should therefore be treated as a controlled technical change.

---

## 15. Duplicate Information

Duplicate policies can create conflicting retrieval results.

Potential duplicates include:

* Identical copies
* Renamed copies
* Different file formats
* Local copies
* Archived copies
* Previous versions
* Department-specific copies

### Duplicate Management

The team should:

1. Identify duplicates.
2. Determine the authoritative version.
3. Mark non-authoritative copies appropriately.
4. Prevent superseded or unverified copies from active retrieval.
5. Document unresolved duplicates.

### Acceptance Criterion

**100% of identified duplicate policy records must have an authority or disposition decision before production release.**

---

## 16. Conflicting Policy Information

Conflicting policy information represents a high governance risk.

Example:

```text
Policy A:
Remote work allowed 3 days per week.

Policy B:
Remote work allowed 2 days per week.
```

If both appear authoritative, PolicyAssist must not guess which is correct.

### Required Response

The system must:

1. Detect or surface the conflict.
2. Prevent unresolved conflicting content from being treated as authoritative.
3. Escalate to the policy owner or governance authority.
4. Record the decision.
5. Revalidate the affected policy data.

### Acceptance Criterion

**100% of unresolved policy authority conflicts must be prevented from entering the authoritative retrieval population.**

---

## 17. Data Access Control

Not all policy information necessarily has the same access requirements.

Access should be evaluated according to:

* User role
* Employee level
* Department
* Policy classification
* Data sensitivity
* Authorization

### Principle

> **Users should receive only policy information they are authorized to access.**

### Acceptance Criteria

* Authentication controls validated = **100%**
* Authorization controls validated = **100%**
* Unauthorized policy access = **0**
* Critical access-control findings = **0**

---

## 18. Knowledge Base Governance

The knowledge base should have defined ownership.

### Governance Roles

| Role                 | Responsibility                       |
| -------------------- | ------------------------------------ |
| Policy Owner         | Owns policy content                  |
| Governance Authority | Resolves authority questions         |
| Data Steward         | Maintains metadata and data quality  |
| Technical Team       | Manages ingestion and indexing       |
| Security Team        | Validates access controls            |
| Project Manager      | Coordinates governance and readiness |
| Business Owner       | Confirms business acceptance         |

Responsibilities should be documented using a **Responsible, Accountable, Consulted, Informed (RACI)** model where appropriate.

---

## 19. Data Change Management

A policy change may affect AI responses.

Examples:

* New policy
* Revised policy
* Policy withdrawal
* Version change
* Ownership change
* Approval change
* Effective-date change

### Change Process

```text
Policy Change
      ↓
Identify Change
      ↓
Validate Authority
      ↓
Validate Metadata
      ↓
Assess AI Impact
      ↓
Update Knowledge Base
      ↓
Revalidate
      ↓
Evaluate
      ↓
Approve
      ↓
Return To Retrieval
```

### Acceptance Criterion

**100% of material policy changes must have a documented change record before the updated policy becomes part of the authoritative retrieval population.**

---

## 20. Data Quality Monitoring

Data quality must continue after initial ingestion.

Monitor for:

* Missing metadata
* Expired policies
* Superseded policies
* Duplicate documents
* Authority conflicts
* Failed ingestion
* Extraction failures
* Unexpected document changes
* Unauthorized changes

### Data Quality Thresholds

| Metric                                                 | Target |
| ------------------------------------------------------ | -----: |
| Eligible policies with complete mandatory metadata     |   100% |
| Active policies with established authority             |   100% |
| Active policies with approval status                   |   100% |
| Active policies with valid version                     |   100% |
| Unresolved authority conflicts in retrieval population |      0 |
| Superseded policies in active retrieval                |      0 |
| Draft policies in active retrieval                     |      0 |
| Unverified policies in active retrieval                |      0 |

---

## 21. Data Security

Data security must protect policy information throughout its lifecycle.

Consider:

* Storage
* Transmission
* Processing
* Retrieval
* Logging
* Backups
* Administrative access
* User access
* Model prompts
* Model responses

Sensitive information should not be exposed unnecessarily through system logs or generated responses.

---

## 22. Data Retention

The project should define:

* How long policy versions are retained
* How superseded policies are stored
* Who can access historical versions
* When documents are archived
* When data should be deleted
* How deletion affects retrieval indexes

Retention requirements should follow applicable organizational and legal requirements.

---

## 23. Data Recovery

The project should establish recovery procedures for:

* Policy repository failure
* Vector database failure
* Corrupted indexes
* Accidental deletion
* Incorrect ingestion
* Unauthorized modification

Recovery should restore the system to a known approved state.

---

## 24. Data Governance Risks

| Risk                       | Severity    | PM Response                     |
| -------------------------- | ----------- | ------------------------------- |
| Outdated policy retrieved  | Critical    | Enforce active/version controls |
| Draft policy retrieved     | Critical    | Exclude draft status            |
| Unauthorized policy access | Critical    | Enforce authorization           |
| Missing metadata           | High        | Data-readiness gate             |
| Conflicting policies       | High        | Hold for authority resolution   |
| Duplicate policies         | High        | Establish source of truth       |
| Poor OCR                   | High        | Validate extracted text         |
| Incorrect chunking         | Medium/High | Evaluate retrieval              |
| Failed ingestion           | High        | Monitor ingestion results       |
| Uncontrolled policy change | High        | Change control                  |
| Unverified document        | High        | Prevent retrieval               |
| Corrupted knowledge index  | High        | Recovery procedure              |

---

## 25. MVP Data Governance

The MVP must have sufficient governance to prevent unsafe or misleading policy responses.

### MVP Must Include

* Approved policy sources
* Policy authority
* Required metadata
* Active status validation
* Version control
* Draft exclusion
* Superseded exclusion
* Authority conflict handling
* Basic access control
* Document validation
* Core ingestion validation
* Core retrieval validation

### Production Requires Additional Controls

Production readiness should additionally address:

* Formal data stewardship
* Automated change detection
* Comprehensive auditability
* Enterprise access controls
* Data retention
* Backup and recovery
* Operational monitoring
* Formal governance workflows
* Production-scale ingestion
* Full regression evaluation after material policy changes

---

## 26. Data Governance Acceptance Criteria

| Acceptance Measure                                 |                 Target |
| -------------------------------------------------- | ---------------------: |
| Eligible policies with complete required metadata  |                   100% |
| Eligible policies with established authority       |                   100% |
| Eligible policies with approval                    |                   100% |
| Eligible policies with valid version               |                   100% |
| Draft policies in active retrieval                 |                      0 |
| Superseded policies in active retrieval            |                      0 |
| Unverified policies in active retrieval            |                      0 |
| Unresolved authority conflicts in active retrieval |                      0 |
| Unauthorized policy access                         |                      0 |
| Required data-readiness checks passed              |                   100% |
| Material policy changes documented                 |                   100% |
| Scanned documents validated after extraction       |                   100% |
| Identified duplicates dispositioned                | 100% before production |

---

## 27. Data Readiness Gate

Before policy data enters the authoritative retrieval population, the Project Manager should confirm:

* Source is approved.
* Authority is established.
* Policy is active.
* Policy is approved.
* Required metadata is complete.
* Version is identified.
* Effective date is valid.
* Content is readable.
* Extraction is accurate.
* Conflicts are resolved.
* Access requirements are defined.

### Gate Decision

**Proceed**

All mandatory criteria pass.

**Proceed With Conditions**

Non-critical conditions are documented with owners and deadlines, and they do not compromise policy accuracy, security, or authority.

**Hold**

Any critical data-readiness requirement fails.

---

## 28. Data Governance Evidence

The PM should require evidence such as:

* Approved policy inventory
* Policy metadata records
* Authority documentation
* Approval records
* Version history
* Data-readiness assessments
* Ingestion results
* Extraction validation
* Duplicate analysis
* Conflict-resolution records
* Access-control validation
* Data-quality reports
* Change records
* Evaluation results

### PM Rule

> **No Evidence = Not Yet Accepted.**

---

## 29. Practical Exercise 6: Evaluate AI Data Readiness

### Scenario

The project team receives 50 policy documents from multiple departments.

The documents include:

* Active policies
* Draft policies
* Old versions
* Duplicate files
* Scanned PDFs
* Documents with missing metadata
* Two documents that appear to conflict

The technical team wants to ingest all 50 documents immediately so development can continue.

### Your Task

As the Project Manager:

1. Determine which documents are eligible for retrieval.
2. Identify the data-readiness failures.
3. Identify the governance risks.
4. Determine which stakeholders must resolve the issues.
5. Define the evidence required before ingestion.
6. Determine which items can proceed to MVP.
7. Determine which items must be placed on Hold.
8. Define measurable data-readiness acceptance criteria.

### PM Decision

Choose:

* **Proceed**
* **Proceed With Conditions**
* **Hold**

Your decision must consider:

* Authority
* Approval
* Status
* Version
* Metadata
* Data quality
* Security
* Conflicts
* Retrieval risk

---

## 30. Artifact / Output

Complete:

**Data Readiness & Knowledge Governance Assessment**

The assessment should include:

* Policy inventory
* Source-of-truth assessment
* Authority assessment
* Metadata assessment
* Version assessment
* Data-quality assessment
* Duplicate analysis
* Conflict analysis
* Access-control assessment
* Ingestion assessment
* Data-change process
* Data risks
* Data-readiness gate
* Acceptance criteria
* Evidence requirements
* PM recommendation

---

## 31. PM Decision

Policy data should not become AI knowledge simply because the technical team can ingest it.

The PM must determine whether the organization can establish that the data is:

* Correct
* Current
* Authorized
* Approved
* Complete
* Governed

### Decision Principle

> **If the organization cannot establish which policy is authoritative, the AI should not decide for them.**

---

## 32. Decision / Reflection

Ask:

> **"If PolicyAssist gives an incorrect answer, can we trace the answer back to the exact policy, version, authority, and data state that produced it?"**

If not, additional data governance is required.

---

## Key Takeaways

* AI quality depends heavily on data quality.
* The most easily retrieved document is not necessarily the authoritative document.
* Active, authoritative, approved, and properly documented policies are eligible for retrieval.
* Draft and superseded policies must be excluded.
* Conflicting authority must be resolved by humans.
* Metadata is a governance control, not just administrative information.
* Scanned documents require extraction validation.
* Duplicate policies can create incorrect retrieval results.
* Policy changes require controlled revalidation.
* Access control must be applied to policy information.
* Data governance continues after initial ingestion.
* MVP requires enough governance to prevent unsafe or misleading answers.
* Production requires stronger operational governance.
* Every critical data decision should have evidence.
* **No Evidence = Not Yet Accepted.**

---

## Connection To Capstone

This document establishes the data governance foundation for Petadel PolicyAssist AI.

It directly supports:

* `03-REQUIREMENTS.md`
* `04-PRODUCT-BACKLOG.md`
* `05-ARCHITECTURE.md`
* `07-EVALUATION-PLAN.md`
* `08-RISK-SECURITY-GOVERNANCE.md`
* `09-TEST-UAT-PILOT.md`
* `10-RELEASE-DEPLOYMENT.md`
* `11-MONITORING-CONTINUOUS-IMPROVEMENT.md`
* `14-TRACEABILITY.md`
* `16-FINAL-GO-HOLD-NO-GO.md`

The data governance decision determines whether policy information is safe to enter the AI retrieval layer and ultimately whether PolicyAssist can be trusted to provide authoritative policy answers.

# 13: Decision Log

## 1. Purpose

The Decision Log provides a formal, traceable record of significant decisions made throughout the Petadel PolicyAssist AI project.

AI projects require frequent decisions involving:

* Business objectives
* Scope
* Requirements
* Product priorities
* Architecture
* Data
* Policy authority
* AI quality
* Security
* Governance
* Testing
* UAT
* Release readiness
* Monitoring
* Production operations

The Decision Log ensures that important decisions are not lost, forgotten, or changed without understanding their original rationale.

It also provides evidence for project governance, stakeholder alignment, audits, release decisions, and future project teams.

---

## 2. Decision Management Principle

Project decisions must be based on evidence, defined requirements, risk assessment, stakeholder input, and approved project objectives.

A decision should not be considered sufficiently supported merely because:

* A technical team recommends it
* A stakeholder prefers it
* A vendor claims it is correct
* The deadline is approaching
* The solution appears to work
* The model produces a convincing response
* The team has always used a particular approach

**No Evidence = Not Yet Accepted.**

---

## 3. What Requires A Decision Log Entry?

A decision should be recorded when it materially affects:

* Project scope
* Business objectives
* Requirements
* MVP definition
* Product backlog priorities
* Architecture
* AI models
* Data sources
* Policy authority
* Security
* Privacy
* Governance
* Evaluation criteria
* Acceptance criteria
* Testing strategy
* UAT
* Release readiness
* Production deployment
* Monitoring
* Risk acceptance
* Schedule or budget
* Stakeholder responsibilities
* Major defects
* Production incidents
* Material changes to approved project decisions

Routine operational actions do not necessarily require a formal Decision Log entry unless they materially change the project.

---

# 4. Decision Identification

Each material decision receives a unique Decision ID.

Recommended format:

`DEC-001`, `DEC-002`, `DEC-003`, etc.

Decision IDs must not be reused.

---

# 5. Decision Log Structure

Each decision should capture:

| Field                  | Description                                         |
| ---------------------- | --------------------------------------------------- |
| Decision ID            | Unique decision identifier                          |
| Date                   | Date decision was made                              |
| Decision Title         | Short description of the decision                   |
| Decision Category      | Business, scope, architecture, data, security, etc. |
| Decision Statement     | What was decided                                    |
| Business Context       | Why the decision was necessary                      |
| Options Considered     | Alternatives evaluated                              |
| Recommended Option     | Preferred option                                    |
| Final Decision         | Approved outcome                                    |
| Rationale              | Why the decision was selected                       |
| Evidence               | Evidence supporting the decision                    |
| Risks                  | Risks created or affected                           |
| Dependencies           | Dependencies affected                               |
| Requirements Affected  | Related requirements                                |
| Epics/Stories Affected | Related backlog items                               |
| Release Affected       | Foundation, MVP, or Production Readiness            |
| Decision Owner         | Person accountable for decision                     |
| Approvers              | Required decision authorities                       |
| Stakeholders Consulted | People/groups consulted                             |
| Effective Date         | When decision becomes effective                     |
| Status                 | Proposed, Approved, Rejected, Deferred, etc.        |
| Follow-Up Actions      | Actions resulting from decision                     |
| Review Date            | Date decision should be reassessed                  |
| Related Artifacts      | Documents containing related information            |

---

# 6. Decision Categories

PolicyAssist decisions should use one of the following categories:

### Business

Decisions involving business objectives, outcomes, value, or organizational priorities.

### Scope

Decisions affecting what is or is not included in the project.

### Requirements

Decisions involving business, functional, non-functional, or AI-specific requirements.

### Product

Decisions involving user experience, MVP scope, product priorities, or backlog sequencing.

### Architecture

Decisions involving application architecture, AI architecture, integrations, models, databases, or technical design.

### Data

Decisions involving policy documents, metadata, ingestion, data quality, authority, versioning, or knowledge management.

### AI Quality

Decisions involving retrieval, grounding, hallucination, citations, evaluation, or model behavior.

### Security

Decisions involving authentication, authorization, privacy, data protection, prompt injection, or information leakage.

### Governance

Decisions involving policy authority, approvals, accountability, risk acceptance, or organizational controls.

### Testing

Decisions involving testing strategy, test coverage, defect disposition, or evaluation.

### UAT

Decisions involving business acceptance and user validation.

### Release

Decisions involving deployment, go-live, rollback, pilot, or release readiness.

### Monitoring

Decisions involving production monitoring, thresholds, incidents, drift, feedback, and continuous improvement.

---

# 7. Decision-Making Framework

Before making a material decision, the PM should consider:

1. What problem requires a decision?
2. What business objective is affected?
3. What requirements are affected?
4. What options are available?
5. What evidence exists?
6. What assumptions are being made?
7. What risks are introduced?
8. What dependencies are affected?
9. Who has decision authority?
10. Which stakeholders need to be consulted?
11. What happens if no decision is made?
12. What is the impact on the MVP?
13. What is the impact on the current release?
14. What testing or evaluation is required?
15. What documentation must be updated?

---

# 8. Decision Authority

The PM should not make every project decision independently.

Decision authority should be aligned with the nature of the decision.

| Decision Area                 | Typical Decision Authority                  |
| ----------------------------- | ------------------------------------------- |
| Business Objectives           | Executive Sponsor / Business Owner          |
| Product Priorities            | Product Owner / Business Owner              |
| Project Scope                 | Sponsor / Product Owner / PM                |
| Requirements                  | Product Owner / Business Stakeholders       |
| Architecture                  | Technical Lead / Architecture Authority     |
| Policy Authority              | Policy Owner / Governance Authority         |
| Security                      | Security Authority                          |
| Data Governance               | Data Owner / Policy Owner                   |
| AI Evaluation                 | PM / AI Lead / Product Owner                |
| Risk Acceptance               | Appropriate Risk Owner / Sponsor            |
| UAT Acceptance                | Business/UAT Owner                          |
| Release                       | Release Authority / Product Owner / Sponsor |
| Production Operations         | Operations Owner                            |
| Material Governance Decisions | Governance Authority                        |

The PM is responsible for coordinating the decision process, ensuring evidence is available, documenting the decision, and communicating the outcome.

---

# 9. Evidence Requirements

A decision should reference objective evidence whenever evidence is available.

Examples include:

* Approved project charter
* Requirements
* Acceptance criteria
* Product backlog
* Architecture assessment
* Data-readiness assessment
* Policy metadata
* Policy owner approval
* Evaluation dataset
* Evaluation results
* Retrieval accuracy results
* Answer accuracy results
* Hallucination measurements
* Citation testing
* Performance testing
* Security testing
* UAT results
* Defect records
* Risk register
* Monitoring results
* Pilot results
* Stakeholder approval
* Governance approval

Evidence should be specific enough that another project participant can understand why the decision was made.

---

# 10. Policy Authority Decisions

Policy authority decisions require special treatment because PolicyAssist must not automatically select between conflicting policies.

The project rule is:

**Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

If policy authority cannot be established, PolicyAssist must not automatically select a conflicting document.

The conflict must be escalated to the appropriate policy owner or governance authority.

---

# 11. Architecture Decisions

Architecture decisions should document:

* Problem being solved
* Architectural options
* Selected architecture
* Alternatives rejected
* Technical rationale
* Business implications
* Performance implications
* Security implications
* Data implications
* Operational implications
* Risks
* Dependencies
* Acceptance evidence

Current approved architecture decisions include:

* Retrieval-Augmented Generation (RAG)
* ChromaDB for vector storage
* Sentence Transformers for embeddings
* `all-MiniLM-L6-v2` embedding model
* Ollama for local AI runtime
* Llama 3.2 3B as the large language model
* Streamlit for the user interface
* Application-controlled citations
* Authoritative active policy filtering
* Local prototype architecture

Architecture decisions should be revisited if performance, security, evaluation, scalability, or business requirements change.

---

# 12. MVP Decisions

The MVP is intentionally limited to the first usable product.

The MVP core journey is:

**Ask A Policy Question → Retrieve Relevant Authoritative Evidence → Receive A Grounded Response → Verify The Supporting Source → Receive An Appropriate Refusal When Evidence Is Insufficient**

The following are part of the MVP:

* Authorized access
* Approved policy ingestion
* Required policy metadata
* Active/authoritative controls
* Semantic retrieval
* Grounded responses
* Unsupported-question handling
* Citation support
* Basic user experience
* Core security
* Basic human escalation
* Basic feedback
* Core testing
* Core AI evaluation

The following are not required to define the first usable MVP but remain important for production readiness:

* Full production monitoring
* Advanced administration
* Production-scale reliability
* Comprehensive regression coverage
* Advanced operational governance
* Long-term continuous-improvement processes
* Formal production deployment readiness

Any decision that materially changes the MVP definition must be recorded.

---

# 13. Evaluation Decisions

Evaluation decisions must use measurable criteria.

Current project targets include:

| Metric                       |                 Target |
| ---------------------------- | ---------------------: |
| Retrieval Accuracy           |                   ≥90% |
| Answer Accuracy              |                   ≥90% |
| Hallucination Rate           |                    <2% |
| Citation Correctness         |                   100% |
| Unsupported-Question Refusal |                   100% |
| Response Latency             | ≥95% within 10 seconds |
| Maximum Response Threshold   | 100% within 15 seconds |
| User Satisfaction            |                   ≥85% |
| Critical Security Incidents  |                      0 |
| Unresolved Critical Defects  |                      0 |

A decision to accept a release should not be based solely on one successful demonstration.

---

# 14. Mixed-Question Decisions

PolicyAssist may receive questions containing both supported and unsupported requests.

The approved decision principle is:

* Evaluate each component independently.
* Answer supported portions.
* Identify unsupported portions.
* Do not invent information.
* Cite evidence for the supported portion.
* Do not imply that the citation supports unsupported content.

Any material change to this behavior should be recorded as a decision.

---

# 15. Security Decisions

Security-related decisions require heightened documentation.

Security decisions should identify:

* Threat or risk
* Affected users/data
* Control
* Testing performed
* Residual risk
* Risk owner
* Approval authority
* Release impact

The following conditions should normally prevent production release until resolved:

* Unresolved critical security findings
* Unauthorized policy access
* Critical data leakage
* Unvalidated required security controls
* Material privacy violations

---

# 16. Release Decisions

Release decisions must consider more than technical functionality.

Before a release decision, the PM should review:

* Requirements
* Data readiness
* AI evaluation
* Security
* Testing
* UAT
* Defects
* Monitoring
* Rollback
* Governance
* Residual risks
* Stakeholder acceptance

A passing technical metric does not automatically create a Go decision.

---

# 17. Decision Status

| Status                   | Definition                                            |
| ------------------------ | ----------------------------------------------------- |
| Proposed                 | Decision has been identified but not finalized        |
| Under Review             | Evidence or stakeholder review is occurring           |
| Approved                 | Decision has been formally accepted                   |
| Approved With Conditions | Decision is accepted subject to documented conditions |
| Rejected                 | Decision was considered and rejected                  |
| Deferred                 | Decision requires additional information              |
| Escalated                | Decision has been moved to a higher authority         |
| Superseded               | A later decision replaced this decision               |
| Closed                   | Required follow-up actions are complete               |

---

# 18. Decision Lifecycle

A material decision should follow:

**Identify → Analyze → Gather Evidence → Evaluate Options → Consult Stakeholders → Decide → Approve → Document → Communicate → Implement → Verify**

The PM should confirm that the decision was actually implemented and that required follow-up actions were completed.

---

# 19. Initial PolicyAssist Decision Log

The following decisions establish the current project baseline.

| ID      | Decision                                                  | Category           | Rationale                                                                                    | Evidence                       | Owner                   | Status   |
| ------- | --------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------- | -------- |
| DEC-001 | Use RAG for policy question answering                     | Architecture       | Responses should be grounded in approved policy evidence                                     | Architecture Assessment        | Technical Lead / PM     | Approved |
| DEC-002 | Use authoritative active policy versions only             | Data/Governance    | Prevent outdated or unauthorized policy information from being used                          | Data Governance Assessment     | Policy Owner            | Approved |
| DEC-003 | Do not automatically resolve conflicting policy authority | Governance         | Conflicting authority requires human resolution                                              | Data Governance Rules          | Policy/Governance Owner | Approved |
| DEC-004 | Use application-controlled citations                      | AI Quality         | Prevent the model from independently inventing source references                             | Evaluation Design              | PM / Technical Lead     | Approved |
| DEC-005 | Refuse unsupported policy questions                       | AI Quality         | Prevent unsupported or fabricated policy responses                                           | Evaluation Requirements        | PM / AI Lead            | Approved |
| DEC-006 | Evaluate mixed questions independently                    | AI Quality         | Prevent supported evidence from being incorrectly presented as support for unrelated content | Evaluation Design              | PM / AI Lead            | Approved |
| DEC-007 | Establish measurable AI acceptance thresholds             | Evaluation         | Enable objective release decisions                                                           | Evaluation Plan                | PM / Product Owner      | Approved |
| DEC-008 | Require a minimum 30-case evaluation dataset              | Evaluation         | Ensure representative evaluation coverage                                                    | Evaluation Plan                | PM / AI Lead            | Approved |
| DEC-009 | Establish ≤10-second response-time target                 | Performance        | Define measurable user experience expectations                                               | Architecture / Evaluation Plan | PM / Technical Lead     | Approved |
| DEC-010 | Use controlled pilot before broad production deployment   | Release            | Reduce operational and adoption risk                                                         | Release Plan                   | PM / Product Owner      | Approved |
| DEC-011 | Require rollback capability before production             | Release            | Production changes must be reversible                                                        | Release Plan                   | Technical Lead          | Approved |
| DEC-012 | Include basic human escalation and feedback               | Product/Governance | Users need a path when AI cannot safely resolve a question                                   | Requirements / Backlog         | Product Owner / PM      | Approved |
| DEC-013 | Treat security and authorization as release gates         | Security           | Prevent unauthorized access and unacceptable security exposure                               | Risk/Security Plan             | Security Authority      | Approved |
| DEC-014 | Treat UAT as separate from technical evaluation           | UAT                | Technical performance does not prove business acceptance                                     | Testing/UAT Plan               | PM / UAT Owner          | Approved |
| DEC-015 | Require evidence before accepting project work            | Governance         | Prevent verbal confirmation from replacing objective validation                              | Course/Capstone Standard       | PM                      | Approved |

---

# 20. Architecture Decision Record Format

For major architecture decisions, use the following structure.

### ADR ID

`ADR-XXX`

### Title

Short architecture decision title.

### Status

Proposed / Approved / Rejected / Superseded

### Context

What problem or requirement created the need for the decision?

### Options

What alternatives were considered?

### Decision

What option was selected?

### Rationale

Why was the option selected?

### Consequences

What benefits, limitations, risks, dependencies, or trade-offs result?

### Evidence

What evidence supports the decision?

### Owner

Who owns the decision?

### Approval

Who approved the decision?

### Related Artifacts

List affected project documents.

---

# 21. Decision Impact Assessment

Before approving a material decision, assess its impact.

| Impact Area  | Questions                                            |
| ------------ | ---------------------------------------------------- |
| Business     | Does the decision change expected business outcomes? |
| Scope        | Does it add or remove work?                          |
| Requirements | Which requirements change?                           |
| Product      | Does the user experience change?                     |
| Architecture | Does the technical design change?                    |
| Data         | Does data sourcing or governance change?             |
| AI Quality   | Does evaluation or model behavior change?            |
| Security     | Does the risk profile change?                        |
| Governance   | Does approval authority change?                      |
| Testing      | Does additional testing become necessary?            |
| UAT          | Does UAT need to be repeated?                        |
| Release      | Does the release date or readiness change?           |
| Monitoring   | Are new production metrics required?                 |
| Risk         | Does residual risk increase or decrease?             |
| Cost         | Does implementation or operating cost change?        |
| Schedule     | Does the project timeline change?                    |

---

# 22. Decision Dependencies

A decision may depend on another project artifact or decision.

Examples:

* Architecture depends on requirements.
* Retrieval configuration depends on evaluation results.
* Policy retrieval depends on data authority.
* Release depends on UAT.
* Production release depends on security validation.
* Monitoring depends on defined production metrics.
* Model changes depend on evaluation.
* Policy changes depend on governance.
* Scope changes may affect requirements, testing, UAT, and release.

Decision dependencies must be documented when they could affect project outcomes.

---

# 23. Decision Communication

Material decisions must be communicated to affected stakeholders.

Communication should include:

* What was decided
* Why it was decided
* Effective date
* Impact
* Required actions
* New responsibilities
* Changes to requirements or scope
* Risks or constraints
* Where the official decision is documented

The Decision Log is the authoritative record of the decision.

---

# 24. Decision Change Control

An approved decision should not be changed informally.

When a decision must change:

1. Identify the original Decision ID.
2. Document the reason for change.
3. Identify new evidence.
4. Assess impact.
5. Reassess risks.
6. Identify affected requirements.
7. Identify affected backlog items.
8. Identify affected tests/evaluation.
9. Determine UAT impact.
10. Determine release impact.
11. Obtain appropriate approval.
12. Record the new decision.
13. Mark the original decision as superseded if appropriate.
14. Update affected artifacts.
15. Communicate the change.

---

# 25. Decision Review

Certain decisions should be reviewed when conditions change.

Review triggers include:

* New evidence
* Requirement changes
* Model changes
* Architecture changes
* Policy changes
* Security findings
* Major defects
* Evaluation failure
* Performance degradation
* UAT failure
* Production incidents
* Significant stakeholder changes
* Material business changes

A decision should remain valid only while its underlying assumptions remain reasonable.

---

# 26. Decision Assumptions

Important assumptions should be documented because decisions may become invalid when assumptions change.

Examples include:

* Policy owners remain available to resolve authority conflicts.
* Required policy metadata remains available.
* Approved policies remain accessible.
* The selected AI architecture meets performance requirements.
* The evaluation dataset remains representative.
* Security controls remain effective.
* Users continue to require the identified capabilities.
* The local prototype architecture remains suitable for the intended project stage.

Assumptions should be reviewed when material project conditions change.

---

# 27. Decision Escalation

Escalate a decision when:

* The PM does not have sufficient authority.
* Stakeholders cannot reach agreement.
* Security risk exceeds approved risk appetite.
* Policy authority is disputed.
* A material business requirement is affected.
* A critical release criterion may be weakened.
* A significant scope change is proposed.
* A high or critical risk requires formal acceptance.
* Governance approval is required.
* The decision could materially affect organizational policy.

Escalation does not transfer responsibility for documenting the decision.

---

# 28. Decision Evidence Standard

Every material decision should answer:

> **What evidence supports this decision?**

> **Who is authorized to make this decision?**

> **What alternatives were considered?**

> **What risks does the decision create?**

> **What project artifacts are affected?**

> **How will we know the decision was implemented successfully?**

If these questions cannot be answered, the decision may require additional analysis before approval.

---

# 29. Decision Log Quality Check

Before closing a decision, the PM should verify:

* [ ] Decision ID is unique.
* [ ] Decision date is recorded.
* [ ] Decision category is identified.
* [ ] Problem/context is documented.
* [ ] Alternatives were considered where appropriate.
* [ ] Final decision is clearly stated.
* [ ] Rationale is documented.
* [ ] Evidence is identified.
* [ ] Decision owner is identified.
* [ ] Required approvers are identified.
* [ ] Affected stakeholders are identified.
* [ ] Risks are assessed.
* [ ] Dependencies are documented.
* [ ] Requirements impact is assessed.
* [ ] Backlog impact is assessed.
* [ ] Testing/evaluation impact is assessed.
* [ ] UAT impact is assessed where applicable.
* [ ] Release impact is assessed where applicable.
* [ ] Follow-up actions are assigned.
* [ ] Decision is communicated.
* [ ] Related artifacts are updated.

---

# 30. Practical Exercise: Complete A Decision Record

## Scenario

The PolicyAssist evaluation results are:

* Retrieval Accuracy: 92%
* Answer Accuracy: 91%
* Hallucination Rate: 1.4%
* Citation Correctness: 100%
* Unsupported-Question Refusal: 100%
* 94% of measured requests complete within 10 seconds
* Security testing is complete
* UAT is complete
* One High defect remains unresolved
* Monitoring is only partially implemented
* Rollback is documented but has not been tested
* One governance approval remains pending
* Leadership wants production release immediately

## PM Tasks

Document a formal decision addressing:

1. Whether the product is ready for production.
2. Which criteria have passed.
3. Which criteria have failed or remain incomplete.
4. Which risks remain.
5. Whether the unresolved High defect can be accepted.
6. Whether incomplete monitoring is acceptable.
7. Whether rollback must be tested.
8. Whether pending governance approval is a release blocker.
9. What evidence is still required.
10. What decision authority must approve the release.

## Expected PM Reasoning

The PM should not automatically approve production merely because most AI quality metrics pass.

The PM should assess:

* The performance threshold.
* The unresolved High defect.
* Monitoring readiness.
* Rollback readiness.
* Governance approval.
* Residual risk.
* Release criteria.

If mandatory release criteria remain incomplete, the appropriate decision may be **HOLD** rather than GO.

The PM must document the rationale and identify the conditions required to move forward.

---

# 31. Artifact / Output

The completed Decision Log should contain:

* Decision Register
* Decision Categories
* Decision Authority
* Decision Evidence
* Architecture Decisions
* MVP Decisions
* Evaluation Decisions
* Security Decisions
* Release Decisions
* Decision Impact Assessments
* Decision Dependencies
* Decision Change Control
* Decision Review Process
* Decision Communication
* Decision Quality Check

---

# 32. PM Decision

The Decision Log is complete when all material project decisions are:

* Clearly documented
* Assigned unique identifiers
* Supported by evidence
* Owned by an accountable decision-maker
* Approved by the appropriate authority
* Connected to affected requirements and project artifacts
* Communicated to affected stakeholders
* Monitored for implementation
* Revisited when material conditions change

The PM should never allow schedule pressure, technical confidence, or verbal agreement to replace formal evidence and appropriate decision authority.

**Final Principle:**

**No Evidence = Not Yet Accepted.**

---

# 33. Connection To The Capstone Portfolio

The Decision Log connects directly to the broader Petadel PolicyAssist AI portfolio.

It provides the governance history behind:

* Project Charter
* Requirements
* Product Backlog
* Architecture
* Data Governance
* Evaluation
* Risk/Security/Governance
* Testing/UAT/Pilot
* Release/Deployment
* Monitoring/Continuous Improvement
* Final Go/Hold/No-Go

The Decision Log should therefore be maintained throughout the project rather than completed only at the end.

A strong AI Project Manager can explain not only **what** the project delivered, but also **why important decisions were made, what evidence supported them, who approved them, and what happened as a result.**

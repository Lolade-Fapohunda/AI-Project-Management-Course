# 12: Capstone & Portfolio

## 1. Purpose

This module brings together the complete AI Project Management lifecycle through the Petadel PolicyAssist AI capstone.

The capstone is designed to demonstrate that the learner can manage an AI project from business problem identification through production readiness and continuous improvement.

The learner is not expected to become an AI engineer.

The objective is to demonstrate the ability to:

* Define and validate an AI business problem.
* Identify and manage stakeholders.
* Translate business needs into requirements.
* Build and prioritize an AI product backlog.
* Understand AI architecture and technology decisions.
* Evaluate data and knowledge readiness.
* Define AI evaluation and quality criteria.
* Manage AI risk, security, and governance.
* Plan testing, UAT, and pilot activities.
* Manage release and deployment readiness.
* Establish monitoring and continuous improvement.
* Make evidence-based Go, Hold, and No-Go decisions.
* Communicate AI project status and recommendations to leadership.

---

## 2. Learning Objectives

By completing this capstone, you should be able to:

1. Apply the AI Project Management lifecycle from initiation through continuous improvement.
2. Build a complete set of AI project management artifacts.
3. Connect business objectives to technical and AI requirements.
4. Manage AI-specific risks and uncertainties.
5. Evaluate whether AI data is ready for use.
6. Define measurable AI quality and evaluation criteria.
7. Establish appropriate security and governance controls.
8. Plan testing, UAT, pilot, release, and rollback activities.
9. Establish production monitoring and improvement processes.
10. Make defensible PM decisions using documented evidence.
11. Build a professional AI Project Management portfolio.

---

# 3. Capstone Project: Petadel PolicyAssist AI

## Organization

**Petadel Technology Services (PTS)**

## Project

**Petadel PolicyAssist AI**

## Business Problem

PTS employees currently face difficulty locating, understanding, and determining the correct version of organizational policies.

Potential challenges include:

* Policies stored across different locations.
* Large numbers of documents.
* PDF and scanned documents.
* Duplicate information.
* Different policy versions.
* Outdated policies.
* Unclear policy ownership.
* Conflicting policy information.
* Difficulty determining which policy is authoritative.
* Time-consuming manual searches.

The project must address the business problem rather than simply demonstrate that an AI model can generate text.

---

# 4. Business Objective

The objective of PolicyAssist is to provide employees with a faster and more reliable way to locate and understand organizational policy information.

PolicyAssist should:

* Retrieve relevant policy information.
* Use only authoritative, active, approved policies.
* Ground responses in retrieved evidence.
* Provide accurate citations.
* Refuse unsupported questions appropriately.
* Respect access controls.
* Escalate situations requiring human judgment.

The system should reduce employee policy-search time by approximately 50% while maintaining defined quality, security, and governance standards.

---

# 5. Initial Success Targets

The capstone uses the following measurable targets.

| Measure                      |                 Target |
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

These are targets that must be demonstrated with evidence. They should not be treated as automatically achieved.

---

# 6. Capstone Lifecycle

The capstone follows the complete AI Project Management lifecycle:

**Initiation → Discovery → Requirements → Agile Planning → Architecture → Data → Evaluation → Risk & Security → Testing → UAT → Release → Monitoring → Continuous Improvement**

Each phase produces an artifact or decision that connects to the next phase.

The learner should be able to explain how decisions made early in the project affect later phases.

---

# 7. Capstone Rule

The capstone is not a collection of disconnected documents.

Each artifact must connect to the others.

For example:

**Business Problem → Requirements → User Stories → Architecture → Data → Evaluation → Testing → UAT → Release → Monitoring**

A requirement should be traceable to:

* A business need.
* A backlog item.
* Acceptance criteria.
* Testing.
* UAT.
* Release readiness.

---

# 8. Capstone Phase 1: Initiation

The first phase establishes why the project exists and whether it should proceed.

### Key Activities

* Define the business problem.
* Identify the business objective.
* Establish project scope.
* Identify major stakeholders.
* Define initial success criteria.
* Identify assumptions and constraints.
* Identify initial risks.
* Establish governance.
* Determine whether AI is appropriate.

### Primary Artifact

**02-PROJECT-CHARTER.md**

### PM Decision

Determine whether the project should:

* Proceed.
* Proceed With Conditions.
* Hold.
* Stop.

---

# 9. Capstone Phase 2: Discovery & Stakeholders

Discovery validates that the proposed solution addresses a real organizational problem.

### Key Activities

* Analyze the current state.
* Identify root causes.
* Identify stakeholders.
* Assess stakeholder influence and interest.
* Identify competing objectives.
* Gather discovery information.
* Define desired business outcomes.
* Validate AI suitability.

### Primary Focus

The PM should avoid jumping directly into technical requirements before understanding the problem.

### Primary Artifact

Discovery and stakeholder analysis contained within the project portfolio.

### PM Decision

Determine whether the problem is sufficiently understood to move into requirements.

---

# 10. Capstone Phase 3: Requirements

Requirements translate business needs into measurable product expectations.

### Requirement Categories

* Business requirements.
* Functional requirements.
* Non-functional requirements.
* AI-specific requirements.
* Data requirements.
* Security requirements.
* Evaluation requirements.
* Testing requirements.
* UAT requirements.
* Release requirements.
* Monitoring requirements.

### Requirements Principle

Requirements should be:

* Specific.
* Measurable.
* Testable.
* Traceable.
* Unambiguous.
* Relevant to business outcomes.

### Primary Artifact

**03-REQUIREMENTS.md**

### PM Decision

Determine whether requirements are sufficiently complete and measurable to support planning and development.

---

# 11. Capstone Phase 4: Agile Product Planning

PolicyAssist is managed using an Agile product-management approach.

## Backlog Structure

The authoritative backlog contains:

**10 Epics and 58 User Stories**

### Epics

1. EP-01 Security & Access
2. EP-02 Policy Knowledge Base/Ingestion
3. EP-03 Policy Retrieval
4. EP-04 AI Response/Grounding
5. EP-05 User Experience
6. EP-06 Performance & Reliability
7. EP-07 Human Escalation & Feedback
8. EP-08 Administration/Governance
9. EP-09 Evaluation/Testing
10. EP-10 Monitoring/Continuous Improvement

## Releases

PolicyAssist uses three release stages:

1. Foundation
2. MVP Product
3. Production Readiness

---

# 12. MVP Definition

The MVP is the first usable PolicyAssist product.

The MVP must support the core user journey:

**Ask a policy question → Retrieve relevant authoritative policy evidence → Receive a grounded response → Verify the supporting source → Receive appropriate refusal when evidence is insufficient**

## MVP Must Include

* Authorized access.
* Approved policy ingestion.
* Required policy metadata.
* Active and authoritative policy controls.
* Semantic retrieval.
* Grounded responses.
* Unsupported-question handling.
* Accurate citations.
* Basic user experience.
* Core security controls.
* Basic human escalation and feedback.
* Core functional and negative testing.
* Evidence-based quality validation.

## MVP Does Not Require Full Production Readiness

The MVP does not require the full implementation of:

* Advanced performance optimization.
* Full production-scale reliability validation.
* Advanced administration.
* Comprehensive governance operations.
* Full regression coverage.
* Production-scale monitoring.
* Formal production deployment.
* Long-term continuous-improvement operations.

These remain necessary before full production release where applicable.

### Primary Artifact

**04-PRODUCT-BACKLOG.md**

### PM Decision

Determine whether the proposed MVP delivers sufficient business value while controlling unacceptable risk.

---

# 13. Capstone Phase 5: AI Technology & Architecture

PolicyAssist uses a Retrieval-Augmented Generation (RAG) architecture.

### Architecture

**Documents → Chunking → Embedding Model → Vector Database → Retrieval → Large Language Model → Grounding/Citation → Streamlit**

### Technology Roles

| Technology            | Role                                     |
| --------------------- | ---------------------------------------- |
| Python                | Programming language                     |
| Streamlit             | Application and user-interface framework |
| Sentence Transformers | Embedding framework/library              |
| all-MiniLM-L6-v2      | Embedding model                          |
| ChromaDB              | Vector database                          |
| Ollama                | Local AI runtime                         |
| Llama 3.2 3B          | Large Language Model                     |

The PM does not need to implement every technical component but must understand what each component does, why it exists, and what risks it introduces.

### Architecture Decisions

The current architecture uses:

* Retrieval-Augmented Generation.
* Local AI through Ollama.
* Llama 3.2 3B.
* all-MiniLM-L6-v2 embeddings.
* ChromaDB.
* Streamlit.
* Authoritative active approved policy filtering.
* Application-controlled citations.
* Measured response-time thresholds.

### Primary Artifact

**05-ARCHITECTURE.md**

### PM Decision

Determine whether the architecture can reasonably support the business requirements, quality targets, security requirements, and MVP objectives.

---

# 14. Capstone Phase 6: Data & Knowledge Management

PolicyAssist depends heavily on the quality and authority of its policy knowledge.

## Data Readiness Rule

**Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

Policies that are:

* Draft.
* Superseded.
* Unverified.
* Conflicting.
* Missing required metadata.

must not automatically become active retrieval sources.

## Authority Rule

PolicyAssist may retrieve and use only the authoritative, active version of a policy.

If authority cannot be established:

**Do not automatically choose a conflicting document.**

The issue must be flagged for human resolution.

### Required Data Controls

* Policy owner.
* Policy ID.
* Policy name.
* Version.
* Effective date.
* Status.
* Approval.
* Authority.
* Document type.
* Applicability.
* Required metadata.

### Primary Artifact

**06-DATA-GOVERNANCE.md**

### PM Decision

Determine whether the policy knowledge base is ready for safe AI retrieval.

---

# 15. Capstone Phase 7: AI Evaluation & Quality

AI quality must be measured rather than assumed.

## Evaluation Dimensions

PolicyAssist must evaluate:

* Retrieval accuracy.
* Answer accuracy.
* Grounding.
* Hallucination.
* Unsupported questions.
* Citation correctness.
* Mixed questions.
* Paraphrased questions.
* Multi-policy questions.
* Policy authority.
* Version handling.
* Performance.

## Evaluation Dataset

The minimum evaluation dataset contains **30 representative cases**.

Recommended categories:

| Category               |  Cases |
| ---------------------- | -----: |
| Direct Questions       |      6 |
| Paraphrased Questions  |      6 |
| Unsupported Questions  |      4 |
| False Premise          |      3 |
| Mixed Questions        |      3 |
| Multi-Policy           |      3 |
| Authority/Version      |      3 |
| Performance/Edge Cases |      2 |
| **Total**              | **30** |

## Evaluation Targets

* Retrieval accuracy ≥90%.
* Answer accuracy ≥90%.
* Hallucination <2%.
* Citation correctness 100%.
* Unsupported-question refusal 100%.
* At least 95% of representative requests within 10 seconds.
* 100% within 15 seconds.

### Citation Rule

PolicyAssist should display a source citation only when retrieved policy evidence substantively supports the answer.

If evidence does not support the answer:

**Do not display the retrieved document as supporting evidence.**

### Mixed Question Rule

If a user asks both supported and unsupported questions:

* Answer the supported portion.
* Cite the supporting evidence.
* Identify the unsupported portion.
* Do not invent an answer for the unsupported portion.

### Primary Artifact

**07-EVALUATION-PLAN.md**

### PM Decision

Determine whether AI quality meets the approved thresholds using documented evidence.

---

# 16. Capstone Phase 8: Risk, Security & Governance

AI projects require active risk management throughout the lifecycle.

## Major Risk Categories

* AI accuracy.
* Hallucination.
* Data quality.
* Policy authority.
* Unauthorized access.
* Data leakage.
* Prompt injection.
* Model misuse.
* Privacy.
* Vendor risk.
* Governance failure.
* Performance.
* Operational failure.

## Security Principles

PolicyAssist must:

* Restrict unauthorized access.
* Protect policy information.
* Validate authentication.
* Validate authorization.
* Prevent unauthorized policy exposure.
* Identify security incidents.
* Provide appropriate human escalation.

## Risk Acceptance Criteria

* 0 unresolved critical security findings.
* 0 unauthorized policy access.
* 0 critical data leakage findings.
* 0 known fabricated policy responses.
* 0 unresolved authority conflicts in active retrieval.
* 0 draft policies in active retrieval.
* 0 superseded policies in active retrieval.
* 100% required security controls validated.
* 100% defined escalation paths implemented.
* 100% material governance decisions documented.

### Primary Artifact

**08-RISK-SECURITY-GOVERNANCE.md**

### PM Decision

Determine whether remaining risks are acceptable for the intended release stage.

---

# 17. Capstone Phase 9: Testing, UAT & Pilot

Testing verifies that the product behaves as expected.

UAT determines whether the product is acceptable to its intended users.

Pilot testing determines whether the product performs appropriately with a controlled user population.

## Testing Areas

* Functional testing.
* Negative testing.
* Edge-case testing.
* Security testing.
* Regression testing.
* AI evaluation.
* UAT.
* Pilot testing.

## UAT Baseline

The PolicyAssist UAT baseline includes:

* UAT-01 Remote Work.
* UAT-02 Attendance.
* UAT-03 Expense Reimbursement.
* UAT-04 Information Security.
* UAT-05 Code of Conduct.
* UAT-06 Unsupported Vacation Question.
* UAT-07 False Premise.
* UAT-08 Multi-Policy Question.
* UAT-09 Superseded/Draft Policy.
* UAT-10 Conflicting Authority.

## Testing Acceptance Criteria

* 100% critical functional requirements have documented test coverage.
* 100% MVP Must-Have functionality is tested.
* 0 unresolved critical functional defects at release.
* 100% negative scenarios demonstrate expected safe behavior.
* 100% critical edge cases are documented and tested.
* 100% authentication and authorization controls are validated.
* 0 critical security findings.
* 0 unauthorized access.
* 0 critical data leakage findings.
* Required regression testing is completed.
* Performance targets are demonstrated.

## UAT Acceptance

* 100% critical UAT scenarios executed.
* 100% critical failures resolved or dispositioned.
* Required policy categories tested.
* User satisfaction ≥85%.
* No unresolved critical security or business defects.

### Primary Artifact

**09-TEST-UAT-PILOT.md**

### PM Decision

Determine whether the product is ready for pilot or release based on test and UAT evidence.

---

# 18. Capstone Phase 10: Release & Deployment

Release readiness requires more than completed development.

## Release Criteria

The PM must verify:

* Business readiness.
* Requirements readiness.
* Data readiness.
* AI quality.
* Security.
* Testing.
* UAT.
* Performance.
* Monitoring.
* Governance.
* Support.
* Rollback.

## Release Decisions

### GO

All required criteria are satisfied and sufficient evidence exists.

### HOLD

A material requirement has not yet been demonstrated, but the issue can reasonably be corrected or resolved before release.

### NO-GO

The product presents unacceptable risk or fails a critical release condition.

Examples include:

* Critical security issue.
* Unauthorized access.
* Critical data leakage.
* Fabricated policy responses.
* Unresolved authority conflict affecting retrieval.
* Unresolved critical defect.
* Unacceptable governance failure.

### Rollback

The approved rollback sequence is:

**Detect → Stop Release → Disable → Restore Previous Approved Version → Investigate → Correct → Retest → Re-Approve → Redeploy**

### Primary Artifact

**10-RELEASE-DEPLOYMENT.md**

### PM Decision

Make the evidence-based Go, Hold, or No-Go recommendation.

---

# 19. Capstone Phase 11: Monitoring & Continuous Improvement

Production operation does not end the PM responsibility.

PolicyAssist must continue to be monitored after release.

## Monitoring Areas

* Availability.
* Performance.
* Retrieval.
* Answer quality.
* Hallucination.
* Citations.
* Unsupported questions.
* Policy changes.
* Model changes.
* Security.
* User feedback.
* Defects.
* Business outcomes.

## Continuous Improvement Loop

**Monitor → Identify Problem → Create Backlog Item → Prioritize → Develop → Test → Evaluate → UAT → Release → Monitor**

## Change Triggers

Additional evaluation or review may be required when there is:

* Model change.
* Major prompt change.
* Policy knowledge-base change.
* Authority conflict.
* Significant retrieval change.
* Performance degradation.
* Critical defect.
* Security incident.
* Significant user complaint trend.
* Major architecture change.
* Governance requirement change.

### Primary Artifact

**11-MONITORING-CONTINUOUS-IMPROVEMENT.md**

### PM Decision

Determine whether PolicyAssist remains safe, accurate, useful, secure, and operational.

---

# 20. Capstone Portfolio

The portfolio demonstrates the learner's ability to manage an AI project professionally.

The portfolio should show not only what was created but **why decisions were made**.

A strong portfolio demonstrates:

* Business thinking.
* PM judgment.
* AI literacy.
* Requirements management.
* Stakeholder management.
* Risk management.
* Data governance.
* AI evaluation.
* Security awareness.
* Testing and UAT.
* Release management.
* Monitoring.
* Executive communication.

---

# 21. Portfolio Structure

The PolicyAssist portfolio should contain:

1. Project Overview.
2. Project Charter.
3. Requirements.
4. Product Backlog.
5. Architecture & Technology Assessment.
6. Data Readiness & Knowledge Governance.
7. AI Evaluation & Quality Plan.
8. Risk, Security & Governance Plan.
9. Testing, UAT & Pilot Plan.
10. Release & Deployment Plan.
11. Monitoring & Continuous Improvement Plan.
12. Decision Log.
13. Risk Register.
14. Requirements Traceability.
15. Executive Summary.
16. Final Go/Hold/No-Go Recommendation.
17. Final Presentation.

---

# 22. Executive Summary

The executive summary should communicate the project to leadership without requiring them to read the entire portfolio.

It should explain:

* The business problem.
* Proposed solution.
* Business value.
* Project scope.
* Major risks.
* AI quality results.
* Security status.
* UAT status.
* Release readiness.
* Outstanding issues.
* Final recommendation.

The executive summary should be evidence-based and concise.

---

# 23. Capstone Decision Log

The decision log records important project decisions.

Examples include:

* Why AI was selected.
* Why the architecture was selected.
* Why a particular model was selected.
* Why a policy was considered authoritative.
* Why a requirement was prioritized.
* Why a feature was excluded from MVP.
* Why a release was held.
* Why a risk was accepted or rejected.
* Why a model or policy change required additional evaluation.

Each material decision should document:

| Field          | Description                       |
| -------------- | --------------------------------- |
| Decision ID    | Unique identifier.                |
| Date           | Decision date.                    |
| Decision       | What was decided.                 |
| Context        | Why the decision was necessary.   |
| Options        | Alternatives considered.          |
| Decision Maker | Person or authority responsible.  |
| Rationale      | Reason for the decision.          |
| Evidence       | Evidence supporting the decision. |
| Impact         | Expected project impact.          |
| Follow-Up      | Required actions.                 |

---

# 24. Capstone Risk Register

The risk register should remain active throughout the project.

It should track:

* Risk ID.
* Risk description.
* Category.
* Likelihood.
* Impact.
* Risk score.
* Owner.
* Preventive control.
* Detective control.
* Response.
* Residual risk.
* Status.
* Trigger.
* Mitigation.
* Evidence.

The risk register should evolve as the project progresses.

---

# 25. Capstone Requirements Traceability

Requirements traceability connects business needs to implementation and validation.

A traceability relationship should demonstrate:

**Business Requirement → Functional Requirement → User Story → Acceptance Criteria → Test Case → UAT → Release Decision**

Example:

| Business Need             | Requirement                                     | User Story             | Test/UAT               | Release Evidence                |
| ------------------------- | ----------------------------------------------- | ---------------------- | ---------------------- | ------------------------------- |
| Reduce policy search time | Policy information must be quickly retrievable. | Policy retrieval story | Retrieval testing      | Performance/evaluation evidence |
| Prevent outdated guidance | Only active authoritative policies may be used. | Policy authority story | Authority/version test | Data governance evidence        |
| Increase trust            | Responses must provide accurate citations.      | Citation story         | Citation evaluation    | Evaluation report               |

### PM Principle

> If a requirement cannot be traced to evidence, acceptance has not been fully demonstrated.

---

# 26. Capstone Go / Hold / No-Go Framework

The final decision should evaluate the complete project.

## GO

Recommend GO when:

* Business objectives are validated.
* Requirements are accepted.
* Data is ready.
* AI quality targets are met.
* Security is acceptable.
* UAT is complete.
* Critical defects are resolved.
* Performance is within target.
* Monitoring is ready.
* Rollback is available.
* Governance approvals are complete.
* Evidence supports the decision.

## HOLD

Recommend HOLD when:

* Evidence is incomplete.
* A required acceptance criterion has not been demonstrated.
* UAT is incomplete.
* Monitoring is incomplete.
* A material governance decision is pending.
* A correctable material issue remains.

## NO-GO

Recommend NO-GO when:

* Critical security risk remains.
* Unauthorized access exists.
* Critical data leakage exists.
* Fabricated policy responses remain unresolved.
* Authoritative policy cannot be determined.
* Critical defects remain unresolved.
* The remaining risk exceeds organizational tolerance.

---

# 27. Capstone Evidence Standard

Every major PM decision must be supported by evidence.

Evidence may include:

* Requirements.
* Acceptance criteria.
* Test results.
* Evaluation results.
* UAT results.
* Security results.
* Data-readiness results.
* Performance results.
* Defect records.
* Monitoring evidence.
* Governance approvals.
* Decision records.

### Governing Rule

> **No Evidence = Not Yet Accepted.**

The PM should never approve a major project gate solely because:

* Development says it is complete.
* A vendor says the model is accurate.
* Leadership wants the deadline met.
* The system appears to work during a demonstration.
* Users say they "like it."
* Technical stakeholders believe the risk is low.

Evidence must support the decision.

---

# 28. Final Capstone Presentation

The final presentation should communicate the entire project to an executive audience.

## Recommended Presentation Structure

### Slide 1 — Project Overview

* Petadel Technology Services.
* Petadel PolicyAssist AI.
* Project objective.

### Slide 2 — Business Problem

* Current-state problem.
* Business impact.
* Why the problem matters.

### Slide 3 — Proposed AI Solution

* How PolicyAssist addresses the problem.
* Core user journey.

### Slide 4 — Stakeholders

* Key stakeholders.
* Major interests.
* Governance responsibilities.

### Slide 5 — Requirements & MVP

* Major requirements.
* MVP scope.
* What is intentionally excluded.

### Slide 6 — Architecture

* High-level architecture.
* Major technology components.
* Key architecture decisions.

### Slide 7 — Data & Knowledge Governance

* Policy authority.
* Version control.
* Data readiness.
* Conflict handling.

### Slide 8 — AI Evaluation

* Dataset.
* Retrieval accuracy.
* Answer accuracy.
* Hallucination.
* Citation correctness.
* Performance.

### Slide 9 — Risk & Security

* Major risks.
* Security controls.
* Governance status.

### Slide 10 — Testing & UAT

* Testing status.
* UAT results.
* Defects.
* Pilot results where applicable.

### Slide 11 — Release Readiness

* Readiness criteria.
* Open issues.
* Rollback.
* Monitoring.

### Slide 12 — Final Recommendation

**GO / HOLD / NO-GO**

Include the evidence supporting the recommendation.

### Slide 13 — Next Steps

* Immediate actions.
* Ownership.
* Monitoring.
* Continuous improvement.

---

# 29. Practical Exercise 12: Complete The AI Project

You are the Project Manager for Petadel PolicyAssist AI.

Leadership is requesting a final production recommendation.

Your responsibility is to review the entire project and determine whether the product is ready.

## Your Task

Complete the following:

1. Review the business problem and objectives.
2. Validate stakeholder alignment.
3. Review requirements.
4. Review the 10-epic/58-story backlog.
5. Confirm MVP scope.
6. Review architecture decisions.
7. Validate data readiness.
8. Review policy authority and version controls.
9. Review AI evaluation results.
10. Review security and governance.
11. Review testing.
12. Review UAT.
13. Review open defects.
14. Review performance evidence.
15. Review monitoring readiness.
16. Review rollback readiness.
17. Review governance approvals.
18. Identify remaining risks.
19. Determine whether evidence is sufficient.
20. Make the final Go, Hold, or No-Go recommendation.

---

# 30. Artifact / Output

Complete the following capstone portfolio:

1. **01-PROJECT-OVERVIEW.md**
2. **02-PROJECT-CHARTER.md**
3. **03-REQUIREMENTS.md**
4. **04-PRODUCT-BACKLOG.md**
5. **05-ARCHITECTURE.md**
6. **06-DATA-GOVERNANCE.md**
7. **07-EVALUATION-PLAN.md**
8. **08-RISK-SECURITY-GOVERNANCE.md**
9. **09-TEST-UAT-PILOT.md**
10. **10-RELEASE-DEPLOYMENT.md**
11. **11-MONITORING-CONTINUOUS-IMPROVEMENT.md**
12. **12-DECISION-LOG.md**
13. **13-RISK-REGISTER.md**
14. **14-TRACEABILITY.md**
15. **15-EXECUTIVE-SUMMARY.md**
16. **16-FINAL-GO-HOLD-NO-GO.md**
17. **Final Presentation**

The portfolio should demonstrate traceability between these artifacts rather than treating them as isolated documents.

---

# 31. PM Decision

Before making the final recommendation, answer:

### Business

* Does PolicyAssist solve the right problem?
* Is the business value demonstrated?

### Requirements

* Are requirements complete and measurable?
* Is the delivered scope aligned with approved requirements?

### Data

* Are policies authoritative?
* Are active versions correctly identified?
* Are conflicting policies resolved?
* Are required metadata and approvals present?

### AI Quality

* Is retrieval accuracy ≥90%?
* Is answer accuracy ≥90%?
* Is hallucination <2%?
* Is citation correctness 100%?
* Is unsupported-question refusal 100%?

### Security

* Are authentication and authorization validated?
* Are there any critical security findings?
* Is unauthorized access possible?

### Testing & UAT

* Has required testing been completed?
* Has UAT been completed?
* Are critical defects resolved?
* Are High defects appropriately dispositioned?

### Performance

* Are at least 95% of representative requests completed within 10 seconds?
* Are 100% completed within 15 seconds?

### Operations

* Is monitoring ready?
* Are owners assigned?
* Is support available?
* Is rollback available?

### Governance

* Are required approvals complete?
* Are material risks documented?
* Are material decisions recorded?

### Final Question

> **Would I recommend that an organization trust this system in its intended operating environment based on the evidence available today?**

If the answer is not clearly supported by evidence, the appropriate decision may be **HOLD**.

---

# 32. Decision / Reflection

Complete the following reflection:

1. What was the most significant business risk in the project?
2. What was the most significant AI-specific risk?
3. What requirement had the greatest impact on architecture?
4. What data-quality issue presented the greatest risk?
5. Which evaluation metric was most important and why?
6. What would cause you to stop a release?
7. How did stakeholder priorities conflict?
8. How did you resolve those conflicts?
9. What evidence gave you confidence in the product?
10. What evidence was still missing?
11. What would you change if you restarted the project?
12. What did you learn about managing AI projects differently from traditional technology projects?

---

# Competency Check

You should be able to:

* Manage an AI project from initiation through continuous improvement.
* Connect business objectives to AI requirements.
* Build and prioritize an AI backlog.
* Understand AI architecture at the PM level.
* Evaluate data readiness and policy authority.
* Define and interpret AI evaluation metrics.
* Manage hallucination, grounding, citation, and refusal risks.
* Establish AI security and governance controls.
* Manage testing, UAT, pilot, and defects.
* Establish release readiness criteria.
* Define rollback and operational readiness.
* Establish production monitoring.
* Manage continuous improvement.
* Maintain decision and risk documentation.
* Build requirements traceability.
* Communicate project status to executives.
* Make evidence-based Go, Hold, or No-Go decisions.

### Capstone Competency Standard

A successful learner can demonstrate that they can manage an AI project as a **Project Manager**, challenge unsupported technical claims, protect business and user interests, coordinate technical and business stakeholders, and make defensible decisions based on evidence.

---

# Key Takeaways

* AI Project Management is broader than managing software development.
* The PM must connect business value, technical decisions, data, AI quality, security, governance, and operations.
* AI systems require measurable evaluation.
* Data authority and versioning can directly affect AI correctness.
* Hallucination and citation failures can create business risk.
* Security and governance must be integrated throughout the lifecycle.
* UAT establishes business acceptance.
* Release decisions must be evidence-based.
* Monitoring continues after deployment.
* AI changes require controlled evaluation.
* The backlog should evolve as new evidence becomes available.
* Traceability connects business objectives to final acceptance.
* The PM does not need to build every technical component but must understand enough to challenge assumptions and manage risk.
* The strongest AI PM decisions are based on evidence rather than optimism, pressure, or technical confidence.

---

# Connection To Portfolio

This capstone represents the culmination of the AI Project Management course.

The learner has now connected:

**Business Problem → Discovery → Stakeholders → Requirements → Backlog → Architecture → Data → Evaluation → Risk → Security → Testing → UAT → Release → Monitoring → Continuous Improvement**

The completed portfolio demonstrates the learner's ability to manage an AI project across its full lifecycle.

The final standard is not:

> **"Did we build the AI?"**

The final standard is:

> **"Did we manage the project well enough to determine whether the AI product is useful, accurate, grounded, secure, governed, tested, operationally ready, and worth releasing?"**

That is the core competency of an **AI Project Manager**.

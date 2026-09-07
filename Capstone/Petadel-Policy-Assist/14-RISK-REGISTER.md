# 14: Risk Register

## 1. Purpose

The Risk Register provides the formal mechanism for identifying, assessing, responding to, monitoring, escalating, and closing risks associated with the Petadel PolicyAssist AI project.

The register provides project leadership with visibility into threats that could affect:

* Business outcomes
* Project scope
* Requirements
* Schedule
* Data quality
* Policy authority
* AI quality
* Security
* Privacy
* Governance
* User acceptance
* Release readiness
* Production operations
* Continuous improvement

The Risk Register must be maintained throughout the project lifecycle.

---

## 2. Risk Management Objective

The objective of risk management is to identify potential problems before they become incidents, determine appropriate responses, assign accountability, establish actionable mitigation plans, and ensure residual risk remains within approved risk appetite.

AI projects require particular attention to risks involving:

* Incorrect answers
* Hallucination
* Outdated information
* Conflicting information
* Unauthorized access
* Data leakage
* Prompt injection
* Model behavior
* Poor retrieval
* Poor data quality
* Insufficient evaluation
* Incomplete testing
* Inadequate monitoring
* Premature release

---

## 3. Risk Versus Issue

A **risk** is a potential future event that may negatively affect the project.

An **issue** is a problem that has already occurred.

Example:

**Risk:** PolicyAssist may retrieve a superseded policy.

**Issue:** PolicyAssist retrieved a superseded policy during testing.

Once a risk occurs, it should be managed as an issue while remaining connected to the original risk where appropriate.

---

## 4. Risk Identification

Risks should be identified through:

* Requirements analysis
* Stakeholder discussions
* Architecture reviews
* Data assessments
* AI evaluation
* Security assessment
* Testing
* UAT
* Pilot activities
* Defect analysis
* Vendor assessments
* Performance testing
* Monitoring
* Production incidents
* Change requests
* Lessons learned

---

## 5. Risk Categories

### Business Risk

Risks affecting business objectives, expected value, adoption, or organizational outcomes.

### Scope Risk

Risks caused by unclear, expanding, or uncontrolled scope.

### Schedule Risk

Risks that could delay milestones, testing, UAT, pilot, or release.

### Requirements Risk

Risks caused by incomplete, ambiguous, conflicting, or changing requirements.

### Technology Risk

Risks involving architecture, infrastructure, models, dependencies, integrations, or technical limitations.

### Data Risk

Risks involving incomplete, inaccurate, outdated, duplicated, inaccessible, or poorly governed policy information.

### AI Quality Risk

Risks involving retrieval, answer accuracy, hallucination, grounding, citations, or unsupported questions.

### Security Risk

Risks involving unauthorized access, data leakage, prompt injection, privacy, or system misuse.

### Governance Risk

Risks involving policy authority, accountability, approvals, compliance, or decision rights.

### Testing Risk

Risks caused by insufficient test coverage, incomplete evaluation, or unresolved defects.

### UAT Risk

Risks caused by insufficient business validation or user acceptance.

### Release Risk

Risks associated with deployment, rollback, production readiness, or premature release.

### Operational Risk

Risks affecting monitoring, support, reliability, incident response, and continuous improvement.

### Vendor Risk

Risks involving third-party technologies, claims, services, dependencies, or support.

---

# 6. Risk Scoring

Each risk should be assessed using:

**Risk Score = Likelihood × Impact**

### Likelihood

| Score | Rating         | Description                          |
| ----: | -------------- | ------------------------------------ |
|     1 | Rare           | Unlikely to occur                    |
|     2 | Unlikely       | Could occur but is not expected      |
|     3 | Possible       | Reasonably possible                  |
|     4 | Likely         | Expected to occur without mitigation |
|     5 | Almost Certain | Very likely to occur                 |

### Impact

| Score | Rating   | Description                                             |
| ----: | -------- | ------------------------------------------------------- |
|     1 | Minimal  | Little or no meaningful effect                          |
|     2 | Minor    | Limited project impact                                  |
|     3 | Moderate | Noticeable business/project impact                      |
|     4 | Major    | Significant impact requiring management attention       |
|     5 | Severe   | Major business, security, governance, or project impact |

### Risk Rating

| Score | Rating   | Typical Response                             |
| ----: | -------- | -------------------------------------------- |
|   1–4 | Low      | Monitor                                      |
|   5–9 | Medium   | Mitigate and monitor                         |
| 10–16 | High     | Active mitigation and management             |
| 17–25 | Critical | Immediate escalation and executive attention |

---

# 7. Risk Response Strategies

### Avoid

Change the project approach to eliminate the risk.

### Mitigate

Reduce the likelihood or impact through controls or corrective action.

### Transfer

Transfer responsibility or financial/operational exposure to another appropriate party.

### Accept

Accept the risk when it falls within approved risk appetite and appropriate authority approves acceptance.

### Escalate

Move the risk to an authority with the appropriate decision rights.

---

# 8. Initial PolicyAssist Risk Register

| Risk ID | Risk                                                         | Category        | Likelihood | Impact | Score | Rating | Response          | Risk Owner         | Mitigation Action                                                                                         | Mitigation Owner | Due Date                  | Status |
| ------- | ------------------------------------------------------------ | --------------- | ---------: | -----: | ----: | -----: | ----------------- | ------------------ | --------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------- | ------ |
| R-001   | PolicyAssist provides an incorrect policy answer             | AI Quality      |          3 |      5 |    15 |   High | Mitigate          | AI Lead            | Review failed cases, identify root causes, correct retrieval/grounding behavior, and retest               | AI Lead          | Before MVP Acceptance     | Open   |
| R-002   | PolicyAssist generates fabricated policy information         | AI Quality      |          2 |      5 |    10 |   High | Mitigate          | AI Lead            | Expand negative evaluation, strengthen grounding/refusal controls, and verify hallucination target        | AI Lead          | Before MVP Acceptance     | Open   |
| R-003   | Superseded policy is retrieved                               | Data/Governance |          2 |      5 |    10 |   High | Avoid/Mitigate    | Data Owner         | Validate status/version metadata and confirm superseded policies are excluded from retrieval              | Data Owner       | Before MVP Acceptance     | Open   |
| R-004   | Draft policy is retrieved                                    | Data/Governance |          2 |      5 |    10 |   High | Avoid/Mitigate    | Data Owner         | Validate ingestion eligibility rules and test draft-policy exclusion                                      | Data Owner       | Before MVP Acceptance     | Open   |
| R-005   | Conflicting policy authority cannot be established           | Governance      |          3 |      5 |    15 |   High | Escalate          | Policy Owner       | Establish authority decision process and resolve all conflicts before production retrieval                | Policy Owner     | Before Production Release | Open   |
| R-006   | Unauthorized user accesses policy information                | Security        |          2 |      5 |    10 |   High | Mitigate          | Security Lead      | Complete authentication/authorization testing and remediate all unauthorized-access findings              | Security Lead    | Before MVP Acceptance     | Open   |
| R-007   | Sensitive information is exposed in an AI response           | Security        |          2 |      5 |    10 |   High | Mitigate          | Security Lead      | Conduct data-leakage testing, review access boundaries, and remediate findings                            | Security Lead    | Before Production Release | Open   |
| R-008   | Retrieval accuracy falls below 90%                           | AI Quality      |          3 |      4 |    12 |   High | Mitigate          | AI Lead            | Analyze failed retrieval cases, tune retrieval configuration, and rerun representative evaluation         | AI Lead          | Before MVP Acceptance     | Open   |
| R-009   | Answer accuracy falls below 90%                              | AI Quality      |          3 |      4 |    12 |   High | Mitigate          | AI Lead            | Review incorrect answers, improve grounding/prompt behavior, and rerun answer evaluation                  | AI Lead          | Before MVP Acceptance     | Open   |
| R-010   | Hallucination rate reaches or exceeds 2%                     | AI Quality      |          2 |      5 |    10 |   High | Mitigate          | AI Lead            | Expand unsupported/false-premise tests and remediate hallucination causes                                 | AI Lead          | Before MVP Acceptance     | Open   |
| R-011   | Citation incorrectly supports an answer                      | AI Quality      |          2 |      5 |    10 |   High | Mitigate          | PM / AI Lead       | Review citation failures and validate application-controlled citation logic against evaluation cases      | AI Lead          | Before MVP Acceptance     | Open   |
| R-012   | Unsupported questions receive unsupported answers            | AI Quality      |          2 |      5 |    10 |   High | Mitigate          | AI Lead            | Expand refusal dataset, test unsupported scenarios, and verify 100% safe refusal behavior                 | AI Lead          | Before MVP Acceptance     | Open   |
| R-013   | Mixed questions incorrectly receive unsupported information  | AI Quality      |          2 |      5 |    10 |   High | Mitigate          | AI Lead            | Add mixed-question evaluation cases and verify supported/unsupported components are independently handled | AI Lead          | Before MVP Acceptance     | Open   |
| R-014   | Required policy metadata is incomplete                       | Data            |          3 |      4 |    12 |   High | Mitigate          | Data Owner         | Complete metadata validation and block ineligible documents from retrieval                                | Data Owner       | Before MVP Acceptance     | Open   |
| R-015   | Scanned policy documents are incorrectly extracted           | Data            |          3 |      4 |    12 |   High | Mitigate          | Data Owner         | Validate extracted text against source documents and quarantine failed documents                          | Data Owner       | Before MVP Acceptance     | Open   |
| R-016   | Duplicate policies create retrieval ambiguity                | Data            |          3 |      4 |    12 |   High | Mitigate          | Data Owner         | Identify duplicates, determine authoritative version, and disposition duplicate records                   | Data Owner       | Before Production Release | Open   |
| R-017   | Policy changes are not reflected in the knowledge base       | Data/Operations |          3 |      4 |    12 |   High | Mitigate          | Data Owner         | Establish policy-change notification, validation, ingestion, and verification process                     | Data Owner       | Before Production Release | Open   |
| R-018   | Prompt injection causes unintended model behavior            | Security        |          2 |      5 |    10 |   High | Mitigate          | Security Lead      | Conduct prompt-injection assessment and remediate identified weaknesses                                   | Security Lead    | Before Production Release | Open   |
| R-019   | Data leakage occurs through retrieval or responses           | Security        |          2 |      5 |    10 |   High | Mitigate          | Security Lead      | Test access boundaries and response behavior for unauthorized information disclosure                      | Security Lead    | Before Production Release | Open   |
| R-020   | Response latency exceeds the required threshold              | Performance     |          3 |      3 |     9 | Medium | Mitigate          | Technical Lead     | Run minimum 30-request performance evaluation and optimize identified bottlenecks                         | Technical Lead   | Before MVP Acceptance     | Open   |
| R-021   | User satisfaction is below 85%                               | UX/Business     |          3 |      3 |     9 | Medium | Mitigate          | Product Owner      | Conduct UAT/pilot feedback review and prioritize usability improvements                                   | Product Owner    | Before Production Release | Open   |
| R-022   | UAT identifies critical business defects                     | UAT             |          2 |      5 |    10 |   High | Mitigate          | PM / UAT Lead      | Log, prioritize, resolve, retest, and formally disposition UAT defects                                    | UAT Lead         | Before Production Release | Open   |
| R-023   | Evaluation dataset does not adequately represent real usage  | Evaluation      |          3 |      4 |    12 |   High | Mitigate          | PM / AI Lead       | Validate dataset categories and expand coverage to at least 30 representative cases                       | PM               | Before MVP Acceptance     | Open   |
| R-024   | Evaluation results are incorrectly interpreted               | Evaluation      |          2 |      4 |     8 | Medium | Mitigate          | PM                 | Establish scoring rules, evidence requirements, and independent review of acceptance results              | PM               | Before MVP Acceptance     | Open   |
| R-025   | Required monitoring is incomplete before production          | Operations      |          3 |      4 |    12 |   High | Mitigate          | Operations Lead    | Implement required monitoring categories, thresholds, alerts, ownership, and escalation procedures        | Operations Lead  | Before Production Release | Open   |
| R-026   | Rollback capability is documented but not validated          | Release         |          3 |      5 |    15 |   High | Mitigate          | Technical Lead     | Execute rollback simulation, document results, correct failures, and retest                               | Technical Lead   | Before Production Release | Open   |
| R-027   | High-severity defect remains unresolved at release           | Release         |          3 |      5 |    15 |   High | Mitigate/Escalate | PM                 | Assess business/security impact, resolve or obtain formal risk acceptance from authorized owner           | PM               | Before Production Release | Open   |
| R-028   | Governance approval is incomplete at release                 | Governance      |          2 |      5 |    10 |   High | Escalate          | Governance Owner   | Obtain required governance review and formal approval before production                                   | Governance Owner | Before Production Release | Open   |
| R-029   | Leadership pressure results in premature release             | Governance      |          3 |      5 |    15 |   High | Mitigate/Escalate | PM / Sponsor       | Apply formal Go/Hold/No-Go criteria and document evidence-based release recommendation                    | PM               | Before Production Release | Open   |
| R-030   | Vendor makes unsupported AI performance claims               | Vendor          |          3 |      3 |     9 | Medium | Mitigate          | PM                 | Require documented evidence, validation criteria, and independent testing before accepting vendor claims  | PM               | Before Vendor Acceptance  | Open   |
| R-031   | Model change reduces AI quality                              | AI Quality      |          3 |      4 |    12 |   High | Mitigate          | AI Lead            | Require regression evaluation and approval before model changes reach production                          | AI Lead          | Before Any Model Release  | Open   |
| R-032   | Production drift reduces system performance                  | Operations      |          3 |      4 |    12 |   High | Mitigate          | Operations Lead    | Establish production monitoring, thresholds, alerts, and corrective-action process                        | Operations Lead  | Before Production Release | Open   |
| R-033   | Policy authority changes without corresponding system update | Governance      |          3 |      5 |    15 |   High | Mitigate          | Policy Owner       | Establish policy-change notification and governance update workflow                                       | Policy Owner     | Before Production Release | Open   |
| R-034   | Required stakeholders are unavailable for decisions          | Stakeholder     |          3 |      3 |     9 | Medium | Mitigate/Escalate | PM                 | Establish decision calendar, backups, escalation path, and required approval dates                        | PM               | Before UAT                | Open   |
| R-035   | Scope expansion delays MVP delivery                          | Scope           |          4 |      3 |    12 |   High | Avoid/Mitigate    | PM / Product Owner | Apply change-control process and defer non-MVP scope unless formally approved                             | PM               | Throughout MVP            | Open   |

---

# 9. Actionable Mitigation Requirements

Every High or Critical risk must have an actionable mitigation plan.

A mitigation action must contain:

* Specific action
* Named mitigation owner
* Due date
* Expected outcome
* Required evidence
* Status
* Escalation path if overdue

Avoid vague actions such as:

* "Monitor"
* "Review later"
* "Team will investigate"
* "Improve AI"
* "Address security"
* "Fix performance"

Instead, define a measurable action.

### Example

**Weak:**

"Improve retrieval."

**Actionable:**

"Analyze all failed retrieval cases in the evaluation dataset, identify failure patterns, adjust retrieval configuration, rerun the evaluation dataset, and document the resulting retrieval accuracy."

---

# 10. Risk Action Tracker

The following tracker should be used to manage mitigation activities independently from the risk rating.

| Action ID | Risk ID | Mitigation Action                                         | Owner              | Due Date                  | Success Criteria                                      | Evidence Required             | Status | Escalation Date                  |
| --------- | ------- | --------------------------------------------------------- | ------------------ | ------------------------- | ----------------------------------------------------- | ----------------------------- | ------ | -------------------------------- |
| RA-001    | R-001   | Analyze incorrect-answer cases and remediate root causes  | AI Lead            | Before MVP Acceptance     | Answer Accuracy ≥90%                                  | Evaluation results            | Open   | 5 business days before due date  |
| RA-002    | R-002   | Complete hallucination and false-premise evaluation       | AI Lead            | Before MVP Acceptance     | Hallucination <2%                                     | Evaluation report             | Open   | 5 business days before due date  |
| RA-003    | R-003   | Validate exclusion of superseded policies                 | Data Owner         | Before MVP Acceptance     | 0 superseded policies retrieved                       | Data/test evidence            | Open   | 5 business days before due date  |
| RA-004    | R-004   | Validate exclusion of draft policies                      | Data Owner         | Before MVP Acceptance     | 0 draft policies retrieved                            | Test evidence                 | Open   | 5 business days before due date  |
| RA-005    | R-005   | Resolve policy authority conflicts                        | Policy Owner       | Before Production Release | 0 unresolved conflicts affecting retrieval            | Governance decision           | Open   | 10 business days before due date |
| RA-006    | R-006   | Complete authorization testing                            | Security Lead      | Before MVP Acceptance     | 100% required authorization tests passed              | Security test report          | Open   | 5 business days before due date  |
| RA-007    | R-007   | Complete data-leakage testing                             | Security Lead      | Before Production Release | 0 critical leakage findings                           | Security report               | Open   | 10 business days before due date |
| RA-008    | R-008   | Rerun retrieval evaluation after remediation              | AI Lead            | Before MVP Acceptance     | Retrieval Accuracy ≥90%                               | Evaluation report             | Open   | 5 business days before due date  |
| RA-009    | R-009   | Rerun answer evaluation after remediation                 | AI Lead            | Before MVP Acceptance     | Answer Accuracy ≥90%                                  | Evaluation report             | Open   | 5 business days before due date  |
| RA-010    | R-010   | Complete hallucination remediation and regression testing | AI Lead            | Before MVP Acceptance     | Hallucination <2%                                     | Evaluation results            | Open   | 5 business days before due date  |
| RA-011    | R-011   | Validate citation correctness                             | AI Lead            | Before MVP Acceptance     | Citation Correctness = 100%                           | Citation evaluation           | Open   | 5 business days before due date  |
| RA-012    | R-012   | Validate unsupported-question refusal                     | AI Lead            | Before MVP Acceptance     | Refusal = 100%                                        | Negative evaluation           | Open   | 5 business days before due date  |
| RA-013    | R-013   | Validate mixed-question behavior                          | AI Lead            | Before MVP Acceptance     | 100% required mixed cases handled correctly           | Evaluation results            | Open   | 5 business days before due date  |
| RA-014    | R-014   | Complete policy metadata audit                            | Data Owner         | Before MVP Acceptance     | 100% eligible policies have required metadata         | Data-readiness report         | Open   | 5 business days before due date  |
| RA-015    | R-015   | Validate scanned-document extraction                      | Data Owner         | Before MVP Acceptance     | 100% required scanned documents validated             | Extraction QA evidence        | Open   | 5 business days before due date  |
| RA-016    | R-016   | Complete duplicate-policy review                          | Data Owner         | Before Production Release | 100% identified duplicates dispositioned              | Duplicate review record       | Open   | 10 business days before due date |
| RA-017    | R-017   | Establish policy-change workflow                          | Data Owner         | Before Production Release | Workflow approved and tested                          | Change-management evidence    | Open   | 10 business days before due date |
| RA-018    | R-018   | Complete prompt-injection assessment                      | Security Lead      | Before Production Release | Required security scenarios assessed                  | Security assessment           | Open   | 10 business days before due date |
| RA-019    | R-019   | Complete unauthorized-information disclosure testing      | Security Lead      | Before Production Release | 0 critical data-leakage findings                      | Security test report          | Open   | 10 business days before due date |
| RA-020    | R-020   | Run representative performance test                       | Technical Lead     | Before MVP Acceptance     | ≥95% within 10 seconds; 100% within 15 seconds        | Performance report            | Open   | 5 business days before due date  |
| RA-021    | R-021   | Analyze UAT/pilot satisfaction results                    | Product Owner      | Before Production Release | User satisfaction ≥85%                                | UAT/pilot results             | Open   | 10 business days before due date |
| RA-022    | R-022   | Resolve and retest critical UAT findings                  | UAT Lead           | Before Production Release | 0 unresolved critical UAT defects                     | UAT defect evidence           | Open   | 10 business days before due date |
| RA-023    | R-023   | Validate minimum evaluation dataset                       | PM                 | Before MVP Acceptance     | ≥30 representative cases across required categories   | Evaluation dataset            | Open   | 5 business days before due date  |
| RA-024    | R-024   | Perform evaluation quality review                         | PM                 | Before MVP Acceptance     | Results independently reviewed and accepted           | Evaluation review record      | Open   | 5 business days before due date  |
| RA-025    | R-025   | Implement production monitoring                           | Operations Lead    | Before Production Release | 100% required monitoring categories operational       | Monitoring validation         | Open   | 10 business days before due date |
| RA-026    | R-026   | Execute rollback simulation                               | Technical Lead     | Before Production Release | Rollback successfully demonstrated                    | Rollback test record          | Open   | 10 business days before due date |
| RA-027    | R-027   | Resolve or formally disposition High defect               | PM                 | Before Production Release | High defect resolved or formally approved disposition | Defect/risk approval          | Open   | 10 business days before due date |
| RA-028    | R-028   | Obtain governance approval                                | Governance Owner   | Before Production Release | Required governance approvals documented              | Approval record               | Open   | 10 business days before due date |
| RA-029    | R-029   | Conduct formal Go/Hold/No-Go review                       | PM                 | Before Production Release | Decision supported by evidence                        | Go/Hold/No-Go record          | Open   | 5 business days before due date  |
| RA-030    | R-030   | Validate vendor claims independently                      | PM                 | Before Vendor Acceptance  | Claims supported by acceptable evidence               | Vendor validation record      | Open   | 5 business days before due date  |
| RA-031    | R-031   | Execute regression evaluation after model changes         | AI Lead            | Before Any Model Release  | Required quality thresholds maintained                | Regression report             | Open   | Before change approval           |
| RA-032    | R-032   | Configure production drift monitoring                     | Operations Lead    | Before Production Release | Required drift monitoring operational                 | Monitoring evidence           | Open   | 10 business days before due date |
| RA-033    | R-033   | Establish policy-authority change notification            | Policy Owner       | Before Production Release | Change workflow approved and operational              | Governance workflow           | Open   | 10 business days before due date |
| RA-034    | R-034   | Confirm decision-maker availability                       | PM                 | Before UAT                | Required decision-makers and backups identified       | Stakeholder/decision calendar | Open   | 5 business days before due date  |
| RA-035    | R-035   | Review proposed scope changes against MVP                 | PM / Product Owner | Throughout MVP            | Non-MVP scope deferred or formally approved           | Change-control record         | Open   | At each scope review             |

---

# 11. Mitigation Due-Date Rules

Due dates should be tied to project gates rather than arbitrary calendar dates when the project schedule is not yet finalized.

Approved milestone-based due dates include:

* Before MVP Acceptance
* Before UAT
* Before Pilot
* Before Production Release
* Before Any Model Release
* Before Vendor Acceptance
* Throughout MVP
* Within defined incident-response timeframe

Once the project schedule is approved, milestone-based dates should be converted into actual calendar dates.

---

# 12. Overdue Mitigation Management

A mitigation action becomes overdue when:

* The due date passes without completion.
* Required evidence has not been produced.
* The action is completed but validation has not occurred.
* The owner cannot complete the action within the agreed timeline.

When a mitigation becomes overdue:

1. Update the action status.
2. Notify the PM.
3. Assess risk impact.
4. Determine whether likelihood or impact has increased.
5. Establish a revised completion date.
6. Escalate if the risk is High or Critical.
7. Determine whether the release gate is affected.
8. Document the decision.

---

# 13. Risk Status

| Status             | Definition                                        |
| ------------------ | ------------------------------------------------- |
| Open               | Risk is active                                    |
| Monitoring         | Controls are in place and risk is being observed  |
| Mitigating         | Active mitigation is underway                     |
| Escalated          | Risk requires higher-level decision               |
| Accepted           | Authorized owner formally accepts residual risk   |
| Blocked            | Mitigation cannot proceed because of a dependency |
| Closed             | Risk is no longer relevant or has been resolved   |
| Converted To Issue | Risk occurred and is now managed as an issue      |

---

# 14. Risk Trend

Risk trend should be recorded as:

| Trend      | Meaning                                     |
| ---------- | ------------------------------------------- |
| Increasing | Probability or impact is increasing         |
| Stable     | Risk level remains materially unchanged     |
| Decreasing | Controls are reducing probability or impact |
| New        | Newly identified risk                       |

Example:

| Risk ID | Current Rating | Trend      | Reason                                   |
| ------- | -------------- | ---------- | ---------------------------------------- |
| R-001   | High           | Stable     | Evaluation remediation underway          |
| R-005   | High           | Increasing | Authority conflict remains unresolved    |
| R-020   | Medium         | Decreasing | Performance optimization underway        |
| R-025   | High           | Increasing | Production monitoring remains incomplete |

---

# 15. Preventive Controls

Preventive controls are designed to stop a risk from occurring.

Examples:

* Authentication
* Authorization
* Policy eligibility validation
* Required metadata
* Authority validation
* Approval requirements
* Draft-policy exclusion
* Superseded-policy exclusion
* Acceptance criteria
* Change control
* Release gates

---

# 16. Detective Controls

Detective controls identify problems after or while they occur.

Examples:

* Monitoring
* Alerts
* Evaluation
* Logging
* Audit trails
* Defect reports
* User feedback
* Security monitoring
* Performance monitoring
* Production reviews

A mature control environment should include both preventive and detective controls.

---

# 17. Policy Authority Risk

Policy authority is a critical project risk because incorrect authority decisions can result in PolicyAssist providing users with outdated or invalid information.

The system must follow:

**Active + Authoritative + Approved + Required Metadata Present = Eligible For Retrieval**

The system must not automatically choose between conflicting policy versions when authority cannot be established.

The conflict must be escalated to the appropriate human authority.

---

# 18. AI Accuracy Risk

PolicyAssist must meet defined quality thresholds.

The PM should monitor:

* Retrieval Accuracy
* Answer Accuracy
* Hallucination Rate
* Citation Correctness
* Unsupported-Question Refusal
* Mixed-Question Handling
* Paraphrase Performance
* Multi-Policy Performance

Failure to meet required thresholds should trigger investigation and corrective action.

---

# 19. Hallucination Risk

Hallucination is a significant risk because PolicyAssist is intended to provide policy information that users may rely upon.

Controls include:

* Retrieval-Augmented Generation
* Grounding
* Authoritative policy filtering
* Citation controls
* Unsupported-question refusal
* Evaluation
* Negative testing
* Human escalation
* Monitoring

The project target is:

**Hallucination Rate <2%**

---

# 20. Citation Risk

A citation creates risk if it is displayed even though the cited policy does not substantively support the response.

PolicyAssist must:

* Display supporting citations when evidence substantively supports the answer.
* Avoid displaying irrelevant documents as supporting sources.
* Use application-controlled citation logic.
* Avoid implying that a citation supports unsupported information.
* Refuse when sufficient evidence cannot be established.

Citation correctness target:

**100%**

---

# 21. Unsupported-Question Risk

PolicyAssist must not invent answers when a policy question cannot be supported by available evidence.

Expected behavior:

**Insufficient Evidence → Appropriate Refusal → Human Escalation Where Necessary**

Unsupported-question refusal target:

**100%**

---

# 22. Security Risk Management

Security risks must be evaluated before release and monitored after deployment.

Security risk areas include:

* Authentication
* Authorization
* Privacy
* Access control
* Data leakage
* Prompt injection
* Model misuse
* Third-party access
* Logging
* Incident management

---

# 23. Human Oversight

Human oversight is required when:

* Policy authority is unclear.
* Conflicting policy documents exist.
* A security issue is identified.
* A material governance decision is required.
* The AI cannot safely answer.
* A High or Critical risk requires acceptance.
* A material production incident occurs.

AI output should not replace organizational decision authority.

---

# 24. Risk Appetite

PolicyAssist should have a very low tolerance for risks involving:

* Unauthorized policy access
* Critical data leakage
* Fabricated policy information
* Critical security vulnerabilities
* Unresolved authority conflicts
* Unresolved critical defects
* Mandatory governance failures

Schedule pressure should not be used as justification for exceeding approved risk appetite.

---

# 25. Residual Risk

Residual risk is the remaining risk after controls and mitigations have been implemented.

For each material risk, the PM should determine:

* Initial likelihood
* Initial impact
* Initial score
* Controls
* Mitigation effectiveness
* Residual likelihood
* Residual impact
* Residual score
* Residual rating
* Risk acceptance decision
* Risk owner

---

# 26. Residual Risk Assessment

| Risk ID | Initial Score | Controls Applied                    | Residual Likelihood | Residual Impact | Residual Score | Residual Rating | Acceptance Authority                  | Accepted? | Evidence |
| ------- | ------------: | ----------------------------------- | ------------------: | --------------: | -------------: | --------------- | ------------------------------------- | --------- | -------- |
| R-001   |            15 | Evaluation, grounding, testing      |                 TBD |             TBD |            TBD | TBD             | Product Owner / AI Authority          | TBD       | TBD      |
| R-003   |            10 | Active/authoritative filtering      |                 TBD |             TBD |            TBD | TBD             | Data Owner                            | TBD       | TBD      |
| R-005   |            15 | Authority validation and escalation |                 TBD |             TBD |            TBD | TBD             | Policy/Governance Owner               | TBD       | TBD      |
| R-006   |            10 | Authentication/authorization        |                 TBD |             TBD |            TBD | TBD             | Security Authority                    | TBD       | TBD      |
| R-010   |            10 | Evaluation and refusal controls     |                 TBD |             TBD |            TBD | TBD             | AI Quality Authority                  | TBD       | TBD      |
| R-018   |            10 | Security testing and controls       |                 TBD |             TBD |            TBD | TBD             | Security Authority                    | TBD       | TBD      |
| R-026   |            15 | Rollback testing                    |                 TBD |             TBD |            TBD | TBD             | Release Authority                     | TBD       | TBD      |
| R-029   |            15 | Formal release gates                |                 TBD |             TBD |            TBD | TBD             | Executive Sponsor / Release Authority | TBD       | TBD      |

---

# 27. Risk Triggers

Risk triggers indicate that a risk may be increasing or that a response is required.

Examples:

* Retrieval Accuracy below 90%
* Answer Accuracy below 90%
* Hallucination at or above 2%
* Citation Correctness below 100%
* Unsupported Refusal below 100%
* More than 5% of measured responses exceeding 10 seconds
* Unauthorized access finding
* Data leakage finding
* Policy authority conflict
* Critical defect
* High defect
* Increasing user complaints
* Reduced user satisfaction
* Policy change
* Model change
* Monitoring alert
* Security incident

---

# 28. Risk Escalation

A risk should be escalated when:

* It becomes Critical.
* It exceeds approved risk appetite.
* The PM lacks authority to accept it.
* Security or privacy is materially affected.
* Policy authority is disputed.
* A mandatory release criterion may be weakened.
* A material business outcome is threatened.
* Stakeholders cannot reach agreement.
* The mitigation action becomes materially overdue.
* The risk threatens an approved milestone.
* The risk requires executive approval.

---

# 29. Risk Ownership

Every material risk must have an accountable risk owner.

The risk owner is responsible for:

* Monitoring the risk
* Confirming mitigation actions
* Providing resources or authority
* Reviewing risk trends
* Reporting changes
* Escalating when thresholds are exceeded
* Providing evidence
* Recommending closure or acceptance

The **mitigation owner** is responsible for completing the specific mitigation action.

The risk owner and mitigation owner may be the same person, but they do not have to be.

---

# 30. Risk Review Cadence

### Weekly During Active Delivery

Review:

* High risks
* Critical risks
* Overdue mitigation actions
* New risks
* Risk trends
* Release blockers

### Before Major Gates

Perform formal risk review before:

* MVP acceptance
* Evaluation acceptance
* Security approval
* UAT
* Pilot
* Production release

### Production

Review risks through:

* Production monitoring
* Incident reviews
* AI quality reviews
* Security reviews
* Policy governance reviews
* Continuous-improvement reviews

---

# 31. Risk Closure

A risk may be closed when:

* The risk no longer exists.
* The risk has been eliminated.
* The risk has been transferred.
* The affected project phase has ended.
* The risk has occurred and is now being managed as an issue.
* Required mitigation has been completed and validated.
* Residual risk has been formally accepted where appropriate.

Closure must include supporting evidence.

---

# 32. Risk Reassessment

Risks must be reassessed when:

* Requirements change
* Scope changes
* Architecture changes
* Models change
* Policies change
* New data is introduced
* Evaluation results change
* Security findings emerge
* UAT identifies new concerns
* A major defect occurs
* Production monitoring identifies degradation
* Business priorities change

---

# 33. Risk And Change Management

Material change requests must include risk assessment.

The PM should determine:

* New risks
* Existing risks affected
* Likelihood changes
* Impact changes
* New controls
* Testing requirements
* Evaluation requirements
* UAT impact
* Release impact
* Governance impact
* New mitigation owners
* New mitigation due dates

---

# 34. Risk And Release Decision

Risk status directly informs the release decision.

### GO

Appropriate when required risks are controlled and residual risk is within approved appetite.

### HOLD

Appropriate when material risks require additional evidence, mitigation, testing, or approval.

### NO-GO

Appropriate when unacceptable risk remains.

---

# 35. Automatic Release Blockers

The following conditions should prevent production release until resolved or formally addressed by the appropriate authority:

* Unresolved critical security finding
* Unauthorized policy access
* Critical data leakage
* Known fabricated policy responses
* Unresolved critical defect
* Unresolved policy authority conflict affecting retrieval
* Mandatory security control not validated
* Mandatory UAT not completed
* Required governance approval absent
* Release criteria deliberately weakened without appropriate approval

---

# 36. Risk Evidence

Risk decisions should be supported by evidence such as:

* Test results
* Evaluation results
* Security results
* UAT results
* Defect records
* Data-readiness assessments
* Performance measurements
* Monitoring results
* Governance approvals
* Risk acceptance records
* Stakeholder decisions
* Mitigation completion evidence

**No Evidence = Not Yet Accepted.**

---

# 37. Risk Communication

Material risks must be communicated to affected stakeholders.

Risk communication should include:

* Risk description
* Current rating
* Trend
* Impact
* Response
* Risk owner
* Mitigation owner
* Due date
* Required action
* Escalation status
* Release impact
* Decision required

Critical risks should be escalated immediately rather than waiting for the next routine status meeting.

---

# 38. Practical Exercise: Complete The Risk Assessment

## Scenario

The PolicyAssist team reports:

* Retrieval Accuracy: 92%
* Answer Accuracy: 91%
* Hallucination Rate: 1.4%
* Citation Correctness: 98%
* Unsupported Refusal: 100%
* Security testing: Complete
* Authorization testing: Incomplete
* One policy authority conflict remains unresolved
* UAT: Complete
* One High defect remains unresolved
* Monitoring: Partially complete
* Rollback: Documented but not tested
* Governance approval: Pending
* Leadership wants immediate production release

## PM Tasks

Assess:

1. Which risks have materialized?
2. Which risks remain open?
3. Which risks are High or Critical?
4. Which release criteria have failed?
5. Which risks require escalation?
6. Which risks require additional evidence?
7. Which risks can be accepted?
8. Which risks are release blockers?
9. What mitigation actions are required?
10. Who owns each mitigation?
11. When must each mitigation be completed?
12. What evidence proves completion?
13. What is the appropriate release recommendation?

### Expected PM Approach

The PM should not approve production simply because retrieval, answer accuracy, and hallucination targets have passed.

The PM must consider:

* Citation performance below the 100% target
* Incomplete authorization testing
* Unresolved policy authority conflict
* Unresolved High defect
* Incomplete monitoring
* Untested rollback
* Pending governance approval

Each material risk should have an actionable mitigation with:

**Owner + Due Date + Success Criteria + Evidence**

The PM should document the risk-based release recommendation and identify the conditions required before production approval.

---

# 39. Artifact / Output

The completed Risk Register should contain:

* Risk Register
* Risk Categories
* Risk Scoring
* Risk Responses
* Risk Controls
* Risk Owners
* Mitigation Owners
* Mitigation Due Dates
* Mitigation Success Criteria
* Risk Action Tracker
* Risk Triggers
* Risk Escalation Rules
* Residual Risk Assessment
* Risk Acceptance Decisions
* Risk Review Schedule
* Risk Closure Criteria
* Risk Evidence
* Release Risk Assessment

---

# 40. PM Risk Quality Check

Before considering risk management complete:

* [ ] Material risks have been identified.
* [ ] Risks are categorized.
* [ ] Likelihood is assigned.
* [ ] Impact is assigned.
* [ ] Risk scores are calculated.
* [ ] Risk owners are assigned.
* [ ] Response strategies are defined.
* [ ] Mitigation actions are specific and actionable.
* [ ] Every High and Critical risk has a mitigation owner.
* [ ] Every material mitigation has a due date.
* [ ] Every mitigation has measurable success criteria.
* [ ] Required evidence is identified.
* [ ] Preventive controls are identified.
* [ ] Detective controls are identified.
* [ ] Risk triggers are defined.
* [ ] Escalation criteria are defined.
* [ ] Overdue-action rules are defined.
* [ ] Residual risk is assessed.
* [ ] Risk acceptance authority is identified.
* [ ] Release blockers are identified.
* [ ] Evidence is documented.
* [ ] Risks are reviewed regularly.
* [ ] Closed risks have documented closure rationale.

---

# 41. PM Decision

The Risk Register is complete when material risks are:

* Visible
* Categorized
* Scored
* Owned
* Actively mitigated
* Assigned due dates
* Supported by evidence
* Monitored
* Escalated when necessary
* Formally accepted or closed

The PM must ensure that risk acceptance is performed by the appropriate authority and that schedule pressure does not override security, governance, quality, or business risk.

**Final Risk Principles:**

**A Risk Without An Owner Is Not Being Managed.**

**A Mitigation Without A Due Date Is Not Actionable.**

**A Mitigation Without Evidence Is Not Proven Complete.**

**A Risk Without Evidence Is Not Yet Controlled.**

**No Evidence = Not Yet Accepted.**

---

# 42. Connection To The Capstone Portfolio

The Risk Register connects directly to:

* `01-PROJECT-OVERVIEW.md`
* `02-PROJECT-CHARTER.md`
* `03-REQUIREMENTS.md`
* `04-PRODUCT-BACKLOG.md`
* `05-ARCHITECTURE.md`
* `06-DATA-GOVERNANCE.md`
* `07-EVALUATION-PLAN.md`
* `08-RISK-SECURITY-GOVERNANCE.md`
* `09-TEST-UAT-PILOT.md`
* `10-RELEASE-DEPLOYMENT.md`
* `11-MONITORING-CONTINUOUS-IMPROVEMENT.md`
* `12-CAPSTONE-PORTFOLIO.md`
* `13-DECISION-LOG.md`
* `15-TRACEABILITY.md`
* `16-EXECUTIVE-SUMMARY.md`
* `17-FINAL-GO-HOLD-NO-GO.md`

Risk status should directly inform major project decisions, governance decisions, and release readiness.

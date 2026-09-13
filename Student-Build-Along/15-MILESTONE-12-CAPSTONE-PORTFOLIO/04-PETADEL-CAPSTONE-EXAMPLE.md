# Petadel PolicyAssist AI — Completed Capstone Example

**Project Status:** Controlled Release Assessment
**Project Type:** Fictional / Synthetic AI Product
**Organization:** Petadel Technology Services (PTS)
**Role:** Project Manager / Product Manager

---

# How to Use This Example

Use this completed example to see what a strong Artificial Intelligence (AI) Project Management (PM) capstone can look like.

Pay attention to how the project connects:

**Problem → Requirements → Solution → Evidence → Risk → Decision → Outcome → Improvement**

This is a reference example.

Do not submit it as your own work.

---

# 1. Executive Summary

Petadel Technology Services employees were spending unnecessary time searching Google, SharePoint, and departmental folders for company policies. Employees also encountered duplicate, outdated, and conflicting documents, creating uncertainty about which policy version was authoritative. Human Resources (HR) also received repetitive questions that could have been answered through a reliable centralized policy experience.

**PolicyAssist** was proposed as an Artificial Intelligence (AI)-enabled policy assistant that allows employees to ask policy questions in natural language and receive responses grounded in approved policy information.

A central product principle was established:

> **The Large Language Model (LLM) is not the source of truth. Approved policy content is the source of truth.**

The project established measurable requirements for:

* Policy search-time reduction.
* Retrieval accuracy.
* Answer accuracy.
* Unsupported / hallucinated response rate.
* Citation correctness.
* Response latency.
* User satisfaction.
* Security.
* Authorization.
* Human escalation.

The product demonstrated meaningful value and strong performance in several areas. However, answer accuracy, unsupported-response performance, refusal / escalation performance, and user satisfaction remained below target.

The evidence supported a:

**RELEASE DECISION: CONDITIONAL GO**

The product was not approved for unrestricted production deployment.

Because production-specific authorization controls still required implementation and validation, the deployment decision was:

**DEPLOYMENT DECISION: HOLD DEPLOYMENT**

The appropriate ongoing monitoring decision was:

**MONITORING DECISION: IMPROVE**

The overall PM recommendation was:

**IMPROVE**

---

# 2. Business Problem & Users

## Business Problem

Employees did not have a single trusted place to quickly determine which company policy applied to a question.

Employees commonly searched:

* Google.
* SharePoint.
* Department folders.
* Older saved documents.
* Informal employee-created references.

This created:

* Longer policy search times.
* Uncertainty about current versions.
* Duplicate and conflicting information.
* Repetitive HR questions.
* Risk of employees relying on outdated information.

## Primary Users

Employees across Petadel Technology Services.

## Key Stakeholders

| Stakeholder                  | Primary Interest                                                |
| ---------------------------- | --------------------------------------------------------------- |
| Employees                    | Fast and accurate policy answers                                |
| Human Resources              | Authoritative policy information and fewer repetitive questions |
| Information Technology       | Application reliability, security, access, and support          |
| Project / Product Management | Scope, delivery, risk, evaluation, and business value           |
| Executive Leadership         | Business value, risk, and readiness                             |

## Key Stakeholder Trade-off

Employees prioritized speed and convenience.

HR prioritized accuracy, authority, current policy versions, and traceability.

The project therefore balanced:

**Speed + Accuracy + Authority + Traceability**

---

# 3. Requirements, Scope & MVP

## Key Requirements

| Requirement                               |      Target |
| ----------------------------------------- | ----------: |
| Policy search-time reduction              |        ≥50% |
| Retrieval accuracy                        |        ≥90% |
| Answer accuracy                           |        ≥90% |
| Unsupported / hallucinated response rate  |         <2% |
| Citation correctness                      |        100% |
| Unsupported-question refusal / escalation |        100% |
| Response latency                          | ≤10 seconds |
| User satisfaction                         |        ≥85% |
| Critical security incidents               |           0 |
| Unauthorized access issues                |           0 |

## MVP

The Minimum Viable Product (MVP) focused on the core employee experience:

* Ask a policy question.
* Retrieve relevant policy information.
* Generate a grounded response.
* Provide supporting evidence or citation.
* Refuse or escalate when the available evidence does not support an answer.

## Out of Scope

The MVP did not attempt to become a general-purpose employee assistant.

Examples included:

* General employee advice unrelated to approved policies.
* Unapproved policy domains.
* Uncontrolled employee-created knowledge sources.
* Broad enterprise knowledge retrieval without governance.

## Release Scope

The release scope included the approved MVP capabilities plus the controls, fixes, evaluation activities, and readiness requirements necessary for the assessed release stage.

This was intentionally broader than simply defining the original MVP.

---

# 4. AI Solution

## Solution Overview

PolicyAssist uses a retrieval-based AI approach to locate relevant policy content before generating a response.

The core flow is:

**Employee Question → Application Interface → Policy Data → Processing / Embeddings → Vector Database → Retrieval → LLM → Grounded Response → Citation → Employee**

## Major Architecture Decision

A retrieval-based architecture was selected so the product could ground responses in approved policy content rather than relying solely on general model knowledge.

### Reason

The business problem required authoritative and current policy information.

### Trade-off

The approach increased the importance of:

* Data quality.
* Metadata.
* Version control.
* Retrieval relevance.
* Conflict management.

### PM Implication

The architecture reduced reliance on unsupported model knowledge but required stronger data governance and evaluation.

---

# 5. Data & Knowledge

## Policy Sources

The prototype used fictional policy content covering areas such as:

* Employee Leave.
* Attendance.
* Remote Work.
* Information Security.
* Code of Conduct.
* Expense Reimbursement.

## Source of Truth

PolicyAssist treated approved policy content as the source of truth.

Source authority was evaluated using:

* Policy owner.
* Approval status.
* Version.
* Effective date.
* Currency.
* Relevance.

The LLM was not treated as an authoritative source.

## Data / Retrieval Finding

Testing showed that more than one policy could be retrieved for some questions.

For example, a remote-work question could surface both Remote Work and Attendance content.

This created a risk that the system could combine relevant information without clearly identifying which source should control.

## PM Response

The project identified stronger:

* Metadata.
* Source authority.
* Version control.
* Retrieval evaluation.
* Conflict-handling rules.

as necessary controls.

---

# 6. AI Evaluation

The project evaluated retrieval, response, citation, and performance measures separately.

| Metric                                    |  Target | Actual | Status    |
| ----------------------------------------- | ------: | -----: | --------- |
| Retrieval Accuracy                        |    ≥90% |    92% | Pass      |
| Answer Accuracy                           |    ≥90% |    89% | Attention |
| Unsupported / Hallucinated Response Rate  |     <2% |   2.5% | Fail      |
| Citation Correctness                      |    100% |   100% | Pass      |
| Unsupported-Question Refusal / Escalation |    100% |    95% | Fail      |
| Response Latency                          | ≤10 sec |  8 sec | Pass      |
| User Satisfaction                         |    ≥85% |    82% | Attention |
| Critical Security Incidents               |       0 |      0 | Pass      |

## What Worked

* Retrieval accuracy exceeded target.
* Citation correctness met target.
* Response latency met target.
* No critical security incidents were observed.

## What Required Improvement

* Answer accuracy remained below target.
* Unsupported response rate exceeded the acceptable threshold.
* Unsupported-question refusal / escalation was below target.
* User satisfaction remained below target.

## PM Interpretation

The product was demonstrating meaningful value, but the evidence did not support unrestricted production use.

The PM therefore recommended controlled progression with corrective actions and continued monitoring.

---

# 7. Risk, Security & Governance

## Major Risks

| Risk                    | Impact                                         | Mitigation / Control                    | Status                         |
| ----------------------- | ---------------------------------------------- | --------------------------------------- | ------------------------------ |
| Unsupported AI response | Employees receive incorrect policy information | Grounding, evaluation, refusal testing  | Requires improvement           |
| Outdated policy         | Employees receive obsolete guidance            | Version and effective-date controls     | Governance improvement         |
| Conflicting policies    | Inconsistent answers                           | Authority and metadata controls         | Governance improvement         |
| Unauthorized access     | Confidential information exposure              | Authentication / authorization controls | Production validation required |
| Missing escalation      | Unsupported questions receive answers          | Refusal / escalation controls           | Requires improvement           |

## Security Position

Testing recorded:

**0 critical security incidents**

However, zero recorded incidents does not by itself prove complete production security readiness.

Production authorization controls still required implementation and validation.

This distinction is important:

**Security Incidents = 0**

does not necessarily mean:

**Authorization Controls = Fully Production Ready**

## Governance Principle

Policy ownership, approval, versioning, and change management remain organizational responsibilities.

They should not be delegated to the AI model.

---

# 8. Testing & User Acceptance Testing

## Testing Coverage

Testing included:

* Straightforward policy questions.
* Questions using different wording.
* Specific policy details.
* Questions involving multiple policy areas.
* Unsupported questions.
* Citation behavior.
* Response quality.
* User experience.

## Key Testing Findings

The core workflow functioned as intended for supported questions.

However, behavior varied by question.

For example, remote-work questions could surface multiple relevant policies.

An unsupported question about pets was correctly refused and escalated, demonstrating the desired behavior for unsupported content.

## UAT

User Acceptance Testing (UAT) focused on whether employees could:

1. Ask a policy question.
2. Understand the response.
3. Identify supporting evidence.
4. Determine what to do when the system could not answer.

UAT indicated that the core experience was usable, but overall satisfaction remained below the target.

## Testing Conclusion

The product demonstrated a functional and useful core experience, but unresolved quality and production-readiness issues remained.

---

# 9. Release Readiness

Release readiness was assessed using:

* Requirements.
* AI evaluation.
* Testing.
* UAT.
* Security and governance.
* Monitoring.
* Operational readiness.
* Rollback readiness.

## Strengths

* Requirements were substantially addressed.
* Retrieval accuracy exceeded target.
* Citation correctness met target.
* Response latency met target.
* No critical security incidents were observed.
* UAT demonstrated the core experience was usable.
* Release and rollback planning were established.

## Gaps

* Answer accuracy remained below target.
* Unsupported response rate exceeded target and crossed the defined threshold.
* Refusal / escalation performance remained below target.
* User satisfaction remained below target.
* Production authorization controls required additional implementation and validation.

---

# 10. Release Decision

## PM Release Recommendation

**CONDITIONAL GO**

The evidence supported proceeding to a controlled release stage under defined conditions.

This did not represent unrestricted production approval.

## Release Conditions

| Condition                 | Owner                | Required Action                        | Success Measure              |
| ------------------------- | -------------------- | -------------------------------------- | ---------------------------- |
| Unsupported response rate | Product / AI Team    | Reduce unsupported responses           | <2%                          |
| Answer accuracy           | Product / AI Team    | Improve answer quality                 | ≥90%                         |
| Refusal / escalation      | Product / AI Team    | Improve unsupported-question handling  | 100%                         |
| User satisfaction         | Product / UX Team    | Address user feedback                  | ≥85%                         |
| Production authorization  | IT / Security        | Implement and validate access controls | 0 unauthorized-access issues |
| Monitoring                | Product / Operations | Establish ongoing monitoring           | Required monitoring active   |

## Authorized Release Decision

**CONDITIONAL GO**

**Decision Authority:**

Designated Product / Business authority.

The PM provided the readiness assessment and recommendation. The formally designated authority made or confirmed the release decision.

---

# 11. Deployment Decision

## Deployment Decision

**HOLD DEPLOYMENT**

Although the release could proceed under controlled conditions, unrestricted production deployment was not yet appropriate.

The primary remaining issue was the need to implement and validate production-specific authorization controls.

This demonstrates:

**Release Decision: CONDITIONAL GO**

does not automatically equal:

**Deployment Decision: DEPLOY**

The deployment decision must independently consider whether the target environment is ready.

---

# 12. KPI & Monitoring

The project used:

**KPI → Target → Actual → Trend → Threshold → Action**

| KPI                                       |  Target | Actual | Status          | Action                  |
| ----------------------------------------- | ------: | -----: | --------------- | ----------------------- |
| Policy Search-Time Reduction              |    ≥50% |    58% | On Target       | Continue monitoring     |
| Retrieval Accuracy                        |    ≥90% |    92% | On Target       | Maintain                |
| Answer Accuracy                           |    ≥90% |    89% | Attention       | Improve                 |
| Unsupported / Hallucinated Response Rate  |     <2% |   2.5% | Below Threshold | Investigate immediately |
| Citation Correctness                      |    100% |   100% | On Target       | Maintain                |
| Unsupported-Question Refusal / Escalation |    100% |    95% | Attention       | Improve                 |
| Response Latency                          | ≤10 sec |  8 sec | On Target       | Maintain                |
| User Satisfaction                         |    ≥85% |    82% | Attention       | Investigate feedback    |
| Critical Security Incidents               |       0 |      0 | On Target       | Maintain                |

## Monitoring Decision

**IMPROVE**

The unsupported-response rate was the highest-priority performance concern because inaccurate policy guidance could directly affect employee decisions and trust.

Production authorization also remained a critical readiness concern.

---

# 13. Business Outcomes

## Target Outcome

Reduce employee policy search time by at least:

**50%**

## Measured Outcome

The assessment demonstrated:

**58% reduction**

This exceeded the target.

## Additional Evidence

* Retrieval accuracy exceeded target.
* Citation correctness met target.
* Response latency met target.
* No critical security incidents were recorded during the assessed testing.

## Remaining Gaps

* Answer accuracy below target.
* Unsupported response rate above target.
* Refusal / escalation below target.
* User satisfaction below target.
* Production authorization controls not yet fully validated.

## Outcome Status

**PARTIALLY ACHIEVED**

The product demonstrated meaningful value, but not all product quality and experience objectives were achieved.

---

# 14. Continuous Improvement

The priority improvement backlog was:

| Improvement                                  | Priority | Success Measure              |
| -------------------------------------------- | -------- | ---------------------------- |
| Reduce unsupported / hallucinated responses  | High     | <2%                          |
| Improve answer accuracy                      | High     | ≥90%                         |
| Improve refusal / escalation                 | High     | 100%                         |
| Improve user satisfaction                    | Medium   | ≥85%                         |
| Strengthen production authorization controls | Critical | 0 unauthorized-access issues |

## First Priority

**Reduce unsupported AI responses.**

This was prioritized because unsupported policy guidance creates direct employee and organizational risk.

Production authorization controls remain a critical release and deployment requirement.

---

# 15. Lessons Learned

## What Worked

* The project began with a clearly defined business problem.
* Requirements were measurable.
* MVP scope focused on the core user need.
* Retrieval and response quality were evaluated separately.
* Citation correctness was explicitly measured.
* Unsupported questions were included in testing.
* Security and governance were considered before deployment.
* KPI results informed PM decisions.

## What Did Not Work

* Answer accuracy did not reach target.
* Unsupported-response performance remained above threshold.
* User satisfaction remained below target.
* Production authorization controls were not yet fully validated.

## What Would Be Done Differently

The project would introduce stronger negative testing for unsupported questions, conflicting policy retrieval, and authorization scenarios earlier in the lifecycle.

---

# 16. PM Contribution

The PM:

* Defined measurable requirements.
* Established scope and MVP priorities.
* Coordinated stakeholders.
* Evaluated AI quality against defined targets.
* Kept retrieval, response, citation, security, and performance measures separate.
* Identified AI-specific risks.
* Coordinated testing and UAT.
* Assessed release readiness.
* Distinguished release approval from deployment readiness.
* Interpreted KPI performance.
* Recommended corrective actions.
* Communicated evidence and risks to decision-makers.

The PM did not treat the AI model as the source of truth.

The PM also did not equate a functioning prototype with production readiness.

---

# 17. Portfolio Evidence

The strongest portfolio evidence included:

| Evidence                         | Demonstrates                             |
| -------------------------------- | ---------------------------------------- |
| Requirements Record              | Measurable product definition            |
| AI Architecture                  | PM-level technical understanding         |
| Data & Retrieval Assessment      | Source-of-truth and retrieval governance |
| AI Evaluation Results            | Evidence-based AI quality assessment     |
| Security & Governance Assessment | AI risk management                       |
| Testing / UAT Results            | Product validation                       |
| Release Readiness Record         | Release decision-making                  |
| KPI Dashboard                    | Performance management                   |
| PolicyAssist Application         | Applied AI product understanding         |

---

# 18. Interview Talking Points

## What Problem Did You Solve?

Employees spent too much time searching for policies and were uncertain which documents were current and authoritative.

## What Did You Manage?

I managed the product lifecycle from problem definition through requirements, AI evaluation, risk management, testing, release readiness, KPI monitoring, and continuous improvement.

## What Was the Biggest AI Risk?

Providing an incorrect policy answer that appeared authoritative.

## How Did You Address It?

We established authoritative policy sources, evaluated retrieval and response quality separately, measured unsupported responses, required citations, tested unsupported questions, and established human escalation.

## What Did the Evidence Show?

The product exceeded the search-time reduction and retrieval targets and met citation and latency targets. However, answer accuracy, unsupported-response performance, and user satisfaction remained below target.

## What Was Your Release Recommendation?

**Conditional Go** for a controlled release stage.

## What Was the Deployment Decision?

**Hold Deployment** until required production authorization controls were implemented and validated.

---

# 19. Final PM Recommendation

## Recommended Action

**IMPROVE**

Continue the product direction while addressing the remaining quality and production-readiness gaps.

## Strongest Evidence

**58% reduction in policy search time vs. 50% target**

**92% retrieval accuracy vs. 90% target**

**100% citation correctness**

**8-second response latency vs. 10-second target**

**0 critical security incidents**

## Primary Risk

Unsupported or inaccurate policy responses could cause employees to act on incorrect information.

## Next Action

Prioritize:

1. Reducing unsupported responses.
2. Improving answer accuracy.
3. Improving refusal / escalation behavior.
4. Validating production authorization controls.
5. Monitoring user satisfaction.

## Next Review

Reassess release and deployment readiness after corrective actions and validation.

---

# Final Capstone Decision Record

| Decision Element            | Assessment                                                |
| --------------------------- | --------------------------------------------------------- |
| Business Outcome            | Partially Achieved                                        |
| Strongest Evidence          | 58% reduction in policy search time                       |
| Primary Product Risk        | Unsupported / inaccurate AI responses                     |
| Primary Business Risk       | Employees relying on incorrect policy information         |
| PM Release Recommendation   | Conditional Go                                            |
| Authorized Release Decision | Conditional Go                                            |
| Release Decision Authority  | Designated Product / Business authority                   |
| Deployment Decision         | Hold Deployment                                           |
| Monitoring Decision         | Improve                                                   |
| Final PM Recommendation     | Improve                                                   |
| Immediate Action            | Improve response quality and validate production controls |
| Action Owner                | Product / AI / IT / Security teams                        |
| Next Review Point           | After corrective actions and validation                   |

---

# Portfolio Takeaway

The PolicyAssist project demonstrates that an AI product can provide meaningful value without yet being ready for unrestricted production deployment.

The PM responsibility is to understand what the evidence demonstrates, identify remaining risks, distinguish release approval from deployment readiness, and recommend an appropriate path forward.

In this case:

**Strong Business Value + Strong Retrieval + Strong Citation + Acceptable Performance**

were balanced against:

**Response Quality + Unsupported Responses + User Satisfaction + Production Authorization**

The resulting path was:

**CONDITIONAL GO → HOLD DEPLOYMENT → CORRECTIVE ACTION → VALIDATION → DEPLOYMENT REASSESSMENT**

This demonstrates evidence-based AI Project Management.

**Problem → Evidence → Decision → Action → Outcome**

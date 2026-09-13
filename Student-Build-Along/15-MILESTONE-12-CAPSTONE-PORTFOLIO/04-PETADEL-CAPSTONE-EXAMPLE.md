# Petadel PolicyAssist AI — Completed Capstone Example

> **Project Status:** Controlled Release Assessment
> **Project Type:** Fictional / Synthetic AI Product
> **Organization:** Petadel Technology Services (PTS)
> **Role:** Project Manager / Product Manager

## How to Use This Example

Use this completed example as a reference for the level of evidence, analysis, and PM judgment expected in your own capstone.

Pay attention to how the example connects:

**Problem → Evidence → Decision → Action → Outcome**

Do not copy the example as your own work.

---

# 1. Executive Summary

Petadel Technology Services employees were spending unnecessary time searching Google, SharePoint, and departmental folders for company policies. Employees also encountered duplicate, outdated, and conflicting documents, creating uncertainty about which policy version was authoritative. Human Resources (HR) received repetitive questions that could have been answered through a reliable centralized policy experience.

**PolicyAssist** was proposed as an Artificial Intelligence (AI)-enabled policy assistant that allows employees to ask policy questions in natural language and receive responses grounded in approved policy information.

The product was designed around a critical principle:

**The Large Language Model (LLM) is not the source of truth. Approved policy content is the source of truth.**

The project established requirements for retrieval accuracy, response accuracy, unsupported response reduction, citation correctness, response time, user satisfaction, security, authorization, and escalation.

Evaluation demonstrated strong performance in several areas, including retrieval accuracy, citation correctness, response latency, and security incident prevention. However, answer accuracy, unsupported-response performance, refusal/escalation performance, and user satisfaction remained below target.

The evidence supported a **CONDITIONAL GO** for a controlled release stage with defined corrective actions and monitoring.

Production deployment was **not automatically approved** because production-specific access and authorization controls still required implementation and validation.

---

# 2. Business Problem

## The Problem

Employees had no single trusted place to quickly determine which company policy applied to a question.

They commonly searched:

* Google.
* SharePoint.
* Department folders.
* Older saved documents.
* Informal employee-created references.

This created several problems:

* Time spent locating policies.
* Uncertainty about current versions.
* Duplicate or conflicting documents.
* Repetitive HR questions.
* Risk of employees relying on outdated information.

## Business Goal

The project targeted:

**At least a 50% reduction in policy search time**

while improving the accuracy, consistency, and confidence of policy responses.

---

# 3. Users & Stakeholders

## Primary Users

Employees across Petadel Technology Services.

## Key Stakeholders

| Stakeholder                  | Interest                                                  |
| ---------------------------- | --------------------------------------------------------- |
| Employees                    | Fast, accurate policy answers                             |
| Human Resources              | Reduced repetitive questions and authoritative policy use |
| Information Technology       | Application reliability, access, and support              |
| Project / Product Management | Scope, delivery, risk, evaluation, and business value     |
| Executive Leadership         | Business value, risk, and readiness                       |

## Major Stakeholder Consideration

Employees wanted fast answers, while HR required confidence that responses were based on approved and current policy information.

The project therefore prioritized:

**Speed + Accuracy + Authority + Traceability**

---

# 4. Requirements, Scope & MVP

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
* Refuse or escalate when the available information does not support an answer.

## Out of Scope

The MVP did not attempt to become a general-purpose employee assistant.

Examples of excluded capabilities included:

* General employee advice unrelated to approved policy content.
* Unsupported policy domains.
* Uncontrolled employee-created knowledge sources.
* Broad enterprise knowledge retrieval without governance.

---

# 5. AI Solution

## Solution Flow

**Employee Question → Application Interface → Policy Data → Processing / Embeddings → Vector Database → Retrieval → LLM → Grounded Response → Citation → Employee**

The design separated the authoritative policy content from the language model.

The AI generated the response, but the policy content supplied the information used to ground the response.

## Major Architecture Decision

A retrieval-based architecture was selected so PolicyAssist could locate relevant policy content before generating an answer.

### Reason

The product required answers grounded in approved policy information rather than relying solely on general model knowledge.

### Trade-off

Retrieval introduced additional complexity around:

* Source quality.
* Metadata.
* Versioning.
* Retrieval relevance.
* Conflicting documents.

### PM Implication

The architecture reduced reliance on unsupported model knowledge but increased the importance of disciplined data management and retrieval evaluation.

---

# 6. Data & Knowledge

## Policy Sources

The PolicyAssist prototype used approved fictional policy content covering areas such as:

* Employee Leave.
* Attendance.
* Remote Work.
* Information Security.
* Code of Conduct.
* Expense Reimbursement.

## Source-of-Truth Approach

PolicyAssist treated approved policy content as the source of truth.

Policy authority was evaluated using:

* Policy owner.
* Approval status.
* Version.
* Effective date.
* Relevance.
* Currency.

The LLM itself was not treated as an authoritative source.

## Data / Retrieval Finding

Testing demonstrated that retrieval could surface more than one potentially relevant policy.

For example, remote-work questions could retrieve both Remote Work and Attendance content.

This created a risk that the system could combine information from multiple sources without adequately distinguishing primary authority.

## PM Response

The project identified stronger metadata, source authority, version control, and retrieval evaluation as necessary controls.

---

# 7. AI Evaluation

The product was evaluated using separate response and citation measures.

| Metric                                    |  Target | Actual | Status    |
| ----------------------------------------- | ------: | -----: | --------- |
| Retrieval Accuracy                        |    ≥90% |    92% | Pass      |
| Answer Accuracy                           |    ≥90% |    89% | Attention |
| Unsupported Response Rate                 |     <2% |   2.5% | Fail      |
| Citation Correctness                      |    100% |   100% | Pass      |
| Unsupported-Question Refusal / Escalation |    100% |    95% | Fail      |
| Response Latency                          | ≤10 sec |  8 sec | Pass      |
| User Satisfaction                         |    ≥85% |    82% | Attention |
| Critical Security Incidents               |       0 |      0 | Pass      |

## Evaluation Findings

PolicyAssist demonstrated strong retrieval, citation, latency, and security results.

However, the product did not meet every quality target.

The most significant gaps were:

* Unsupported response rate remained above the <2% target.
* Answer accuracy remained below the 90% target.
* Unsupported questions were not refused or escalated 100% of the time.
* User satisfaction remained below the 85% target.

## PM Interpretation

The evidence demonstrated meaningful product value, but it did not support unrestricted production use.

The appropriate PM response was to continue the product direction while addressing the identified quality and readiness gaps.

---

# 8. Risk, Security & Governance

## Major Risks

| Risk                    | Impact                                         | Mitigation                              | Status                         |
| ----------------------- | ---------------------------------------------- | --------------------------------------- | ------------------------------ |
| Unsupported AI response | Employees receive incorrect policy information | Evaluation, grounding, refusal testing  | Requires improvement           |
| Outdated policy         | Incorrect employee guidance                    | Version and effective-date controls     | Requires governance            |
| Conflicting policies    | Inconsistent answers                           | Authority and metadata controls         | Requires governance            |
| Unauthorized access     | Confidential information exposure              | Authentication / authorization controls | Production validation required |
| Missing escalation      | Employee receives unsupported answer           | Refusal and escalation testing          | Requires improvement           |

## Security Position

The evaluation recorded:

**0 critical security incidents**

This result does not, by itself, prove complete production security readiness.

Production authorization controls must be implemented and validated before unrestricted employee deployment.

## Governance Principle

Policy ownership, approval, versioning, and change management must remain outside the language model.

---

# 9. Testing & User Acceptance Testing

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

## Testing Findings

The system generally demonstrated the intended core workflow.

However, testing showed that retrieval and response behavior could vary depending on the question.

A remote-work question could surface more than one relevant policy.

An unsupported question about pets was correctly handled through refusal and escalation, demonstrating the desired behavior for unsupported content.

## User Acceptance Testing

User Acceptance Testing (UAT) focused on whether an employee could:

1. Ask a policy question.
2. Understand the response.
3. Identify supporting evidence.
4. Determine what to do when the system could not answer.

UAT indicated that the core experience was usable, but overall satisfaction remained below the 85% target.

## Testing / UAT Conclusion

The evidence supported continued product improvement.

Known limitations were documented rather than treated as passing results.

---

# 10. Release Readiness

Release readiness was assessed using evidence from:

* Requirements.
* AI evaluation.
* Security and governance.
* Testing.
* UAT.
* Monitoring.
* Operational readiness.

## Strengths

* Retrieval accuracy exceeded target.
* Citation correctness met target.
* Response latency met target.
* No critical security incidents were observed.
* Core employee question-answering workflow functioned.

## Remaining Gaps

* Answer accuracy below target.
* Unsupported response rate above target.
* Refusal / escalation below target.
* User satisfaction below target.
* Production authorization controls required further validation.

---

# 11. Release Decision

## PM Release Recommendation

**CONDITIONAL GO**

The evidence supported proceeding to a controlled release stage with defined conditions.

This was **not** an unrestricted production approval.

## Release Conditions

| Condition                 | Owner                | Required Action                       | Success Measure              |
| ------------------------- | -------------------- | ------------------------------------- | ---------------------------- |
| Unsupported response rate | Product / AI team    | Reduce unsupported responses          | <2%                          |
| Answer accuracy           | Product / AI team    | Improve response quality              | ≥90%                         |
| Refusal / escalation      | Product / AI team    | Improve unsupported-question handling | 100%                         |
| User satisfaction         | Product / UX team    | Address user feedback                 | ≥85%                         |
| Production authorization  | IT / Security        | Implement and validate controls       | 0 unauthorized-access issues |
| Monitoring                | Product / Operations | Establish ongoing monitoring          | Required monitoring active   |

## Authorized Release Decision

**Authorized Decision:** Conditional Go

**Decision Authority:** Designated Product / Business authority

The Project Manager provides the readiness assessment and recommendation. The formally designated authority makes or confirms the release decision.

---

# 12. Deployment Decision

## Deployment Decision

**HOLD DEPLOYMENT**

The release may proceed through the approved controlled-release stage, but unrestricted production deployment should not occur until the required production-specific controls are implemented and validated.

This demonstrates the difference between:

**Release Decision: CONDITIONAL GO**

and:

**Deployment Decision: HOLD DEPLOYMENT**

Release approval does not automatically authorize deployment.

---

# 13. KPI & Monitoring

The KPI framework used:

**KPI → Target → Actual → Trend → Threshold → Action**

| KPI                                       |  Target | Actual | Status          | PM Action               |
| ----------------------------------------- | ------: | -----: | --------------- | ----------------------- |
| Policy Search-Time Reduction              |     50% |    58% | On Target       | Continue monitoring     |
| Retrieval Accuracy                        |     90% |    92% | On Target       | Maintain                |
| Answer Accuracy                           |     90% |    89% | Attention       | Improve                 |
| Unsupported / Hallucinated Response Rate  |     <2% |   2.5% | Below Threshold | Immediate investigation |
| Citation Correctness                      |    100% |   100% | On Target       | Maintain                |
| Unsupported-Question Refusal / Escalation |    100% |    95% | Attention       | Improve                 |
| Response Latency                          | ≤10 sec |  8 sec | On Target       | Maintain                |
| User Satisfaction                         |     85% |    82% | Attention       | Investigate feedback    |
| Critical Security Incidents               |       0 |      0 | On Target       | Maintain                |

## Monitoring Decision

**IMPROVE**

The strongest improvement priority was reducing unsupported responses because an incorrect policy answer could directly affect employee decisions and trust.

---

# 14. Business Outcome

## Target

Reduce employee policy search time by at least:

**50%**

## Measured Result

The assessment showed:

**58% reduction**

This exceeded the target.

## Additional Results

PolicyAssist also demonstrated:

* Retrieval accuracy above target.
* Citation correctness at target.
* Response latency within target.
* No critical security incidents during the assessed testing.

However:

* Answer accuracy remained below target.
* Unsupported response rate remained above target.
* Unsupported-question refusal / escalation remained below target.
* User satisfaction remained below target.

## Outcome Status

**PARTIALLY ACHIEVED**

The product demonstrated meaningful business value, but not all product quality and experience objectives had been achieved.

---

# 15. Continuous Improvement

The highest-priority improvement areas were:

| Improvement                                       | Priority | Success Measure              |
| ------------------------------------------------- | -------- | ---------------------------- |
| Reduce unsupported / hallucinated responses       | High     | <2%                          |
| Improve answer accuracy                           | High     | ≥90%                         |
| Improve unsupported-question refusal / escalation | High     | 100%                         |
| Improve user satisfaction                         | Medium   | ≥85%                         |
| Strengthen production authorization controls      | Critical | 0 unauthorized-access issues |

## First Improvement Priority

**Reduce unsupported AI responses.**

This was prioritized because an incorrect policy answer could directly affect employee behavior and undermine trust in the product.

---

# 16. Lessons Learned

## What Worked

* The product focused on a specific employee problem.
* Requirements were measurable.
* Retrieval and response quality were evaluated separately.
* Citation correctness was explicitly measured.
* Unsupported questions were included in testing.
* Security and governance were considered before deployment.
* KPI results were used to support PM decisions.

## What Did Not Work

* Response quality did not consistently meet all targets.
* Unsupported-response performance remained above the acceptable threshold.
* User satisfaction remained below target.
* Production authorization requirements were not yet fully validated.

## What Would Be Done Differently

The project would establish stronger evaluation coverage for unsupported questions, conflicting policy retrieval, and authorization scenarios earlier in the lifecycle.

---

# 17. PM Contribution

The PM role included:

* Defining measurable requirements.
* Establishing product scope and MVP priorities.
* Coordinating stakeholder needs.
* Evaluating AI quality against defined targets.
* Separating retrieval, response, citation, security, and performance measures.
* Identifying AI-specific risks.
* Coordinating testing and UAT.
* Assessing release readiness.
* Distinguishing release approval from deployment readiness.
* Interpreting KPI results.
* Recommending corrective actions.
* Communicating evidence and risk to decision-makers.

The PM did not treat the AI model as the source of truth and did not equate a working prototype with production readiness.

---

# 18. Portfolio Evidence

Selected evidence included:

| Evidence                         | Demonstrates                             |
| -------------------------------- | ---------------------------------------- |
| Requirements record              | Measurable product definition            |
| AI architecture                  | PM-level technical understanding         |
| Data & Retrieval Assessment      | Source-of-truth and retrieval governance |
| AI Evaluation Results            | Evidence-based AI quality assessment     |
| Security & Governance Assessment | AI risk management                       |
| Testing / UAT Results            | Product validation                       |
| Release Readiness Record         | Release decision-making                  |
| KPI Dashboard                    | Performance management                   |
| PolicyAssist application         | Applied AI product understanding         |

---

# 19. Interview Talking Points

## What Problem Did You Solve?

Employees spent too much time searching for policies and were uncertain which documents were current and authoritative.

## What Did You Manage?

I managed the product lifecycle from problem definition through requirements, AI evaluation, risk management, testing, release readiness, KPI monitoring, and continuous improvement.

## What Was the Biggest AI Risk?

Providing an incorrect policy answer that appeared authoritative.

## How Did You Address It?

We established authoritative policy sources, evaluated retrieval and response quality separately, measured unsupported responses, required citations, tested unsupported questions, and established human escalation.

## What Did the Evidence Show?

The product exceeded the search-time reduction and retrieval targets and met citation and latency targets, but answer accuracy, unsupported-response performance, and user satisfaction still required improvement.

## What Was Your Recommendation?

I recommended **Conditional Go** for a controlled release stage, while keeping **deployment on hold** until required production controls were implemented and validated.

---

# 20. Final PM Recommendation

## Recommended Action

**IMPROVE**

Continue the product direction while addressing the remaining quality and production-readiness gaps.

## Strongest Evidence

* Search-time reduction: **58% vs. 50% target**
* Retrieval accuracy: **92% vs. 90% target**
* Citation correctness: **100%**
* Response latency: **8 seconds vs. ≤10-second target**
* Critical security incidents: **0**

## Primary Risk

Unsupported or inaccurate policy responses could cause employees to act on incorrect information.

## Required Next Action

Prioritize response-quality improvements and production authorization controls.

## Next Review

Reassess release and deployment readiness after corrective actions and validation.

---

# Final Capstone Decision Record

| Decision Element            | Assessment                                                   |
| --------------------------- | ------------------------------------------------------------ |
| Business Outcome            | Partially Achieved                                           |
| Strongest Evidence          | 58% reduction in policy search time                          |
| Primary Product Risk        | Unsupported / inaccurate AI responses                        |
| Primary Business Risk       | Employees relying on incorrect policy information            |
| PM Release Recommendation   | Conditional Go                                               |
| Authorized Release Decision | Conditional Go                                               |
| Release Decision Authority  | Designated Product / Business authority                      |
| Deployment Decision         | Hold Deployment                                              |
| Monitoring Decision         | Improve                                                      |
| Final PM Recommendation     | Improve                                                      |
| Immediate Action            | Improve AI response quality and validate production controls |
| Action Owner                | Product / AI / IT / Security teams                           |
| Next Review Point           | After corrective actions and validation                      |

---

# Portfolio Takeaway

The PolicyAssist project demonstrates an important AI Project Management principle:

**A product can demonstrate meaningful value without being ready for unrestricted production deployment.**

The PM's responsibility is to understand what the evidence demonstrates, identify what remains unresolved, distinguish release readiness from deployment readiness, and make a defensible recommendation.

In this case:

**Business Value + Strong Retrieval + Strong Citation + Acceptable Performance**

were balanced against:

**Response Quality + Unsupported Responses + User Satisfaction + Production Authorization**

The resulting decision was:

**CONDITIONAL GO → HOLD DEPLOYMENT → CORRECTIVE ACTION → VALIDATION → DEPLOYMENT REASSESSMENT**

That is evidence-based AI Project Management.

**Problem → Evidence → Decision → Action → Outcome**

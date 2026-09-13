# Milestone 13 — Final Assessment

## Instructions

Answer all **15 questions**.

Use the concepts, frameworks, evidence, and PM practices taught throughout the course.

For scenario-based questions, explain your reasoning rather than providing only a conclusion.

Where numerical evidence is provided, use it in your analysis.

Where evidence is incomplete, identify the gap rather than inventing information.

---

# Section 1 — AI Project Management Knowledge

## Question 1 — AI Project Management

What is the primary role of a Project Manager (PM) when managing an Artificial Intelligence (AI) product?

Explain how managing an AI product differs from managing a traditional technology project.

---

## Question 2 — Business Problem

Why should an AI project begin with a clearly defined business problem rather than the AI technology itself?

Provide an example of how a poorly defined business problem could lead to an unsuccessful AI product.

---

## Question 3 — Minimum Viable Product

What is a **Minimum Viable Product (MVP)**?

Explain why an MVP is useful when developing an AI product.

How is MVP scope different from the scope of a later release?

---

## Question 4 — RACI

What is a **Responsible, Accountable, Consulted, and Informed (RACI)** matrix?

Explain how a PM could use it to clarify ownership on an AI project.

---

## Question 5 — Source of Truth

Why is it important for an AI product such as PolicyAssist to identify authoritative information?

Explain why the **Large Language Model (LLM)** should not automatically be treated as the source of truth.

---

# Section 2 — Scenario-Based PM Judgment

## Question 6 — Scope Change

During development, a stakeholder asks to add a new AI capability that was not included in the approved scope.

The feature could provide value, but adding it would increase delivery time and introduce additional security and testing requirements.

What should the PM do?

Explain your recommendation, including:

* Scope impact.
* Business value.
* Risk.
* Dependencies.
* Impact to the MVP or release.
* Decision-making and approval.

---

## Question 7 — AI Evaluation

PolicyAssist produces the following results:

| Metric                                   |      Target |    Actual |
| ---------------------------------------- | ----------: | --------: |
| Retrieval Accuracy                       |        ≥90% |       92% |
| Answer Accuracy                          |        ≥90% |       89% |
| Unsupported / Hallucinated Response Rate |         <2% |      2.5% |
| Citation Correctness                     |        100% |      100% |
| Response Time                            | ≤10 seconds | 8 seconds |

What do these results tell you?

Which issue should receive the greatest attention and why?

Should the PM recommend proceeding without changes?

Explain your reasoning.

---

## Question 8 — Data Governance

Two policy documents contain different answers to the same employee question.

Document A is an approved policy, Version 2.0, effective January 1, 2026.

Document B is an older employee-created document with no approval information.

PolicyAssist retrieves both.

What should the PM expect the product to do?

Explain how authority, version, effective date, and governance should influence the result.

---

## Question 9 — Security & Authorization

An employee asks PolicyAssist a question about information that belongs to a restricted department.

The system retrieves and displays the restricted information even though the employee is not authorized to access it.

What should the PM do?

Explain:

* Why the issue matters.
* Whether the issue should block release.
* What immediate action is required.
* What control should prevent the problem.
* What additional testing should be performed.

---

## Question 10 — User Acceptance Testing

PolicyAssist passes technical testing.

The application responds correctly, retrieves the expected policy, and produces a technically accurate answer.

However, User Acceptance Testing (UAT) participants report that the responses are difficult to understand and do not clearly explain what the employee should do next.

Should UAT be considered successful?

Explain why or why not.

What should the PM recommend?

---

# Section 3 — Release Decision

## Question 11 — Release Readiness

PolicyAssist has the following results:

| Area                                     | Result    |
| ---------------------------------------- | --------- |
| Requirements                             | Complete  |
| Critical Defects                         | 0         |
| UAT                                      | Passed    |
| Retrieval Accuracy                       | 92%       |
| Answer Accuracy                          | 89%       |
| Unsupported / Hallucinated Response Rate | 2.5%      |
| Citation Correctness                     | 100%      |
| Response Time                            | 8 seconds |
| User Satisfaction                        | 82%       |
| Critical Security Incidents              | 0         |
| Release Plan                             | Complete  |
| Rollback Plan                            | Complete  |

Targets are:

* Retrieval Accuracy: ≥90%
* Answer Accuracy: ≥90%
* Unsupported / Hallucinated Response Rate: <2%
* Citation Correctness: 100%
* Response Time: ≤10 seconds
* User Satisfaction: ≥85%
* Critical Security Incidents: 0

### Select the strongest release recommendation:

**A. GO**

**B. CONDITIONAL GO**

**C. HOLD**

**D. NO-GO**

Explain your decision.

Your response should address:

* Which targets were met.
* Which targets were missed.
* The severity of the failures.
* Business or user impact.
* Risk.
* Whether the product can reasonably proceed to the intended release stage.
* Conditions that would be required, if applicable.

Remember:

**GO = Proceed**

**CONDITIONAL GO = Proceed under defined conditions**

**HOLD = Do not proceed yet because required evidence, remediation, validation, or readiness work is incomplete**

**NO-GO = Do not release the current version**

A strong answer may select a different option when the reasoning is well supported by the evidence.

---

# Section 4 — KPI Analysis

## Question 12 — KPI Decision

After release, PolicyAssist reports:

| KPI                                       |      Target |    Actual |
| ----------------------------------------- | ----------: | --------: |
| Policy Search-Time Reduction              |         50% |       58% |
| Retrieval Accuracy                        |         90% |       92% |
| Answer Accuracy                           |         90% |       89% |
| Unsupported / Hallucinated Response Rate  |         <2% |      2.5% |
| Citation Correctness                      |        100% |      100% |
| Unsupported-Question Refusal / Escalation |        100% |       95% |
| Response Latency                          | ≤10 seconds | 8 seconds |
| User Satisfaction                         |         85% |       82% |
| Critical Security Incidents               |           0 |         0 |

Which KPI should receive the highest priority for PM action?

Explain:

* Why you selected it.
* What risk it creates.
* What action you would recommend.
* What other metrics should be considered alongside it.

Use:

**KPI → Target → Actual → Trend / Threshold → Action**

---

# Section 5 — Executive Recommendation

## Question 13 — Executive Communication

Your executive sponsor asks:

> "Is PolicyAssist ready, and what should we do next?"

Prepare a concise executive recommendation.

Your response should include:

* Current product status.
* Strongest evidence.
* Most significant risk.
* Business value.
* Recommended action.
* What needs to happen next.

Communicate the decision without unnecessary technical detail.

---

# Section 6 — End-to-End AI PM Challenge

## Question 14 — End-to-End AI Project

Imagine you are assigned to manage a new AI product.

The organization has identified a business problem, but the product has not yet been defined.

Describe how you would manage the initiative from initiation through continuous improvement.

Your response should cover:

1. Business problem.
2. Users and stakeholders.
3. Requirements.
4. Scope and MVP.
5. AI solution.
6. Data and knowledge.
7. AI evaluation.
8. Security and governance.
9. Testing and UAT.
10. Release readiness.
11. Deployment.
12. KPI monitoring.
13. Business outcomes.
14. Continuous improvement.

Explain the major PM decisions you would make throughout the lifecycle.

---

# Section 7 — Reflection

## Question 15 — PM Reflection

Reflect on what you learned from managing an AI product.

Address:

* What concept became most important to you?
* What AI-specific risk would you pay more attention to now?
* What PM skill did you strengthen?
* What would you approach differently on your next AI project?
* How has your understanding of AI Project Management changed?

Use specific examples where possible.

---

# Final Assessment Reminder

Strong answers demonstrate:

**Understanding → Application → Evidence → PM Judgment**

Do not focus only on whether an AI system technically works.

Consider:

**Business Value → Product Quality → Risk → Governance → Readiness → Outcome**

When evidence is incomplete, say what is missing.

When a risk is significant, explain its impact.

When a metric misses target, explain what the miss means.

When making a release recommendation, distinguish:

**PM Recommendation**

from:

**Authorized Release Decision**

When considering deployment, distinguish:

**Release Decision**

from:

**Deployment Decision**

---

# Final Decision Framework

Use these terms consistently throughout your assessment.

## Release Decision

**GO / CONDITIONAL GO / HOLD / NO-GO**

## Deployment Decision

**DEPLOY / HOLD DEPLOYMENT / ROLLBACK**

## Monitoring Decision

**CONTINUE / IMPROVE / ESCALATE / REASSESS**

## Final PM Recommendation

**CONTINUE / IMPROVE / ESCALATE / REASSESS / SCALE**

---

# Final Submission Checklist

* [ ] All 15 questions answered.
* [ ] Scenario responses include reasoning.
* [ ] Numerical evidence is used where provided.
* [ ] AI evaluation concepts are applied correctly.
* [ ] Data and retrieval are distinguished from response quality.
* [ ] Security and authorization risks are treated appropriately.
* [ ] UAT is distinguished from technical testing.
* [ ] Release terminology is used correctly.
* [ ] Deployment terminology is used correctly.
* [ ] KPI analysis connects targets to action.
* [ ] Recommendations are supported by evidence.
* [ ] Missing evidence is identified rather than invented.
* [ ] Answers reflect your own understanding.

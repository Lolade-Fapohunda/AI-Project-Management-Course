# Petadel PolicyAssist AI — Completed Capstone Example

## Instructor Reference Project

This is the completed capstone example for the Petadel PolicyAssist AI project.

It demonstrates how the Project Management (PM) artifacts developed throughout the course can be integrated into a complete AI product lifecycle.

This example is provided to demonstrate the **standard expected for a completed capstone**.

Students may:

* Follow this project as the reference example.
* Build their own version of PolicyAssist.
* Apply the same PM process to their own AI product or use case.

---

# 1. Project Overview

**Organization:**
Petadel Technology Services (PTS)

**Project:**
Petadel PolicyAssist AI

**Project Type:**
Internal Artificial Intelligence (AI) policy-assistance product

**Project Role:**
AI Project Manager / Project Manager

**Product Status:**
Reference implementation / completed capstone

### Project Objective

Create an AI-enabled policy assistance solution that allows employees to locate, retrieve, understand, and reference authoritative organizational policies more efficiently while reducing the risk of unsupported or inaccurate answers.

### Core Product Principle

**Retrieve → Ground → Answer → Cite**

If sufficient authoritative evidence is unavailable:

**Do Not Invent → Refuse or Escalate**

---

# 2. Business Problem

Organizations may maintain thousands of policy documents across departments and repositories.

Employees may have difficulty determining:

* Which policy applies.
* Where the policy is located.
* Whether the document is current.
* Which version is authoritative.
* Whether they are authorized to access the information.
* How the policy applies to their question.

A large document repository does not automatically create an effective policy-access experience.

The project therefore focused on creating a controlled AI-assisted policy retrieval and response experience.

---

# 3. Users & Stakeholders

## Primary Users

The primary users are employees seeking answers to policy-related questions.

## Key Stakeholders

Representative stakeholder groups include:

* Employees.
* Human Resources.
* Finance.
* Department leadership.
* Information Technology.
* Security.
* Governance/compliance stakeholders.
* Product/project leadership.

## Stakeholder Considerations

Important stakeholder concerns include:

* Accuracy.
* Authority of policy sources.
* Data access.
* Security.
* Privacy.
* Ease of use.
* Response speed.
* Trust in AI-generated answers.
* Human escalation.

### PM Takeaway

The project demonstrates that AI product management requires coordination between business users, technical teams, governance stakeholders, and product owners.

---

# 4. Business Requirements

The solution was designed around measurable business and product outcomes.

Key requirements included:

* Reduce employee policy search time by at least 50%.
* Provide retrieval accuracy of at least 90%.
* Provide answer accuracy of at least 90%.
* Maintain hallucination below 2%.
* Provide 100% citation correctness.
* Correctly refuse unsupported questions.
* Keep response latency at or below 10 seconds.
* Achieve user satisfaction of at least 85%.
* Maintain zero critical security incidents.

The requirements establish measurable success criteria rather than simply requiring that an AI chatbot be created.

---

# 5. Scope

## In Scope

* Policy document ingestion.
* Policy document retrieval.
* Semantic search.
* Authoritative-source identification.
* AI-generated grounded responses.
* Source citations.
* Unsupported-question handling.
* Access-control considerations.
* AI evaluation.
* Security and governance.
* Testing and UAT.
* Deployment.
* KPI monitoring.
* Continuous improvement.

## Out of Scope

The project does not attempt to:

* Replace policy owners.
* Replace organizational governance.
* Make independent policy decisions.
* Authorize employee access outside established controls.
* Guarantee an answer when authoritative evidence is unavailable.

### PM Takeaway

The scope deliberately positions AI as an assistance and retrieval capability rather than as the final authority on organizational policy.

---

# 6. Product Strategy & MVP

## Product Vision

Enable employees to obtain faster, evidence-based access to authoritative policy information while maintaining appropriate controls around accuracy, access, governance, and escalation.

## Minimum Viable Product (MVP)

The MVP focuses on the essential workflow:

**Policy Documents → Retrieval → Grounded AI Response → Citation**

The MVP establishes the foundation needed to validate:

* Retrieval.
* Grounding.
* Answer generation.
* Citation.
* Unsupported-question handling.

Additional improvements can be introduced through the product backlog and continuous-improvement process.

---

# 7. AI Solution

## Architecture

The reference implementation uses the following architecture:

**Policy Documents → Chunking → Embeddings → Vector Database → Retrieval → Large Language Model (LLM) → Grounding/Citation → User Interface**

## Technology Components

The reference implementation uses:

* Python.
* Streamlit.
* Sentence Transformers.
* `all-MiniLM-L6-v2` embeddings.
* ChromaDB vector database.
* Google Gen AI SDK.
* Gemini 2.5 Flash as the primary cloud Large Language Model (LLM).
* Ollama / Llama 3.2 3B as a local fallback.
* pytest for testing.
* Streamlit Community Cloud for deployment.

## PM-Level Technical Decision

The technical architecture supports semantic retrieval before generation.

This allows the product to ground its response in retrieved policy evidence rather than relying only on the model's general knowledge.

### Key PM Principle

The Project Manager does not need to become an AI engineer.

The PM needs to understand:

**What the component does → Why it is needed → What risk it introduces → How it will be evaluated.**

---

# 8. Data & Knowledge Management

## Core Data Challenge

Policy documents are only useful when the system can identify relevant and authoritative information.

Important data-management concerns include:

* Duplicate policies.
* Outdated policies.
* Different departmental versions.
* Missing metadata.
* Scanned PDF documents.
* Irrelevant documents.
* Unauthorized information.
* Conflicting policy versions.

## Authority Rule

A policy document is eligible for authoritative retrieval only when it satisfies the required governance conditions:

**Active + Authoritative + Approved + Required Metadata Present**

This prevents the system from treating every document in the repository as equally trustworthy.

---

# 9. AI Evaluation

The project uses measurable AI quality targets.

| KPI                          |  Target | Reference Actual | Status          |
| ---------------------------- | ------: | ---------------: | --------------- |
| Policy Search-Time Reduction |    ≥50% |              58% | On Target       |
| Retrieval Accuracy           |    ≥90% |              92% | On Target       |
| Answer Accuracy              |    ≥90% |              89% | Needs Attention |
| Hallucination Rate           |     <2% |             2.5% | Below Threshold |
| Citation Correctness         |    100% |             100% | On Target       |
| Unsupported-Question Refusal |    100% |              95% | Needs Attention |
| Response Latency             | ≤10 sec |            8 sec | On Target       |
| User Satisfaction            |    ≥85% |              82% | Needs Attention |
| Critical Security Incidents  |       0 |                0 | On Target       |

## Evaluation Interpretation

The dashboard shows that the product has several strong performance indicators.

However, not all targets are satisfied.

The most significant concerns are:

* Hallucination rate above the approved target.
* Answer accuracy below target.
* Unsupported-question refusal below target.
* User satisfaction below target.

### PM Decision

The product should **not be treated as fully optimized simply because several KPIs are on target**.

The AI quality gaps require corrective action.

This demonstrates an important PM principle:

> **A good dashboard does not automatically mean a good product. The PM must interpret the evidence.**

---

# 10. Risk, Security & Governance

## Major AI Risks

### Hallucination

The system may generate information that is not supported by authoritative policy evidence.

**Control:**

Ground responses in retrieved policy evidence and refuse or escalate when sufficient evidence is unavailable.

### Incorrect Retrieval

The system may retrieve an irrelevant policy.

**Control:**

Use semantic retrieval thresholds and evaluate retrieval accuracy.

### Outdated Policy

The system may retrieve an obsolete version.

**Control:**

Apply policy authority and status rules before documents become eligible for retrieval.

### Unauthorized Access

Employees may attempt to retrieve information they are not authorized to access.

**Control:**

Access authority must be considered before exposing policy information.

### Human Escalation

Some questions should not be answered solely by AI.

**Control:**

Unsupported or insufficiently grounded questions should be refused or escalated.

---

# 11. Governance Principle

The product follows:

**Retrieve → Ground → Answer → Cite**

When evidence is insufficient:

**Do Not Invent → Refuse or Escalate**

This creates an explicit boundary around what the AI system should and should not do.

---

# 12. Testing

Testing addresses more than whether the application runs.

The project considers:

* Functional behavior.
* Retrieval quality.
* Answer quality.
* Citation correctness.
* Hallucination.
* Unsupported questions.
* Response latency.
* Security.
* Unauthorized access.
* Regression behavior.
* User acceptance.

## Testing Principle

A technically functioning AI product is not necessarily a production-ready AI product.

The PM must evaluate:

**Functionality + Quality + Security + User Acceptance + Business Readiness**

---

# 13. User Acceptance Testing

UAT evaluates whether the product actually meets user needs.

Representative UAT scenarios include:

* Finding a known policy.
* Asking a question requiring policy retrieval.
* Receiving a response with supporting citations.
* Asking a question where evidence is insufficient.
* Testing whether unsupported information is refused.
* Verifying that users can understand the response.
* Evaluating response usefulness.

### UAT Decision

The PM should use documented UAT results, user feedback, and acceptance criteria to determine whether the product is acceptable for the intended release stage.

---

# 14. Release Readiness

Release readiness should be assessed across:

* Requirements.
* Acceptance criteria.
* AI evaluation.
* Security.
* Testing.
* UAT.
* Monitoring.
* Support.
* Rollback.

The release decision should not be based solely on whether the application is technically deployable.

---

# 15. Release Decision

## Reference Assessment

**CONDITIONAL GO**

The reference project demonstrates a functioning AI product and several KPIs are on target.

However, the reference KPI results identify areas requiring improvement:

* Hallucination rate.
* Answer accuracy.
* Unsupported-question refusal.
* User satisfaction.

### Conditions

Before broader scaling, the team should:

1. Investigate the hallucination-rate breach.
2. Improve answer accuracy.
3. Improve unsupported-question refusal.
4. Investigate user-satisfaction results.
5. Continue monitoring post-release KPIs.
6. Reassess readiness after corrective actions.

### PM Principle

A Conditional Go allows the organization to move forward while explicitly managing remaining risk.

---

# 16. KPI & Monitoring

The KPI dashboard provides a post-release view of product health.

The PM uses:

**KPI → Target → Actual → Trend → Threshold → Action**

### Decision Rules

**On Target → Continue**

**Needs Attention → Improve**

**Below Threshold → Escalate / Reassess**

### Security

Security performance requires additional consideration.

**0 critical incidents → On Target**

**1 critical incident → Needs Attention + immediate investigation**

**2+ critical incidents → Escalation / Reassessment**

Security, governance, and compliance decisions should also consider severity and business impact rather than relying solely on a numeric threshold.

---

# 17. Continuous Improvement

Based on the KPI evidence, improvement priorities include:

## Priority 1 — Hallucination Reduction

Investigate unsupported model behavior and strengthen grounding controls.

**Success Measure:**
Hallucination rate below 2%.

## Priority 2 — Answer Accuracy

Investigate incorrect or incomplete answers.

**Success Measure:**
Answer accuracy at or above 90%.

## Priority 3 — Unsupported Questions

Improve the system's ability to recognize when sufficient evidence does not exist.

**Success Measure:**
Unsupported-question refusal at 100%.

## Priority 4 — User Satisfaction

Investigate usability, clarity, trust, and usefulness.

**Success Measure:**
User satisfaction at or above 85%.

---

# 18. Business Outcomes

## Intended Outcomes

The project targets:

* Faster policy discovery.
* Improved access to authoritative policy information.
* Reduced employee search effort.
* Better user experience.
* Improved confidence in policy answers.
* Reduced risk from unsupported responses.

## Reference Results

The reference KPI data indicates a:

**58% policy search-time reduction**

against a target of at least 50%.

This demonstrates that the product is meeting the search-time improvement objective in the reference evaluation.

---

# 19. Lessons Learned

## What Worked

* Establishing measurable AI KPIs.
* Separating retrieval from generation.
* Grounding responses in policy evidence.
* Requiring citations.
* Establishing authority rules.
* Defining explicit unsupported-question behavior.
* Monitoring product performance after release.

## What Required Attention

The KPI results demonstrate that a product can perform well in some dimensions while still having important quality gaps.

The project therefore requires continuous evaluation rather than a one-time launch assessment.

## Key PM Lesson

AI projects require the PM to manage uncertainty.

The question is not simply:

> "Does the model work?"

The stronger question is:

> "Does the product perform reliably enough, safely enough, and consistently enough to achieve the intended business outcome?"

---

# 20. Portfolio Evidence

Students should use the actual course artifacts as supporting evidence rather than copying the entire project into this document.

Recommended evidence includes:

* Problem statement.
* Stakeholder analysis.
* Requirements.
* Scope.
* Product backlog.
* MVP definition.
* AI architecture.
* Data/retrieval approach.
* Risk register.
* Evaluation framework.
* Test results.
* UAT results.
* Release-readiness assessment.
* KPI dashboard.
* Continuous-improvement backlog.

### Evidence Structure

**Artifact → Decision → Evidence → Outcome**

The artifact supports the decision.

The decision explains the PM action.

The evidence supports the decision.

The outcome demonstrates what happened as a result.

---

# 21. PM Decisions Demonstrated

The Petadel PolicyAssist project demonstrates the following PM decisions:

| PM Area     | Example Decision                                                                            |
| ----------- | ------------------------------------------------------------------------------------------- |
| Problem     | Improve policy discovery                                                                    |
| Scope       | Focus on retrieval, grounding, citation, and controlled response                            |
| MVP         | Establish core policy-assistance workflow                                                   |
| AI          | Use retrieval-grounded generation                                                           |
| Data        | Restrict retrieval to authoritative eligible documents                                      |
| Risk        | Treat hallucination as a measurable product risk                                            |
| Security    | Consider authorization before exposing policy information                                   |
| Evaluation  | Measure retrieval, answer quality, hallucination, citations, refusal, latency, satisfaction |
| Release     | Use evidence to determine readiness                                                         |
| Monitoring  | Track KPIs after release                                                                    |
| Improvement | Prioritize corrective actions based on KPI evidence                                         |

---

# 22. Portfolio Story

The completed case study can be summarized as:

### Problem

Employees struggle to efficiently locate and interpret authoritative organizational policies.

### Solution

Petadel PolicyAssist uses AI-assisted retrieval and grounded generation to help employees find relevant policy information and receive responses supported by source citations.

### PM Approach

The project applies structured Project Management across:

**Discovery → Requirements → Planning → AI Design → Data → Evaluation → Governance → Testing → UAT → Release → Monitoring → Improvement**

### Evidence

The product is evaluated against measurable performance targets.

### Key Result

The reference evaluation demonstrates a 58% reduction in policy search time against a target of at least 50%.

### Remaining Risk

AI quality metrics reveal areas requiring improvement, particularly hallucination and answer accuracy.

### PM Recommendation

Proceed with a **Conditional Go** while corrective actions are completed and product performance continues to be monitored.

---

# 23. Interview Summary

A concise interview explanation could follow this structure:

> I managed an AI policy-assistance product designed to reduce the time employees spend finding and understanding organizational policies. I managed the project across requirements, scope, AI solution planning, data and knowledge management, AI evaluation, risk and governance, testing, UAT, release readiness, and KPI monitoring. One important PM decision was recognizing that strong overall product performance did not eliminate AI quality risks. The evaluation showed a 58% reduction in policy search time, but hallucination and answer-accuracy metrics still required corrective action. Based on the evidence, I would recommend a Conditional Go with targeted improvements and continued monitoring.

---

# 24. Instructor Standard

This example demonstrates the expected capstone standard.

A completed capstone should show that the student can:

* Define a meaningful business problem.
* Identify users and stakeholders.
* Manage requirements and scope.
* Prioritize an MVP.
* Understand AI architecture at a PM level.
* Manage data and knowledge risks.
* Evaluate AI performance.
* Manage AI-specific risks.
* Coordinate testing and UAT.
* Assess release readiness.
* Make a Go/Conditional Go/No-Go decision.
* Monitor KPIs.
* Recommend corrective actions.
* Connect technical performance to business outcomes.
* Communicate the project professionally.

---

# Final Principle

The purpose of the Petadel PolicyAssist example is not to teach students to copy one project.

It is to demonstrate **how an AI Project Manager thinks.**

You should be able to look at the example and understand:

**Problem → Evidence → Decision → Action → Outcome**

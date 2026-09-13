# Milestone 12 — Capstone & Portfolio

## Objective

In this milestone, you will integrate the Project Management (PM) work completed throughout the course into a complete Artificial Intelligence (AI) project capstone and professional portfolio package.

You will demonstrate that you can manage an AI product through its lifecycle:

**Problem → Stakeholders → Requirements → Planning → AI Design → Data → Evaluation → Governance → Testing → Release → Monitoring → Continuous Improvement**

The goal is not simply to show that an AI application was built.

The goal is to demonstrate that you can:

**Define the problem → Make informed decisions → Manage risk → Evaluate evidence → Determine readiness → Measure outcomes → Recommend what happens next**

---

# How M12 Works

Milestone 12 brings together the work completed in Milestones 1–11.

You are not expected to recreate every artifact inside this guide.

Instead, you will:

1. Review the work completed throughout the course.
2. Confirm that the major decisions and evidence are documented.
3. Assemble the work into the **Capstone Submission Template**.
4. Create a professional **Portfolio Package** using the Portfolio Package Template.
5. Compare your work against the completed Petadel PolicyAssist reference example.
6. Make a final evidence-based PM recommendation.

### Your M12 Files

Use the four files provided for this milestone:

**Milestone 12 Guide**
Explains what to do and how to evaluate your capstone.

**Capstone Submission Template**
Your working document for assembling the complete capstone.

**Portfolio Package Template**
Your professional case-study format for presenting the project publicly.

**Completed Capstone Example**
The Petadel PolicyAssist reference showing the expected standard.

---

# Capstone Options

You may complete the capstone using one of two approaches.

## Option A — Petadel PolicyAssist

Use the Petadel PolicyAssist AI project as the reference implementation provided throughout this course.

You will assemble the PM artifacts and evidence developed throughout the course into a complete project package.

## Option B — Your Own AI Product

Apply the same Project Management process to your own AI product, use case, or business problem.

You do not need to recreate the PolicyAssist technical application.

Your project should demonstrate the same PM lifecycle and evidence-based decision-making.

---

# Capstone Completion Model

Your completed project should demonstrate evidence across the full lifecycle.

| Area                          | Evidence                                                     |
| ----------------------------- | ------------------------------------------------------------ |
| Problem                       | Problem statement and business need                          |
| Stakeholders                  | Stakeholder analysis and engagement approach                 |
| Requirements                  | Business, functional, and non-functional requirements        |
| Scope                         | In-scope, out-of-scope, assumptions, and constraints         |
| Product Planning              | Backlog, prioritization, and Minimum Viable Product (MVP)    |
| AI Design                     | Architecture and technology decisions                        |
| Data                          | Data sources, quality, authority, and retrieval approach     |
| Evaluation                    | AI evaluation framework and results                          |
| Risk                          | Risk register and mitigation                                 |
| Security & Governance         | Access, security, privacy, and governance controls           |
| Testing                       | Test strategy, results, and defects                          |
| User Acceptance Testing (UAT) | User scenarios and acceptance results                        |
| Release                       | Release readiness and deployment approach                    |
| Monitoring                    | Key Performance Indicators (KPIs), dashboard, and monitoring |
| Continuous Improvement        | Improvement actions and future roadmap                       |
| Business Outcome              | Evidence of product value                                    |

The evidence should tell one connected story.

**Problem → Decision → Action → Evidence → Outcome**

---

# Part 1 — Reconstruct the Project Story

Review your work from Milestones 1–11.

Do not simply place the files into a folder.

Create a logical project story.

Your capstone should answer:

1. What problem were we solving?
2. Who experienced the problem?
3. Why did the problem matter?
4. What solution did we propose?
5. What requirements defined success?
6. What did we decide to build?
7. Why did we make those product and technical decisions?
8. What risks did we identify?
9. How did we evaluate the AI?
10. How did we test the product?
11. What did UAT tell us?
12. Was the product ready for release?
13. How did we measure product performance?
14. What business outcome did the product target?
15. What should happen next?

### PM Standard

Do not describe activities without explaining their purpose.

For example:

**Weak:**
"We created a risk register."

**Stronger:**
"We identified hallucination and authorization as high-impact AI risks and assigned mitigation actions before release."

The second statement demonstrates PM judgment.

---

# Part 2 — Review Requirements, Scope & MVP

Review the work completed in Milestones 3 and 4.

Confirm that your final capstone clearly shows:

* Business requirements.
* Functional requirements.
* Non-functional requirements.
* AI-specific requirements.
* Security and access requirements.
* Acceptance criteria.
* In-scope capabilities.
* Out-of-scope capabilities.
* MVP scope.
* Deferred or rejected capabilities.
* Major assumptions and constraints.

### PM Decision

Answer:

> **Is the delivered or proposed product aligned with the approved scope and MVP?**

Identify any item that was:

* Completed
* Partially completed
* Deferred
* Rejected

Support your conclusion with evidence from your requirements, backlog, and MVP artifacts.

---

# Part 3 — Review the AI Solution

Review the architecture and technical decisions developed in Milestone 5.

Your capstone should demonstrate that you understand the AI solution at a PM level.

You should be able to explain:

* What the major components do.
* How information moves through the system.
* Where AI is used.
* Where data enters the process.
* How retrieval supports the AI response.
* Where grounding occurs.
* How citations or evidence are produced.
* What dependencies exist.
* What major technical risks were identified.

For PolicyAssist, the core flow is:

**Policy Documents → Processing → Embeddings → Vector Database → Retrieval → Large Language Model (LLM) → Grounded Response → Citation → User**

### PM Decision

Identify at least one important technical or architecture decision.

Explain:

**Decision → Reason → Tradeoff → Risk**

You do not need to claim that you personally engineered technical components you did not build.

Your role is to demonstrate that you can manage and communicate technical decisions.

---

# Part 4 — Review Data & Knowledge Management

Review Milestone 6.

Your capstone should explain how the project manages the data or knowledge required by the AI product.

Address:

* Data or knowledge sources.
* Data quality.
* Authority.
* Versioning.
* Duplicates.
* Outdated information.
* Conflicting information.
* Metadata.
* Access considerations.
* Retrieval quality.

For PolicyAssist, remember:

**The LLM is not the source of truth.**

The authoritative source must be identified before the AI relies on the information.

### PM Decision

Identify the most important data or knowledge risk and explain:

**Risk → Impact → Control → Evidence**

---

# Part 5 — Review AI Evaluation

Review Milestone 7.

Do not combine retrieval quality and generated-response quality into one general score.

Your capstone should demonstrate that you evaluated the appropriate dimensions separately.

For example:

* Retrieval accuracy.
* Response accuracy.
* Grounded response rate.
* Unsupported response rate.
* Citation presence.
* Citation accuracy.
* Citation support.
* Response time.
* Appropriate refusal or escalation.

Compare actual performance against the approved targets and thresholds.

Use:

**Metric → Target → Actual → Status → Interpretation → Decision**

### PM Decision

Answer:

> **Does the evaluation evidence support continued use, improvement, or additional validation?**

Do not simply report the numbers.

Explain what they mean for the product.

---

# Part 6 — Review Security & Governance

Review Milestone 8.

Your capstone should distinguish between:

**Controls that were actually tested**

and

**Production controls that remain requirements or future work.**

Address applicable areas such as:

* Authentication.
* Authorization.
* Role-based access.
* Confidential data protection.
* Privacy.
* Logging.
* Auditability.
* Policy authority and versioning.
* Governance ownership.
* Human escalation.
* Production security testing.

Do not claim that a control passed if it was not implemented or tested.

### PM Decision

Identify the most significant remaining security or governance risk.

Explain:

**Risk → Impact → Control → Evidence → Decision**

---

# Part 7 — Review Testing & UAT

Review Milestone 9.

Your capstone should demonstrate that the product was evaluated as a complete product, not merely as a functioning application.

Review evidence for:

* Functional testing.
* Integration behavior.
* AI behavior.
* Citation or evidence behavior.
* Unsupported-question handling.
* User experience.
* Business or operational expectations.
* User Acceptance Testing (UAT).
* Defects and issues.

Carry forward relevant evidence rather than unnecessarily repeating earlier tests.

### Testing Decision

Determine whether the remaining issues are:

**Acceptable → Can Defer → Must Fix**

Explain the release impact.

### UAT Decision

Determine whether the product was:

**Accepted → Accepted with Conditions → Not Accepted**

Support the decision with UAT evidence.

---

# Part 8 — Review Release & Deployment

Review Milestone 10.

Keep two decisions separate:

### Release Decision

Should the product be approved for release?

**Go → Hold → No-Go**

### Deployment Decision

Can the approved release actually be deployed into the intended environment?

**Deploy → Hold Deployment → Rollback**

Your capstone should demonstrate that release approval does not automatically mean production deployment is appropriate.

Review:

* Release criteria.
* Open defects.
* UAT.
* AI quality.
* Security conditions.
* Deployment readiness.
* Environment and configuration requirements.
* Support ownership.
* Monitoring.
* Rollback.

### PM Decision

Document your final release position and explain the evidence behind it.

---

# Part 9 — Review KPI & Monitoring

Review Milestone 11.

Use the established framework:

**KPI → Target → Actual → Trend → Threshold → Action**

Your capstone should identify:

* KPIs on target.
* KPIs needing attention.
* KPIs below threshold.
* Improving trends.
* Declining trends.
* Product risks.
* Business risks.
* Recommended actions.

Do not treat a dashboard as the decision itself.

The dashboard provides evidence.

The PM interprets the evidence and determines what should happen next.

### PM Decision

Select the appropriate action:

**Continue → Improve → Escalate → Reassess**

Explain why.

---

# Part 10 — Business Outcome

Connect product performance to the business problem.

Your capstone should answer:

> **Did the product create or demonstrate the intended value?**

Consider outcomes such as:

* Reduced search time.
* Reduced repetitive support questions.
* Improved accuracy.
* Improved confidence.
* Reduced operational effort.
* Reduced risk.
* Improved user experience.

Distinguish clearly between:

**Target Outcome**

What the project intended to achieve.

**Measured Outcome**

What the available evidence demonstrates.

**Expected Outcome**

What is projected but has not yet been validated.

Do not present expected results as proven results.

### PM Decision

Classify the outcome:

**Achieved → Partially Achieved → Not Yet Achieved**

Explain the evidence.

---

# Part 11 — Continuous Improvement

Review the evidence collected throughout the lifecycle.

Create a post-release improvement backlog.

Potential improvement categories include:

* Product.
* AI performance.
* Data.
* Retrieval.
* User experience.
* Security.
* Governance.
* Operations.
* Business value.

Prioritize improvements using an appropriate method such as:

* Business value.
* User impact.
* Risk.
* Feasibility.
* Dependencies.
* MoSCoW.

For major improvements, identify:

**Problem → Improvement → Value → Priority → Owner → Success Measure**

### PM Decision

Identify the first improvement that should receive attention and explain why.

---

# Part 12 — Lessons Learned

Document lessons from the project.

## What Worked

Identify decisions, processes, or practices that contributed to success.

## What Did Not Work

Identify delays, defects, weak assumptions, unclear requirements, retrieval problems, governance gaps, or other challenges.

## What Would You Do Differently?

Identify specific changes you would make on the next AI project.

## Key PM Lesson

Explain what the project taught you about managing AI products.

Your answer should demonstrate growth in PM judgment, not simply summarize activities.

---

# Part 13 — Assemble the Capstone Submission

Open the:

**Capstone Submission Template**

Use it to assemble your complete capstone.

Do not simply copy every previous milestone into the document.

Select the evidence that best demonstrates:

* The problem.
* The decisions.
* The risks.
* The evidence.
* The outcomes.

Use artifact links where appropriate.

The final submission should be understandable without requiring the reviewer to open every course file.

---

# Part 14 — Build the Portfolio Package

After completing the capstone submission, use the:

**Portfolio Package Template**

The portfolio is different from the capstone submission.

The capstone demonstrates that you completed the project lifecycle.

The portfolio demonstrates that you can communicate that experience professionally.

Your portfolio story should follow:

**Problem → Users → PM Strategy → AI Solution → Risk → Evaluation → Testing → Release → Outcomes → Continuous Improvement**

Focus on your individual PM contribution.

Clearly distinguish:

**What the project did**

from

**What you personally managed, influenced, decided, coordinated, or evaluated.**

Do not claim technical work you did not perform.

---

# Part 15 — Use the Completed Example

Review:

**Petadel PolicyAssist AI — Completed Capstone Example**

Use the example to understand the expected standard.

Do not copy it as though it were your own project.

Instead, examine how the example connects:

**Problem → Evidence → Decision → Action → Outcome**

Look especially for:

* Measurable requirements.
* PM-level technical understanding.
* Explicit AI risks.
* Separate evaluation dimensions.
* Governance controls.
* Release reasoning.
* KPI interpretation.
* Corrective actions.
* Business outcomes.

### PM Question

Ask yourself:

> **Does my capstone demonstrate the same level of PM thinking, even if my project is different?**

---

# Part 16 — Final Executive Review

Imagine you are presenting the project to an executive steering committee.

You have limited time.

Be prepared to answer:

### What problem did we solve?

### Who benefits?

### What did we build?

### Why did we make these decisions?

### What risks remain?

### What does the evidence show?

### Is the product ready?

### What business value has been demonstrated?

### What should happen next?

Your presentation should focus on decisions and evidence, not a chronological list of tasks.

---

# Final PM Recommendation

Make a final recommendation for the product.

Select the action that best reflects the evidence:

**Continue**

Continue the current direction because performance and risk remain acceptable.

**Improve**

Continue while addressing identified performance or product gaps.

**Escalate**

A significant issue requires leadership attention or stronger intervention.

**Reassess**

The product, scope, assumptions, or business case should be reconsidered.

**Scale**

Evidence supports expanding the product to additional users, departments, or environments.

Your recommendation should include:

1. Business value.
2. Strongest evidence.
3. Most significant risk.
4. Recommended action.
5. Action owner.
6. Next review point.

---

# Final Capstone Checkpoint

Answer:

> **Would you recommend moving this AI product forward today?**

Your answer must connect:

**Business Value → Evidence → Risk → Recommendation**

Do not answer based on whether the technology is interesting.

Evaluate whether the product is:

* Valuable.
* Feasible.
* Safe.
* Governable.
* Testable.
* Measurable.
* Ready for its intended stage.

---

# Definition of Done

The capstone is complete when you can:

* Explain the business problem.
* Identify the users and stakeholders.
* Connect stakeholder needs to requirements.
* Explain scope and MVP decisions.
* Explain the AI architecture at a PM level.
* Explain the data and retrieval approach.
* Identify major AI-specific risks.
* Explain evaluation results.
* Explain testing and UAT results.
* Explain release and deployment decisions.
* Interpret KPI performance.
* Connect technical performance to business outcomes.
* Recommend evidence-based corrective actions.
* Explain continuous-improvement priorities.
* Assemble a complete capstone submission.
* Transform the capstone into a professional portfolio case study.
* Explain your individual PM contribution.
* Present the project confidently to executives or interviewers.

---

# Final Principle

A successful AI Project Manager does not simply ask:

> **Did we build the AI?**

The stronger questions are:

> **Did we solve the right problem?**

> **Did we build the right product?**

> **Did we manage the right risks?**

> **Does the evidence support the current release decision?**

> **Is the product creating the intended value?**

> **What should we improve next?**

The capstone demonstrates the ability to answer those questions using structured Project Management practices, AI-specific risk management, measurable evidence, and sound PM judgment.

**Problem → Evidence → Decision → Action → Outcome**

# Module 4: Agile Product Planning

## Purpose

AI projects require structured planning, but traditional project plans alone are often not enough.

AI systems evolve as teams learn more about the data, model behavior, user needs, and technical limitations.

This module teaches how an AI Project Manager translates requirements into an actionable product backlog, prioritizes work, manages scope, and plans iterative delivery.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain Agile principles in AI projects.
* Distinguish between an epic, user story, task, and acceptance criteria.
* Build and prioritize an AI product backlog.
* Apply prioritization frameworks such as MoSCoW.
* Identify dependencies between technical and business work.
* Manage changing requirements without losing project control.
* Plan iterative releases and MVP delivery.
* Identify risks created by poor backlog management.
* Connect backlog items to measurable business outcomes.

---

## Agile Project Management

Agile is an approach to delivering products incrementally through short development cycles, continuous feedback, and reprioritization.

Instead of attempting to define every detail before development begins, Agile allows the team to learn and adjust as the project progresses.

### Why Agile Matters For AI

AI projects contain uncertainty that traditional projects may not fully anticipate.

Examples include:

* Data quality problems discovered during development.
* Model performance below expectations.
* Unexpected user behavior.
* Retrieval or classification errors.
* Changes in business priorities.
* New regulatory or security requirements.
* Technical limitations discovered during implementation.

The PM must therefore maintain enough structure to control the project while allowing enough flexibility to respond to learning.

---

## Agile Principles For AI Projects

A strong AI project should:

* Deliver value incrementally.
* Validate assumptions early.
* Use measurable outcomes.
* Prioritize the highest-value work.
* Incorporate stakeholder feedback.
* Treat evaluation as part of development.
* Continuously manage risk.
* Reprioritize when evidence changes.

Agile does **not** mean:

> Build quickly without planning.

It means:

> Plan continuously while delivering measurable value in controlled increments.

---

## Product Backlog

A product backlog is the prioritized list of work required to deliver a product.

The backlog may contain:

* Epics
* User stories
* Technical work
* Data work
* Security requirements
* Evaluation activities
* Defects
* Documentation
* Governance activities

The backlog should represent the **complete product**, not only the software development work.

---

## Epics

An epic is a large body of related work that is too broad to complete as a single user story.

For example:

> Improve AI response quality

could represent an epic.

The epic can then be broken into smaller user stories involving:

* Retrieval
* Grounding
* Citations
* Evaluation
* Error handling
* Feedback

Epics help the PM organize the project at a strategic level.

---

## User Stories

A user story describes a capability from the perspective of the person who needs it.

A common format is:

> As a [user], I want [capability], so that [business value].

### Example

> As an employee, I want to search company policies using natural language, so that I can find the information I need without manually searching through multiple documents.

A good user story should communicate **who needs something, what they need, and why it matters.**

---

## Acceptance Criteria

Acceptance criteria define the conditions that must be satisfied for a user story to be considered complete.

Weak:

> The system should provide accurate answers.

Better:

> Given a policy question supported by an authoritative active policy, the system must provide an answer grounded in the applicable policy and identify the supporting source.

Acceptance criteria should be:

* Specific
* Testable
* Measurable where possible
* Connected to the requirement
* Understandable by both business and technical stakeholders

---

## Tasks

Tasks are smaller pieces of work required to complete a user story.

For example:

**User Story:** Retrieve relevant policy information.

Possible tasks:

* Prepare policy documents.
* Extract document text.
* Create document chunks.
* Generate embeddings.
* Store searchable representations.
* Implement retrieval.
* Test retrieval accuracy.

The PM does not necessarily perform these technical tasks, but must understand their purpose, dependencies, and impact on delivery.

---

## Backlog Hierarchy

A typical AI product backlog can follow this structure:

**Product Goal**

↓

**Epic**

↓

**User Story**

↓

**Task**

↓

**Acceptance Criteria**

The hierarchy allows the PM to move between strategic objectives and detailed delivery work.

---

## Prioritization

Not every backlog item should be treated equally.

The PM must determine which work provides the greatest value while considering:

* Business impact
* User impact
* Risk
* Dependencies
* Regulatory requirements
* Security
* Technical feasibility
* Cost
* Effort
* Time to value

Prioritization should be evidence-based rather than based solely on stakeholder preference.

---

## MoSCoW Prioritization

MoSCoW is a prioritization framework that categorizes requirements into four groups.

| Category        | Meaning                                                          |
| --------------- | ---------------------------------------------------------------- |
| **Must Have**   | Required for the product to function or meet critical objectives |
| **Should Have** | Important but not immediately critical                           |
| **Could Have**  | Valuable but lower priority                                      |
| **Won't Have**  | Not included in the current release                              |

### Example

For an AI knowledge assistant:

**Must Have**

* Secure user access
* Accurate retrieval
* Grounded responses
* Source citations

**Should Have**

* Feedback collection
* Administrative reporting

**Could Have**

* Advanced personalization
* Additional interface customization

**Won't Have**

* Features outside the current business objective

The PM should clearly document why an item receives its priority.

---

## MVP Planning

MVP means **Minimum Viable Product**.

An MVP is the smallest version of a product that can provide meaningful value while allowing the team to validate important assumptions.

An MVP should **not** mean:

> Build the lowest-quality version possible.

Instead:

> Build the smallest controlled version capable of testing the product's core value proposition.

### MVP Questions

The PM should ask:

1. What problem must the MVP solve?
2. Who is the MVP for?
3. What capabilities are absolutely necessary?
4. What can wait?
5. What risks must be tested before release?
6. What evidence will determine whether the MVP is successful?

---

## Release Planning

AI products should generally be delivered through controlled releases rather than one large launch.

A release might contain:

**Release 1 — Foundation**

* Core data preparation
* Access controls
* Initial knowledge base
* Basic retrieval

↓

**Release 2 — MVP Product**

* User experience
* AI responses
* Grounding
* Citations
* Feedback

↓

**Release 3 — Production Readiness**

* Evaluation
* Security validation
* UAT
* Monitoring
* Governance
* Rollback planning

The exact release structure may vary by project.

---

## Dependencies

A dependency exists when one piece of work relies on another piece of work being completed first.

Examples:

* Retrieval depends on usable document data.
* AI responses depend on retrieval.
* Evaluation depends on a functioning system.
* UAT depends on a testable release.
* Production deployment depends on security and approval.

The PM should identify dependencies early because they can become schedule constraints.

---

## Backlog Refinement

Backlog refinement is the ongoing process of reviewing and improving backlog items.

During refinement, the team may:

* Clarify requirements.
* Split large stories.
* Add acceptance criteria.
* Estimate effort.
* Identify dependencies.
* Identify risks.
* Remove obsolete work.
* Reprioritize items.

The backlog should be treated as a **living project control mechanism**, not a static document.

---

## Managing Scope Changes

AI projects will change.

A stakeholder may request:

> Can we also add a chatbot that answers questions about benefits?

The PM should not immediately say yes or no.

Instead, evaluate:

* Business value
* Scope impact
* Cost
* Schedule impact
* Technical dependencies
* Security implications
* Data requirements
* Risk
* Impact on current priorities

Then make a documented decision.

### Change Decision

**Request → Analyze Impact → Evaluate Priority → Approve / Defer / Reject → Update Backlog → Communicate Decision**

This prevents uncontrolled scope growth.

---

## Definition Of Ready

Definition of Ready describes the conditions that should exist before a backlog item is ready for development.

A story may be considered ready when:

* The objective is understood.
* The user or stakeholder is identified.
* Acceptance criteria are defined.
* Dependencies are known.
* Required information is available.
* Major risks are understood.
* The team can reasonably estimate the work.

---

## Definition Of Done

Definition of Done describes the conditions required for completed work to be accepted.

For an AI feature, this may include:

* Requirement satisfied.
* Acceptance criteria passed.
* Testing completed.
* AI behavior evaluated.
* Security requirements satisfied.
* Documentation completed.
* Stakeholder acceptance obtained where required.

**Done** should mean usable and acceptable, not merely coded.

---

## AI Project Planning Risks

Poor Agile planning can create significant risks.

### Backlog Too Technical

The backlog focuses on implementation tasks without explaining business value.

**Risk:** Stakeholders cannot determine whether the project is solving the right problem.

### Backlog Too Vague

Stories lack measurable acceptance criteria.

**Risk:** The team cannot determine when work is actually complete.

### Everything Is High Priority

Every stakeholder labels their request as urgent.

**Risk:** The team loses focus and critical work is delayed.

### No Dependency Management

The PM does not identify sequencing requirements.

**Risk:** Development becomes blocked.

### Scope Creep

New requests are added without evaluating impact.

**Risk:** Schedule, cost, and project objectives become uncontrolled.

---

## Practical Exercise 4: Build And Prioritize An AI Product Backlog

### Scenario

Your organization wants to develop an AI customer support assistant.

The assistant should help customers find answers to common questions while reducing the workload on support representatives.

Leadership wants the first usable release within three months.

The project team has identified the following potential capabilities:

* Secure customer authentication
* Natural-language question input
* Knowledge-base ingestion
* AI-powered retrieval
* Grounded responses
* Source citations
* Human escalation
* Customer feedback
* Analytics dashboard
* Response-time monitoring
* Personalized recommendations
* Voice interaction
* Automated email follow-up
* Advanced reporting

### Part 1: Create Epics

Group the capabilities into logical epics.

For example:

* Security
* Knowledge Management
* AI Response
* User Experience
* Monitoring

Create your own appropriate structure.

### Part 2: Create User Stories

Write at least **five user stories** using:

> As a [user], I want [capability], so that [business value].

### Part 3: Write Acceptance Criteria

Choose **three** of your user stories.

Write measurable acceptance criteria for each.

### Part 4: Prioritize

Use **MoSCoW** to classify the backlog items.

Identify:

* Must Have
* Should Have
* Could Have
* Won't Have

### Part 5: Identify Dependencies

Identify at least **three dependencies**.

Explain why the dependency exists and what happens if it is not completed.

### Part 6: Plan The MVP

Select the capabilities that should be included in the first release.

Explain:

* Why each capability is necessary.
* What value it provides.
* What you intentionally excluded.
* What risks remain.

---

## PM Decision

Leadership says:

> "Everything on the list is important. Put everything into the first release so we don't have to come back later."

As the AI Project Manager, decide whether to accept this approach.

Your response must include:

1. **Decision**
2. **Evidence**
3. **Business Impact**
4. **Project Risk**
5. **Recommendation**
6. **Stakeholders Who Should Be Involved**

Do not simply say that the scope is too large.

Explain **how you would use prioritization and evidence to make the decision.**

---

## Artifact / Output

Create an **AI Product Backlog** containing:

* Product goal
* Epics
* User stories
* Acceptance criteria
* Priority
* Dependencies
* MVP scope
* Release assignment
* Risks

The artifact should demonstrate that you can translate business objectives into controlled, actionable delivery work.

---

## Decision / Reflection

Answer the following:

1. What makes an AI backlog different from a traditional software backlog?
2. Why should evaluation and security work appear in the backlog?
3. What happens when every requirement is classified as a Must Have?
4. How should a PM respond when a stakeholder requests new functionality during development?
5. Why is an MVP important when AI performance is uncertain?

---

## Key Takeaways

* Agile provides structure while allowing controlled adaptation.
* AI backlogs must include business, technical, data, evaluation, security, and governance work.
* Epics organize large bodies of work.
* User stories describe capabilities from the user's perspective.
* Acceptance criteria make requirements testable.
* Prioritization protects the project from uncontrolled scope.
* MoSCoW provides a simple framework for prioritization.
* Dependencies should be identified before they become blockers.
* MVP means the smallest version capable of delivering meaningful value and validating assumptions.
* Definition of Done establishes what completion actually means.
* A backlog is a living project-management artifact.

---

## Connection To Capstone

The backlog-management techniques from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will use:

* Epics
* User stories
* Acceptance criteria
* Prioritization
* Dependencies
* MVP planning
* Release planning
* Definition of Done

to organize the PolicyAssist AI product into controlled, measurable releases.

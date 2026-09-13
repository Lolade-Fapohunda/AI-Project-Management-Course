# Milestone 4 — Backlog & Minimum Viable Product (MVP)

## Objective

In this milestone, you will translate approved requirements into an actionable product backlog and define the **Minimum Viable Product (MVP)** for PolicyAssist.

The goal is not to build everything that could be useful.

The goal is to determine:

> **What should we build first, why, what is necessary to validate the core business need, and what should wait until a later release?**

You will apply:

**Requirement → User Story → Acceptance Criteria → Priority → MVP → Release Scope**

---

# What You Will Do

You will:

1. Review the requirements from Milestone 3.
2. Convert requirements into user stories.
3. Define acceptance criteria.
4. Prioritize the backlog.
5. Identify high-risk capabilities and dependencies.
6. Define the MVP.
7. Distinguish MVP scope from release scope.
8. Document what is deferred or out of scope.
9. Identify important scope trade-offs.
10. Make evidence-based backlog and MVP decisions.

---

# Why Backlog & MVP Matter

A requirements document describes what the product needs to accomplish.

A backlog turns those requirements into manageable pieces of product work.

An MVP defines the smallest useful product that can provide meaningful value and generate evidence for further decisions.

Without prioritization, AI projects can expand quickly into:

* Too many features.
* Uncontrolled technical work.
* Delayed validation.
* Increased risk.
* Unclear release goals.
* More complexity than the business problem requires.

The PM must protect the core business outcome while keeping the product small enough to validate.

---

# Part 1 — Review Your Requirements

Review Milestone 3.

Identify the requirements that are essential to solving the PolicyAssist problem.

Pay particular attention to:

* Core user value.
* AI quality.
* Retrieval.
* Grounding.
* Citations.
* Unsupported questions.
* Performance.
* Security.
* Governance.

Do not assume that every requirement belongs in the MVP.

Ask:

> **Which requirements are necessary to prove that the core product is useful, reliable, and safe enough for the intended validation stage?**

---

# Part 2 — Create User Stories

Create at least **8 user stories** from your approved requirements.

Use the standard structure:

> **As a [user], I want [capability], so that [benefit].**

### Example

> As an employee, I want to ask a policy question and receive a source-backed answer so that I can find reliable policy information quickly.

A useful user story should identify:

* The user.
* The capability.
* The value.

Avoid writing technical tasks as user stories.

### Weak

> Build a vector database.

### Stronger

> As an employee, I want PolicyAssist to retrieve relevant policy information so that I can find the information needed to answer my question.

The implementation may require a vector database, but the user story should describe the user value.

---

# Part 3 — Add Acceptance Criteria

Each user story should include acceptance criteria.

Acceptance criteria explain how you will know that the story has been completed successfully.

### Example

### User Story

> As an employee, I want to receive a policy answer with a supporting citation so that I can verify the information.

### Acceptance Criteria

* A relevant policy response is generated.
* The response is grounded in retrieved policy information.
* A citation identifies the supporting source.
* The cited source supports the response.
* Unsupported information is not presented as fact.
* The response passes the defined evaluation criteria.

Acceptance criteria should be specific enough to test.

---

# Part 4 — Trace Stories Back to Requirements

Do not create a disconnected backlog.

Each major user story should trace back to an approved requirement.

Use:

**Requirement → User Story → Acceptance Criteria**

This helps the PM determine whether the backlog actually represents the approved product need.

### Example

**Requirement**

PolicyAssist shall provide grounded responses supported by authoritative policy information.

↓

**User Story**

As an employee, I want to receive a policy answer supported by a source citation so that I can verify the information.

↓

**Acceptance Criteria**

* Relevant policy evidence is retrieved.
* The response is grounded in that evidence.
* A supporting citation is provided.
* Unsupported material is not presented as fact.

A strong backlog preserves this connection.

---

# Part 5 — Prioritize the Backlog

Use:

**Must → Should → Could → Deferred / Out of Scope**

Prioritize based on:

* Business value.
* User impact.
* Risk.
* AI quality.
* Security.
* Governance.
* Dependencies.
* Technical feasibility.
* MVP necessity.

Do not prioritize only by stakeholder preference.

A stakeholder can identify an important need without automatically making that need an MVP priority.

---

# Prioritization Questions

For each major item, ask:

### Business Value

Does this directly support the business problem?

### User Value

Does this materially improve the user's ability to accomplish the primary task?

### Risk

Does failing to implement this create significant product, security, governance, or business risk?

### Dependency

Does another capability depend on this item?

### MVP Necessity

Is this required to validate the core product?

### Feasibility

Can the capability reasonably be implemented within the current scope and constraints?

---

# Part 6 — Identify High-Risk Backlog Items

Identify at least **three high-risk or high-dependency items**.

Examples:

* Authoritative document identification.
* Retrieval quality.
* Authorization.
* Citation correctness.
* Hallucination control.
* Unsupported-question handling.
* Performance.
* Sensitive information protection.

For each item, explain:

**Item → Risk → Impact → Mitigation / Validation**

### Example

**Item:** Authorization

**Risk:** Unauthorized users could retrieve restricted policy information.

**Impact:** Security, privacy, governance, and trust risk.

**Mitigation / Validation:** Define access requirements, implement the appropriate control, and perform negative authorization testing before production deployment.

The purpose is to make risk visible in the backlog.

---

# Part 7 — Define the MVP

The PolicyAssist MVP should support the essential workflow:

**Employee Question → Relevant Policy Retrieval → Grounded Response → Citation**

The MVP should also define appropriate behavior when sufficient evidence is unavailable:

**Insufficient Evidence → Do Not Invent → Refuse or Escalate**

The MVP is not simply the smallest amount of code.

It is the smallest product capability set that can provide meaningful value and produce useful evidence about whether the core business problem is being solved.

---

# What Makes a Capability Part of the MVP?

A capability belongs in the MVP when it is necessary to:

* Address the core user problem.
* Deliver the intended primary value.
* Validate an important business assumption.
* Demonstrate required AI behavior.
* Meet critical security or governance expectations applicable to the validation stage.
* Generate meaningful evaluation evidence.

A capability does not automatically belong in the MVP simply because it would be useful.

The PM should ask:

> **Can we meaningfully validate the core product without this capability?**

If the answer is yes, the capability may be a candidate for a later release or may be deferred.

---

# Part 8 — MVP Scope vs. Release Scope

**MVP scope and release scope are related, but they are not necessarily the same.**

This distinction is important.

## MVP Scope

The **Minimum Viable Product (MVP)** is the smallest set of capabilities needed to deliver the core user value and generate meaningful evidence that the product solves the intended problem.

The MVP answers:

> **What is the smallest useful version we need to validate the product?**

For PolicyAssist, the MVP centers on:

**Employee Question → Relevant Policy Retrieval → Grounded Response → Citation**

with appropriate handling when sufficient evidence is unavailable:

**Insufficient Evidence → Do Not Invent → Refuse or Escalate**

The MVP should contain enough capability to validate the core product assumptions around:

* Usefulness.
* Retrieval.
* Grounding.
* Response quality.
* Citation behavior.
* Unsupported-question handling.
* Required controls for the intended validation stage.

---

# Release Scope

**Release scope** is the set of capabilities, controls, fixes, and requirements approved for a specific release.

A release may contain:

* Original MVP capabilities.
* Additional features added after MVP validation.
* Required security and governance controls.
* Defect fixes.
* Performance improvements.
* User-experience improvements.
* Additional policy categories.
* Operational capabilities.
* Monitoring capabilities.
* Other approved changes.

The release answers:

> **What are we approving for this specific release, and is it ready?**

---

# MVP and Release Scope Example

Suppose the PolicyAssist MVP contains:

* Policy search.
* Relevant policy retrieval.
* Grounded responses.
* Citations.
* Unsupported-question handling.

After MVP validation, the team may identify additional needs such as:

* Production role-based access control.
* Additional policy categories.
* Improved monitoring.
* Additional user feedback capabilities.
* Performance improvements.
* Expanded operational support.

Those capabilities do not necessarily change what the original MVP was.

They may become part of a subsequent release scope.

The progression can be:

**MVP Definition → MVP Build → MVP Validation → Improvements / Additional Requirements → Release Scope → Release Validation → Release Decision**

---

# Important PM Distinction

Do not assume:

**MVP = Release Scope**

Instead:

**MVP = Smallest useful version for validation**

**Release Scope = What is included in a specific approved release**

An MVP can be released as a:

* Prototype.
* Pilot.
* Limited release.
* Controlled user release.

A later production release may include a broader scope than the original MVP.

---

# MVP vs. Release Scope Decision

For each capability, determine whether it belongs in:

**MVP**

**Later Release**

**Deferred**

**Out of Scope**

Use the following logic:

| Category          | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| **MVP**           | Required to validate the core product                         |
| **Later Release** | Approved or planned for a subsequent release                  |
| **Deferred**      | Not included now but may be considered later                  |
| **Out of Scope**  | Intentionally outside the current product or project boundary |

### PM Question

> **What must exist to validate the core product, what must exist for a specific release, and what can wait?**

This distinction helps prevent the PM from treating every future product capability as an MVP requirement.

---

# Part 9 — Define MVP Inclusions

Document the capabilities that belong in the MVP.

For PolicyAssist, consider:

* Policy document ingestion.
* Policy retrieval.
* Semantic search.
* Grounded responses.
* Citations.
* Unsupported-question handling.
* Defined response performance.
* Required AI evaluation.
* Required security and governance considerations for the intended validation stage.

Do not automatically include every possible enhancement.

The question is:

> **What must exist for us to meaningfully validate the product?**

---

# Part 10 — Define MVP Exclusions

Document what is explicitly outside the MVP.

Examples may include:

* Advanced analytics.
* Additional user roles not required for initial validation.
* Unnecessary integrations.
* Advanced personalization.
* Capabilities that do not support the core business problem.
* Enhancements that can be validated after the core product proves useful.

For each exclusion, explain whether it is:

**Later Release**

**Deferred**

or

**Out of Scope**

Do not silently remove work from the product.

---

# Deferred vs. Out of Scope

These terms are not interchangeable.

### Later Release

A capability is intentionally planned for a subsequent release.

### Deferred

A capability is not included now but may be considered after additional validation, prioritization, or dependency resolution.

### Out of Scope

A capability is intentionally excluded from the current product or project boundary.

### Example

**Advanced analytics** may be Deferred.

**Additional policy categories** may be planned for a Later Release.

**Replacing Human Resources as the policy authority** should remain Out of Scope.

---

# Part 11 — Create the Consolidated Backlog

Use the following structure:

| ID    | User Story | Requirement | Acceptance Criteria | Priority | Risk / Dependency | MVP? | Release |
| ----- | ---------- | ----------- | ------------------- | -------- | ----------------- | ---- | ------- |
| US-01 |            |             |                     |          |                   |      |         |
| US-02 |            |             |                     |          |                   |      |         |
| US-03 |            |             |                     |          |                   |      |         |
| US-04 |            |             |                     |          |                   |      |         |
| US-05 |            |             |                     |          |                   |      |         |
| US-06 |            |             |                     |          |                   |      |         |
| US-07 |            |             |                     |          |                   |      |         |
| US-08 |            |             |                     |          |                   |      |         |

Use the **Release** column to identify the intended release stage when known.

Your backlog should make the following visible:

**What → Why → Priority → Risk → Dependency → MVP → Release**

---

# Part 12 — MVP Trade-Offs

Identify at least **two trade-offs**.

Examples:

### Scope vs. Speed

Adding more capabilities may increase value but delay validation.

### Accuracy vs. Coverage

Using more documents may increase information coverage while increasing the risk of retrieving outdated or conflicting information.

### Security vs. Convenience

More restrictive access controls may reduce convenience while reducing unauthorized-access risk.

### Complexity vs. Maintainability

Additional AI capabilities may improve functionality while increasing operational complexity.

### Build vs. Validate

Adding more functionality before testing the core workflow can delay the evidence needed to determine whether the product is working.

For each trade-off, explain:

**Option A → Option B → Impact → Decision**

---

# Part 13 — Identify Dependencies

Document important dependencies that could affect MVP delivery or a later release.

Examples:

* Authoritative policy documents.
* Document metadata.
* Identity and access controls.
* AI model availability.
* Retrieval infrastructure.
* Evaluation data.
* Security validation.
* Stakeholder approvals.
* Operational support.

For each major dependency, identify:

**Dependency → Impact if Unavailable → Owner / Responsible Group → Mitigation**

The PM should know which dependencies can block the MVP and which affect only later releases.

---

# Part 14 — Define the Release Relationship

Use your backlog to show how MVP validation leads to future release decisions.

The progression should be:

**MVP → Validate → Learn → Prioritize → Define Release Scope → Validate Release → Release Decision**

For example:

### MVP

Validate core policy retrieval and grounded response behavior.

### Validation

Review retrieval, answer quality, citation, unsupported-question, user, and risk evidence.

### Learn

Identify product gaps and improvements.

### Prioritize

Determine which improvements are necessary, valuable, or risky enough to address next.

### Release Scope

Define the capabilities and controls included in the next release.

### Release Validation

Test the release against its requirements and acceptance criteria.

### Release Decision

Determine whether the release receives:

**GO → CONDITIONAL GO → HOLD → NO-GO**

This keeps the MVP decision separate from the later release decision.

---

# Part 15 — MVP Decision

Make a clear MVP recommendation.

Your decision should answer:

> **What is the smallest product we can build that provides meaningful value and produces reliable evidence about whether PolicyAssist should continue?**

Document:

* MVP capabilities.
* Later-release capabilities.
* Deferred capabilities.
* Out-of-scope items.
* Major dependencies.
* Major risks.
* Validation objectives.
* Important assumptions.

Your MVP should be small enough to validate and complete enough to produce meaningful evidence.

---

# Part 16 — PM Decisions

Make at least **three PM decisions** from the backlog.

Examples:

* Which capability must be in the MVP?
* Which capability belongs in a later release?
* Which capability can be deferred?
* Which capability must remain out of scope?
* Which item presents the greatest delivery risk?
* Which dependency must be resolved first?
* Which feature has insufficient business value to justify MVP scope?
* Which capability should not proceed until a security or governance condition is satisfied?

Use:

**Evidence → Priority → Trade-Off → Decision**

Where appropriate, also include:

**Risk → Owner → Next Action**

---

# Backlog Quality Check

Before moving forward, verify that:

### Every major requirement is represented

Requirements should have a clear relationship to backlog items.

### Every major user story has acceptance criteria

You should know how completion will be evaluated.

### Priorities are justified

The priority should reflect business value, risk, user impact, dependency, or MVP necessity.

### MVP scope is clear

A reviewer should be able to identify exactly what the first useful version includes.

### Release scope is distinguishable

A reviewer should be able to tell which capabilities belong to a later release rather than the MVP.

### Deferred work is visible

Do not silently remove features.

### Out-of-scope work is visible

The project boundary should remain clear.

### High-risk items are visible

The backlog should help the PM see where attention is required.

### Dependencies are visible

The team should know what could block progress.

---

# Common Backlog Problems

Avoid:

### Feature dumping

Adding every stakeholder request to the MVP.

### Treating MVP and release scope as the same thing

An MVP is designed for validation.

A release is an approved scope for a particular release event.

### Technical-task backlogs

A backlog should express product value, not simply a list of engineering activities.

### Missing acceptance criteria

Without acceptance criteria, the team may disagree about completion.

### Unjustified priorities

"High priority" is not enough. Explain why.

### Hidden scope

Do not move work out of the MVP without documenting the decision.

### Ignoring security

Security and authorization should be visible in the backlog rather than discovered only before release.

### Confusing deferred work with rejected work

A deferred feature may be considered later.

An out-of-scope feature is intentionally outside the current product boundary.

### Assuming an MVP is automatically production-ready

An MVP may be useful for validation without satisfying all requirements for a broader production release.

---

# Deliverable

Complete a **PolicyAssist Product Backlog & MVP Record** containing:

1. At least 8 user stories.
2. Requirement traceability.
3. Acceptance criteria.
4. Priorities.
5. Risks and dependencies.
6. MVP designation.
7. Later-release designation where applicable.
8. Deferred capabilities.
9. Out-of-scope capabilities.
10. At least two trade-offs.
11. At least three PM backlog or MVP decisions.

---

# Checkpoint

Before moving forward, answer:

> **What should we build first, what should be included in a later release, what should we defer, what should remain out of scope, and why?**

Your answer should connect:

**Business Need → Requirement → User Story → Priority → MVP → Release Scope**

---

# PM Perspective

The backlog is not just a task list.

It is a decision tool.

The PM uses the backlog to make trade-offs about:

**Value → Risk → Scope → Sequence → Evidence**

The MVP protects the project from trying to solve everything before proving that the core solution works.

Release scope then builds on what was learned from MVP validation and determines what is actually approved for a specific release.

The next milestone will use the defined product scope to examine the AI architecture required to deliver it.

---

# Milestone Completion Standard

Milestone 4 is complete when you have:

* Created at least 8 user stories.
* Traced major stories to requirements.
* Defined acceptance criteria.
* Prioritized the backlog.
* Identified at least 3 high-risk items or dependencies.
* Defined the MVP.
* Distinguished MVP scope from release scope.
* Documented later-release capabilities where applicable.
* Documented deferred and out-of-scope capabilities.
* Identified at least 2 trade-offs.
* Made at least 3 PM backlog or MVP decisions.
* Completed the final checkpoint.

The quality standard is not the number of backlog items.

The quality standard is whether the backlog clearly communicates:

**What we are building → Why we are building it → What comes first → What belongs in the MVP → What belongs in a later release → What can wait → What remains out of scope → What creates risk → What evidence will guide the next decision**

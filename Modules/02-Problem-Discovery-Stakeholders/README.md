# Module 2: Problem Discovery & Stakeholder Engagement

## Purpose

Before an AI solution is designed, the project manager must understand the problem, the people affected by it, and the business outcome the organization is trying to achieve.

This module teaches how to move from an initial business complaint to a clearly defined problem that can be investigated, measured, and eventually addressed through an AI solution.

The goal is not to start with technology.

The goal is to understand the problem first.

## Learning Objectives

By the end of this module, you should be able to:

* Define a clear business problem
* Distinguish symptoms from root causes
* Identify and analyze stakeholders
* Understand competing stakeholder objectives
* Conduct effective discovery
* Identify measurable business outcomes
* Evaluate whether AI is appropriate for a problem
* Translate discovery findings into a foundation for requirements

## Start With The Problem

A common mistake in technology projects is starting with a proposed solution.

Examples:

* "We need an AI chatbot."
* "We need automation."
* "We need a machine learning model."
* "We need a new application."

These statements describe solutions rather than problems.

An AI project manager should ask:

> What problem are we actually trying to solve?

For example:

Instead of:

> "We need an AI assistant."

Ask:

> "What process is taking too much time, causing errors, or preventing employees from achieving the desired outcome?"

The distinction is important because the proposed technology may not be the best solution.

## Problem Statement

A strong problem statement should explain:

* Who is experiencing the problem
* What is happening
* Why it matters
* What impact it creates
* How the problem can be measured

A useful structure is:

> [User or stakeholder] is experiencing [problem] because of [known or suspected cause], resulting in [business impact].

The problem statement should describe the current state rather than prematurely prescribe the solution.

## Current-State Analysis

Before designing a future state, understand the current state.

Document:

* Current process
* People involved
* Systems used
* Inputs
* Outputs
* Manual steps
* Delays
* Errors
* Dependencies
* Exceptions
* Pain points
* Existing controls

The project manager should understand how work happens today before determining how technology should change it.

## Root Cause vs. Symptom

A symptom is what people experience.

A root cause explains why the problem exists.

Example:

**Symptom:**

Employees spend too much time searching for information.

**Possible root causes:**

* Information is stored in multiple systems
* Documents are difficult to locate
* Ownership is unclear
* Processes are inconsistent
* Information is outdated
* Employees do not know which source to trust

If the project addresses only the symptom, the underlying problem may remain.

## Stakeholder Identification

AI projects often affect more people than the direct users.

Potential stakeholders include:

* Executive sponsors
* Business owners
* End users
* Subject matter experts
* Project managers
* Product owners
* IT teams
* Data teams
* Security teams
* Legal or compliance teams
* Operations teams
* Support teams
* Customers
* Regulators

The project manager should identify who:

* Uses the solution
* Owns the process
* Provides information
* Approves decisions
* Supports the technology
* Bears the risk
* Is affected by the outcome

## Conflicting Stakeholder Objectives

Stakeholders rarely want exactly the same thing.

For example:

A business leader may want:

> Faster delivery.

Security may want:

> Stronger controls.

Users may want:

> A simple experience.

Finance may want:

> Lower cost.

Technical teams may want:

> Additional development time.

The project manager must balance these objectives rather than simply accepting the loudest request.

A strong PM makes tradeoffs visible.

## Stakeholder Analysis

A stakeholder analysis should consider:

| Stakeholder       | Interest | Influence | Concern             | Desired Outcome      |
| ----------------- | -------- | --------- | ------------------- | -------------------- |
| Executive Sponsor | High     | High      | Business value      | Successful outcome   |
| Business Owner    | High     | High      | Process improvement | Better performance   |
| End Users         | High     | Medium    | Usability           | Easier workflow      |
| Security          | Medium   | High      | Risk                | Controlled solution  |
| Technical Team    | High     | Medium    | Feasibility         | Deliverable solution |

The exact stakeholders will vary by project.

## Discovery Questions

Good discovery questions uncover facts rather than confirm assumptions.

Examples:

### Problem

* What is happening today?
* Who experiences the problem?
* How frequently does it occur?
* What happens when the problem occurs?

### Process

* What steps are currently performed?
* Which steps are manual?
* Where are delays occurring?
* Where do errors occur?

### Business Impact

* How much time is being lost?
* What does the problem cost?
* Does it affect customers?
* Does it create compliance or operational risk?

### Stakeholders

* Who owns the process?
* Who approves changes?
* Who will use the solution?
* Who could block implementation?

### Success

* What would improvement look like?
* How will success be measured?
* What would make leadership consider the project unsuccessful?

## Requirements Should Not Be Gathered Too Early

Requirements should be based on an understanding of the problem.

If requirements are gathered before discovery, the team may simply document assumptions.

The progression should generally be:

**Problem → Current State → Root Cause → Stakeholders → Desired Outcomes → Requirements**

This creates a stronger foundation for the project.

## Business Outcomes

A business outcome describes the result the organization wants to achieve.

Examples:

* Reduce processing time by 40%
* Reduce manual work
* Improve information accuracy
* Increase customer satisfaction
* Reduce operational risk
* Improve employee productivity

Outcomes should be measurable whenever possible.

## AI Suitability

Not every business problem requires AI.

An AI project manager should evaluate:

* Is the problem information-intensive?
* Does the process involve patterns, classification, prediction, search, summarization, or language?
* Is sufficient data available?
* Is the data reliable?
* Can the organization tolerate AI uncertainty?
* Are there security or privacy concerns?
* Would a simpler solution work better?

The question is not:

> "Can AI do this?"

The better question is:

> "Is AI an appropriate solution for this business problem?"

## Course Project Preview: Petadel PolicyAssist AI

The course includes a fictional capstone project that will be used later to apply the AI project-management concepts taught throughout the course.

The project is:

**Petadel PolicyAssist AI**

Petadel Technology Services (PTS) wants to improve how employees access and understand organizational policies.

The proposed solution is an AI-powered policy assistant designed to help users locate relevant policy information and receive grounded responses based on approved policy documents.

At this stage, you are **not** expected to design or build the solution.

You are simply being introduced to the project so you understand the context that will appear later in the course.

As you progress through the course, you will apply the PM concepts you learn to this project through clearly labeled **Connection To Capstone** sections.

The detailed requirements, architecture, backlog, evaluation, testing, governance, and implementation work will be developed later.

## Practical Exercise 2: Discover The Real Problem

### Scenario

A company reports that employees are spending too much time completing an internal administrative process.

Leadership proposes building an AI assistant to solve the problem.

Employees, managers, IT, and compliance teams have different opinions about what is causing the issue.

You have been assigned as the project manager.

### Part 1: Define The Problem

Write a problem statement that describes:

* Who is affected
* What is happening
* Why it matters
* The business impact

Do not mention a technology solution.

### Part 2: Analyze The Current State

Identify:

* Three current-state problems
* Two possible root causes
* Two process dependencies
* One major risk

### Part 3: Identify Stakeholders

Identify at least five stakeholders.

For each stakeholder, identify:

* Interest
* Influence
* Primary concern
* Desired outcome

### Part 4: Define Business Outcomes

Create three measurable outcomes for the project.

### Part 5: Evaluate AI Suitability

Explain:

1. Why AI could potentially help
2. One reason AI might not be appropriate
3. What additional information you would need before recommending AI

## PM Decision Scenario

Leadership says:

> "We already know we need an AI assistant. Just start writing the requirements."

As the project manager, what should you do?

The strongest PM response is to **pause requirements definition long enough to validate the problem, stakeholders, current state, root causes, and desired outcomes**.

The objective is not to delay the project.

The objective is to prevent the team from building the wrong solution.

## Deliverable

Create a:

**Problem Discovery & Stakeholder Analysis**

Your deliverable should contain:

* Problem Statement
* Current-State Summary
* Root Cause Analysis
* Stakeholder Analysis
* Discovery Findings
* Business Outcomes
* AI Suitability Assessment
* Key Risks

## Key Takeaways

* Start with the problem, not the technology.
* Symptoms are not always root causes.
* Stakeholders may have conflicting objectives.
* Discovery should happen before detailed requirements.
* Business outcomes should be measurable.
* AI should be evaluated for suitability rather than assumed.
* A strong AI PM validates the problem before approving the solution.

## Connection To Capstone

Petadel PolicyAssist AI will later use the discovery and stakeholder-management techniques from this module.

In the capstone, you will translate the project's business problem, stakeholders, current state, and desired outcomes into formal requirements and project decisions.

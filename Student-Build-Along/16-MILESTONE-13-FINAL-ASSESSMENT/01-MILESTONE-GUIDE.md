# Milestone 13 — Final Assessment

## Purpose

This final assessment measures your ability to apply the Artificial Intelligence (AI) Project Management (PM) concepts, tools, and decision-making practices covered throughout the course.

You will demonstrate that you can:

**Understand the problem → Define the product → Plan the work → Manage AI-specific risks → Evaluate evidence → Test the product → Assess readiness → Measure performance → Recommend what happens next**

This is not a test of software-engineering ability.

It is a test of your ability to **manage, evaluate, govern, and make decisions about AI products.**

---

# What You Are Being Assessed On

Your assessment evaluates your ability to:

* Apply Project Management principles to AI initiatives.
* Translate business problems into measurable requirements.
* Define product scope and Minimum Viable Product (MVP).
* Explain AI solutions at a PM level.
* Evaluate data and retrieval quality.
* Evaluate AI response quality.
* Assess citations, grounding, and unsupported responses.
* Identify security, privacy, authorization, and governance risks.
* Evaluate testing and User Acceptance Testing (UAT).
* Assess release and deployment readiness.
* Interpret Key Performance Indicators (KPIs).
* Connect product performance to business outcomes.
* Make evidence-based PM decisions.
* Communicate recommendations to stakeholders and executives.

---

# Assessment Standard

The strongest answers do more than identify a problem.

They demonstrate:

**Evidence → Analysis → Risk → Decision → Action**

For scenario-based questions, explain:

1. What you observe.
2. Why it matters.
3. What risk or requirement is affected.
4. What you would recommend.
5. Why your recommendation is appropriate.

Do not select an answer simply because it sounds cautious or technically sophisticated.

Choose the response that best reflects sound PM judgment based on the evidence provided.

---

# Assessment Structure

The final assessment contains **15 questions**.

| Section                    | Questions |  Points |
| -------------------------- | --------: | ------: |
| AI PM Knowledge            |       1–5 |      20 |
| Scenario-Based PM Judgment |      6–10 |      30 |
| Release Decision           |        11 |      10 |
| KPI Analysis               |        12 |      10 |
| Executive Recommendation   |        13 |      10 |
| End-to-End AI PM Challenge |        14 |      15 |
| Reflection                 |        15 |       5 |
| **Total**                  |    **15** | **100** |

---

# Passing Standard

**80 points or higher = Pass**

|    Score | Result            |
| -------: | ----------------- |
|   90–100 | Excellent         |
|    80–89 | Pass              |
|    70–79 | Needs Improvement |
| Below 70 | Not Passed        |

A strong score is important, but the most important consideration is demonstrated competence in the critical AI PM areas.

---

# Critical Competencies

You must demonstrate sufficient understanding of the following areas:

* AI product requirements.
* Data and knowledge governance.
* AI evaluation.
* Security and authorization.
* Testing and UAT.
* Release readiness.
* KPI interpretation.
* Evidence-based PM decision-making.

A serious misunderstanding in a critical area may require reassessment even when the overall numerical score meets the passing threshold.

---

# Assessment Conditions

You may use:

* Your course notes.
* Your own project artifacts.
* Your own capstone materials.
* Course frameworks and templates.

You may not:

* Copy answers from the Instructor Answer Key.
* Submit another student's work.
* Present the completed Petadel PolicyAssist example as your own project.
* Claim experience or project results you did not personally perform or demonstrate.

The purpose of the assessment is to demonstrate your own understanding and PM judgment.

---

# How to Answer Knowledge Questions

For questions about concepts or frameworks, provide the clearest correct answer.

Demonstrate that you understand:

**What the concept is → Why it matters → How a PM uses it**

Avoid unnecessarily long answers.

---

# How to Answer Scenario Questions

Scenario questions are designed to test judgment.

Read the evidence carefully before answering.

A strong scenario response should identify:

**Situation → Evidence → Risk → PM Response**

For example:

> The AI response is technically plausible, but the retrieved policy is outdated. The issue is therefore not simply answer quality. It is a source-authority and data-governance problem. The PM should prevent the outdated source from being treated as authoritative and require validation of the current policy version.

Your answer should respond to the scenario that was actually presented.

---

# Incomplete Evidence

AI projects often contain incomplete information.

Do not invent missing facts.

When evidence is incomplete:

1. Identify what is known.
2. Identify what is unknown.
3. Explain the risk created by the missing information.
4. State what evidence is needed.
5. Recommend whether to proceed, hold, escalate, or reassess.

A strong PM does not turn missing evidence into an unsupported assumption.

---

# AI Evaluation Guidance

When evaluating an AI product, distinguish between:

## Retrieval Quality

Did the system retrieve the right information?

## Response Quality

Did the AI correctly use the available evidence to produce an acceptable response?

## Citation Quality

Did the citation identify and support the information used?

Do not treat these as one combined measurement.

For example, a system could:

* Retrieve the correct policy.
* Generate an incorrect answer.
* Provide a citation that does not support the claim.

That represents different quality failures.

---

# Grounding

A grounded response is supported by the evidence available to the AI.

When evaluating grounding, ask:

> **Can the important claims in the response be traced back to the supporting evidence?**

An answer that sounds reasonable is not necessarily grounded.

---

# Unsupported Responses

A reliable AI product should not invent information when evidence is unavailable.

When the available evidence does not support an answer, the appropriate response may be:

**Refuse → Explain the limitation → Escalate when appropriate**

Do not reward an AI system simply because it produces an answer.

A correct refusal can be better product behavior than an unsupported answer.

---

# Security and Authorization

Security questions should be evaluated based on the user's authority and the information involved.

Remember:

> **A technically correct answer can still be an unacceptable product response if the user is not authorized to receive the information.**

Unauthorized disclosure is a serious product failure.

Treat authorization and confidential-information exposure as high-priority risks.

---

# Testing and User Acceptance Testing

Testing determines whether requirements and expected behavior are being met.

User Acceptance Testing (UAT) determines whether intended users can successfully complete the required task and accept the result.

A product can:

* Pass technical testing.
* Still fail UAT.

Technical correctness does not automatically equal user acceptance.

---

# Release Decision Framework

Use the same release terminology established throughout the course.

## GO

The product meets the required release conditions and identified risks are acceptable.

**Decision: Proceed with release.**

## CONDITIONAL GO

The product may proceed only under clearly defined conditions.

Conditions should identify:

* What must be monitored or completed.
* Who owns the action.
* When it must be reviewed.
* How success will be verified.

**Decision: Proceed under approved conditions.**

Conditional Go should not be used to bypass a critical unresolved security, authorization, privacy, or safety issue.

## HOLD

The release decision cannot proceed yet because required evidence, remediation, validation, or readiness work is incomplete.

**Decision: Do not proceed until the outstanding condition is resolved or formally reassessed.**

## NO-GO

The product should not be released in its current state.

Examples include:

* Critical security failure.
* Unauthorized information disclosure.
* Material product failure.
* Critical release requirement not satisfied.
* Unacceptable risk for the intended release stage.

**Decision: Do not release. Significant remediation or reassessment is required.**

---

# Release Decision vs. Deployment Decision

These are different decisions.

## Release Decision

> **Should this version be approved to proceed to its intended release stage?**

Choices:

**GO / CONDITIONAL GO / HOLD / NO-GO**

## Deployment Decision

> **Can the approved release be deployed into the intended environment now?**

Choices:

**DEPLOY / HOLD DEPLOYMENT / ROLLBACK**

For example:

**Release = CONDITIONAL GO**

does not automatically mean:

**Deployment = DEPLOY**

A product can have conditional release approval while deployment remains on hold because a production-specific control has not yet been validated.

---

# Release Decision Authority

The Project Manager assesses readiness and provides a recommendation.

The PM should not assume authority to approve a release unless that authority has been explicitly assigned.

The authorized decision-maker may be:

* Product Owner.
* Executive Sponsor.
* Business Owner.
* Steering Committee.
* Release board.
* Governance authority.
* Other formally designated authority.

When answering a release scenario, distinguish between:

**PM Recommendation**

and

**Authorized Release Decision**

when appropriate.

---

# KPI Guidance

For KPI questions, use:

**KPI → Target → Actual → Trend → Threshold → Action**

Do not stop at identifying whether a KPI passed or failed.

Explain:

* What the metric shows.
* Whether it meets the target.
* Whether it is approaching a decision threshold.
* What risk it represents.
* What action the PM should take.

For example:

A KPI may technically be close to target but still represent an important risk if it is trending in the wrong direction.

---

# Security Exceptions

Not every issue has equal severity.

When evaluating security or governance:

* Consider the impact.
* Consider whether the issue is reversible.
* Consider whether confidential information could be exposed.
* Consider whether authorization was bypassed.
* Consider whether the issue affects the intended release stage.

Critical security or authorization failures require action regardless of otherwise strong product performance.

---

# Executive Communication

Executive recommendations should be:

* Clear.
* Evidence-based.
* Decision-oriented.
* Focused on business impact.
* Focused on significant risks.
* Specific about the requested action.

Avoid lengthy technical explanations unless they are necessary to support the decision.

A strong executive recommendation answers:

**What is happening? → Why does it matter? → What does the evidence show? → What do you recommend?**

---

# End-to-End AI PM Thinking

The strongest responses connect the entire lifecycle.

For example:

**Business Problem**

↓

**Requirements**

↓

**MVP / Scope**

↓

**AI Solution**

↓

**Data / Retrieval**

↓

**Evaluation**

↓

**Security / Governance**

↓

**Testing / UAT**

↓

**Release**

↓

**Deployment**

↓

**KPI Monitoring**

↓

**Business Outcome**

↓

**Continuous Improvement**

A decision made in one area can affect another.

For example:

Poor data quality can affect retrieval.

Poor retrieval can affect grounding.

Poor grounding can affect response accuracy.

Poor response accuracy can affect business trust.

That is why AI PM decisions must consider the full product chain.

---

# Question 14: End-to-End AI PM Challenge

The final scenario requires you to think across the complete lifecycle.

When answering, demonstrate that you can move from:

**Problem → Requirements → Scope → AI Solution → Data → Evaluation → Security → Testing → Release → Monitoring → Improvement**

Do not focus only on the technical implementation.

Focus on the PM decisions required at each stage.

---

# Question 15: Reflection

Your reflection should demonstrate what you learned about managing AI products.

Consider:

* What changed in your understanding of AI PM?
* What concept became most important to you?
* What risk would you pay more attention to now?
* What PM skill do you want to strengthen?
* How would you approach an AI project differently after completing this course?

Use specific examples where possible.

---

# Final Assessment Deliverable

Submit your completed:

**Final Assessment**

Make sure all 15 questions are answered.

Your answers should demonstrate:

* Understanding.
* Application.
* Evidence-based reasoning.
* PM judgment.
* Clear communication.

Where a scenario provides numerical evidence, use the numbers in your reasoning.

Where evidence is missing, identify the gap rather than inventing information.

---

# Final PM Challenge

Before submitting, ask yourself:

> **If I were responsible for this AI product, could I defend my decisions to an executive, business owner, technical team, or governance authority?**

Your answers should demonstrate that you can do more than identify what is wrong.

You should be able to explain:

**Why it matters → What evidence supports the concern → What decision is appropriate → What action should happen next**

---

# Final Submission Checklist

Before submitting:

* [ ] All 15 questions are answered.
* [ ] Scenario questions are supported by evidence.
* [ ] Numerical evidence is used where provided.
* [ ] Missing information is identified rather than invented.
* [ ] AI evaluation concepts are applied correctly.
* [ ] Data and retrieval are distinguished from response quality.
* [ ] Security and authorization risks are treated appropriately.
* [ ] UAT is distinguished from technical testing.
* [ ] Release decisions use GO / CONDITIONAL GO / HOLD / NO-GO.
* [ ] Deployment decisions use DEPLOY / HOLD DEPLOYMENT / ROLLBACK.
* [ ] Release authority is considered where applicable.
* [ ] KPI analysis connects target, actual, trend, threshold, and action.
* [ ] Recommendations are evidence-based.
* [ ] Answers reflect your own understanding.
* [ ] The assessment does not copy the Instructor Answer Key.

---

# Reassessment

If you do not meet the passing standard, review the areas where points were lost.

Focus on the underlying competency rather than memorizing the correct answer.

You may need to demonstrate stronger understanding of:

* Requirements.
* AI evaluation.
* Data governance.
* Security and authorization.
* UAT.
* Release readiness.
* KPI interpretation.
* PM decision-making.

The goal of reassessment is demonstrated competency.

---

# Final Course Completion

You have completed the course when you have:

1. Completed the required PM Track.
2. Completed the required course assessments.
3. Completed the M12 Capstone Submission.
4. Completed the Portfolio Package.
5. Passed the Final Assessment.

The optional AI Build-Along provides additional hands-on experience but does not replace the required PM learning or assessment.

---

# Final PM Perspective

AI Project Management is not simply about managing an AI implementation.

It is about managing the decisions surrounding AI.

A strong AI Project Manager can:

**Define the right problem.**

**Build the right product.**

**Use the right evidence.**

**Manage the right risks.**

**Test the right outcomes.**

**Make the right readiness decision.**

**Measure the right results.**

**Improve the product based on evidence.**

The final question is not:

> **Did the AI work?**

The stronger question is:

> **Did the product create sufficient value, meet its requirements, manage its risks, and generate enough evidence to justify the next decision?**

That is the standard of evidence-based AI Project Management.

**Problem → Evidence → Decision → Action → Outcome**

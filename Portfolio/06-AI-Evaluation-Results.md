# 06: AI Evaluation Results

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Evaluation Area:** AI Evaluation & Quality

---

## Purpose

This artifact documents the evaluation approach, current prototype evidence, quality targets, identified gaps, and release implications for PolicyAssist AI.

The purpose of evaluation is to determine whether the system performs according to measurable requirements rather than relying on subjective statements such as:

> "The AI works well."

A working prototype demonstrates technical feasibility.

Formal evaluation determines whether the product meets its quality requirements.

---

# Evaluation Objective

PolicyAssist must demonstrate that it can:

* Retrieve relevant policy information.
* Use authoritative and active policy content.
* Produce accurate responses.
* Ground responses in supporting evidence.
* Provide correct citations.
* Refuse unsupported questions safely.
* Handle false premises.
* Handle mixed questions.
* Handle multi-policy questions.
* Protect restricted information.
* Respond within the required performance threshold.

---

# Evaluation Vs. Testing

Testing determines whether defined system requirements and behaviors function correctly.

Evaluation measures the quality of AI behavior.

Both are required.

For example:

**Testing**

> Can the application retrieve a policy document?

**Evaluation**

> How often does the application retrieve the correct policy evidence across representative questions?

---

# Quality Dimensions

PolicyAssist evaluation covers:

| Dimension                | Evaluation Question                                        |
| ------------------------ | ---------------------------------------------------------- |
| Retrieval Accuracy       | Did the system find the correct evidence?                  |
| Answer Accuracy          | Is the final answer correct?                               |
| Grounding                | Is the answer supported by retrieved evidence?             |
| Hallucination            | Did the system invent unsupported information?             |
| Citation Correctness     | Does the citation actually support the answer?             |
| Refusal Behavior         | Does the system safely refuse unsupported questions?       |
| False-Premise Handling   | Does the system avoid accepting unsupported assumptions?   |
| Mixed Questions          | Are supported and unsupported portions handled separately? |
| Multi-Policy Performance | Can the system combine evidence across policies correctly? |
| Security Behavior        | Does the system prevent unauthorized disclosure?           |
| Performance              | Does the system meet the latency requirement?              |

---

# Evaluation Targets

The project established the following targets:

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported-Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |
| Critical Security Incidents  |            0 |
| User Satisfaction            |        ≥ 85% |

These targets represent project acceptance criteria and must be supported by evidence.

---

# Evaluation Dataset

A formal evaluation dataset should contain at least **30 representative cases**.

The dataset should not consist exclusively of easy questions.

The current evaluation design contains:

| Category                      |  Cases |
| ----------------------------- | -----: |
| Direct Questions              |      6 |
| Paraphrased Questions         |      6 |
| Unsupported Questions         |      4 |
| False-Premise Questions       |      3 |
| Mixed Questions               |      3 |
| Multi-Policy Questions        |      3 |
| Authority / Version Questions |      3 |
| Performance / Edge Cases      |      2 |
| **Total**                     | **30** |

---

# Evaluation Case Structure

Each evaluation record should contain:

| Field             | Purpose                             |
| ----------------- | ----------------------------------- |
| Test ID           | Unique identifier                   |
| Question          | User input                          |
| Category          | Evaluation type                     |
| Expected Behavior | Required system behavior            |
| Expected Source   | Required evidence                   |
| Expected Answer   | Correct answer or required elements |
| Pass Criteria     | Conditions for success              |
| Actual Result     | Observed response                   |
| Result            | Pass / Fail / Partial               |
| Defect ID         | Related defect where applicable     |
| Notes             | Evaluation observations             |

---

# Direct Questions

Direct questions test normal policy retrieval.

Example:

> "How many days per week can an eligible employee work remotely?"

Expected behavior:

* Retrieve the Remote Work Policy.
* Use eligible evidence.
* Provide the correct answer.
* Provide a supporting citation.

---

# Paraphrased Questions

Paraphrased questions test whether semantic retrieval works beyond exact wording.

Example:

> "What is the maximum number of days I can work from home each week?"

The system should identify the same relevant policy information even though the wording differs.

---

# Unsupported Questions

Unsupported questions test whether the system knows when it lacks sufficient evidence.

Example:

> "How many vacation days do PTS employees receive?"

If an approved vacation policy is unavailable, the system should not invent a number.

Expected result:

**Safe refusal / limitation.**

---

# False-Premise Questions

False-premise questions contain an unsupported assumption.

Example:

> "Why does PTS provide fathers with 20 weeks of paid leave?"

The system should not accept the premise as fact unless approved evidence establishes it.

Expected behavior:

* Identify the unsupported premise.
* Avoid fabricating policy information.
* Provide correction or safe limitation where appropriate.

---

# Mixed Questions

Mixed questions contain both supported and unsupported requests.

Example:

> "How much parental leave do I receive, and how many vacation days do I receive?"

The system should:

* Answer the supported portion.
* Identify the unsupported portion.
* Cite evidence for the supported portion.
* Avoid inventing information for the unsupported portion.

---

# Multi-Policy Questions

Multi-policy questions require information from more than one policy.

Example:

> "Can I work remotely when I am absent from work, and what are the attendance requirements?"

This type of scenario tests:

* Retrieval across policies.
* Evidence selection.
* Response synthesis.
* Citation correctness.
* Grounding.
* Potential conflicts.

Poor performance on multi-policy questions can be hidden by strong single-policy performance.

---

# Authority And Version Evaluation

The evaluation must verify that the system does not use:

* Draft policies.
* Superseded policies.
* Unverified policies.
* Conflicting policies whose authority has not been established.

Expected behavior:

> **If authority cannot be established, the system must not automatically select one source.**

---

# Prototype Evaluation Evidence

The prototype has demonstrated successful behavior across several initial scenarios.

### Evaluation 1 — Happy Path

**Question:** Parental leave question.

**Expected:** Retrieve approved leave information.

**Result:** PASS.

---

### Evaluation 2 — Paraphrase

**Question:** Paraphrased parental leave question.

**Expected:** Retrieve semantically related policy information.

**Result:** PASS.

---

### Evaluation 3 — Unsupported Question

**Question:** Vacation-day question where approved evidence was unavailable.

**Expected:** Refuse or state insufficient information.

**Result:** PASS.

---

### Evaluation 4 — False Premise

**Question:** Question assuming fathers receive a specific amount of paid leave not established by policy.

**Expected:** Do not accept unsupported premise.

**Result:** PASS.

---

### Evaluation 5 — Mixed Question

**Question:** Supported parental-leave question combined with unsupported vacation information.

**Expected:** Answer supported portion and identify unsupported portion.

**Result:** PARTIAL PASS / REQUIRES FURTHER VALIDATION.

This scenario demonstrated why mixed questions must be explicitly included in formal evaluation.

---

# Prototype Evaluation Interpretation

The initial results demonstrate that the architecture can support several important AI behaviors.

However, these tests are not sufficient to claim that the project has achieved the formal evaluation targets.

A small number of successful examples cannot establish:

* 90% retrieval accuracy.
* 90% answer accuracy.
* Less than 2% hallucination.
* 100% citation correctness.
* 100% unsupported-question refusal.

Those claims require a structured evaluation dataset and documented results.

---

# Citation Evaluation

Citation correctness is treated separately from citation presence.

A response may contain a citation but still fail evaluation if the cited source does not support the answer.

### Pass

**Answer:** Supported by retrieved policy evidence.

**Citation:** Correctly identifies the supporting evidence.

### Fail

**Answer:** Contains unsupported information.

**Citation:** Points to a document that does not substantively support the claim.

This is a significant quality risk because an incorrect citation can create false confidence.

---

# Grounding Evaluation

A response passes grounding evaluation when its substantive claims are supported by the evidence provided to the model.

The evaluator should determine:

1. What claims were made?
2. What evidence was retrieved?
3. Does the evidence support each material claim?
4. Did the model add unsupported information?
5. Does the citation correspond to the actual supporting evidence?

---

# Hallucination Evaluation

Hallucination should be evaluated using representative questions.

A hallucination occurs when the system presents unsupported or incorrect information as fact.

The project target is:

**Hallucination Rate < 2%**

High-risk hallucinations should be treated more seriously than cosmetic or wording errors.

A fabricated policy requirement can be a release-blocking defect.

---

# Retrieval Evaluation

Retrieval evaluation should determine whether the system found the evidence needed to answer the question.

A retrieval failure can occur when:

* The correct policy exists but is not retrieved.
* The wrong policy is retrieved.
* Irrelevant sections dominate results.
* An outdated policy is retrieved.
* An unauthorized policy is retrieved.
* A conflicting policy is selected.

The PM should distinguish retrieval failures from generation failures.

---

# Answer Accuracy Evaluation

A response can fail even when retrieval succeeds.

Example:

**Retrieved Evidence**

> Employees may work remotely up to three days per week.

**Generated Answer**

> Employees may work remotely five days per week.

Retrieval succeeded.

Answer generation failed.

This distinction is important for root-cause analysis.

---

# Performance Evaluation

The target response latency is:

**≤ 10 seconds**

Measurement should begin when the user submits the question and end when the complete response is displayed.

The measurement should include:

* Processing.
* Embedding.
* Retrieval.
* Eligibility validation.
* LLM generation.
* Grounding.
* Citation handling.
* Display.

Formal performance testing must use representative conditions rather than a single successful response.

---

# Evaluation Results By Category

Overall metrics should not be considered sufficient without category-level analysis.

For example:

| Category               |                             Result |
| ---------------------- | ---------------------------------: |
| Direct Questions       |                             Strong |
| Paraphrased Questions  |                             Strong |
| Unsupported Questions  |                             Strong |
| False Premises         |                             Strong |
| Mixed Questions        |        Requires Further Validation |
| Multi-Policy Questions |        Poor / Requires Remediation |
| Authority / Version    |         Requires Formal Validation |
| Performance            | Requires Formal Dataset Validation |

The category results demonstrate why an overall score can hide important weaknesses.

---

# Multi-Policy Failure

The project identified poor performance on multi-policy questions.

Potential causes include:

### Data

Relevant information may be fragmented across policies.

### Retrieval

The retrieval layer may return only one relevant policy.

### Chunking

Required context may be separated across chunks.

### Prompting

The model may not receive clear instructions for combining evidence.

### Application Logic

The application may not correctly manage multiple evidence sources.

### Model

The model may struggle to synthesize multiple sources accurately.

### Citation Handling

The application may not correctly associate claims with multiple supporting sources.

The failure therefore requires root-cause analysis rather than assuming that the language model is solely responsible.

---

# Defect Severity

AI defects are classified according to business impact.

## Critical

Examples:

* Unauthorized disclosure.
* Fabricated critical policy information.
* Severe security failure.
* Major compliance risk.

**Release impact:** No-Go.

## High

Examples:

* Incorrect policy answer.
* Incorrect citation.
* Active policy not retrieved.
* Significant grounding failure.
* Frequent multi-policy failures affecting important business use.

**Release impact:** Fix before production unless formally accepted through appropriate governance.

## Medium

Examples:

* Confusing response.
* Minor inconsistency.
* Usability problem.

## Low

Examples:

* Cosmetic formatting.
* Minor wording issue.

---

# Root-Cause Process

When an evaluation failure occurs:

```text id="b5c8dv"
Failure
   ↓
Classify
   ↓
Identify Affected Layer
   ↓
Analyze Root Cause
   ↓
Create Defect / Backlog Item
   ↓
Correct
   ↓
Retest
   ↓
Regression Evaluation
   ↓
Accept / Escalate
```

Potential failure layers include:

* Data.
* Document processing.
* Retrieval.
* Prompt/application logic.
* Model.
* Response handling.
* User interface.

---

# Evaluation Evidence

A production-quality evaluation package should contain:

* Evaluation dataset.
* Expected answers.
* Expected evidence.
* Evaluation methodology.
* Scoring rules.
* Actual results.
* Category-level results.
* Defect records.
* Root-cause analysis.
* Corrective actions.
* Retest evidence.
* Final metrics.
* Approval.

---

# Regression Evaluation

AI changes can alter behavior that previously worked.

Regression evaluation should therefore be triggered by changes such as:

* Model changes.
* Embedding changes.
* Retrieval changes.
* Prompt changes.
* Knowledge-base changes.
* Chunking changes.
* Application logic changes.
* Security changes.

Previously passing evaluation cases should be rerun when affected functionality changes.

---

# Current Evaluation Status

| Area                       | Status                 |
| -------------------------- | ---------------------- |
| Evaluation Strategy        | Defined                |
| Quality Metrics            | Defined                |
| Thresholds                 | Defined                |
| Evaluation Categories      | Defined                |
| 30-Case Dataset Structure  | Defined                |
| Initial Prototype Tests    | Completed              |
| Retrieval Target           | Not Formally Validated |
| Answer Accuracy Target     | Not Formally Validated |
| Hallucination Target       | Not Formally Validated |
| Citation Target            | Not Formally Validated |
| Unsupported Refusal Target | Not Formally Validated |
| Multi-Policy Performance   | Requires Remediation   |
| Security Evaluation        | Pending                |
| Formal UAT                 | Pending                |

---

# Evaluation Release Gate

Production evaluation should not be approved unless:

* [ ] Minimum 30-case evaluation completed.
* [ ] Retrieval accuracy ≥ 90%.
* [ ] Answer accuracy ≥ 90%.
* [ ] Hallucination rate < 2%.
* [ ] Citation correctness = 100%.
* [ ] Unsupported-question refusal = 100%.
* [ ] Multi-policy performance validated.
* [ ] Authority/version scenarios pass.
* [ ] Security-sensitive scenarios pass.
* [ ] Performance target is met.
* [ ] Critical/high defects are resolved or formally dispositioned.
* [ ] Failed cases have documented root causes.
* [ ] Corrections have been retested.
* [ ] Evaluation evidence has been reviewed and approved.

---

# PM Decision

The correct PM decision is not:

> "The prototype works, so evaluation is complete."

The correct decision is:

> **Continue evaluation and remediation before production approval.**

The prototype has demonstrated technical feasibility and several successful AI behaviors.

However, the formal quality targets have not yet been demonstrated through sufficient evidence.

The multi-policy weakness is particularly important because it represents a known category-specific quality problem.

---

# Current Evaluation Decision

**MVP Evaluation Position:** Continue.

**Production Evaluation Position:** HOLD.

### Conditions To Remove HOLD

1. Complete the formal 30-case evaluation.
2. Measure results by category.
3. Investigate multi-policy failures.
4. Correct identified defects.
5. Retest affected cases.
6. Validate citation correctness.
7. Validate unsupported-question refusal.
8. Validate authority/version behavior.
9. Validate performance.
10. Complete security-sensitive evaluation.
11. Document evidence.
12. Obtain appropriate approval.

---

# Portfolio Evidence

This evaluation demonstrates the ability to:

* Define measurable AI quality.
* Separate testing from evaluation.
* Design an evaluation dataset.
* Measure retrieval and answer accuracy separately.
* Evaluate grounding.
* Measure hallucination.
* Assess citation correctness.
* Test unsupported and false-premise questions.
* Identify category-specific weaknesses.
* Perform root-cause analysis.
* Classify AI defects.
* Establish release gates.
* Make evidence-based release decisions.

---

# Key PM Judgment

The strongest PM judgment in this evaluation was recognizing that:

> **A high overall metric does not automatically mean the AI product is ready for production.**

Category-specific failures, particularly failures involving important business scenarios, must be investigated even when aggregate performance appears acceptable.

---

# Final Evaluation Principle

> **AI quality is demonstrated through repeatable evidence across representative scenarios—not through a successful demonstration or a single accuracy score.**

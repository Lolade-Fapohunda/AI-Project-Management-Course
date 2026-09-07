# Module 7: AI Evaluation & Quality

## Purpose

An AI system should not be considered successful simply because it works.

The AI Project Manager must determine whether the system is producing results that are:

* Accurate
* Reliable
* Grounded
* Consistent
* Relevant
* Safe
* Fast enough
* Acceptable to users

This module teaches how to establish AI quality standards, define measurable evaluation criteria, design evaluation datasets, interpret results, manage defects, and make evidence-based project decisions.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain why AI systems require specialized evaluation.
* Distinguish between testing and evaluation.
* Define measurable AI quality metrics.
* Create evaluation criteria and acceptance thresholds.
* Build an evaluation dataset.
* Evaluate accuracy, relevance, grounding, and hallucination.
* Understand precision, recall, and related concepts at a PM level.
* Analyze evaluation results and identify trends.
* Define defect severity for AI failures.
* Make Go, Hold, or No-Go decisions based on evidence.

---

## What Is AI Evaluation?

AI evaluation is the structured process of measuring whether an AI system performs according to defined expectations.

Traditional software testing may ask:

> "Does the feature work?"

AI evaluation must also ask:

> "How well does it work, under what conditions, and how often does it fail?"

AI outputs can vary even when the same general functionality is working.

Therefore, evaluation must be measurable and repeatable.

---

## Testing Vs. Evaluation

Testing and evaluation are related but not identical.

### Testing

Testing determines whether a system behaves according to defined requirements.

Examples:

* Can a user log in?
* Does the search button work?
* Does the application return a response?
* Is an unauthorized user blocked?

### Evaluation

Evaluation measures the **quality of AI behavior**.

Examples:

* How often does the system retrieve the correct information?
* How accurate are the generated answers?
* How often does the AI hallucinate?
* How frequently are citations correct?
* How well does the system handle unsupported questions?

A mature AI project requires both.

---

## Quality Dimensions

AI quality can be evaluated across multiple dimensions.

| Quality Dimension | Question                                                |
| ----------------- | ------------------------------------------------------- |
| **Accuracy**      | Is the answer correct?                                  |
| **Relevance**     | Does the response address the question?                 |
| **Grounding**     | Is the response supported by reliable evidence?         |
| **Consistency**   | Does the system behave reliably across similar cases?   |
| **Completeness**  | Does the answer contain the required information?       |
| **Safety**        | Does the system avoid harmful or unauthorized behavior? |
| **Latency**       | Does the system respond quickly enough?                 |
| **Usability**     | Can users effectively use the system?                   |

The PM should determine which dimensions are critical for the specific product.

---

## Evaluation Metrics

Metrics convert expectations into measurable outcomes.

For example:

> "The AI should be accurate."

is difficult to manage.

A measurable requirement might be:

> "Answer accuracy must be at least 90% on the approved evaluation dataset."

This allows the PM to determine whether the requirement has been achieved.

---

## Retrieval Accuracy

Retrieval accuracy measures whether the system finds the information needed to answer a question.

For a knowledge-based AI system, retrieval is often the first major quality gate.

If the correct information is not retrieved, the model may not have the evidence necessary to produce a correct answer.

### PM Question

> "Did the system retrieve the correct evidence?"

before asking:

> "Did the model generate a good answer?"

---

## Answer Accuracy

Answer accuracy measures whether the final AI response correctly answers the user's question.

A system may retrieve the correct information but still generate an incorrect answer.

Therefore:

**Correct Retrieval ≠ Automatically Correct Answer**

Both must be evaluated.

---

## Grounding

Grounding measures whether the AI response is supported by the information provided to it.

A grounded response should be traceable to appropriate evidence.

For example:

**Question**

> What is the required process?

**Retrieved Evidence**

> Approved source document describing the process.

**AI Response**

> Response accurately reflects the approved source.

The response is grounded.

If the model adds unsupported information, grounding has failed even if part of the answer is correct.

---

## Hallucination

Hallucination occurs when an AI system produces information that is unsupported or incorrect.

The PM should establish a measurable hallucination target.

For example:

> Hallucination rate must remain below the agreed project threshold.

The exact threshold depends on the risk profile of the product.

For high-risk applications, acceptable hallucination may be extremely low.

---

## Unsupported Questions

AI systems must know when they do not have enough evidence to answer.

For example:

> "How many vacation days do I receive?"

If the knowledge base does not contain an approved vacation policy, the system should not invent an answer.

A successful AI system should be able to say:

> "I don't have sufficient information to answer that question."

Refusal behavior is therefore a quality requirement, not necessarily a failure.

---

## Citation Correctness

If an AI system displays sources, the cited source must actually support the answer.

This creates two separate requirements:

1. **Citation Presence**
2. **Citation Correctness**

A citation that exists but does not support the response can be more dangerous than having no citation because it creates false confidence.

### PM Principle

> **A source should only be presented as supporting evidence when it substantively supports the response.**

---

## Precision And Recall

Precision and recall are commonly used evaluation concepts.

### Precision

Precision asks:

> "Of the information the system retrieved, how much was relevant?"

High precision means the system retrieves fewer irrelevant results.

### Recall

Recall asks:

> "Of the relevant information that could have been retrieved, how much did the system find?"

High recall means the system misses fewer relevant results.

A PM does not need to calculate these metrics manually in most projects.

The PM needs to understand what they measure and why they matter.

---

## Evaluation Dataset

An evaluation dataset is a controlled collection of questions, expected answers, source evidence, and expected system behavior.

A useful dataset should include different types of scenarios.

### Happy Path

Questions that should be answered successfully.

### Paraphrased Questions

Questions that use different wording but have the same meaning.

### Unsupported Questions

Questions where the system should refuse to answer.

### False Premise Questions

Questions containing incorrect assumptions.

### Multi-Part Questions

Questions containing both supported and unsupported information.

### Edge Cases

Unusual or difficult questions that may expose weaknesses.

### Access-Control Cases

Questions involving information that some users should not be able to access.

---

## Building An Evaluation Dataset

A basic evaluation record may contain:

| Field                 | Purpose                               |
| --------------------- | ------------------------------------- |
| **Test ID**           | Unique identifier                     |
| **Question**          | User input                            |
| **Expected Behavior** | What the system should do             |
| **Expected Source**   | Supporting evidence                   |
| **Expected Answer**   | Correct response or required elements |
| **Category**          | Type of evaluation                    |
| **Pass Criteria**     | Conditions for success                |
| **Actual Result**     | System response                       |
| **Pass / Fail**       | Evaluation result                     |
| **Notes**             | Observations or defects               |

The evaluation dataset becomes a repeatable measurement tool.

---

## Evaluation Categories

A strong evaluation should cover more than obvious questions.

Recommended categories include:

* Retrieval
* Answer accuracy
* Grounding
* Citation correctness
* Unsupported questions
* False premises
* Multi-part questions
* Edge cases
* Security-sensitive behavior
* Performance

This helps identify weaknesses that happy-path testing may miss.

---

## Evaluation Thresholds

Every important metric should have an agreed threshold.

Example:

| Metric                       |       Target |
| ---------------------------- | -----------: |
| Retrieval Accuracy           |        ≥ 90% |
| Answer Accuracy              |        ≥ 90% |
| Hallucination Rate           |         < 2% |
| Citation Correctness         |         100% |
| Unsupported Question Refusal |         100% |
| Response Latency             | ≤ 10 seconds |

These are example project targets.

The PM should ensure that thresholds are agreed upon **before** evaluating results whenever possible.

---

## Measuring Performance

Performance should be measured under realistic conditions.

A response that takes two seconds during development may take much longer when:

* More users are active.
* More documents are indexed.
* Queries become complex.
* Infrastructure resources are constrained.

The PM should therefore define:

* Target response time.
* Test conditions.
* Sample size.
* Measurement method.
* Acceptable threshold.

---

## Evaluation Results

Evaluation results should be analyzed rather than simply recorded.

For example:

> Retrieval Accuracy = 94%

This sounds positive.

But suppose:

* Employee questions = 98%
* Policy exception questions = 72%
* Multi-policy questions = 68%

The overall metric hides important weaknesses.

The PM should therefore examine performance by category where appropriate.

---

## Defect Severity

AI defects should be classified according to business impact.

### Critical

Examples:

* Unauthorized disclosure of sensitive information.
* Fabricated critical policy information.
* Major security failure.
* System behavior creating severe legal or compliance risk.

**Release impact:** No-Go.

### High

Examples:

* Incorrect policy answer.
* Incorrect supporting citation.
* Failure to retrieve an active authoritative source.
* Significant grounding failure.

**Release impact:** Fix before production unless formally accepted through appropriate governance.

### Medium

Examples:

* Confusing response.
* Poor formatting.
* Minor usability issue.
* Non-critical inconsistency.

### Low

Examples:

* Cosmetic formatting issue.
* Minor wording problem.

Severity should reflect **impact**, not merely technical complexity.

---

## Root Cause Analysis

When an AI system fails, the PM should avoid assuming that the model is always the problem.

A failure could originate from:

**Data**

↓

**Document Processing**

↓

**Retrieval**

↓

**Prompt / Application Logic**

↓

**Model**

↓

**Response Handling**

↓

**User Interface**

The PM should work with technical stakeholders to identify the actual source of the failure.

---

## Evaluation Feedback Loop

AI evaluation should be iterative.

**Evaluate**

↓

**Identify Failure**

↓

**Analyze Root Cause**

↓

**Create Defect / Backlog Item**

↓

**Fix**

↓

**Retest**

↓

**Evaluate Again**

This creates continuous quality improvement.

---

## Evaluation Evidence

A PM should be able to answer:

* What was tested?
* How many cases were tested?
* What categories were included?
* What were the results?
* What failed?
* How severe were the failures?
* What caused the failures?
* What was corrected?
* Were the corrections retested?
* Does the system meet the agreed thresholds?

Without this evidence, a claim such as:

> "The AI is accurate."

is not sufficient for a release decision.

---

## Practical Exercise 7: Build An AI Evaluation Plan

### Scenario

An AI knowledge assistant has completed initial development.

The development team reports:

> "The system is working well."

You are given the following results:

| Metric                       |    Result |       Target |
| ---------------------------- | --------: | -----------: |
| Retrieval Accuracy           |       94% |        ≥ 90% |
| Answer Accuracy              |       91% |        ≥ 90% |
| Hallucination Rate           |      1.5% |         < 2% |
| Citation Correctness         |       96% |         100% |
| Unsupported Question Refusal |      100% |         100% |
| Response Latency             | 8 seconds | ≤ 10 seconds |

Additional evaluation shows that the system performs poorly on multi-policy questions.

### Part 1: Evaluate The Results

Identify which metrics pass and which fail.

### Part 2: Investigate The Failure

Explain why the overall metrics may not tell the complete story.

Identify additional information you would request.

### Part 3: Define Evaluation Categories

Create at least **six evaluation categories**.

For each category, define:

* Example test case
* Expected behavior
* Pass criteria

### Part 4: Define Defect Severity

Create examples of Critical, High, Medium, and Low AI defects.

### Part 5: Analyze Root Cause

Identify possible causes of poor multi-policy performance.

Consider:

* Data
* Retrieval
* Prompting
* Model
* Application logic
* User experience

### Part 6: PM Decision

Decide whether the system should:

* Proceed
* Proceed With Conditions
* Hold

Support your decision using:

1. **Evidence**
2. **Quality Metrics**
3. **Defects**
4. **Risk**
5. **Required Actions**

---

## PM Decision

Leadership says:

> "The overall accuracy is above 90%, so we should launch."

You discover that citation correctness is only 96%, even though the project target is 100%.

You also discover that multi-policy questions fail frequently.

As the AI Project Manager, determine whether the system should proceed toward production.

Your decision should address:

* Metric thresholds
* Business risk
* Citation reliability
* Failure patterns
* User impact
* Defect severity
* Required remediation
* Release readiness

---

## Artifact / Output

Create an **AI Evaluation & Quality Plan** containing:

* Evaluation objectives
* Quality dimensions
* Evaluation dataset structure
* Test categories
* Metrics
* Thresholds
* Defect severity
* Evaluation results
* Root-cause process
* Retesting process
* Release decision criteria

The artifact should demonstrate that you can determine whether an AI system is actually meeting its quality requirements.

---

## Decision / Reflection

Answer the following:

1. Why is "the AI works" not an adequate quality statement?
2. Why should evaluation include unsupported and false-premise questions?
3. Why can a high overall accuracy score hide important failures?
4. Why is citation correctness different from citation presence?
5. Why should hallucination be measured?
6. Why should evaluation thresholds be established before release decisions?
7. When should an AI quality failure prevent production release?

---

## Key Takeaways

* AI systems require measurable evaluation, not subjective confidence.
* Testing determines whether requirements are met; evaluation measures AI quality and behavior.
* Retrieval accuracy and answer accuracy are separate measurements.
* Grounding connects responses to reliable evidence.
* Hallucination must be actively measured and controlled.
* Unsupported questions require appropriate refusal behavior.
* Citations must substantively support the responses they accompany.
* Evaluation datasets should include normal cases, paraphrases, unsupported questions, false premises, multi-part questions, and edge cases.
* Metrics should have agreed thresholds.
* Overall metrics can hide serious category-specific failures.
* Defect severity should reflect business impact.
* Failed AI behavior should be investigated for root cause rather than automatically blamed on the model.
* Evaluation is an iterative process that continues throughout the AI product lifecycle.

---

## Connection To Capstone

The evaluation principles from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will evaluate:

* Retrieval accuracy
* Answer accuracy
* Grounding
* Citation correctness
* Unsupported-question refusal
* False-premise handling
* Multi-policy questions
* Performance
* Security-sensitive behavior

The capstone evaluation targets include:

* **Retrieval Accuracy ≥ 90%**
* **Answer Accuracy ≥ 90%**
* **Hallucination < 2%**
* **Citation Correctness = 100%**
* **Unsupported-Question Refusal = 100%**
* **Response Latency ≤ 10 Seconds**

These targets will be validated through a structured evaluation dataset rather than assumed to be achieved.

---

## Module Completion Checklist

Before moving to Module 8, confirm that you can:

* [ ] Explain the difference between testing and AI evaluation.
* [ ] Define measurable AI quality metrics.
* [ ] Create an evaluation dataset.
* [ ] Evaluate retrieval and answer accuracy separately.
* [ ] Assess grounding and citation correctness.
* [ ] Test unsupported and false-premise questions.
* [ ] Define evaluation thresholds.
* [ ] Classify AI defects by severity.
* [ ] Analyze failures and potential root causes.
* [ ] Make a **Proceed, Proceed With Conditions, or Hold** decision based on evidence.
* [ ] Complete the **AI Evaluation & Quality Plan**.

**Module Complete When:** You can determine whether an AI system meets its quality requirements using measurable evidence rather than assumptions.

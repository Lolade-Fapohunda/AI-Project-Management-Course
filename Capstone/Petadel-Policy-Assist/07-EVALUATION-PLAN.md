# 07: AI Evaluation & Quality Plan

## Purpose

This document defines how Petadel PolicyAssist AI will be evaluated to determine whether the system produces accurate, grounded, reliable, and acceptable results.

AI evaluation is different from simply confirming that the application works.

A system can:

* Run successfully
* Retrieve documents
* Generate fluent answers
* Pass functional tests

and still produce incorrect or unsafe answers.

The Project Manager must therefore establish measurable evaluation criteria and require evidence before approving an MVP or production release.

---

## 1. Evaluation Objective

The evaluation objective is to determine whether PolicyAssist:

1. Retrieves the correct policy information.
2. Generates accurate answers.
3. Grounds answers in authoritative policy evidence.
4. Avoids hallucinating unsupported information.
5. Refuses questions when sufficient evidence does not exist.
6. Provides correct citations.
7. Handles paraphrased and multi-policy questions.
8. Meets response-time requirements.
9. Maintains quality across representative scenarios.
10. Provides sufficient evidence for release decisions.

### Evaluation Principle

> **An AI system is not accepted because it sounds correct. It is accepted because measured evidence demonstrates that it meets defined quality criteria.**

---

## 2. Evaluation Vs. Testing

Testing and evaluation are related but different.

| Testing                                           | Evaluation                                                      |
| ------------------------------------------------- | --------------------------------------------------------------- |
| Determines whether the system behaves as expected | Determines how well the AI performs                             |
| Often focuses on individual functions             | Measures system quality across datasets                         |
| Identifies defects                                | Measures quality and performance                                |
| Example: Can a user submit a question?            | Example: Does retrieval achieve ≥90% accuracy?                  |
| Example: Does login work?                         | Example: Does the system consistently ground answers correctly? |

Both are required.

---

## 3. Evaluation Dimensions

PolicyAssist should be evaluated across multiple dimensions.

### Core Dimensions

* Retrieval accuracy
* Answer accuracy
* Grounding
* Hallucination
* Unsupported-question handling
* Citation correctness
* Paraphrase handling
* Multi-policy handling
* Response latency
* User satisfaction
* Security-related quality

---

## 4. Retrieval Accuracy

Retrieval accuracy measures whether PolicyAssist retrieves the relevant policy evidence needed to answer a question.

### Example

Question:

> "How many days can I work remotely?"

Expected evidence:

**Remote Work Policy**

The system should retrieve the relevant policy section rather than unrelated documents.

### Target

**Retrieval Accuracy ≥90%**

### Measurement

```text
Correctly Retrieved Cases
------------------------- × 100
Total Retrieval Cases
```

### Acceptance Criterion

At least **90% of representative retrieval evaluation cases** must retrieve the required supporting policy evidence.

---

## 5. Answer Accuracy

Answer accuracy measures whether the generated answer correctly represents the policy evidence.

An answer may retrieve the correct document but still provide an incorrect answer.

### Example

Policy:

> Employees may work remotely up to three days per week.

Incorrect answer:

> Employees may work remotely five days per week.

Retrieval succeeded, but answer accuracy failed.

### Target

**Answer Accuracy ≥90%**

### Acceptance Criterion

At least **90% of representative answer evaluation cases** must receive an answer judged correct against the authoritative policy evidence.

---

## 6. Grounding

Grounding determines whether an AI response is supported by retrieved evidence.

A grounded response should be traceable to the relevant policy content.

### Grounding Requirements

The response should:

* Use retrieved policy evidence.
* Avoid unsupported claims.
* Stay within the scope of the evidence.
* Identify uncertainty when evidence is insufficient.
* Avoid relying on general model knowledge for policy decisions.

### Acceptance Criterion

**100% of supported policy answers must be grounded in authoritative retrieved evidence.**

---

## 7. Hallucination

A hallucination occurs when the AI generates information that is unsupported by the available evidence.

### Example

User asks:

> "How many vacation days do employees receive?"

If the knowledge base does not contain a vacation policy, PolicyAssist should not invent a number.

### Target

**Hallucination Rate <2%**

### Measurement

```text
Unsupported AI Claims
--------------------- × 100
Total Evaluated AI Responses
```

### Acceptance Criterion

The measured hallucination rate must remain **below 2%** across the approved evaluation dataset.

---

## 8. Unsupported Questions

PolicyAssist must recognize when a question cannot be answered from authoritative policy evidence.

Examples:

* A policy does not exist.
* The requested information is not contained in the policy.
* Evidence is insufficient.
* The policy is unresolved or conflicting.
* The user asks for information outside the system's approved scope.

### Expected Behavior

The system should:

1. Identify insufficient evidence.
2. Avoid inventing an answer.
3. Clearly communicate the limitation.
4. Avoid presenting unrelated policy evidence as support.
5. Escalate when appropriate.

### Target

**Unsupported-Question Refusal = 100%**

### Acceptance Criterion

**100% of approved unsupported-question test cases must result in an appropriate refusal or escalation rather than an invented answer.**

---

## 9. Citation Correctness

Citations are a critical trust control.

A citation should only be displayed when the retrieved policy evidence substantively supports the answer.

### Required Behavior

If evidence supports the answer:

> Answer + Supporting Source

If evidence does not support the answer:

> Refusal / Limitation + No Misleading Source

### Citation Rules

PolicyAssist must:

* Cite the relevant policy.
* Cite only evidence actually supporting the response.
* Avoid irrelevant citations.
* Avoid citing superseded policies.
* Avoid citing draft policies.
* Avoid citing unverified policies.
* Avoid allowing the language model to invent citation metadata.

### Target

**Citation Correctness = 100%**

### Acceptance Criterion

**100% of evaluated citations must correctly identify evidence that substantively supports the associated answer.**

---

## 10. Mixed-Question Evaluation

Users may ask questions containing both supported and unsupported components.

### Example

> "How much parental leave do I get, and how many vacation days do I receive?"

PolicyAssist may have evidence for parental leave but no authoritative vacation policy.

### Expected Behavior

The system should:

1. Evaluate each component independently.
2. Answer the supported portion.
3. Identify the unsupported portion.
4. Avoid inventing the missing information.
5. Cite evidence for the supported portion only.

### Acceptance Criterion

**100% of approved mixed-question evaluation cases must correctly separate supported and unsupported components.**

---

## 11. Paraphrase Evaluation

Users will rarely ask questions using the exact language found in policy documents.

Evaluation should therefore include paraphrases.

### Example

Policy language:

> "Employees may work remotely up to three days per week."

User question:

> "How often am I allowed to work from home?"

The system should retrieve the correct evidence.

### Acceptance Criterion

Paraphrased retrieval and answer cases must meet the overall **≥90% accuracy targets**.

---

## 12. Multi-Policy Evaluation

Some questions may require information from more than one policy.

Example:

> "What do I need to do if I am absent and need to notify my manager?"

The system may need to evaluate:

* Attendance Policy
* Other applicable policy information

### Evaluation Requirements

The evaluator should determine whether:

* All necessary policies were retrieved.
* The response correctly combines evidence.
* No policy is incorrectly treated as authoritative.
* Citations support the relevant portions.

### Acceptance Criterion

**100% of approved multi-policy cases must use only applicable authoritative evidence and correctly identify the supporting policies.**

---

## 13. Policy Authority Evaluation

Evaluation must verify that PolicyAssist respects the data governance rules.

The system must not use:

* Draft policies
* Superseded policies
* Unverified policies
* Conflicting unresolved policies

### Acceptance Criteria

* **100%** of ineligible policies excluded from authoritative retrieval.
* **100%** of unresolved authority conflicts prevented from being treated as authoritative.
* **0** evaluated responses based on superseded policy content.
* **0** evaluated responses based on draft policy content.

---

## 14. Evaluation Dataset

A formal evaluation dataset should be created before final acceptance.

The dataset should contain representative questions and expected outcomes.

### Dataset Categories

| Category                | Purpose                             |
| ----------------------- | ----------------------------------- |
| Direct questions        | Basic retrieval and answer accuracy |
| Paraphrased questions   | Semantic retrieval                  |
| Unsupported questions   | Hallucination prevention            |
| False-premise questions | Resistance to incorrect assumptions |
| Mixed questions         | Supported/unsupported separation    |
| Multi-policy questions  | Cross-policy reasoning              |
| Authority cases         | Governance validation               |
| Negative cases          | Safe refusal                        |
| Edge cases              | Boundary behavior                   |
| Performance cases       | Response-time validation            |

---

## 15. Evaluation Dataset Size

The final evaluation should contain enough cases to produce meaningful evidence.

### MVP Minimum

**At least 30 representative evaluation cases.**

The dataset should include multiple policy areas and question types.

### Recommended Distribution

| Category                 | Minimum Cases |
| ------------------------ | ------------: |
| Direct                   |             6 |
| Paraphrased              |             6 |
| Unsupported              |             4 |
| False Premise            |             3 |
| Mixed                    |             3 |
| Multi-Policy             |             3 |
| Authority / Version      |             3 |
| Performance / Edge Cases |             2 |
| **Total**                |        **30** |

The final dataset may contain more than 30 cases when additional coverage is necessary.

---

## 16. Evaluation Case Structure

Each evaluation case should contain:

| Field             | Description                  |
| ----------------- | ---------------------------- |
| Case ID           | Unique identifier            |
| Category          | Evaluation category          |
| User Question     | Question presented to AI     |
| Expected Policy   | Required source              |
| Expected Evidence | Relevant policy content      |
| Expected Answer   | Correct result               |
| Expected Citation | Required source              |
| Expected Behavior | Answer/refusal/escalation    |
| Actual Answer     | System response              |
| Actual Citation   | System source                |
| Result            | Pass/Fail                    |
| Defect ID         | Related defect if applicable |
| Evaluator         | Person completing evaluation |
| Evaluation Date   | Date tested                  |

---

## 17. Evaluation Scoring

Each evaluation case should be scored against predefined criteria.

### Example

| Criterion                  | Result |
| -------------------------- | ------ |
| Correct policy retrieved   | Pass   |
| Correct evidence retrieved | Pass   |
| Answer accurate            | Pass   |
| Grounded                   | Pass   |
| Citation correct           | Pass   |
| Response behavior correct  | Pass   |

A case should not be considered fully successful merely because the final answer appears reasonable.

---

## 18. Evaluation Thresholds

The following targets are established for PolicyAssist.

| Metric                       |                 Target |
| ---------------------------- | ---------------------: |
| Retrieval Accuracy           |                   ≥90% |
| Answer Accuracy              |                   ≥90% |
| Hallucination Rate           |                    <2% |
| Citation Correctness         |                   100% |
| Unsupported-Question Refusal |                   100% |
| Response Latency             | ≥95% within 10 seconds |
| Maximum Response Threshold   | 100% within 15 seconds |
| User Satisfaction            |                   ≥85% |
| Critical Security Incidents  |                      0 |
| Unresolved Critical Defects  |                      0 |

### Important Distinction

The **10-second requirement is a response-time acceptance target**, not a quality metric that can compensate for poor AI accuracy.

A system that responds quickly but gives incorrect answers has failed.

---

## 19. Response-Time Evaluation

Response time must be measured from:

> **User question submission → Complete PolicyAssist response displayed**

Measurement should include:

* Question processing
* Embedding generation
* Vector retrieval
* Policy eligibility validation
* LLM generation
* Grounding
* Citation processing
* Final response display

### MVP Acceptance Criteria

At least:

* **95%** of representative requests complete within **10 seconds**.
* **100%** complete within **15 seconds**.
* At least **30 representative requests** are measured.
* Dataset includes direct, paraphrased, multi-policy, unsupported, and refusal-required questions.
* Every request exceeding **15 seconds** is recorded as a performance failure.

### Evidence Required

| Measure            | Result |
| ------------------ | ------ |
| Number of requests |        |
| Average            |        |
| Median             |        |
| 95th Percentile    |        |
| Maximum            |        |
| Requests >10 sec   |        |
| Requests >15 sec   |        |
| Environment        |        |
| Model Version      |        |
| Result             |        |

---

## 20. Evaluation Evidence

The PM should require documented evidence.

Evidence may include:

* Evaluation dataset
* Evaluation results
* Accuracy calculations
* Hallucination analysis
* Citation review
* Retrieval results
* Response-time measurements
* Defect records
* UAT results
* Security findings
* User feedback

### Evidence Principle

> **No Evidence = Not Yet Accepted.**

---

## 21. Defect Classification

Evaluation failures should be connected to defect management.

### Critical

Examples:

* Fabricated policy
* Unauthorized information exposure
* Security breach
* System consistently using invalid policy authority

**Release impact: No-Go**

### High

Examples:

* Wrong policy answer
* Incorrect citation
* Active policy not retrieved
* Significant hallucination
* Repeated refusal failure

**Release impact: Must be resolved or formally dispositioned before production**

### Medium

Examples:

* Confusing response
* Inconsistent formatting
* Minor usability issue

### Low

Examples:

* Cosmetic issue
* Minor wording improvement

---

## 22. Root Cause Analysis

When evaluation fails, the team should determine why.

Possible root causes include:

* Poor document quality
* Incorrect metadata
* Incorrect authority rules
* Retrieval threshold
* Chunking
* Embedding model
* Prompt design
* Grounding logic
* Citation logic
* Model limitations
* Application logic
* Missing evaluation coverage

### PM Requirement

The team should not simply retest until a failure disappears.

The underlying cause should be investigated and documented.

---

## 23. Evaluation Feedback Loop

Evaluation should follow a controlled improvement cycle:

```text
Evaluate
   ↓
Identify Failure
   ↓
Classify Defect
   ↓
Determine Root Cause
   ↓
Correct
   ↓
Retest
   ↓
Regression Evaluate
   ↓
Document Evidence
   ↓
Accept / Hold
```

---

## 24. Regression Evaluation

Changes can improve one area while damaging another.

Examples:

* New embedding model
* New LLM
* Prompt change
* Retrieval threshold change
* Policy ingestion change
* Chunking change
* Citation logic change

Material changes should trigger regression evaluation.

### Acceptance Criterion

**100% of defined regression-triggering changes must have documented regression evaluation before release approval.**

---

## 25. Model Change Evaluation

Changing the AI model may affect:

* Accuracy
* Hallucination
* Retrieval interpretation
* Response time
* Citation behavior
* Refusal behavior
* User experience

A model change should therefore be treated as a controlled change.

### PM Questions

* Why is the model changing?
* What problem does the change solve?
* What could the change break?
* What evaluation dataset will be used?
* Did quality improve?
* Did performance change?
* Did hallucination increase?
* Did citation correctness remain at 100%?
* Was UAT repeated where necessary?

---

## 26. Evaluation Governance

Evaluation ownership should be clearly assigned.

| Role                 | Responsibility                       |
| -------------------- | ------------------------------------ |
| Project Manager      | Evaluation governance and acceptance |
| AI/Technical Team    | Execute technical evaluation         |
| Data Owner           | Validate policy evidence             |
| Security Team        | Validate security-related evaluation |
| Business Owner       | Validate business relevance          |
| UAT Users            | Validate real-world usability        |
| Governance Authority | Resolve authority-related cases      |

---

## 27. MVP Evaluation Gate

PolicyAssist cannot pass the MVP evaluation gate unless the required evidence demonstrates:

* Retrieval Accuracy ≥90%
* Answer Accuracy ≥90%
* Hallucination Rate <2%
* Citation Correctness = 100%
* Unsupported-Question Refusal = 100%
* Mixed-question handling meets defined criteria
* Authority controls pass
* Required response-time targets pass
* Required MVP evaluation dataset completed
* No unresolved critical defects
* No unresolved critical security findings

### MVP Decision

**Proceed**

All mandatory criteria pass.

**Proceed With Conditions**

Only non-critical gaps remain, with documented owners, deadlines, and controls.

**Hold**

A mandatory quality, safety, security, authority, or acceptance threshold fails.

---

## 28. Production Evaluation Gate

Production evaluation requires stronger evidence than MVP.

Before production release, confirm:

* Required evaluation dataset completed
* Accuracy targets achieved
* Hallucination target achieved
* Citation correctness achieved
* Unsupported-question handling validated
* Regression evaluation completed
* Performance validated
* Security evaluation completed
* UAT completed
* Critical defects = 0
* High defects resolved or formally dispositioned
* Monitoring established
* Rollback available
* Governance approval obtained

---

## 29. Evaluation Reporting

The final evaluation report should summarize:

### Executive Summary

* Overall result
* Major findings
* Quality metrics
* Risks
* Defects
* Release recommendation

### Metrics

| Metric               |       Target | Actual | Status |
| -------------------- | -----------: | -----: | ------ |
| Retrieval Accuracy   |         ≥90% |        |        |
| Answer Accuracy      |         ≥90% |        |        |
| Hallucination        |          <2% |        |        |
| Citation Correctness |         100% |        |        |
| Unsupported Refusal  |         100% |        |        |
| Response Time        | ≥95% ≤10 sec |        |        |
| User Satisfaction    |         ≥85% |        |        |

### Recommendation

* Go
* Proceed With Conditions
* Hold / No-Go

---

## 30. Practical Exercise 7: Build An AI Evaluation Plan

### Scenario

The technical team reports:

> "The model looks really good. Most answers are correct."

Leadership wants to move directly toward release.

However, there is:

* No formal evaluation dataset.
* No documented hallucination measurement.
* No citation accuracy measurement.
* No unsupported-question test set.
* No response-time evidence.
* No regression evaluation.
* No documented evaluation thresholds.

### Your Task

As the Project Manager:

1. Define the evaluation dimensions.
2. Build a minimum 30-case evaluation dataset.
3. Define expected results for each category.
4. Establish measurable acceptance thresholds.
5. Define how hallucination will be measured.
6. Define how citation correctness will be measured.
7. Define unsupported-question evaluation.
8. Define response-time measurement.
9. Define evidence requirements.
10. Determine the release recommendation.

### PM Decision

Choose:

* **Proceed**
* **Proceed With Conditions**
* **Hold**

Your decision must be based on evidence rather than confidence.

---

## 31. Artifact / Output

Complete:

**AI Evaluation & Quality Report**

The artifact should contain:

* Evaluation strategy
* Evaluation dataset
* Evaluation categories
* Expected results
* Actual results
* Metric calculations
* Defect findings
* Hallucination analysis
* Citation analysis
* Response-time analysis
* Regression results
* Evidence
* Acceptance decision
* PM recommendation

---

## 32. PM Decision

The Project Manager should not approve an AI product based on statements such as:

> "The model seems accurate."

or:

> "We tested it and it worked."

The PM should require measurable evidence.

### Decision Principle

> **If quality cannot be measured, quality cannot be reliably accepted.**

---

## 33. Decision / Reflection

Ask:

> **"If leadership asks me to prove that PolicyAssist is accurate, safe, grounded, and ready, can I show them measurable evidence?"**

If the answer is no, the evaluation process is incomplete.

---

## Key Takeaways

* AI evaluation measures how well an AI system performs.
* Testing and evaluation are not the same.
* Retrieval accuracy and answer accuracy must be measured separately.
* Grounding prevents unsupported responses.
* Hallucination must be measured.
* Unsupported questions must be tested explicitly.
* Citation correctness is a critical trust metric.
* Mixed and multi-policy questions require dedicated evaluation.
* Evaluation datasets must represent realistic usage.
* Measurable thresholds are required for acceptance.
* Response time must be measured rather than judged subjectively.
* Material changes require regression evaluation.
* Evaluation failures should trigger root-cause analysis.
* MVP and production require different levels of evidence.
* **No Evidence = Not Yet Accepted.**

---

## Connection To Capstone

This document provides the evaluation framework for Petadel PolicyAssist AI.

It directly supports:

* `03-REQUIREMENTS.md`
* `04-PRODUCT-BACKLOG.md`
* `05-ARCHITECTURE.md`
* `06-DATA-GOVERNANCE.md`
* `08-RISK-SECURITY-GOVERNANCE.md`
* `09-TEST-UAT-PILOT.md`
* `10-RELEASE-DEPLOYMENT.md`
* `11-MONITORING-CONTINUOUS-IMPROVEMENT.md`
* `14-TRACEABILITY.md`
* `16-FINAL-GO-HOLD-NO-GO.md`

The evaluation results become a major input into the MVP gate, UAT decision, production release decision, and final capstone recommendation.

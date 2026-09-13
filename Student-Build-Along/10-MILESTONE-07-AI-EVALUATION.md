# Milestone 7: AI Evaluation

## PM Objective

Determine whether the Artificial Intelligence (AI) product generates responses that are accurate, grounded, safe, useful, and fast enough to meet its defined quality and business requirements.

## Hands-On Objective

Evaluate PolicyAssist using a small, realistic test set and clear Pass/Fail rules.

In Milestone 6, you evaluated **data quality and retrieval quality**.

In this milestone, you will evaluate what happens **after the relevant evidence has been retrieved**.

Your primary question is:

> **Given the information available to the AI, does it produce an acceptable response?**

---

## Important: Evaluate Quality, Not Just Functionality

A working response is not automatically a good response.

Your job is not simply to confirm that:

* The application runs
* A response appears
* The system returns something for the question

Your job is to determine whether the response is good enough for its intended use.

Evaluate whether:

* The answer is correct
* The answer is grounded in the available evidence
* The AI avoids unsupported claims
* The system handles questions it cannot answer appropriately
* The response is delivered within the required time
* The response is useful and understandable
* Citations are present when required
* Citations identify the correct source
* Citations actually support the claims made

> **The goal is not to prove that the AI works. The goal is to determine, using evidence, whether it works well enough to move forward.**

---

# Section 1: Understand What You Are Evaluating

Keep the evaluation layers separate.

### Milestone 6: Retrieval

The question was:

> **Did PolicyAssist retrieve the right evidence?**

You evaluated relevance, authority, currency, metadata, and retrieval quality.

### Milestone 7: Response

The question is:

> **Given the available evidence, did PolicyAssist produce the right answer?**

You will evaluate response accuracy, grounding, unsupported claims, refusal or escalation, usefulness, clarity, and response time.

### Citation Evaluation

Citation quality is evaluated separately from the response.

You will determine:

> **Was a citation provided, did it identify the correct source, and does that source support the claim?**

This separation helps you identify the actual source of a quality problem.

---

# Section 2: Define the Evaluation Test Set

You will use **eight test scenarios**.

Five starter tests are provided below. Add at least **three additional tests** based on the PolicyAssist policy content.

## Starter Tests

| Test ID | Test Question                                               | Expected Behavior                                                                                            | Citation Expected?                   |
| ------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| T01     | How many paid time off days do employees receive each year? | Provide the applicable policy answer based on the approved leave policy.                                     | Yes                                  |
| T02     | How many sick days are available to employees?              | Provide the applicable policy answer based on the approved leave policy.                                     | Yes                                  |
| T03     | What is the company's remote work policy?                   | Provide relevant information from the applicable policy.                                                     | Yes                                  |
| T04     | What are the information security requirements?             | Provide relevant information from the applicable policy.                                                     | Yes                                  |
| T05     | What is the company's policy on bringing pets to work?      | Do not invent an answer. Refuse or escalate because the available policy content does not support an answer. | Yes, when applicable to the response |

Create at least three additional tests.

Your additional tests should include realistic variations such as:

* Different wording for the same policy concept
* A question requiring a specific policy detail
* A question involving more than one policy area
* A question that should not be answerable from the available policy content
* A question that tests whether the system avoids unsupported information

Record your complete test set:

| Test ID | Question | Expected Answer | Expected Behavior | Citation Expected? |
| ------- | -------- | --------------- | ----------------- | ------------------ |
| T01     |          |                 |                   |                    |
| T02     |          |                 |                   |                    |
| T03     |          |                 |                   |                    |
| T04     |          |                 |                   |                    |
| T05     |          |                 |                   |                    |
| T06     |          |                 |                   |                    |
| T07     |          |                 |                   |                    |
| T08     |          |                 |                   |                    |

---

# Section 3: Define the Expected Result Before Testing

For each test, determine what a successful result looks like **before** reviewing the actual response.

Your benchmark should identify:

* The expected answer
* Expected behavior
* Whether the system should answer, refuse, or escalate
* Whether a citation is expected

Do not change your benchmark after seeing the response.

This prevents the evaluation from becoming subjective.

---

# Section 4: Run the Tests

Run all eight questions through PolicyAssist.

For each test, record:

* Question
* Actual response
* Response time
* Whether the system answered appropriately
* Any unsupported claims
* Whether refusal or escalation occurred when expected
* Citation provided, when applicable

Use the same evaluation rules for every test.

---

# Section 5: Evaluate Response Quality

This section evaluates the **response itself**.

Do not use this section to score retrieval quality or citation quality.

## Response Accuracy

Ask:

> **Is the answer factually correct based on the available evidence?**

**Pass:** The response provides the correct answer and contains no material factual error.

**Fail:** The response contains a material factual error or fails to answer the question correctly.

## Completeness

Ask:

> **Does the response contain enough information to answer the question appropriately?**

**Pass:** The response contains the information needed for the intended user to understand the answer.

**Fail:** The response is materially incomplete and does not adequately address the question.

## Grounding

Ask:

> **Are the material claims in the response supported by the evidence available to the AI?**

**Pass:** Material claims can be traced to the available supporting evidence.

**Fail:** One or more material claims cannot be supported by the available evidence.

## Unsupported Claims

Ask:

> **Did the AI add information that is not supported by the available evidence?**

**Pass:** No material unsupported claim is present.

**Fail:** One or more material unsupported claims are present.

## Contradictions

Ask:

> **Does the response conflict with the supporting policy information?**

**Pass:** The response does not materially contradict the supporting evidence.

**Fail:** The response materially contradicts the supporting evidence.

Record your results:

| Test ID | Accurate? | Complete? | Grounded? | Unsupported Claims? | Contradiction? | Response Result |
| ------- | --------- | --------- | --------- | ------------------- | -------------- | --------------- |
| T01     |           |           |           |                     |                |                 |
| T02     |           |           |           |                     |                |                 |
| T03     |           |           |           |                     |                |                 |
| T04     |           |           |           |                     |                |                 |
| T05     |           |           |           |                     |                |                 |
| T06     |           |           |           |                     |                |                 |
| T07     |           |           |           |                     |                |                 |
| T08     |           |           |           |                     |                |                 |

---

# Section 6: Evaluate Refusal and Escalation

A reliable AI product should not invent an answer when the available evidence does not support one.

Use your unsupported-question tests to determine whether PolicyAssist handles these situations appropriately.

Evaluate whether the system:

* Clearly states that it cannot answer
* Avoids inventing information
* Provides an appropriate explanation
* Escalates to a human resource when required

### Pass/Fail Rule

**Pass:** The system does not invent an answer and follows the expected refusal or escalation behavior.

**Fail:** The system provides an unsupported answer, fails to escalate when required, or refuses or escalates when a supported answer should have been provided.

Record:

| Test ID | Expected Behavior | Actual Behavior | Unsupported Claim? | Escalation Appropriate? | Result |
| ------- | ----------------- | --------------- | ------------------ | ----------------------- | ------ |
|         |                   |                 |                    |                         |        |
|         |                   |                 |                    |                         |        |

---

# Section 7: Evaluate Citation Quality Separately

Citation quality is separate from response quality.

A response can be correct while the citation is wrong.

A citation can identify the correct source while failing to support the claim.

Evaluate three separate citation measures.

## Citation Presence

> **Was a citation provided when one was required?**

**Pass:** A citation is present when required.

**Fail:** A required citation is missing.

## Citation Accuracy

> **Does the citation identify the correct authoritative source and applicable version?**

**Pass:** The citation identifies the correct source and correct version when version information applies.

**Fail:** The citation identifies the wrong source, wrong version, outdated source, or another source that does not correspond to the response.

## Citation Support

> **Does the cited source actually support the material claim?**

**Pass:** The cited source supports the material claim or claims made in the response.

**Fail:** The cited source does not support a material claim, only partially supports it in a material way, or conflicts with the claim.

Record:

| Test ID | Citation Required? | Citation Present? | Correct Source? | Correct Version? | Supports Claim? | Citation Result |
| ------- | ------------------ | ----------------- | --------------- | ---------------- | --------------- | --------------- |
| T01     |                    |                   |                 |                  |                 |                 |
| T02     |                    |                   |                 |                  |                 |                 |
| T03     |                    |                   |                 |                  |                 |                 |
| T04     |                    |                   |                 |                  |                 |                 |
| T05     |                    |                   |                 |                  |                 |                 |
| T06     |                    |                   |                 |                  |                 |                 |
| T07     |                    |                   |                 |                  |                 |                 |
| T08     |                    |                   |                 |                  |                 |                 |

Remember:

> **Response accuracy asks: "Is the answer correct?"**

> **Citation presence asks: "Was a citation provided when required?"**

> **Citation accuracy asks: "Does the citation identify the correct source?"**

> **Citation support asks: "Does the cited source support the claim?"**

Do not treat the presence of a citation as proof that the citation is correct.

---

# Section 8: Evaluate Response Performance

Evaluate the employee experience separately from accuracy and citation quality.

## Response Time

Measure how long the system takes to respond.

**Pass:** Response time is **10 seconds or less**.

**Fail:** Response time is greater than **10 seconds**.

## Usefulness

**Pass:** An intended user could reasonably use the response to address the question.

**Fail:** The response is materially incomplete, irrelevant, confusing, or impractical.

## Clarity

**Pass:** The response is understandable and communicates the answer without material ambiguity.

**Fail:** The response is materially unclear, contradictory, or difficult for the intended user to understand.

Record:

| Test ID | Response Time | Useful? | Clear? | Performance Result |
| ------- | ------------: | ------- | ------ | ------------------ |
| T01     |               |         |        |                    |
| T02     |               |         |        |                    |
| T03     |               |         |        |                    |
| T04     |               |         |        |                    |
| T05     |               |         |        |                    |
| T06     |               |         |        |                    |
| T07     |               |         |        |                    |
| T08     |               |         |        |                    |

---

# Section 9: Apply the Overall Test Pass/Fail Rule

Evaluate each applicable quality criterion separately.

Use:

| Quality Area       | Result                       |
| ------------------ | ---------------------------- |
| Response Accuracy  | Pass / Fail                  |
| Completeness       | Pass / Fail                  |
| Grounding          | Pass / Fail                  |
| Unsupported Claims | Pass / Fail                  |
| Contradictions     | Pass / Fail                  |
| Refusal/Escalation | Pass / Fail / Not Applicable |
| Response Time      | Pass / Fail                  |
| Usefulness         | Pass / Fail                  |
| Clarity            | Pass / Fail                  |
| Citation Presence  | Pass / Fail / Not Applicable |
| Citation Accuracy  | Pass / Fail / Not Applicable |
| Citation Support   | Pass / Fail / Not Applicable |

### Overall Test Result

**Pass:** Every applicable mandatory criterion passes.

**Fail:** Any applicable mandatory criterion fails.

One strong result does not cancel another failure.

Examples:

* Correct response + incorrect citation = **Fail**
* Correct response + missing required citation = **Fail**
* Incorrect response + correct citation = **Fail**
* Correct response + material unsupported claim = **Fail**
* Appropriate refusal + no fabricated information = **Pass**, when refusal is the expected behavior

---

# Section 10: Calculate Response Metrics

Calculate these response metrics separately from citation metrics.

## Response Accuracy Rate

**Correct responses ÷ Total applicable response tests × 100**

**Target: ≥ 90%**

## Grounded Response Rate

**Responses supported by available evidence ÷ Total applicable response tests × 100**

**Target: ≥ 90%**

## Unsupported Response Rate

**Responses containing material unsupported claims ÷ Total applicable response tests × 100**

**Target: < 2%**

## Appropriate Refusal/Escalation Rate

**Correct refusals or escalations ÷ Total applicable unsupported-question tests × 100**

**Target: 100%**

## Response Time

**Target: ≤ 10 seconds**

Calculate the average response time across applicable tests.

Record:

| Response Metric                     |    Target | Actual | Pass/Fail | Action Needed |
| ----------------------------------- | --------: | -----: | --------- | ------------- |
| Response Accuracy Rate              |     ≥ 90% |        |           |               |
| Grounded Response Rate              |     ≥ 90% |        |           |               |
| Unsupported Response Rate           |      < 2% |        |           |               |
| Appropriate Refusal/Escalation Rate |      100% |        |           |               |
| Average Response Time               | ≤ 10 sec. |        |           |               |

### Metric Pass/Fail Rules

For metrics where **higher is better**:

**Pass:** Actual ≥ Target

**Fail:** Actual < Target

For metrics where **lower is better**:

**Pass:** Actual ≤ Target

**Fail:** Actual > Target

---

# Section 11: Calculate Citation Metrics

Evaluate citation performance separately.

## Citation Presence Rate

**Citations present when required ÷ Total applicable citation tests × 100**

**Target: 100%**

## Citation Accuracy Rate

**Correct citations ÷ Total applicable citation tests × 100**

**Target: ≥ 95%**

## Citation Support Rate

**Citations that support the material claim ÷ Total applicable citation tests × 100**

**Target: ≥ 95%**

Record:

| Citation Metric        | Target | Actual | Pass/Fail | Action Needed |
| ---------------------- | -----: | -----: | --------- | ------------- |
| Citation Presence Rate |   100% |        |           |               |
| Citation Accuracy Rate |  ≥ 95% |        |           |               |
| Citation Support Rate  |  ≥ 95% |        |           |               |

For all citation metrics:

**Pass:** Actual ≥ Target

**Fail:** Actual < Target

Do not combine response metrics and citation metrics into one overall score.

---

# Section 12: Identify Critical Failures

Some failures require attention regardless of other results.

Treat the following as **critical failures**:

* Unauthorized information is disclosed
* A material policy answer is fabricated
* A response materially contradicts an authoritative policy
* A required refusal or escalation does not occur
* A security or authorization control is bypassed
* A citation materially identifies an incorrect authoritative source when the source could affect the employee's decision
* A citation materially contradicts the answer

A critical failure requires review and corrective action even when a percentage-based quality target has been achieved.

Record any critical failure:

| Critical Failure | Evidence | Potential Impact | Required Action |
| ---------------- | -------- | ---------------- | --------------- |
|                  |          |                  |                 |

---

# Section 13: Analyze Failures

For every failed or concerning test, document:

**What happened?**

[Your observation]

**What should have happened?**

[Expected behavior]

**Which quality area was affected?**

[Response / Citation / Safety / Performance]

**Why does it matter?**

[Business, user, compliance, security, or trust impact]

**Likely cause or hypothesis:**

[Your hypothesis]

**Recommended action:**

[Your recommendation]

Look for patterns rather than treating every failure as an isolated event.

---

# Section 14: Determine Whether Quality Targets Were Met

Review the response and citation metrics separately.

Ask:

* Which response targets were met?
* Which response targets were missed?
* Which citation targets were met?
* Which citation targets were missed?
* Are any critical failures present?
* Which failures create the greatest business risk?
* Is additional testing required?
* Is corrective action required?

Do not allow strong performance in one metric to hide a weakness in another.

For example:

**Response Accuracy = 95%**
**Citation Accuracy = 70%**

The response metric passes, but the citation metric fails.

Both results must remain visible.

---

# Section 15: Make the PM Decision

Based on the evidence, determine what should happen next.

### Proceed

Use this decision when:

* All mandatory quality targets are met
* There are no unresolved critical failures
* The evidence is sufficient to support moving forward

### Hold

Use this decision when:

* The evidence is incomplete
* Additional testing is required
* The team cannot yet make a confident decision

### Return for Improvement

Use this decision when:

* One or more mandatory quality targets are missed
* A critical failure requires corrective action
* The product is not ready for the next stage

Document:

**Decision:**
[Proceed / Hold / Return for Improvement]

**Evidence:**
[Key response and citation results]

**Primary risks:**
[Most important issues]

**Required actions:**
[Actions needed]

**Decision owner:**
[Role responsible]

---

# Section 16: Create a Regression Test Set

AI behavior can change when the data, retrieval configuration, prompts, model, or application changes.

Select at least **three tests** from this milestone that should be repeated after future changes.

Include tests that protect important response and citation behaviors.

| Test ID | What Should Be Verified? | Why This Test Matters | Failure Impact |
| ------- | ------------------------ | --------------------- | -------------- |
|         |                          |                       |                |
|         |                          |                       |                |
|         |                          |                       |                |

These tests become part of your regression test set.

---

# Deliverable: AI Evaluation Results Report

Create an **AI Evaluation Results Report** containing:

* Eight representative test scenarios
* Expected results and evaluation benchmarks
* Actual responses
* Test-level Pass/Fail results
* Response accuracy results
* Grounded response results
* Unsupported response results
* Refusal and escalation results
* Response-time results
* Usefulness and clarity results
* Citation presence results
* Citation accuracy results
* Citation support results
* Response metric targets versus actuals
* Citation metric targets versus actuals
* Any critical failures
* Failure analysis
* At least three regression tests
* PM decision: Proceed, Hold, or Return for Improvement
* Evidence supporting the decision

---

# PM Checkpoint

Before moving forward, you should be able to answer:

> **Does PolicyAssist produce responses that are accurate, grounded, safe, useful, and appropriately supported by citations?**

You should also be able to explain:

* The difference between retrieval quality and response quality
* How response accuracy is measured
* How grounding is evaluated
* How unsupported responses are identified
* How refusal and escalation are evaluated
* How response time is evaluated
* How citation presence is measured
* How citation accuracy is measured
* How citation support is measured
* Why response and citation metrics remain separate
* How an individual test receives a Pass or Fail
* How metric-level Pass/Fail decisions are made
* Which failures are considered critical
* What evidence supports your PM decision
* Which tests should become part of regression testing

---

# PM Perspective

**AI evaluation is evidence-based product management.**

You are not asking whether the system seems impressive.

You are asking whether the product consistently meets defined expectations for response quality, citation quality, safety, performance, and user value.

The progression is:

**Test Scenario → Expected Result → Actual Response → Test Pass/Fail → Response Metrics + Citation Metrics → Target vs. Actual → Critical Failure Review → PM Decision**

The next milestone will focus on **Security & Governance**, where you will determine whether the product can protect users, information, access rights, and organizational policy while delivering its intended value.

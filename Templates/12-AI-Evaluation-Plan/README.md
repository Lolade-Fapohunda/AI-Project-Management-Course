# AI Evaluation Plan

## Purpose

The AI Evaluation Plan defines how an AI solution will be measured for accuracy, reliability, grounding, safety, and business usefulness.

Evaluation should be based on evidence rather than claims that the AI system "works."

---

## 1. Evaluation Overview

| Field            | Details        |
| ---------------- | -------------- |
| Project          | [Project Name] |
| Evaluation Owner | [Name]         |
| Evaluation Date  | [Date]         |
| Version Tested   | [Version]      |
| Dataset Version  | [Version]      |

---

## 2. Evaluation Objectives

* [Objective]
* [Objective]
* [Objective]

---

## 3. Evaluation Dataset

| Category               | Number Of Cases | Purpose   |
| ---------------------- | --------------: | --------- |
| Happy Path             |             [#] | [Purpose] |
| Paraphrased Questions  |             [#] | [Purpose] |
| Unsupported Questions  |             [#] | [Purpose] |
| Edge Cases             |             [#] | [Purpose] |
| Negative Cases         |             [#] | [Purpose] |
| Multi-Source Questions |             [#] | [Purpose] |

---

## 4. Evaluation Metrics

| Metric               | Definition   |   Target |   Actual | Result      |
| -------------------- | ------------ | -------: | -------: | ----------- |
| Retrieval Accuracy   | [Definition] | [Target] | [Actual] | [Pass/Fail] |
| Answer Accuracy      | [Definition] | [Target] | [Actual] | [Pass/Fail] |
| Hallucination Rate   | [Definition] | [Target] | [Actual] | [Pass/Fail] |
| Citation Correctness | [Definition] | [Target] | [Actual] | [Pass/Fail] |
| Unsupported Refusal  | [Definition] | [Target] | [Actual] | [Pass/Fail] |
| Response Latency     | [Definition] | [Target] | [Actual] | [Pass/Fail] |

---

## 5. Grounding And Citation Evaluation

For each evaluated response, determine:

* Did the response use appropriate evidence?
* Does the evidence actually support the answer?
* Is the cited source authoritative?
* Is the cited version current?
* Did the system avoid citing irrelevant evidence?
* Did the system refuse when sufficient evidence was unavailable?

---

## 6. Evaluation Results

| Test ID  | Question / Scenario | Expected Result | Actual Result | Pass/Fail | Notes   |
| -------- | ------------------- | --------------- | ------------- | --------- | ------- |
| EVAL-001 | [Scenario]          | [Expected]      | [Actual]      | [Result]  | [Notes] |
| EVAL-002 | [Scenario]          | [Expected]      | [Actual]      | [Result]  | [Notes] |
| EVAL-003 | [Scenario]          | [Expected]      | [Actual]      | [Result]  | [Notes] |

---

## 7. Defect Analysis

| Defect   | Severity                   | Root Cause | Corrective Action | Retest Required |
| -------- | -------------------------- | ---------- | ----------------- | --------------- |
| [Defect] | [Critical/High/Medium/Low] | [Cause]    | [Action]          | [Yes/No]        |

---

## 8. Evaluation Decision

**Overall Result:**

[Pass / Conditional Pass / Fail]

**Release Recommendation:**

[Proceed / Proceed With Conditions / Hold]

**Reason:**

[Enter rationale.]

---

## PM Quality Check

* [ ] Evaluation objectives are defined.
* [ ] Dataset covers multiple realistic scenarios.
* [ ] Positive and negative cases are included.
* [ ] Metrics are measurable.
* [ ] Targets are defined before testing.
* [ ] Grounding is evaluated.
* [ ] Citation correctness is evaluated.
* [ ] Unsupported questions are evaluated.
* [ ] Defects are documented.
* [ ] Results support the final decision.

---

## Course Connection

Use this template to establish evidence-based AI quality before UAT, pilot, release, and production approval.

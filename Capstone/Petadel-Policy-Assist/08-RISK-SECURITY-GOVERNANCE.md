# 08: AI Risk, Security & Governance

## Purpose

This document defines how the Project Manager identifies, assesses, controls, and governs risks associated with an AI project.

AI projects introduce risks that may not exist, or may be less significant, in traditional technology projects.

Examples include:

* Incorrect AI responses
* Hallucinations
* Unauthorized data access
* Prompt injection
* Data leakage
* Poor-quality source data
* Incorrect policy authority
* Model misuse
* Vendor risk
* Lack of human oversight
* Unclear accountability
* Regulatory or compliance concerns

The Project Manager does not need to implement every technical security control. The PM must ensure that risks are identified, owners are assigned, controls are defined, evidence is collected, and release decisions account for unresolved risk.

---

## 1. Risk Management Objective

The objective is to ensure that AI risks are:

1. Identified early.
2. Assessed consistently.
3. Assigned to accountable owners.
4. Controlled appropriately.
5. Tested where necessary.
6. Monitored after release.
7. Escalated when thresholds are exceeded.
8. Considered in Go/Hold/No-Go decisions.

### Core Principle

> **An AI project should not accept a risk simply because the system technically works.**

---

## 2. AI Risk Categories

AI project risks should be evaluated across multiple categories.

| Category        | Examples                                 |
| --------------- | ---------------------------------------- |
| Business        | Wrong business outcome, low adoption     |
| Requirements    | Ambiguous or incomplete requirements     |
| Data            | Poor quality, outdated, conflicting data |
| AI Quality      | Hallucination, inaccurate answers        |
| Security        | Unauthorized access, data leakage        |
| Privacy         | Exposure of sensitive information        |
| Governance      | Unclear authority or accountability      |
| Technology      | Model failure, integration failure       |
| Performance     | Slow response time                       |
| Operational     | Monitoring or support gaps               |
| Vendor          | Unsupported vendor claims, dependency    |
| Change          | Uncontrolled model or policy changes     |
| User Experience | Confusing or misleading responses        |
| Compliance      | Failure to meet applicable requirements  |

---

## 3. Risk Identification

Risk identification should occur throughout the project lifecycle.

The PM should ask:

* What could go wrong?
* What could cause an incorrect AI response?
* What could expose information?
* What could prevent users from trusting the system?
* What could prevent release?
* What assumptions could prove incorrect?
* What changes could introduce new risk?

Risk identification should not stop after project planning.

---

## 4. Likelihood And Impact

Each significant risk should be evaluated based on:

* Likelihood
* Impact
* Overall risk level

### Example Scale

| Rating | Likelihood     |
| ------ | -------------- |
| 1      | Rare           |
| 2      | Unlikely       |
| 3      | Possible       |
| 4      | Likely         |
| 5      | Almost Certain |

| Rating | Impact   |
| ------ | -------- |
| 1      | Minimal  |
| 2      | Minor    |
| 3      | Moderate |
| 4      | Major    |
| 5      | Severe   |

### Risk Score

```text
Risk Score = Likelihood × Impact
```

Higher scores generally require greater management attention.

---

## 5. Risk Response

Common risk responses include:

### Avoid

Change the project approach so the risk no longer exists.

### Mitigate

Reduce the likelihood or impact.

### Transfer

Move responsibility or exposure to another party where appropriate.

### Accept

Acknowledge the risk and proceed deliberately.

### Escalate

Move the risk to an authority with the appropriate decision-making responsibility.

### PM Rule

> **Risk acceptance must be intentional and documented.**

---

## 6. Risk Controls

Controls reduce the probability or impact of a risk.

Examples:

* Access controls
* Data-readiness gates
* Authority validation
* Version control
* Retrieval thresholds
* Grounding
* Citation controls
* Human escalation
* Evaluation datasets
* UAT
* Monitoring
* Audit logging
* Rollback procedures

---

## 7. Preventive Vs. Detective Controls

### Preventive Controls

Designed to stop a problem before it occurs.

Examples:

* Excluding draft policies
* Authorization checks
* Data-readiness validation
* Blocking unresolved authority conflicts

### Detective Controls

Designed to identify problems after or while they occur.

Examples:

* Monitoring
* Alerts
* Audit logs
* Evaluation
* Defect detection
* User feedback

Strong AI governance often requires both.

---

## 8. Residual Risk

Residual risk is the risk that remains after controls are implemented.

Example:

**Initial Risk:** PolicyAssist retrieves outdated policy information.

**Control:** Active-status and version validation.

**Residual Risk:** Metadata may still be incorrectly maintained.

The PM should determine whether the residual risk is acceptable.

---

## 9. Policy Authority Risk

Policy authority is a critical PolicyAssist risk.

If two documents appear to be authoritative but contain different requirements, the system must not decide which one is correct.

### Required Control

```text
Conflict Detected
       ↓
Do Not Treat Either As Authoritative
       ↓
Escalate
       ↓
Authority Decision
       ↓
Update Governance Record
       ↓
Revalidate
       ↓
Return To Retrieval
```

### Acceptance Criteria

* **100%** of unresolved authority conflicts are excluded from authoritative retrieval.
* **100%** of authority decisions are documented.
* **0** production responses may knowingly rely on unresolved authority conflicts.

---

## 10. AI Accuracy Risk

Incorrect AI responses can create business and user harm.

### Controls

* Retrieval evaluation
* Answer evaluation
* Grounding
* Citation validation
* Evaluation dataset
* Human review
* UAT
* Monitoring

### Acceptance Criteria

* Retrieval accuracy ≥ **90%**
* Answer accuracy ≥ **90%**
* Hallucination rate < **2%**
* Citation correctness = **100%**

---

## 11. Hallucination Risk

Hallucination occurs when the AI provides unsupported information as though it were factual.

For PolicyAssist, this is particularly serious because users may rely on the response as organizational policy guidance.

### Controls

* Retrieval grounding
* Evidence validation
* Unsupported-question refusal
* Citation controls
* Evaluation
* Human escalation

### Acceptance Criteria

* Hallucination rate < **2%**
* Unsupported-question refusal = **100%**
* Supported answers grounded = **100%**

---

## 12. Access Control

PolicyAssist must ensure that users can only access information they are authorized to receive.

### Security Principle

> **Authentication determines who the user is. Authorization determines what the user can access.**

The PM should ensure both requirements are defined and validated.

### Acceptance Criteria

* Authentication validation = **100%**
* Authorization validation = **100%**
* Unauthorized policy access = **0**
* Critical access-control findings = **0**

---

## 13. Privacy

AI systems may process information that should not be exposed unnecessarily.

The PM should ensure the project identifies:

* Sensitive information
* Data access requirements
* Storage requirements
* Logging requirements
* Retention requirements
* Appropriate user access

The system should not expose information merely because the model has access to it.

---

## 14. Prompt Injection

Prompt injection occurs when malicious or unexpected instructions attempt to manipulate an AI system.

Potential examples include instructions embedded within documents or user-provided content that attempt to:

* Override system instructions
* Reveal confidential information
* Change system behavior
* Ignore access controls
* Manipulate responses

### PM Responsibilities

The PM should ensure that:

* Prompt-injection risk is documented.
* Security stakeholders review the architecture.
* Appropriate technical controls are defined.
* Security testing includes relevant scenarios.
* Findings are tracked and resolved.

The PM does not need to personally implement offensive security techniques.

---

## 15. Data Leakage

Data leakage occurs when information is exposed to users, systems, logs, models, or third parties without appropriate authorization.

Potential causes include:

* Incorrect access control
* Poor prompt handling
* Excessive logging
* Misconfigured storage
* Vendor integrations
* Incorrect retrieval filtering

### Acceptance Criteria

**0 critical data-leakage findings may remain unresolved at production release.**

---

## 16. Model Misuse

An AI system may be used for purposes outside its intended scope.

PolicyAssist should have clearly defined boundaries.

Examples of misuse:

* Treating AI output as legal advice
* Using the system to make unauthorized employment decisions
* Asking the system to reveal restricted information
* Treating unsupported answers as official policy
* Using the model outside approved business processes

### PM Control

Document:

* Intended use
* Prohibited use
* User responsibilities
* Escalation requirements
* Human oversight

---

## 17. Human Oversight

AI should not automatically replace human authority where a human decision is required.

Human review may be required when:

* Policy authority is unclear.
* Policies conflict.
* Evidence is insufficient.
* A high-impact decision is involved.
* Security concerns are detected.
* The AI cannot confidently answer.

### Principle

> **The AI can assist with information retrieval; it does not become the policy authority.**

---

## 18. Human Escalation

Escalation should have:

* Defined trigger
* Responsible owner
* Response path
* Documentation
* Resolution process

### Acceptance Criteria

* **100%** of defined escalation scenarios have an assigned path.
* **100%** of escalated issues have an accountable owner.
* Material governance decisions are documented.

---

## 19. Responsible AI

Responsible AI considerations include:

* Accuracy
* Transparency
* Explainability
* Privacy
* Security
* Fairness
* Human oversight
* Accountability
* Appropriate use

The PM should ensure that responsible-AI considerations are incorporated into requirements and governance rather than treated as a final checklist.

---

## 20. Governance Roles & Accountability

| Role                 | Responsibility                     |
| -------------------- | ---------------------------------- |
| Project Manager      | Risk and governance coordination   |
| Business Owner       | Business risk acceptance           |
| Policy Owner         | Policy authority                   |
| Governance Authority | Resolves policy conflicts          |
| Security Team        | Security risk and controls         |
| Data Owner           | Data quality and authority         |
| Technical Team       | Technical controls                 |
| Legal/Compliance     | Applicable compliance requirements |
| UAT Users            | Business acceptance                |
| Executive Sponsor    | Escalated decisions                |

### Accountability Principle

Every significant risk should have an identifiable owner.

---

## 21. Risk Appetite

Risk appetite defines how much risk the organization is willing to accept.

For PolicyAssist, certain risks should have effectively zero tolerance at production.

### Zero-Tolerance Examples

* Critical security breach
* Unauthorized access
* Fabricated policy information
* Known use of superseded policy as authoritative
* Known use of unresolved conflicting policy
* Critical data leakage
* Unresolved critical defect affecting safety or trust

---

## 22. Third-Party And Vendor Risk

AI vendors may make claims regarding:

* Accuracy
* Security
* Availability
* Performance
* Compliance
* Reliability

The PM should not accept vendor claims without evidence.

### Example

Vendor states:

> "Our model has 99% accuracy."

The PM should request:

* Definition of accuracy
* Test methodology
* Dataset
* Evaluation results
* Test conditions
* Limitations
* Independent validation where appropriate

### Principle

> **Vendor claims are inputs to evaluation, not evidence of acceptance.**

---

## 23. Incident Management

An AI incident may involve:

* Incorrect policy guidance
* Unauthorized access
* Data leakage
* Security attack
* Severe performance failure
* Governance failure

### Incident Process

```text
Detect
  ↓
Contain
  ↓
Assess
  ↓
Escalate
  ↓
Correct
  ↓
Retest
  ↓
Approve
  ↓
Resume
  ↓
Monitor
```

Critical incidents should trigger immediate escalation.

---

## 24. Governance Gates

Governance gates prevent the project from progressing when critical controls are incomplete.

### Gate 1: Data Readiness

Confirm:

* Authority
* Approval
* Status
* Version
* Metadata
* Data quality

### Gate 2: AI Evaluation

Confirm:

* Accuracy
* Hallucination
* Grounding
* Citation
* Refusal behavior

### Gate 3: Security

Confirm:

* Authentication
* Authorization
* Privacy
* Data protection
* Security findings

### Gate 4: UAT

Confirm:

* Business scenarios
* User acceptance
* Critical defects
* High-priority defects

### Gate 5: Release

Confirm:

* Evaluation
* Security
* UAT
* Monitoring
* Rollback
* Governance approval

---

## 25. Security Testing At The PM Level

Security testing should be coordinated with qualified technical/security personnel.

The PM should understand:

* What is being tested
* Why it matters
* What constitutes failure
* Who owns remediation
* What evidence is required
* What blocks release

### PM Security Questions

* Can unauthorized users access restricted policies?
* Can users bypass authorization?
* Can sensitive information appear in responses?
* Can prompts manipulate system behavior?
* Can policy documents contain malicious instructions?
* Are sensitive details exposed in logs?
* Are security findings tracked?
* Have critical findings been resolved?

---

## 26. AI Risk Decision Framework

The PM should consider four factors:

```text
Risk Severity
     +
Control Effectiveness
     +
Residual Risk
     +
Release Impact
     =
PM Risk Decision
```

### Possible Decisions

**Accept**

Risk is within approved tolerance.

**Mitigate**

Additional controls are required.

**Escalate**

A higher authority must decide.

**Hold**

Risk is unacceptable for the current release.

---

## 27. Risk Register Requirements

The project risk register should contain:

| Field         | Description                |
| ------------- | -------------------------- |
| Risk ID       | Unique identifier          |
| Risk          | Risk description           |
| Category      | Risk category              |
| Likelihood    | Probability                |
| Impact        | Consequence                |
| Risk Score    | Likelihood × Impact        |
| Owner         | Accountable person         |
| Controls      | Existing controls          |
| Response      | Mitigate/Avoid/etc.        |
| Residual Risk | Remaining exposure         |
| Trigger       | Condition indicating risk  |
| Due Date      | Required action date       |
| Status        | Open/Closed/etc.           |
| Decision      | Acceptance/escalation/hold |

---

## 28. AI Risk Acceptance Criteria

The following conditions apply to production readiness.

| Risk Control                                | Target |
| ------------------------------------------- | -----: |
| Critical security findings unresolved       |      0 |
| Unauthorized policy access                  |      0 |
| Critical data leakage findings              |      0 |
| Known fabricated policy responses           |      0 |
| Unresolved authority conflicts in retrieval |      0 |
| Draft policies in active retrieval          |      0 |
| Superseded policies in active retrieval     |      0 |
| Required security controls validated        |   100% |
| Defined escalation paths implemented        |   100% |
| Material governance decisions documented    |   100% |

---

## 29. Risk Evidence

The PM should require evidence such as:

* Risk register
* Security assessment
* Access-control test results
* Privacy assessment
* Evaluation results
* UAT results
* Defect records
* Vendor evidence
* Governance decisions
* Incident records
* Risk acceptance records
* Remediation evidence

### Evidence Rule

> **No Evidence = Not Yet Accepted.**

---

## 30. MVP Risk & Security Gate

The MVP should not proceed unless the following are validated:

* Core authentication
* Core authorization
* Policy authority controls
* Draft/superseded exclusion
* Basic grounding
* Citation controls
* Unsupported-question refusal
* Core security testing
* No unresolved critical security findings
* No known critical data leakage
* Defined human escalation

### MVP Decision

**Proceed**

Mandatory controls pass.

**Proceed With Conditions**

Only non-critical gaps remain and documented controls exist.

**Hold**

A critical security, privacy, authority, or AI-quality risk remains unresolved.

---

## 31. Production Risk & Security Gate

Production requires:

* Security validation
* Privacy review where applicable
* Access-control validation
* AI evaluation
* Data governance validation
* UAT
* Monitoring
* Incident procedures
* Rollback capability
* Governance approval
* No unresolved critical security findings
* No unresolved critical defects

---

## 32. Practical Exercise 8: Build An AI Risk, Security & Governance Plan

### Scenario

PolicyAssist is approaching MVP.

The technical team reports:

* Retrieval accuracy is 92%.
* Answer accuracy is 91%.
* Hallucination is 1.5%.
* Citation correctness is 98%.
* Authentication works.
* Authorization testing is incomplete.
* One policy authority conflict remains unresolved.
* Monitoring is incomplete.
* Leadership wants to release immediately.

### Your Task

As the Project Manager:

1. Identify the major risks.
2. Assign risk severity.
3. Identify required controls.
4. Identify risk owners.
5. Determine residual risks.
6. Identify which risks block MVP.
7. Determine required security evidence.
8. Determine required governance decisions.
9. Decide whether the project should Proceed, Proceed With Conditions, or Hold.

### PM Decision

Your decision must consider:

* AI quality
* Citation correctness
* Security
* Authority conflicts
* Monitoring
* Governance
* Release impact

---

## 33. Artifact / Output

Complete:

**AI Risk, Security & Governance Plan**

The artifact should include:

* AI risk assessment
* Risk register
* Security risks
* Privacy considerations
* Access-control requirements
* Governance roles
* Risk controls
* Residual risks
* Vendor risks
* Human escalation
* Incident process
* Governance gates
* Evidence requirements
* MVP risk decision
* Production risk decision

---

## 34. PM Decision

The Project Manager should not treat security and governance as activities that happen after development.

They must be integrated throughout the AI project lifecycle.

### Decision Principle

> **A fast, accurate AI system is not ready for release if critical security or governance risks remain unresolved.**

---

## 35. Decision / Reflection

Ask:

> **"If this AI system fails tomorrow, do we know who is responsible, what control should have prevented the failure, how the incident will be handled, and whether we should stop the system?"**

If not, governance is incomplete.

---

## Competency Check

You should now be able to:

* Identify AI-specific project risks.
* Categorize AI risks.
* Assess likelihood and impact.
* Build and maintain a risk register.
* Define preventive and detective controls.
* Evaluate residual risk.
* Identify security and privacy risks.
* Explain authentication versus authorization.
* Recognize prompt-injection and data-leakage risks.
* Define human oversight and escalation.
* Challenge unsupported vendor claims.
* Define governance roles and accountability.
* Establish risk acceptance criteria.
* Identify security and governance release blockers.
* Require evidence before accepting risk.
* Make a Go, Proceed With Conditions, or Hold decision.

---

## Key Takeaways

* AI projects require broader risk management than traditional technology projects.
* AI quality is a risk category.
* Data authority is a governance risk.
* Security must be integrated throughout the lifecycle.
* Authentication and authorization are different controls.
* Hallucination can become a business and trust risk.
* Prompt injection and data leakage require security controls.
* Human oversight remains important for high-impact decisions.
* Vendor claims must be supported by evidence.
* Critical risks should have clearly defined release consequences.
* Risk acceptance must be deliberate and documented.
* Governance gates prevent unsafe progression.
* **No Evidence = Not Yet Accepted.**

---

## Connection To Capstone

This document provides the risk, security, and governance framework for Petadel PolicyAssist AI.

It directly supports:

* `03-REQUIREMENTS.md`
* `04-PRODUCT-BACKLOG.md`
* `05-ARCHITECTURE.md`
* `06-DATA-GOVERNANCE.md`
* `07-EVALUATION-PLAN.md`
* `09-TEST-UAT-PILOT.md`
* `10-RELEASE-DEPLOYMENT.md`
* `11-MONITORING-CONTINUOUS-IMPROVEMENT.md`
* `13-RISK-REGISTER.md`
* `14-TRACEABILITY.md`
* `16-FINAL-GO-HOLD-NO-GO.md`

Risk, security, and governance findings become direct inputs into UAT, release readiness, and the final Go/Hold/No-Go recommendation.

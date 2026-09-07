# 07: Risk & Security Decision

## Project

**Project:** Petadel PolicyAssist AI
**Organization:** Petadel Technology Services (PTS)
**Role:** AI Project Manager
**Decision Area:** AI Risk, Security & Governance

---

# Purpose

This artifact demonstrates how AI-specific risks and security concerns were identified, assessed, controlled, and incorporated into project and release decisions.

The Project Manager must ensure that AI risks are managed as business risks, not treated solely as technical problems.

---

# Risk Management Objective

The objective is to ensure that PolicyAssist:

* Protects users and organizational information.
* Prevents unauthorized policy disclosure.
* Uses approved and authoritative information.
* Controls hallucination and unsupported responses.
* Provides reliable citations.
* Escalates unresolved policy conflicts.
* Maintains appropriate human oversight.
* Meets defined security and governance requirements.
* Provides evidence before production release.

---

# AI Risk Categories

PolicyAssist risks were evaluated across several categories.

| Category    | Example Risk                           |
| ----------- | -------------------------------------- |
| Business    | Incorrect policy guidance              |
| Data        | Outdated or conflicting policy         |
| AI Quality  | Hallucinated information               |
| Retrieval   | Wrong evidence retrieved               |
| Security    | Unauthorized information disclosure    |
| Privacy     | Exposure of sensitive information      |
| Governance  | No established policy authority        |
| Vendor      | Dependency on third-party technology   |
| Performance | Excessive response latency             |
| Operational | Failure to monitor production behavior |
| Change      | AI behavior changes after updates      |

---

# Risk Assessment Method

Risks are assessed using:

**Likelihood × Impact = Risk Score**

The score supports prioritization but does not replace PM judgment.

A low-probability event with severe consequences may still require strong controls.

---

# Initial Risk Register

| Risk                            | Category    | Likelihood | Impact   | Response            | Owner                | Status |
| ------------------------------- | ----------- | ---------- | -------- | ------------------- | -------------------- | ------ |
| Outdated policy retrieved       | Data        | Medium     | High     | Mitigate            | Policy Owner         | Open   |
| Conflicting policy sources      | Governance  | Medium     | High     | Mitigate / Escalate | Policy Governance    | Open   |
| Hallucinated policy answer      | AI Quality  | Medium     | High     | Mitigate            | AI Product Team      | Open   |
| Incorrect citation              | AI Quality  | Medium     | High     | Mitigate            | AI Product Team      | Open   |
| Unsupported question answered   | AI Quality  | Medium     | High     | Mitigate            | AI Product Team      | Open   |
| Unauthorized policy access      | Security    | Low        | Critical | Prevent             | Security             | Open   |
| Sensitive information leakage   | Security    | Low        | Critical | Prevent             | Security             | Open   |
| Poor multi-policy performance   | AI Quality  | Medium     | High     | Mitigate            | AI Product Team      | Open   |
| Response latency exceeds target | Performance | Medium     | Medium   | Mitigate            | Engineering          | Open   |
| Insufficient monitoring         | Operational | Medium     | High     | Mitigate            | Operations           | Open   |
| Rollback not validated          | Release     | Low        | High     | Mitigate            | Engineering / PM     | Open   |
| Governance approval delayed     | Governance  | Medium     | High     | Escalate            | Sponsor / Governance | Open   |

---

# Security Principle

Security must be considered throughout the product lifecycle.

Security is not a final checklist item added immediately before launch.

Security requirements affect:

* Architecture.
* Data ingestion.
* Retrieval.
* User access.
* Application behavior.
* Testing.
* UAT.
* Monitoring.
* Incident response.
* Release decisions.

---

# Access Control

PolicyAssist must distinguish between:

**Can the system retrieve the information?**

and

**Is this user authorized to receive the information?**

A policy may be:

* Active.
* Authoritative.
* Approved.
* Relevant.

and still be restricted.

The system must therefore validate authorization before disclosing restricted information.

---

# Unauthorized Access Risk

### Risk

A user receives policy information they are not authorized to access.

### Potential Impact

* Confidentiality breach.
* Privacy exposure.
* Regulatory or contractual risk.
* Loss of user trust.
* Security incident.

### Required Control

Authorization must be enforced before restricted content is returned to the user.

### Release Requirement

> **Unauthorized policy access = 0**

Any critical unauthorized-access finding should block production release.

---

# Data Leakage

Data leakage may occur when sensitive information is exposed through:

* AI responses.
* Retrieved document content.
* Citations.
* Logs.
* Error messages.
* Application interfaces.

The PM should ensure that the project evaluates each potential exposure path.

---

# Privacy

The project should identify whether policy documents contain:

* Personally Identifiable Information (PII).
* Employee information.
* Confidential business information.
* Security-sensitive information.

Privacy considerations should influence:

* Data ingestion.
* Storage.
* Access.
* Logging.
* Retention.
* Testing.
* Monitoring.

---

# Prompt Injection

Prompt injection occurs when instructions contained in user input or retrieved content attempt to manipulate system behavior.

Examples may include instructions attempting to:

* Ignore system rules.
* Reveal confidential information.
* Override policy controls.
* Change the intended task.

The PM should ensure that prompt-injection risk is included in security requirements and test planning.

The project does not require the PM to perform offensive security testing.

The PM must ensure that the risk is identified, assigned, tested by appropriate technical stakeholders, and resolved or accepted through governance.

---

# Model Misuse

AI capabilities can be misused even when the underlying model functions correctly.

Examples include:

* Asking the system to expose restricted information.
* Attempting to bypass authorization.
* Treating AI output as formal organizational approval.
* Using generated responses as a substitute for required human decisions.

PolicyAssist should clearly establish its role as an information-assistance system rather than an autonomous policy authority.

---

# Human Oversight

Certain situations require human involvement.

Examples:

* Conflicting policy authority.
* Unclear policy ownership.
* Sensitive policy decisions.
* Security incidents.
* High-impact incorrect responses.
* Governance exceptions.

The system should provide an escalation path rather than attempting to resolve every situation autonomously.

---

# Authority Conflict Control

If two policies conflict and the project cannot establish which is authoritative:

**Do Not Guess**

↓

**Block Automatic Selection**

↓

**Escalate**

↓

**Policy Owner / Governance Authority Resolves**

↓

**Update Knowledge Base**

↓

**Revalidate**

This is both a data-governance and risk-control requirement.

---

# AI Quality Risks

## Hallucination

The system generates unsupported policy information.

**Target:** < 2%

## Incorrect Citation

The system provides a source that does not support its response.

**Target:** 100% citation correctness.

## Unsupported Answer

The system answers when sufficient evidence is unavailable.

**Target:** 100% safe refusal behavior.

## Retrieval Failure

The system fails to retrieve the authoritative evidence required for the question.

**Target:** Retrieval accuracy ≥ 90%.

---

# Preventive Controls

Preventive controls are designed to stop problems before they occur.

PolicyAssist preventive controls include:

* Policy eligibility validation.
* Authority validation.
* Status validation.
* Version validation.
* Required metadata.
* Access controls.
* Grounding requirements.
* Application-controlled citations.
* Unsupported-question refusal.
* Scope controls.
* Human escalation.

---

# Detective Controls

Detective controls identify problems after or during system operation.

Examples include:

* Evaluation datasets.
* Monitoring.
* User feedback.
* Defect logging.
* Security alerts.
* Audit logs.
* Performance monitoring.
* Citation evaluation.
* Incident reviews.

---

# Risk Response Strategies

The project may use:

### Avoid

Remove the risky capability from scope.

### Mitigate

Implement controls that reduce likelihood or impact.

### Transfer

Assign responsibility through an appropriate vendor, contract, or service arrangement.

### Accept

Formally accept residual risk through the appropriate authority.

### Escalate

Move the decision to a stakeholder with appropriate authority.

Risk acceptance must not be assumed simply because the project has a deadline.

---

# Residual Risk

Residual risk is the remaining risk after controls are implemented.

Example:

**Initial Risk**

Unauthorized disclosure of restricted policy.

↓

**Controls**

Authorization + access testing + monitoring.

↓

**Residual Risk**

Reduced but not necessarily eliminated.

The PM must determine whether the residual risk is acceptable under the project's risk appetite and governance rules.

---

# Risk Appetite

PolicyAssist should have very low tolerance for:

* Unauthorized information disclosure.
* Critical data leakage.
* Fabricated critical policy information.
* Unresolved authority conflicts.
* Security control failures.

The project may have greater tolerance for:

* Minor formatting problems.
* Cosmetic issues.
* Non-critical usability defects.

Risk appetite should influence release decisions.

---

# Security Acceptance Criteria

Production security readiness requires:

| Requirement                                 | Target |
| ------------------------------------------- | -----: |
| Unresolved Critical Security Findings       |      0 |
| Unauthorized Policy Access                  |      0 |
| Critical Data Leakage                       |      0 |
| Known Fabricated Policy Responses           |      0 |
| Unresolved Authority Conflicts In Retrieval |      0 |
| Draft / Superseded Policies In Retrieval    |      0 |
| Required Security Controls Validated        |   100% |
| Required Escalation Paths                   |   100% |
| Material Governance Decisions Documented    |   100% |

---

# Security Testing At The PM Level

The Project Manager does not need to write penetration-testing tools or exploit systems.

The PM must ensure that appropriate security validation covers:

* Authentication.
* Authorization.
* Restricted information.
* Data leakage.
* Prompt injection.
* Unsafe requests.
* Logging.
* Access boundaries.
* Failure behavior.

The PM's responsibility is to define expectations, coordinate stakeholders, track evidence, and make release decisions.

---

# Governance Roles

Key governance responsibilities include:

| Role                   | Responsibility                       |
| ---------------------- | ------------------------------------ |
| Executive Sponsor      | Business accountability              |
| AI Project Manager     | Project governance and delivery      |
| Product Owner          | Product priorities                   |
| Policy Owner           | Policy authority                     |
| Security               | Security controls and risk           |
| Legal / Compliance     | Regulatory and policy considerations |
| Engineering            | Technical implementation             |
| Data / Knowledge Owner | Data quality and lifecycle           |
| UAT Representatives    | Business acceptance                  |

Clear accountability reduces the risk of unresolved decisions.

---

# Security Incident Response

A security incident should follow a controlled process:

```text id="o8s5k0"
Detect
  ↓
Contain
  ↓
Assess
  ↓
Escalate
  ↓
Remediate
  ↓
Retest
  ↓
Approve
  ↓
Resume / Release
```

A critical incident should trigger appropriate release or operational controls.

---

# Risk Escalation

Risks should be escalated when:

* Impact exceeds PM authority.
* Risk exceeds organizational appetite.
* A critical security issue is identified.
* A policy authority conflict cannot be resolved.
* A release blocker cannot be remediated within schedule.
* A stakeholder proposes accepting unacceptable risk.

The PM should document the escalation and decision.

---

# Governance Gates

PolicyAssist should pass governance gates before production.

### Gate 1 — Data Governance

* Authority established.
* Ownership established.
* Versions validated.
* Conflicts resolved.

### Gate 2 — Security

* Required controls validated.
* Authorization tested.
* No critical security findings.

### Gate 3 — AI Quality

* Evaluation targets achieved.
* Hallucination controlled.
* Citation correctness validated.

### Gate 4 — UAT

* Business scenarios passed.
* Critical defects resolved.

### Gate 5 — Production

* Monitoring ready.
* Rollback validated.
* Governance approval complete.
* Final release decision made.

---

# Risk-Based Release Decision

Risk should influence release decisions even when functional testing appears successful.

Example:

> Retrieval accuracy = 94%
> Answer accuracy = 92%
> Citation correctness = 100%
> Security testing = incomplete

The project should not automatically proceed to production.

The missing security evidence represents an unresolved release dependency.

---

# Current Security Position

The project has designed the required security and governance controls.

The prototype demonstrates controlled policy eligibility and response behavior.

However, production security readiness is not yet established.

Formal validation remains required for:

* Authorization.
* Restricted information.
* Data leakage.
* Prompt injection.
* Security-sensitive scenarios.
* Audit and monitoring controls.

---

# Current Risk Position

The overall project remains in a controlled but incomplete risk state.

Known areas requiring continued management include:

* Multi-policy AI performance.
* Formal evaluation.
* Security validation.
* UAT.
* Monitoring readiness.
* Rollback validation.
* Governance approval.
* Final release evidence.

---

# Automatic Release Blockers

The following should block production release unless resolved through an explicitly authorized governance process:

* Critical security finding.
* Unauthorized policy access.
* Critical data leakage.
* Fabricated critical policy information.
* Unresolved policy authority conflict affecting retrieval.
* Draft or superseded policy used as authoritative production evidence.
* Missing required security control.
* Unresolved critical business defect.
* Required evidence unavailable.

---

# PM Decision

The correct PM approach is not to eliminate every possible risk.

The objective is to:

1. Identify risk.
2. Assess risk.
3. Establish controls.
4. Assign ownership.
5. Monitor residual risk.
6. Escalate unacceptable risk.
7. Use risk evidence in release decisions.

---

# Current Risk & Security Decision

**Decision:** Continue risk mitigation and security validation.

**Production Decision:** HOLD.

The project should not move to production until:

* Required security controls are validated.
* Authorization is tested.
* Critical security risks are resolved.
* Data leakage risks are addressed.
* AI quality targets are demonstrated.
* Governance decisions are documented.
* UAT and release evidence are complete.

---

# Portfolio Evidence

This artifact demonstrates the ability to:

* Identify AI-specific risks.
* Assess likelihood and impact.
* Establish preventive and detective controls.
* Manage security and privacy risks.
* Separate authorization from retrieval relevance.
* Establish human oversight.
* Define risk appetite.
* Manage residual risk.
* Establish security release gates.
* Escalate risks appropriately.
* Connect security evidence to release decisions.

---

# Key PM Judgment

The central security principle is:

> **A system should not be considered safe because no incident has occurred during development. It should be considered ready only when required controls have been validated with evidence.**

---

# Final Risk Principle

> **Risk management is not a documentation exercise. It is a decision-making mechanism that determines what the project can safely proceed with, what requires mitigation, and what must remain on hold.**

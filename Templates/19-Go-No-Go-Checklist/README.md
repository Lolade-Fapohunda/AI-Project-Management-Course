# Go/No-Go Checklist

## Purpose

The Go/No-Go Checklist provides a structured framework for determining whether an AI project is ready to proceed to production.

A release decision should be based on evidence, risk, business acceptance, and governance—not schedule pressure alone.

---

## Release Readiness

| Area         | Requirement                          | Evidence   | Status      | Owner   |
| ------------ | ------------------------------------ | ---------- | ----------- | ------- |
| Business     | Business objectives are satisfied.   | [Evidence] | [Pass/Fail] | [Owner] |
| Requirements | Approved requirements are complete.  | [Evidence] | [Pass/Fail] | [Owner] |
| Data         | Data is ready and governed.          | [Evidence] | [Pass/Fail] | [Owner] |
| Evaluation   | AI evaluation targets are satisfied. | [Evidence] | [Pass/Fail] | [Owner] |
| Testing      | Required testing is complete.        | [Evidence] | [Pass/Fail] | [Owner] |
| UAT          | Business acceptance is complete.     | [Evidence] | [Pass/Fail] | [Owner] |
| Security     | Security requirements are satisfied. | [Evidence] | [Pass/Fail] | [Owner] |
| Governance   | Required approvals are complete.     | [Evidence] | [Pass/Fail] | [Owner] |
| Monitoring   | Production monitoring is ready.      | [Evidence] | [Pass/Fail] | [Owner] |
| Rollback     | Rollback capability is available.    | [Evidence] | [Pass/Fail] | [Owner] |
| Support      | Production support is prepared.      | [Evidence] | [Pass/Fail] | [Owner] |

---

## Defect Review

| Severity | Open Defects | Release Impact      |
| -------- | -----------: | ------------------- |
| Critical |          [#] | No-Go               |
| High     |          [#] | [Decision Required] |
| Medium   |          [#] | [Decision Required] |
| Low      |          [#] | [May Defer]         |

---

## Risk Review

**Highest Remaining Risk:**

[Risk]

**Residual Risk Level:**

[Low / Medium / High / Critical]

**Risk Accepted By:**

[Name/Role]

---

## Decision Rules

### GO

Proceed when:

* Required readiness criteria are satisfied.
* No unresolved critical issues exist.
* Required approvals are complete.
* Business acceptance is confirmed.
* Monitoring and rollback are ready.
* Remaining risks are within approved tolerance.

### PROCEED WITH CONDITIONS

Proceed only when:

* Remaining conditions are explicitly documented.
* Owners and deadlines are assigned.
* Risks are understood and accepted.
* Conditions do not create unacceptable security, business, or governance exposure.

### NO-GO / HOLD

Do not proceed when:

* Critical security concerns remain.
* Critical defects remain unresolved.
* Required UAT has not been completed.
* Required evaluation evidence is missing.
* Data authority or readiness cannot be established.
* Required governance approval is missing.
* Rollback or monitoring is not adequately prepared.

---

## Final Decision

**Decision:**

[GO / PROCEED WITH CONDITIONS / NO-GO]

**Decision Authority:**

[Name/Role]

**Decision Date:**

[Date]

**Rationale:**

[Enter rationale.]

---

## PM Quality Check

* [ ] Evidence has been reviewed.
* [ ] Critical defects are resolved.
* [ ] High-severity defects have been evaluated.
* [ ] Security readiness is confirmed.
* [ ] UAT is complete.
* [ ] AI evaluation is complete.
* [ ] Data readiness is confirmed.
* [ ] Monitoring is ready.
* [ ] Rollback is available.
* [ ] Required approvals are documented.

---

## Course Connection

Use this checklist as the final release-readiness gate before production deployment.

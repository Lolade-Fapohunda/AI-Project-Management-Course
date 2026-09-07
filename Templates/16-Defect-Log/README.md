# Defect Log

## Purpose

The Defect Log provides a centralized record of problems discovered during testing, evaluation, UAT, pilot, or production.

It ensures defects are documented, prioritized, assigned, resolved, and verified.

---

## Defect Log

| Defect ID | Date   | Source           | Description   | Severity                   | Priority          | Owner   | Status | Resolution   | Retest      |
| --------- | ------ | ---------------- | ------------- | -------------------------- | ----------------- | ------- | ------ | ------------ | ----------- |
| DEF-001   | [Date] | [Test/UAT/Pilot] | [Description] | [Critical/High/Medium/Low] | [High/Medium/Low] | [Owner] | Open   | [Resolution] | [Pass/Fail] |
| DEF-002   | [Date] | [Test/UAT/Pilot] | [Description] | [Critical/High/Medium/Low] | [High/Medium/Low] | [Owner] | Open   | [Resolution] | [Pass/Fail] |

---

## Defect Severity

| Severity | Definition                                                                                           |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Critical | Severe failure such as a security breach, unauthorized exposure, or fabricated critical information. |
| High     | Significant failure affecting a critical requirement or major business function.                     |
| Medium   | Material issue that does not prevent overall use.                                                    |
| Low      | Minor or cosmetic issue.                                                                             |

---

## Defect Priority

Priority determines **how quickly the defect should be addressed**.

| Priority | Response                                        |
| -------- | ----------------------------------------------- |
| High     | Address immediately or before release.          |
| Medium   | Address according to planned delivery priority. |
| Low      | Address when capacity permits.                  |

Severity describes **how serious the defect is**.

Priority describes **how urgently it should be addressed**.

---

## Defect Lifecycle

```text
Identified
    ↓
Logged
    ↓
Triaged
    ↓
Assigned
    ↓
Resolved
    ↓
Retested
    ↓
Closed
```

---

## Root Cause

For significant defects:

**Root Cause:**

[Enter root cause.]

**Corrective Action:**

[Enter corrective action.]

**Preventive Action:**

[Enter preventive action.]

---

## Release Impact

| Defect   | Release Impact | Decision                      |
| -------- | -------------- | ----------------------------- |
| [DEF-ID] | [Impact]       | [Fix / Accept / Hold Release] |

---

## PM Quality Check

* [ ] Every significant defect is documented.
* [ ] Severity is assigned consistently.
* [ ] Priority is assigned separately from severity.
* [ ] An owner is assigned.
* [ ] Resolution is documented.
* [ ] Retesting is completed.
* [ ] Release impact is evaluated.
* [ ] Critical and high defects receive appropriate attention.

---

## PM Decision

**Defect Status:** [Acceptable / At Risk / Release Blocking]

**Decision:**

[Enter decision.]

**Reason:**

[Enter rationale.]

---

## Course Connection

Use this template throughout testing, UAT, pilot, release, and production monitoring to maintain defect accountability.

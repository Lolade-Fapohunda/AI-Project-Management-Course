# Module 8: AI Risk, Security & Governance

## Purpose

AI projects introduce risks that traditional technology projects may not encounter.

An AI Project Manager must understand how to identify, assess, control, monitor, and communicate risks associated with:

* AI behavior
* Data
* Privacy
* Security
* Access
* Governance
* Compliance
* Human oversight
* Third-party technology
* Model misuse
* Operational failures

The PM does not need to become a cybersecurity engineer or AI security researcher.

The PM must understand the risks well enough to ensure that appropriate controls, owners, approvals, and decisions are in place.

---

## Learning Objectives

By the end of this module, you will be able to:

* Explain why AI projects require specialized risk management.
* Identify common AI security and governance risks.
* Assess likelihood and impact.
* Create an AI risk register.
* Identify appropriate risk controls.
* Understand access control and data protection responsibilities.
* Explain privacy risks in AI projects.
* Understand prompt injection and model misuse at a PM level.
* Define human oversight requirements.
* Establish risk ownership and accountability.
* Evaluate third-party and vendor risks.
* Define governance and approval requirements.
* Make evidence-based risk decisions.
* Determine when an AI project should Proceed, Proceed With Conditions, or Hold.

---

## AI Risk Management

Risk management is the process of identifying potential problems before they cause unacceptable business impact.

Traditional project risks may include:

* Budget overruns
* Schedule delays
* Resource shortages
* Scope changes
* Vendor delays

AI projects can include all of these risks plus AI-specific risks.

Examples include:

* Hallucinated information
* Biased outputs
* Unauthorized data exposure
* Prompt injection
* Incorrect automated decisions
* Inappropriate model behavior
* Poor data quality
* Model dependency
* Lack of explainability
* Inadequate human oversight

The PM must ensure these risks are identified and managed throughout the project lifecycle.

---

## AI Risk Categories

A useful AI risk framework may include:

| Risk Category         | Example                                                |
| --------------------- | ------------------------------------------------------ |
| **Data Risk**         | Incorrect, outdated, or unauthorized data              |
| **Security Risk**     | Unauthorized access or data exposure                   |
| **Privacy Risk**      | Personal information used or disclosed improperly      |
| **Model Risk**        | Incorrect or unpredictable model behavior              |
| **Accuracy Risk**     | AI produces incorrect information                      |
| **Bias Risk**         | Outputs create unfair or discriminatory outcomes       |
| **Operational Risk**  | System fails or becomes unavailable                    |
| **Compliance Risk**   | Product violates applicable requirements               |
| **Governance Risk**   | No clear ownership or approval process                 |
| **Vendor Risk**       | Third-party AI provider creates dependency or exposure |
| **Reputational Risk** | AI failure damages organizational trust                |

A single issue may belong to multiple categories.

---

## Risk Identification

Risk identification should begin early.

The PM should ask:

* What could go wrong?
* Who could be affected?
* What information could be exposed?
* What decisions could the AI influence?
* What happens if the AI is wrong?
* What happens if the system is unavailable?
* What happens if users misuse the system?
* What happens if a third-party service changes?
* What happens if the underlying data changes?
* What happens if the AI behaves differently than expected?

Risk identification should continue throughout the project.

---

## Likelihood And Impact

Risk is commonly assessed using:

**Likelihood × Impact = Risk Level**

### Likelihood

How likely is the risk to occur?

Example scale:

* 1 = Rare
* 2 = Unlikely
* 3 = Possible
* 4 = Likely
* 5 = Almost Certain

### Impact

How serious would the consequences be?

Example scale:

* 1 = Minimal
* 2 = Minor
* 3 = Moderate
* 4 = Major
* 5 = Severe

The organization may use different scoring systems.

The important principle is consistency.

---

## Risk Register

A risk register provides a structured way to manage project risks.

A basic AI risk register may include:

| Field                | Purpose                               |
| -------------------- | ------------------------------------- |
| **Risk ID**          | Unique identifier                     |
| **Risk Description** | What could happen                     |
| **Category**         | Type of risk                          |
| **Likelihood**       | Probability                           |
| **Impact**           | Consequence                           |
| **Risk Score**       | Overall risk level                    |
| **Control**          | Action that reduces risk              |
| **Owner**            | Person responsible                    |
| **Status**           | Open, Monitoring, Mitigated, Accepted |
| **Residual Risk**    | Remaining risk after controls         |
| **Decision**         | PM/governance decision                |
| **Notes**            | Additional information                |

The risk register should be treated as a living project artifact.

---

## Risk Controls

Identifying a risk is not enough.

The project must determine how the risk will be controlled.

Examples include:

* Access restrictions
* Authentication
* Authorization
* Data classification
* Human review
* Approval workflows
* Source validation
* Audit logging
* Monitoring
* Rate limiting
* Input validation
* Output validation
* User training
* Vendor controls
* Incident response procedures

Controls should be proportionate to the risk.

---

## Preventive Vs. Detective Controls

Controls can be designed to prevent problems or detect them.

### Preventive Controls

Designed to stop an unwanted event before it occurs.

Examples:

* Restrict access to authorized users.
* Block unsupported file types.
* Require approval before sensitive data is processed.
* Prevent users from accessing information outside their authorization level.

### Detective Controls

Designed to identify problems after or while they occur.

Examples:

* Audit logs
* Monitoring alerts
* Security reviews
* Incident reports
* Quality monitoring
* Periodic access reviews

Strong AI governance often requires both.

---

## Residual Risk

Risk may remain even after controls are implemented.

This is called **residual risk**.

For example:

> A system may restrict access to authorized employees, but there may still be a risk that an authorized employee enters sensitive information into an AI prompt.

The PM must determine:

* What risk remains?
* Is it acceptable?
* Who accepts it?
* What additional controls are required?

A risk is not automatically eliminated simply because a control exists.

---

## Access Control

AI systems may process information with different levels of sensitivity.

Users should only receive information they are authorized to access.

The PM should understand:

* Authentication
* Authorization
* Role-based access
* Least privilege
* Data classification
* Access reviews
* Auditability

### PM Principle

> **A user being authorized to use an AI system does not automatically mean they are authorized to access every piece of information available to that system.**

Access requirements should therefore be defined during requirements and architecture planning.

---

## Privacy

AI systems may process:

* Names
* Contact information
* Employee information
* Customer information
* Financial information
* Health-related information
* Confidential business information

The PM should determine:

* What information is being collected?
* Why is it being collected?
* Where is it stored?
* Who can access it?
* How long is it retained?
* Is it shared with third parties?
* Is the use authorized?
* What happens if the information is exposed?

Privacy requirements should involve appropriate legal, privacy, security, and compliance stakeholders when necessary.

---

## Prompt Injection

Prompt injection is a class of AI security risk in which specially crafted input attempts to influence the AI system to ignore intended instructions or perform unintended actions.

For example, a malicious input might attempt to:

* Override system instructions.
* Expose hidden information.
* Manipulate the AI into ignoring restrictions.
* Cause the system to reveal sensitive content.

The PM does not need to build an attack.

The PM needs to recognize the risk and ensure that technical teams evaluate appropriate controls.

### PM Responsibilities

The PM should ensure:

* The risk is documented.
* Security stakeholders are involved.
* Appropriate controls are defined.
* Security testing is planned.
* Results are documented.
* Critical findings are resolved before release.

---

## Data Leakage

Data leakage occurs when information is exposed to people, systems, or environments that are not authorized to receive it.

Potential causes include:

* Incorrect access permissions
* Insecure integrations
* Poor data handling
* Misconfigured systems
* User mistakes
* AI prompts containing sensitive information
* Third-party services

A data leakage risk should generally receive serious attention because the impact may include:

* Privacy violations
* Regulatory consequences
* Financial loss
* Reputational damage
* Loss of customer trust

---

## Model Misuse

AI systems may be used in ways that were not intended by the project team.

Examples:

* Using the system for decisions it was not designed to support.
* Attempting to extract restricted information.
* Using outputs without required human review.
* Using the AI for high-risk decisions without authorization.

The PM should ensure that:

* Intended use is documented.
* Prohibited use is documented.
* User guidance exists.
* Appropriate controls are implemented.
* High-risk uses require appropriate oversight.

---

## Human Oversight

Not every AI decision should be fully automated.

Human oversight may be required when:

* The consequences of an incorrect answer are significant.
* The AI cannot reliably determine the correct outcome.
* A decision affects a person's rights or access.
* The system detects uncertainty.
* Policy or governance requires human approval.

The PM should define:

* When human review is required.
* Who performs the review.
* What information the reviewer receives.
* What happens when the reviewer disagrees with the AI.
* How decisions are documented.

---

## Responsible AI

Responsible AI focuses on developing and using AI systems in a manner consistent with organizational values, applicable requirements, and acceptable risk.

Important principles may include:

* Fairness
* Transparency
* Accountability
* Privacy
* Security
* Human oversight
* Reliability
* Appropriate use

The PM should ensure that responsible AI considerations are incorporated into project planning rather than treated as an afterthought.

---

## Governance

Governance establishes who has authority to make decisions about the AI system.

Governance should answer:

* Who owns the product?
* Who owns the data?
* Who approves AI use?
* Who approves production release?
* Who owns security?
* Who owns compliance?
* Who manages incidents?
* Who can accept residual risk?
* Who can stop the system?
* Who approves significant changes?

Without clear governance, important decisions may fall between organizational boundaries.

---

## Roles And Accountability

A RACI framework can help establish accountability.

**RACI** stands for:

* **Responsible** — Performs the work.
* **Accountable** — Ultimately owns the outcome.
* **Consulted** — Provides expertise or input.
* **Informed** — Needs to know the outcome.

Example:

| Activity            | PM | Security | Data Owner | Product Owner |
| ------------------- | -- | -------- | ---------- | ------------- |
| Risk Identification | R  | C        | C          | A             |
| Security Review     | C  | R/A      | C          | I             |
| Data Approval       | C  | C        | R/A        | I             |
| Release Decision    | R  | C        | C          | A             |
| Risk Acceptance     | C  | C        | C          | A             |

The exact structure will vary by organization.

---

## Risk Appetite

Risk appetite describes how much risk an organization is willing to accept.

For example:

An organization may tolerate:

> Minor usability issues.

But may have zero tolerance for:

> Unauthorized disclosure of confidential information.

The PM should understand the difference between:

* Risk that can be accepted.
* Risk that must be mitigated.
* Risk that requires escalation.
* Risk that prevents release.

---

## Third-Party And Vendor Risk

Many AI projects depend on external providers.

Examples include:

* AI model providers
* Cloud platforms
* Software vendors
* Data providers
* APIs
* Infrastructure providers

The PM should evaluate:

* Security requirements
* Data handling
* Availability
* Service dependencies
* Contractual requirements
* Vendor reliability
* Exit strategy
* Business continuity
* Changes to vendor services

A technically strong AI product can still have significant project risk if a critical vendor becomes unavailable.

---

## Incident Management

AI incidents should have a defined response process.

A basic process is:

**Detect**

↓

**Assess**

↓

**Contain**

↓

**Escalate**

↓

**Investigate**

↓

**Correct**

↓

**Retest**

↓

**Approve**

↓

**Resume**

The PM should ensure that serious incidents have:

* Defined owners
* Escalation procedures
* Communication plans
* Documentation
* Corrective actions
* Lessons learned

---

## Governance Gates

Governance should be connected to project lifecycle decisions.

Examples:

### Before Development

* Problem approved
* AI use justified
* Risks identified
* Data approved

### Before Pilot

* Security review completed
* Evaluation completed
* Access controls validated
* Known risks documented

### Before Production

* UAT completed
* Critical defects resolved
* High risks addressed or formally accepted
* Monitoring established
* Incident response defined
* Required approvals obtained

Governance gates prevent the project from moving forward based solely on schedule pressure.

---

## Security Testing At The PM Level

The PM is not expected to perform penetration testing or develop security exploits.

The PM is responsible for ensuring that appropriate security testing is:

* Planned
* Assigned
* Executed by qualified personnel
* Documented
* Reviewed
* Connected to release criteria

Security testing may include evaluation of:

* Unauthorized access
* Data exposure
* Prompt injection
* Inappropriate model behavior
* Authentication
* Authorization
* Logging
* Sensitive data handling

The PM manages the process and decision-making rather than performing the technical attack.

---

## AI Risk Decision Framework

When evaluating a significant AI risk, ask:

1. **What can go wrong?**
2. **Who or what could be affected?**
3. **How likely is it?**
4. **How severe is the impact?**
5. **What controls exist?**
6. **Are the controls effective?**
7. **What residual risk remains?**
8. **Who owns the risk?**
9. **Can the risk be accepted?**
10. **Does the risk affect the release decision?**

This converts risk management from a documentation exercise into a decision-making process.

---

## Practical Exercise 8: Build An AI Risk, Security & Governance Plan

### Scenario

An organization is preparing to pilot an AI assistant that helps employees locate and understand internal company information.

The technical team reports that the application is functioning correctly.

During project review, you discover the following:

* Some information contains confidential employee data.
* Users have different levels of access.
* The AI can retrieve information from multiple internal sources.
* Security testing has not yet been completed.
* A third-party AI service is being considered.
* Leadership wants to begin the pilot next week.
* No formal risk register currently exists.
* No one has formally accepted the remaining risks.
* The project team has not documented when human review is required.

### Part 1: Identify Risks

Identify at least **eight risks**.

For each risk, identify:

* Risk category
* Description
* Potential impact
* Likelihood

### Part 2: Build The Risk Register

Create a risk register containing:

* Risk ID
* Risk description
* Category
* Likelihood
* Impact
* Risk score
* Control
* Owner
* Status
* Residual risk

### Part 3: Define Security Controls

Identify appropriate controls for:

* Access control
* Sensitive information
* Data leakage
* Prompt injection
* Authentication
* Authorization
* Auditability

### Part 4: Define Governance

Identify:

* Product owner
* Data owner
* Security owner
* PM
* Technical owner
* Approval authority
* Risk acceptance authority

Create a simple RACI matrix for the major governance activities.

### Part 5: Human Oversight

Define at least **three situations** in which the AI assistant should require human review.

### Part 6: Third-Party Risk

Identify the major risks associated with using an external AI provider.

Define the questions you would ask before approving the provider.

### Part 7: PM Decision

Leadership wants to begin the pilot next week.

Determine whether the project should:

* **Proceed**
* **Proceed With Conditions**
* **Hold**

Support your decision using:

1. Evidence
2. Risk
3. Security
4. Governance
5. Controls
6. Residual risk
7. Required actions
8. Approval requirements

---

## PM Decision

Leadership says:

> "The application works and we need to start the pilot next week."

You discover that:

* Security testing is incomplete.
* Access controls have not been fully validated.
* Sensitive information may be involved.
* No formal risk acceptance exists.
* Human oversight requirements have not been defined.

As the AI Project Manager, determine whether the project should proceed.

Your decision should explain:

* Which risks are unacceptable.
* Which risks may be mitigated.
* Which controls are required.
* Who must approve the remaining risks.
* What evidence is required before the pilot.
* Whether the schedule should change.

### Key Principle

> **Schedule pressure does not eliminate project risk.**

A PM must protect the project's business objectives even when that means recommending a delay.

---

## Artifact / Output

Create an **AI Risk, Security & Governance Plan** containing:

* AI risk categories
* Risk register
* Likelihood and impact assessment
* Risk controls
* Residual risk
* Access-control requirements
* Privacy considerations
* Security requirements
* Human oversight requirements
* Governance structure
* RACI matrix
* Third-party risk considerations
* Incident management process
* Governance gates
* Risk acceptance process
* Release decision criteria

The artifact should demonstrate that you can manage AI risk from identification through governance and release decision.

---

## Decision / Reflection

Answer the following:

1. Why do AI projects require specialized risk management?
2. Why is risk identification not enough without controls?
3. What is residual risk?
4. Why is access to the AI system different from access to all information available to the system?
5. Why is prompt injection an AI security concern?
6. Why should human oversight be defined before deployment?
7. Who should be allowed to accept significant residual risk?
8. Why should third-party AI providers be treated as project risks?
9. When should security findings prevent a pilot or production release?
10. Why should governance be connected to project lifecycle gates?

---

## Key Takeaways

* AI projects introduce risks beyond traditional technology project risks.
* Risk should be identified, assessed, controlled, monitored, and owned.
* Likelihood and impact help prioritize risks.
* A risk register should remain active throughout the project lifecycle.
* Controls reduce risk but do not necessarily eliminate it.
* Residual risk must be evaluated and formally accepted when appropriate.
* Access control must consider both system access and information access.
* Privacy and sensitive data handling require deliberate planning.
* Prompt injection and data leakage are important AI security considerations.
* Human oversight should be defined for appropriate high-risk situations.
* Governance establishes ownership, authority, approvals, and accountability.
* RACI helps clarify responsibilities.
* Third-party AI services introduce additional dependency and security risks.
* Security testing should be managed by qualified technical personnel.
* The PM is responsible for ensuring security work is planned, completed, reviewed, and connected to release decisions.
* Schedule pressure should never override unacceptable risk.
* AI governance should continue throughout the product lifecycle.

---

## Connection To Capstone

The risk, security, and governance principles from this module will later be applied to **Petadel PolicyAssist AI**.

In the capstone, you will apply these principles to:

* Access control
* Policy authorization
* Sensitive information
* Data protection
* AI security risks
* Human escalation
* Governance
* Risk ownership
* Incident management
* Release gates

Security testing will remain a **PM-led design, coordination, and decision activity**, while technical security validation will be performed by appropriate technical stakeholders.

---

## Competency Check

Before moving to Module 9, confirm that you can:

* [ ] Identify AI-specific project risks.
* [ ] Categorize AI risks appropriately.
* [ ] Assess likelihood and impact.
* [ ] Build and maintain an AI risk register.
* [ ] Identify preventive and detective controls.
* [ ] Evaluate residual risk.
* [ ] Explain access control and least privilege.
* [ ] Identify AI privacy and data-leakage risks.
* [ ] Explain prompt injection at a PM level.
* [ ] Define appropriate human oversight.
* [ ] Establish governance roles and accountability.
* [ ] Use RACI to clarify responsibilities.
* [ ] Evaluate third-party AI vendor risks.
* [ ] Define incident-management responsibilities.
* [ ] Establish governance gates.
* [ ] Determine when risk should cause a Proceed, Proceed With Conditions, or Hold decision.
* [ ] Complete the **AI Risk, Security & Governance Plan**.

**Module Complete When:** You can identify, assess, control, govern, and communicate AI project risks and make defensible release decisions based on evidence and risk tolerance.

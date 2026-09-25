# SBI — Silent Breakpoint Intelligence™

I built SBI as a **student-developed, simulated, no-PHI healthcare operations portfolio project** around a question I keep coming back to:

> **Where did the workflow first lose control?**

As I work toward my Bachelor's of Science degree in Healthcare Administration at the University of Phoenix, I am building a patient-to-professional foundation in healthcare operations. I do not have formal healthcare operations employment experience yet. SBI is one way I turn coursework, independent study, and patient-side observations into structured practice without presenting student work as professional healthcare experience.

## Why I Built SBI

From the patient side, the visible problem often appears late.

A person may experience another phone call, a delayed next step, a rescheduled service, a request to resend information, billing confusion, or uncertainty about what happens next. Internally, the earlier workflow condition may involve intake information, documentation readiness, prior-authorization follow-up, exception ownership, a handoff, or a recurring workaround.

SBI helps me practice separating those two views:

**What became visible downstream?**

and

**What earlier workflow condition should be investigated rather than assumed?**

The project is not designed to prove causation. It is designed to help me practice tracing a workflow backward, identifying where control may have weakened, documenting a root-cause hypothesis, and thinking about what information or control could make the problem visible sooner.

## What I Mean by a “Silent Breakpoint”

In SBI, a **silent breakpoint** is a student-developed label for a modeled point where a workflow becomes less reliable before the full downstream effect is visible.

Examples can include:

- incomplete or inconsistent intake information,
- documentation that is not ready for the next administrative step,
- an eligibility exception that is identified but not fully closed,
- an aging prior-authorization request without visible ownership or escalation,
- an open-loop handoff,
- repeated manual workarounds,
- duplicate manual data entry,
- a payment adjustment, reversal, offset, or recovery signal that is visible after money has moved but is not yet fully reconciled,
- or an issue that becomes visible only after it reaches scheduling, claims/revenue cycle, staff workload, or operational reporting.

**“Silent breakpoint” is not a clinical term, compliance standard, payer definition, or validated industry risk model.** It is an educational framework I use to organize simulated workflow analysis.

## Workflow View

SBI follows a simplified administrative workflow while asking where the first instability may have appeared:

```text
Patient Access / Intake
        ↓
Documentation Readiness
        ↓
Eligibility / Authorization
        ↓
Handoff / Ownership
        ↓
Administrative Execution
        ↓
Claims / Revenue Cycle
        ↓
Operational Reporting / Visibility
```

This is a learning model, not a universal healthcare workflow. Actual workflows vary by organization, service, payer, technology, policy, and role.

## Upstream Requirement Intelligence

SBI now includes a requirement-to-breakpoint layer for cases where evidence shows that an external or organizational requirement shaped the workflow.

The analytical path is:

**Supported requirement → operational requirement → workflow / role / system → control point → exception / breakpoint → patient, staff, or revenue signal → measure → analyze → adjust**

This strengthens SBI's backward-trace model by asking not only where control may have weakened, but—when supported—what requirement first became operational and where the workflow was expected to respond to it.

SBI distinguishes among policy or regulation, payer rules, contractual requirements, coverage conditions, documentation or authorization requirements, and internal organizational procedures. It does **not** assume that every breakpoint has a policy root cause.

Key evidence boundary:

> **A denial, delay, complaint, rework pattern, or workflow exception is a signal for investigation—not proof of a policy, payer-rule, contractual, regulatory, or organizational cause.**

The student review sequence is:

1. **Identify** the requirement and source only when evidence supports the connection.
2. **Translate** the requirement into its operational consequence: workflow, role, queue, technology, documentation, communication, timing, oversight, or measurement.
3. **Trace** the workflow to the first control point where the requirement should have been detected, completed, handed off, escalated, or verified.
4. **Separate** the upstream requirement, workflow failure, visible signal, and downstream effect.
5. **Measure** the relevant simulated process pattern.
6. **Analyze** why the result occurred and where the earliest supported loss of control appears.
7. **Adjust** the modeled control, workflow, escalation, communication, or monitoring rule and review the resulting evidence.

This remains student-developed, simulated, no-PHI healthcare operations practice and does not represent policy, legal, compliance, payer, coding, clinical, or management authority.

## Current 2026 Context

SBI is intentionally not a payer-rule engine or a compliance tool. Prior-authorization requirements and electronic data-exchange expectations continue to change.

For example, under **CMS-0057-F**, certain prior-authorization operational provisions for impacted payers began in 2026, while many API requirements generally begin in 2027. CMS also requires specific reasons for denied prior-authorization decisions for impacted payers beginning in 2026. SBI does not attempt to reproduce those payer requirements; it uses prior authorization only as a simulated workflow domain for studying ownership, aging, documentation readiness, escalation, and handoffs.

Official CMS source:
https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f

## Simulated Breakpoint Review Tool

The live project includes a student-designed educational calculator with five modeled dimensions:

1. Patient-facing impact potential
2. Revenue-cycle impact potential
3. Staff/workflow burden
4. Repeat-pattern potential
5. Visibility gap

Each dimension is scored from 1 to 5 and summed into a 5-to-25 **practice review score**.

The score is used only to compare fictional scenarios within the project. It is **not** a validated risk score, severity scale, patient-safety instrument, financial forecast, compliance threshold, or healthcare benchmark.

The current student-designed review bands are:

| Total Score | Educational Interpretation |
|---:|---|
| 5–9 | Lower-priority modeled review |
| 10–14 | Moderate-priority modeled review |
| 15–19 | Higher-priority modeled review |
| 20–25 | Highest-priority modeled review |

These bands are learning assumptions only.

## Synthetic Dashboard Example

The site includes demonstration values such as:

- 24 modeled breakpoint records
- 5 highest-priority modeled reviews
- 9 higher-priority modeled reviews
- 18.7 modeled average practice score
- authorization as an example recurring workflow area
- unclear ownership as an example review theme

These values are synthetic design examples. They do **not** represent an employer, patient population, payer, healthcare organization, benchmark, observed operational result, or validated finding.

## What I Am Practicing Through SBI

Through this project, I am practicing:

- healthcare administrative workflow mapping,
- patient-to-professional analysis,
- root-cause hypothesis development,
- closed-loop handoff thinking,
- eligibility-exception ownership and closure,
- prior-authorization aging and escalation visibility,
- documentation-readiness review,
- operational drift and repeated-workaround awareness,
- patient-access risk interpretation,
- staff-rework visibility,
- claims/revenue-cycle workflow reasoning,
- payment recovery and reconciliation traceback,
- ERA/EOB evidence review concepts,
- post-payment ownership and closure thinking,
- synthetic KPI and dashboard design,
- student-level process-control thinking,
- continuous-improvement and process-gap review,
- recurrence review and small-control-change testing,
- pre-change/post-change evidence comparison,
- sustainability and post-control verification thinking,
- and clear separation between simulated evidence and real-world claims.

## Continuous Improvement & Process Gap Review™

SBI now includes a premium interactive continuous-improvement module for practicing the difference between resolving an individual case and strengthening the process that produced it.

Interactive path:

**Visible issue → immediate resolution → backward trace → recurring pattern review → process-gap hypothesis → small control change → owner → implementation evidence → post-change review → recurrence result**

Synthetic fields include:

- Issue Category
- Immediate Case Resolution Status
- Immediate Case Resolution
- Earlier Workflow Point Reviewed
- Earliest Supported Gap
- Similar Cases Found?
- Recurrence Count
- Pattern Classification
- Process-Gap Hypothesis
- Proposed Small Improvement
- Control Owner
- Implementation Date
- Evidence of Implementation
- Pre-Change Pattern
- Pre-Change Evidence
- Post-Change Pattern
- Post-Change Evidence
- Patient-Facing Effect
- Staff Effect
- Follow-Up Review Date
- Improvement Supported?
- Additional Review Needed?

The interactive decision logic can return states such as **Resolve Case**, **Trace the Gap**, **Evidence Boundary**, **Design Control**, **Implementation Evidence**, **Baseline Needed**, **Post-Change Review**, **Interpret Result**, **Supported in Simulation**, **Revise Control**, and **More Evidence**.

Key distinctions:

- **Case closed ≠ process gap closed**
- **Immediate correction ≠ preventive improvement**
- **Process change ≠ proven improvement**
- **Repeated issue ≠ proven systemic cause**

Core question:

> **Did the preventive control actually change the recurring pattern?**

Patient-to-professional insight:

> **The patient needs the individual problem resolved. Healthcare operations also has to determine whether the workflow that created the problem was strengthened.**

This is student-developed continuous-improvement practice. It does not represent Lean/Kaizen certification, quality-improvement employment experience, management authority, or real-world operational outcomes.

### Production-Quality Interactive Controls

The Continuous Improvement & Process Gap Review™ now includes:

- explicit **Newsreader** editorial typography and **Inter** interface/body typography,
- real browser persistence using `localStorage`,
- automatic draft restoration after refresh on the same browser/device,
- a Saved Review / Review History panel,
- Resume Review, Start New Review, and Delete Saved Review actions,
- progress shown as both percentage and **controls documented out of 15**,
- stage-specific missing-field highlighting after evaluation,
- a visible **Next Control** instruction,
- an **Improvement Evidence Summary** for recruiter-readable review,
- mobile-first button, form, spacing, and overflow improvements,
- and a strict white / black / Tennessee Orange (#FF8200) brand treatment.

Saved simulations remain in the user's browser on that device and are not uploaded by SBI. The project continues to require synthetic, no-PHI entries.

The interactive logic is designed to allow different evidence-based outcomes, including **Supported in Simulation**, **Revise Control**, and **More Evidence**. The tool does not force every modeled change to appear successful.

## Payment Recovery / Reconciliation Breakpoint

SBI now includes a simulated financial-workflow breakpoint example for situations where a later payment is reduced, reversed, adjusted, or linked to earlier recovery activity.

The review path is:

**Financial signal → trace original transaction → review evidence → separate fact from unanswered questions → assign owner → document next action → reconcile remaining balance → verify closure**

Key distinctions:

- **Paid ≠ correctly reconciled**
- **Reduced payment ≠ explanation of the underlying recovery**
- **Adjusted balance ≠ reconciled account**

Control question:

> **If a later payment is reduced because of an earlier account, what evidence should connect the recovery to the original transaction before the adjustment is treated as fully reconciled?**

Patient-to-professional insight:

> **The patient sees the balance. The operations team has to understand the chain of transactions that produced it.**

This remains a student workflow-analysis exercise. SBI does not determine payer liability, contract correctness, coding accuracy, refund obligations, reimbursement, or legal requirements.

## Patient-to-Professional Perspective

The patient usually does not experience an internal workflow label. The patient experiences the result.

They may know that they had to call again, wait longer, resend information, clarify coverage, or understand why the next step did not happen when expected. They may not know whether the internal issue involved eligibility, documentation, authorization, ownership, handoff, claim readiness, or a system workaround.

That is why SBI keeps the patient-facing consequence connected to the internal workflow question without pretending the project can prove that one caused the other.

My goal as a student and emerging healthcare operations professional is to learn how to ask better operational questions:

- What should have happened?
- What information or ownership was required?
- What exception remained open?
- Where did the workflow first lose control?
- What became visible downstream?
- What evidence supports the hypothesis?
- What should remain a question rather than be treated as a conclusion?

## Portfolio Evidence

This repository includes:

- `index.html` — interactive SBI project overview
- `continuous-improvement-process-gap-review.html` — interactive Continuous Improvement & Process Gap Review™
- `kp-logo.svg` — Kori Pickle KP brand mark
- `style.css` — project styling
- `templates/breakpoint-log.csv` — fictional breakpoint log using cautious, hypothesis-based language
- `templates/root-cause-library.csv` — possible contributing conditions, potential effects, student practice controls, and example measures
- `templates/case-study-template.md` — student-level workflow case-study structure
- `templates/kpi-dictionary.md` — educational KPI definitions and evidence boundaries
- `assets/` — project visual assets

## How SBI Fits in the Portfolio

SBI is the fourth project in the workflow path I use across my Healthcare Operations Intelligence Engine™ portfolio:

**EVIS → PARCS → DPIS → SBI → Habit Audit**

- **EVIS** looks at eligibility, intake, and exception closure.
- **PARCS** looks at prior-authorization workflow risk, documentation readiness, ownership, aging, and escalation.
- **DPIS** looks at claim readiness and upstream denial-risk signals.
- **SBI** looks across those workflows and asks where the first modeled control loss may have occurred.
- **Habit Audit** steps back and asks whether repeated operational habits may be making similar problems more likely to recur.

## What This Project Is — and Is Not

This is a **student-developed educational portfolio project**.

- All examples, cases, scores, dashboard values, and templates are simulated.
- No protected health information (PHI) is used.
- No real patient, payer, employer, claim, EHR, staffing, or financial data is used.
- It does not represent formal healthcare employment experience.
- It has not been deployed in a healthcare organization.
- It is not a clinical, coding, billing, compliance, payer, financial, or medical-necessity decision tool.
- The scoring model is not validated.
- Root-cause statements are hypotheses for practice, not proven causation.
- Potential effects are modeled possibilities, not documented patient, staff, financial, or quality outcomes.
- I do not claim SBI has reduced denials, delays, staff workload, costs, patient-access problems, or any other real-world outcome.

I want SBI to show how I am learning to trace administrative workflow problems upstream, keep the patient experience visible, organize evidence carefully, and communicate what a student simulation can and cannot support.

## Live Project

[View Silent Breakpoint Intelligence](https://koripickle1101-TN.github.io/silent-breakpoint-intelligence-system/)

## Connect

- [Healthcare Operations Portfolio Hub](https://healthcare-operations-portfolio-hub.vercel.app/)
- [LinkedIn](https://www.linkedin.com/in/kori-pickle)
- [GitHub profile](https://github.com/koripickle1101-TN)

Created by Kori Pickle. Student-developed portfolio project. Synthetic data only. No PHI.


## Patient Experience Signal → Process Gap Review

The existing Continuous Improvement & Process Gap Review™ includes one focused synthetic patient-experience scenario, **PX-001 — Repeated Appointment Waiting Complaints**. This is intentionally an extension of SBI rather than a separate complaint-management project.

PX-001 practices translating repeated patient-experience signals into structured operational investigation:

**Repeated signal → detection point → backward trace → evidence boundary → earliest supported gap → hypothesis → owner/control → baseline → post-change review → recurrence result**

The scenario reinforces:

- **Signal ≠ root cause**
- **Detection point ≠ origin point**
- **Recurrence ≠ proof of systemic cause**
- **Complaint closed ≠ process gap closed**
- **Process change ≠ proven improvement**

Career insight:

> **Patient experience can reveal where to investigate without proving why the experience occurred.**

The fictional complaints support a waiting/communication pattern but do not establish staffing, scheduling, registration, capacity, technology, or another cause. The learner must document evidence before drawing a root-cause conclusion.

This remains student-developed, simulated, synthetic, no-PHI portfolio practice and does not represent complaint-management employment experience, quality-improvement authority, management authority, or real patient outcomes.

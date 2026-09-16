# SBI — Silent Breakpoint Intelligence

I built SBI as a student-developed healthcare operations project around a question I keep coming back to: **where did the workflow first lose control before the downstream problem became obvious?**

As I work toward my Bachelor's of Science degree in Healthcare Administration at the University of Phoenix, I am learning that many healthcare problems become visible late. A denial may show up in billing. A delayed authorization may show up when a service has to be rescheduled. A documentation gap may show up when someone downstream has to stop and investigate. Staff may experience repeated rework while the patient experiences another call, another delay, or another explanation they were not expecting.

SBI gives me a way to practice looking upstream instead of treating the final visible problem as the whole story.

## Why I Built SBI

I do not have formal healthcare operations employment experience yet, so I use simulated projects to turn coursework and independent study into visible practice.

With SBI, I wanted to study the space between **the first control loss** and **the point where the consequences finally become visible**.

That means asking questions such as:

- Did inaccurate information enter during intake?
- Was documentation incomplete when the next team needed it?
- Did an authorization sit without clear ownership?
- Did a handoff happen without a closed loop?
- Did staff create a manual workaround that hid the underlying problem?
- Did leadership see the issue only after it reached billing, staffing, quality, or the patient?

The core question is:

> **Where did the workflow first lose control?**

## What I Mean by a “Silent Breakpoint”

In this project, a **silent breakpoint** is a modeled point where a workflow becomes less reliable even though the full downstream impact may not be visible yet.

Examples can include:

- incomplete intake information,
- documentation that is not ready for the next step,
- unclear authorization ownership,
- aging work without escalation,
- open-loop handoffs,
- repeated manual workarounds,
- inconsistent data capture,
- or a problem that is visible to staff but not yet visible in formal reporting.

I use the term as a learning framework. It is not a clinical definition, industry standard, or validated risk model.

## Workflow View

SBI follows the workflow forward while asking where the first instability appeared:

```text
Intake
  ↓
Documentation
  ↓
Authorization
  ↓
Handoff
  ↓
Technical / Administrative Execution
  ↓
Billing / Revenue Cycle
  ↓
Leadership Visibility
```

The important part for me is that the visible consequence may occur several steps after the original breakdown.

## Simulated Breakpoint Scoring Tool

The live project includes a simple educational calculator using five modeled dimensions:

1. Patient impact
2. Revenue impact
3. Staff burden
4. Repeat risk
5. Visibility gap

Each dimension is scored from 1 to 5. The values are added to create a total score from 5 to 25.

The current educational ranges are:

| Total Score | Modeled Interpretation |
|---:|---|
| 5–9 | Low friction |
| 10–14 | Moderate breakpoint |
| 15–19 | High-risk breakpoint |
| 20–25 | Critical modeled breakpoint |

These ranges are **student-designed learning assumptions**. They are not validated healthcare thresholds, benchmarks, compliance standards, or predictions of actual patient, financial, or operational outcomes.

## Simulated Dashboard Example

The site also shows a synthetic dashboard example with values such as:

- 24 modeled breakpoints logged
- 5 modeled critical breakpoints
- 9 modeled high-risk breakpoints
- 18.7 modeled average breakpoint score
- Authorization as the example top failure origin
- Unclear ownership as the example most common root-cause theme

These values are demonstration data only. They do not represent an employer, healthcare organization, payer, patient population, or observed operational results.

## What I Learned

The biggest lesson from SBI is that the last visible problem is not always the best place to start the analysis.

A denial can be the signal rather than the original failure. A rescheduled service can be the patient-facing consequence of an earlier ownership problem. Staff rework can be evidence that the workflow is depending on people to compensate for a weak process.

From the patient side, none of those internal categories really matter in isolation. What matters is what the person experiences: delay, uncertainty, repeated requests, a confusing bill, or a service that cannot move forward as expected.

That patient-to-professional perspective is why I want to learn how to trace problems back through the workflow instead of only reacting to the final outcome.

## Portfolio Evidence

This repository includes:

- `index.html` — interactive SBI project overview
- `style.css` — project styling
- `templates/breakpoint-log.csv` — simulated breakpoint-tracking structure
- `templates/root-cause-library.csv` — root-cause practice library
- `templates/case-study-template.md` — workflow case-study template
- `templates/kpi-dictionary.md` — KPI-definition practice asset
- `assets/` — project visual assets

## What I Am Practicing Through SBI

Through this project, I am practicing:

- Healthcare workflow mapping
- Root-cause thinking
- Handoff analysis
- Prior authorization workflow visibility
- Operational drift awareness
- Patient-access risk interpretation
- Staff-rework and workload visibility
- Revenue-cycle workflow analysis
- KPI and dashboard communication
- Simulated risk scoring
- Process-control thinking
- Operational documentation
- Patient-to-professional analysis
- Clear separation between simulated evidence and real-world claims

## How SBI Fits in the Portfolio

SBI is the fourth project in the workflow path I use across my healthcare operations portfolio:

**EVIS → PARCS → DPIS → SBI → Habit Audit**

- **EVIS** looks at eligibility and intake risk.
- **PARCS** looks at prior authorization workflow risk, ownership, and escalation.
- **DPIS** looks at upstream denial-prevention and claim-readiness risk.
- **SBI** looks across the workflow and asks where the first control loss occurred.
- **Habit Audit** looks at recurring operational habits that may make workflow risk more likely.

## What This Project Is — and Is Not

This is a **student-developed educational project**.

- All examples, cases, scores, dashboard values, and templates are simulated.
- No protected health information (PHI) is used.
- No real patient, payer, employer, claim, EHR, staffing, or financial data is used.
- The project does not represent formal healthcare employment experience.
- It has not been deployed in a healthcare organization.
- The scoring model is not a validated clinical, financial, compliance, or operational risk instrument.
- I do not claim that SBI has reduced denials, delays, staff burnout, costs, or patient-access problems in the real world.

I want SBI to show how I am learning to trace healthcare workflow problems upstream, think about the people affected downstream, and communicate what the evidence can and cannot support.

## Live Project

[View Silent Breakpoint Intelligence](https://koripickle1101-TN.github.io/silent-breakpoint-intelligence-system/)

## Connect

- [Healthcare Operations Portfolio Hub](https://healthcare-operations-portfolio-hub.vercel.app/)
- [LinkedIn](https://www.linkedin.com/in/kori-pickle)
- [GitHub profile](https://github.com/koripickle1101-TN)

Created by Kori Pickle. Student-developed portfolio project. Synthetic data only. No PHI.
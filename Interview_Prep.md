# Interview Preparation Guide
## Management Analyst I — Maine Department of Transportation
### Bureau of Finance and Administration | Augusta, ME | Salary: $21.54–$30.14/hr

---

## 0. PRESENTING THE DASHBOARD — Your 10-Minute Interview Demo

> This is your centerpiece. Open http://localhost:5000 on your laptop before you
> walk into the room. The moment they say "tell us about yourself," pivot to showing
> it. Below is a word-for-word walkthrough, section by section.

---

### STEP 1 — Open with the problem (30 seconds, before touching the screen)

Say this before you even turn the laptop around:

> "I wanted to come in today with something concrete rather than just talking about
> what I *could* do. So I took the exact work described in the job posting —
> cellphone management, financial transaction review, cost-effectiveness analysis —
> and I built it. This is a live audit dashboard for a 20-person simulated DOT
> department. May I walk you through it?"

*Then turn the screen toward them.*

---

### STEP 2 — The KPI strip at the top (60 seconds)

Point to the six tiles across the top and say:

> "These are the executive-level numbers. Current spend is **$1,252 a month —
> $15,024 a year** across 20 employees. The moment I ran the analysis, **7 employees
> lit up as flagged** — either over-provisioned or generating overage charges.
> The net savings projection is **$1,824 a year — a 12.1% reduction** — at absolutely
> zero impact to any employee's service."

*Pause. Let the savings number land.*

> "That's the kind of number you can put in front of a bureau director and get a
> decision same day."

---

### STEP 3 — The scatter chart: Cost vs. Data Usage (90 seconds)

Point to the left chart:

> "This scatter plot is where the story starts. Each dot is an employee. Color tells
> you the plan tier — blue Basic, orange Standard, red Premium. The X-axis is how
> much data they actually use. The Y-axis is what we're paying."

Hover over one of the diamond markers (downgrade candidates) and show the tooltip:

> "See these diamond shapes? Those are the downgrade candidates — people on Premium
> or Standard plans clustered here on the left side of the chart. Low data usage,
> high cost. Robert Landry is the worst case: $80 a month, Premium plan, using half
> a gigabyte. That's **$160 per gigabyte**. The Basic plan would cost $50 per
> gigabyte for him. There's no defensible reason for that billing."

Hover over a triangle marker:

> "The triangles are the opposite problem — employees generating overage charges
> because their plan is too small. Patricia Ouellete is on Standard with a $8
> overage last month. Upgrading her to Premium actually *saves* money month-to-month
> by eliminating unpredictable charges and simplifying invoice reconciliation."

---

### STEP 4 — The department bar chart (45 seconds)

Point to the middle chart:

> "This shows monthly spend by department. Finance is the highest at $260 a month —
> and not coincidentally, two of the downgrade flags are Finance employees. When I
> pull the thread on the highest-spending department, that's exactly where the waste
> surfaces. That's how you prioritize in a review like this: start with the biggest
> budget line."

---

### STEP 5 — The donut chart (30 seconds)

Point to the right chart:

> "The donut shows plan tier distribution. 7 of 20 employees — 35% — are on Premium.
> That's the most expensive tier. The analysis shows that 4 of those 7 Premium
> employees are using under 5% of their included data. Premium is the right plan
> for someone like Michael in IT using 12 gigabytes a month. It is not the right
> plan for a Finance officer using 0.5."

---

### STEP 6 — Scroll down to the employee table (60 seconds)

Scroll to the full table:

> "This is the full dataset — every employee, their plan, actual usage, and the
> utilization bar. Red bars are the problem — those employees are using less than
> 30% of their plan capacity. I set that threshold deliberately because it's
> objective. I'm not making judgment calls person by person; I'm applying a
> consistent rule across all 20, which is what holds up under audit."

Point to the Recommendation column:

> "The last column tells the manager exactly what to do. No ambiguity. 'Downgrade
> to Basic' means call the carrier and move the plan — it takes minutes. The
> employee keeps the same number, same device, same service — they just stop paying
> for 14 gigabytes they never touch."

---

### STEP 7 — The action summary table at the bottom (60 seconds)

Scroll to the bottom table:

> "This bottom table is the memo in visual form. Every action, the dollar impact
> per month, and per year. Green is savings, red is additional cost. The net row
> at the bottom is what I'd put in front of a director for approval: **negative
> $152 a month, negative $1,824 a year.** Specific. Actionable. Ready to sign."

---

### STEP 8 — Close the demo with the methodology statement (45 seconds)

Step back from the screen and say:

> "The methodology is straightforward: collect the data, define an objective
> threshold, apply it consistently, quantify the outcome, and write it up in
> language a manager can act on. That's what this job description is asking for —
> and from what I've seen, the phone program is the first place that discipline
> pays off. But the same process applies to any vendor invoice review, any credit
> card reconciliation, any usage trend you need to report to leadership."

---

### STEP 9 — The confidence statement (if they ask "why should we hire you?")

> "Because I didn't wait to be hired to start doing this job. I read the posting,
> I read the department's history, I understood what the real pain point is —
> and I built the analysis. I can do this work, and I can explain it clearly to
> people who don't want to look at spreadsheets. That combination — analytical
> rigor and plain-language communication — is exactly what a Management Analyst I
> needs to be effective here."

---

### What to have ready before you walk in

| Item | How |
|---|---|
| Dashboard running | `python dashboard.py` in terminal — keep it open |
| URL bookmarked | http://localhost:5000 |
| Print the memo | [Phone_Plan_Audit_Memo.md](Phone_Plan_Audit_Memo.md) — 1 copy per panel member |
| Know all 7 numbers | $1,252/mo · $15,024/yr · 7 flagged · 5 downs · 2 ups · $1,824 saved · 12.1% |
| Charger plugged in | Nothing kills a demo like a dying battery |

---

## 1. Know the Organization

**MaineDOT was founded in 1913** as the State Highway Commission — one of the earliest
state transportation agencies in the country. It became the full Department of
Transportation in 1972, absorbing the Highway Commission, Port Authority, Department
of Aeronautics, and several other agencies into one unified body.

**What makes this organization tick:**
- A deep public service ethos embedded since day one: *"serve the largest number
  of people possible"*
- Aggressive cost discipline: competitive bidding has been standard practice since
  the Commission's earliest years; the 1972 report explicitly cites the goal of
  building highways that "cost as little as possible"
- Early technology adoption: digital computers and data processing were in use by
  **1961** — the culture of using data to work smarter has long roots here
- Today: ~21,000 miles of public roads maintained across Maine

**Your bureau — Finance and Administration** — is the backbone that makes the
field mission possible. Every dollar you save or process accurately maps directly
to road maintenance, bridge repair, and public safety.

---

## 2. Understand the Real Job

The posting is titled "Management Analyst I" but read carefully what the work
actually is:

> *"Setting up cellphones, troubleshooting issues, and performing other tasks related
> to cellphone management. Organize, review, and process financial transactions,
> including vendor invoices and credit card payments. Conduct research and provide
> data to analyze trends, statistical and historical information, cost effectiveness,
> and phone usage."*

This is a **financial analyst + operations coordinator** role. The phone program
is the biggest administrative headache listed — a department-wide utility generating
recurring invoices, plan change requests, and usage data that nobody has apparently
systematized yet. That is your opening.

---

## 3. How the Demo Maps to Every Requirement

| Job Description Requirement | Your Demo Demonstrates |
|---|---|
| Cellphone management | You audited a real phone program — plans, tiers, usage, overages |
| Review/process financial transactions & vendor invoices | You analyzed carrier billing data and identified billing inefficiencies |
| Analyze trends, cost effectiveness, and phone usage | That is *literally* what the cost-per-GB trend analysis does |
| Gather, assemble, calculate, and analyze facts | Collect CSV → calculate utilization % → flag outliers → quantify savings |
| Draw valid conclusions | "$1,824/year net savings, 12.1% reduction" — specific and defensible |
| Communicate effectively / write clearly | The one-page memo is your writing sample |
| Develop recommendations for revision of procedures | "Establish a semi-annual review cycle" — that's a policy recommendation |
| Knowledge of data collection & analytical techniques | Python/Excel analysis with a defined threshold methodology |

---

## 4. Your Interview Narrative

### Opening — when asked "Tell me about yourself"
> "I have [X years] of experience in [your background]. For this interview, I wanted
> to demonstrate practically how I approach the core work of this role — so I built
> an analysis that mirrors exactly what a Management Analyst does here. I took a
> simulated dataset of 20 DOT employees and their phone plans, analyzed usage trends,
> identified waste, quantified the savings, and wrote it up as a recommendation memo.
> I'd like to walk you through it if that's useful."

### Walking through the demo — the 60-second pitch
> "I started by defining the problem: are we spending the right amount on the right
> plans? I collected usage data — data in gigabytes, voice minutes, overage charges —
> and calculated cost-per-GB for each person. That ratio immediately surfaced four
> employees on $80 Premium plans using under 1 GB per month — paying effectively
> $100 to $160 per gigabyte when the Basic plan at $40 would cost them $50. I set
> a threshold: anyone using less than 30% of their plan's capacity is a downgrade
> candidate. Applied consistently, that flags five employees and projects $2,160 in
> gross annual savings. The memo leads with the bottom line and tells the director
> exactly what to approve."

### On your analytical method — if pressed
> "I believe in objective, defensible thresholds. Setting 30% utilization as the
> flag removes subjectivity — I'm not making judgment calls employee by employee,
> I'm applying a rule consistently across all 20. That's also what holds up if a
> vendor or an auditor questions the recommendation."

### On vendor invoices and financial transactions
> "The review I built is essentially the same discipline you'd apply before approving
> a carrier invoice. If someone is on a Premium plan and the invoice shows 0.5 GB
> of usage, that's a line item worth questioning before you process payment. I'd
> bring that same habit to credit card reconciliations and any other transaction
> review — verify the charge matches both the agreement and what was actually used."

---

## 5. MaineDOT Talking Points — Show You Did Your Homework

Use one or two of these naturally in conversation:

- **History:** *"I was reading about the Commission's early years — they were doing
  competitive bidding and public hearings before construction as far back as 1913.
  That culture of accountability and cost-consciousness clearly runs through the
  organization, and it's the same mindset I'd bring to this budget work."*

- **Technology:** *"The Department adopted computers and data processing in 1961 —
  well ahead of most state agencies at the time. The idea of using data to work
  smarter obviously has deep roots here, which makes me think a structured phone
  plan review process would fit right in."*

- **Local Roads Center:** *"I noticed DOT also runs the Local Roads Center, training
  municipal crews across Maine. The department isn't just internally focused — it's
  actively helping communities operate more efficiently. That outward-facing mission
  resonates with me."*

- **Mission alignment:** *"The 1972 annual report says the goal has always been highways
  that 'do the most good for the greatest number of people and still cost as little
  as possible.' That's essentially what a Finance and Administration bureau exists
  to protect."*

---

## 6. Anticipate These Questions

**"What's your experience with cellphone management?"**
> Frame whatever you have honestly. If limited:
> *"I may not have managed a fleet of hundreds of devices, but this audit shows I
> understand the structure of a phone program end-to-end: plan tiers, usage tracking,
> overage billing, vendor invoices, and the policy levers for cost control. I can
> get current on the specific carrier and platform quickly."*

**"What software do you use for data analysis?"**
> If you ran the Python script: *"I'm comfortable in Excel for day-to-day work and
> I also built this analysis in Python using pandas — it generates the charts and
> the full report automatically so it can be re-run as new billing data comes in
> each month."*
> If Excel only: *"Excel is my primary tool — I used pivot tables to segment usage
> by department and plan tier, and built the charts from there."*

**"How do you communicate findings to non-technical audiences?"**
> *"The memo in this audit is my answer to that. I lead with the dollar amount and
> the specific action needed. The methodology is there for validation if anyone wants
> to review it, but a bureau director shouldn't need to read past the executive
> summary to know what to approve."*

**"How do you ensure accuracy when processing invoices?"**
> *"I verify against source data before approving anything. On a phone bill that
> means cross-checking the carrier's invoice against the plan assignment records on
> file. If someone is billed for a Premium plan but you've already requested a
> downgrade, that discrepancy needs to catch before payment — not after."*

**"Describe a time you found an inefficiency and fixed it."**
> Use this demo as the example if you don't have a direct parallel. Walk through
> the problem → methodology → finding → recommendation → outcome structure.
> The entire demo is a self-contained STAR story.

---

## 7. Minimum Qualifications — Know Where You Stand

The posting requires:
> *"Six (6) years of education, training, and/or experience analyzing, evaluating,
> and/or developing improvements to organizational and/or managerial systems,
> programs, and practices."*

**This is broad by design — education counts toward the 6 years.**

| Category | What to Include |
|---|---|
| Education | 4-year degree = typically 4 years credit; relevant coursework counts |
| Training | Certifications, workshops, on-the-job training programs |
| Experience | Any role involving analysis, reporting, financial review, or operations |

Frame your background deliberately when completing the application.
Be specific: *"analyzed vendor invoices for accuracy"*, *"maintained records and identified
discrepancies"*, *"developed recommendations to improve department workflow"*.

---

## 8. Questions to Ask Them

These signal genuine interest and give you useful information:

1. *"What does the current cellphone program look like — how many devices, and how
   is the fleet currently managed?"*
2. *"What tools does the Finance team use for financial reporting and invoice
   reconciliation today?"*
3. *"Is there a current backlog of process improvement projects the team is working
   through, or would this be somewhat greenfield?"*
4. *"What does success look like in the first six months for someone in this role?"*

---

## 9. Day-Of Checklist

- [ ] Print 3 copies of `Phone_Plan_Audit_Memo.md` (formatted, one-page) for the panel
- [ ] Have `phone_plan_audit_charts.png` ready to show on laptop or phone
- [ ] Know your salary target — range is $21.54–$30.14/hr ($44,803–$62,691/year)
- [ ] Arrive with a copy of your application for reference
- [ ] Closing statement: express genuine interest in the public service mission,
      specifically the Finance bureau as the operational backbone of MaineDOT

---

## 10. The One-Sentence Version

If you can only remember one thing for the interview, make it this:

> *"I defined the problem, gathered the data, ran the analysis, and produced a
> recommendation a manager could act on immediately. That's the job."*

# EXACT PRESENTATION SCRIPT
## Maine DOT — Management Analyst I Interview
### Read this out loud. Every word is ready to say.

---

# BEFORE YOU ENTER THE ROOM

Open your laptop. Go to http://localhost:5000. The dashboard must be live.
Have the memo printed — one copy per interviewer.
Take a breath. You have done this work. You understand this role better than
most candidates who walk through that door.

---

# THE MOMENT YOU SIT DOWN

*They will say: "So tell us a little about yourself."*
*Do NOT give a generic bio. Open with this instead:*

> "I'd love to — but before I do, I actually want to show you something,
> because I think it explains who I am better than anything I could just tell you.
>
> When I saw this posting, I read every word carefully. The job description says:
> cellphone management, financial transaction review, cost analysis, and data trends.
> So instead of talking about how I'd approach that work, I went ahead and did it.
>
> This is a live audit dashboard I built for this interview — a complete cellphone
> plan cost review for a 20-person simulated DOT department. It pulls from a real
> dataset, runs the analysis, flags the problems, and produces a recommendation.
>
> May I walk you through it?"

*Turn the laptop screen toward them.*
*Wait for them to nod. Then begin.*

---

---

# SECTION 1 — THE SIX TILES AT THE TOP OF THE SCREEN
## (The KPI Strip)

*Point to the row of six colored boxes at the very top of the dashboard.*

> "The first thing I designed here is what I'd call the executive summary view —
> six numbers that tell the whole story before you read a single row of data.
>
> Starting on the left:"

*Point to tile 1 — "20 Employees Audited"*

> "Twenty employees across seven departments: Finance, Engineering, Planning,
> Maintenance, Administration, IT, and Safety. That's the scope of this audit."

*Point to tile 2 — "$1,252 Monthly Spend"*

> "Current total monthly spend is $1,252. That's what the department is paying
> right now, across all twenty devices and plans."

*Point to tile 3 — "$15,024 Annual Spend"*

> "Annualized, that's $15,024 per year. For twenty phones. That's the number
> a finance bureau wants to benchmark and track."

*Point to tile 4 — "7 Employees Flagged" — it will be in red*

> "Seven employees are flagged for right-sizing. That means seven people are either
> on plans that far exceed what they actually use, or they're on plans so small
> they're generating overage charges every month. Both situations cost the department
> money unnecessarily."

*Point to tile 5 — "$1,824 Projected Annual Savings" — in green*

> "After right-sizing all seven — five downgrades, two upgrades — the projected
> net savings is $1,824 per year."

*Point to tile 6 — "12.1% Budget Reduction" — in green*

> "That is a 12.1% reduction in the phone budget. With zero change to any
> employee's device, phone number, or day-to-day service.
>
> That's the entire audit, in six numbers. Now let me show you how I got there."

---

---

# SECTION 2 — THE SCATTER CHART (Left Chart)
## "Cost vs. Data Usage"

*Point to the chart in the top left — the one with dots scattered across it.*

> "This is the chart where the analysis begins. Every dot is one employee.
>
> The X-axis — the horizontal — is how much data they actually used last month,
> measured in gigabytes.
>
> The Y-axis — the vertical — is how much we're paying for their plan per month.
>
> The color tells you the plan tier. Blue dots are Basic — $40 a month.
> Orange dots are Standard — $60 a month. Red dots are Premium — $80 a month."

*Hover your mouse over a RED DOT on the LEFT side of the chart — a downgrade candidate.*
*The tooltip will pop up showing the name, usage, and cost.*

> "Now here's where it gets interesting. Look at these red dots — Premium plans —
> that are sitting all the way over here on the left side of the chart.
> Low data usage. High cost. That combination is a red flag.
>
> Let me hover over this one."

*Hover over Robert Landry's dot.*

> "Robert Landry. Finance department. Premium plan — $80 a month.
> Monthly data used: 0.5 gigabytes.
>
> His Premium plan includes 15 gigabytes. He's using 3% of what he's paying for.
>
> Calculated out: he's paying $160 per gigabyte of data used.
> The Basic plan at $40 a month would give him 2 gigabytes — more than four times
> what he actually uses — for half the price.
>
> That one change saves $40 a month. $480 a year. For doing absolutely nothing
> except making a phone call to the carrier."

*Hover over Sarah Mitchell's dot.*

> "Same story here — Sarah Mitchell, Finance. Premium plan, $80 a month,
> 0.8 gigabytes used. 5% of her plan. Downgrade to Basic saves another $40
> a month."

*Now hover over a TRIANGLE dot — an upgrade candidate.*

> "Now the triangles are the opposite problem.
>
> Patricia Ouellete, Maintenance. She's on a Standard plan — $60 a month —
> but she used 5.8 gigabytes last month. Her plan only includes 5.
> So she got charged $8 in overage fees on top of the $60.
>
> That means her real cost last month was $68 — and it's unpredictable.
> Some months it could be $12 in overage, some months $20.
>
> Upgrading Patricia to Premium — $80 flat — actually saves money by stopping
> the overage bleeding and making her costs predictable on the invoice."

*Lean back slightly.*

> "So one chart tells you: who is overpaying, who is underpaying, and exactly
> what to do about each one."

---

---

# SECTION 3 — THE DEPARTMENT BAR CHART (Middle Chart)
## "Monthly Spend by Department"

*Point to the middle horizontal bar chart.*

> "This chart shows total monthly spend organized by department.
>
> Finance is the highest — $260 a month across their people.
> Engineering is second at $220. Then Administration at $180.
>
> Now here's why this matters from an analyst's perspective:
> When I see Finance at the top of this spending chart, that's where I pull
> the thread first. And sure enough — two of the five downgrade flags are
> Finance employees. Robert Landry and Sarah Mitchell.
>
> That's not a coincidence. High-spending departments often have people who
> got put on Premium plans when they were onboarded and nobody ever checked
> whether the plan matched actual usage.
>
> In a real audit, I'd start every review by sorting by department spend,
> then drilling into the highest-cost departments first. That's how you find
> the biggest savings fastest."

---

---

# SECTION 4 — THE DONUT CHART (Right Chart)
## "Plan Tier Distribution"

*Point to the donut/ring chart on the right.*

> "This gives a quick structural view of how the fleet is set up.
>
> 25% of employees — 5 people — are on Basic.
> 40% — 8 people — are on Standard.
> 35% — 7 people — are on Premium.
>
> 35% on Premium is significant. Premium is absolutely the right plan for
> someone like Michael Bouchard in IT, who uses 12 gigabytes a month running
> field diagnostics and connecting remote systems.
>
> But 4 of those 7 Premium employees are using under 5% of their included data.
> That means more than half of our Premium spend is going to the wrong people.
>
> This chart is what I'd show a bureau director in a quarterly review to justify
> the recommendation. It's simple, it's visual, and it immediately answers
> the question: 'Do our plan assignments match our actual usage profile?'
> Right now, the answer is no — and here's what we're doing about it."

---

---

# SECTION 5 — SCROLL DOWN TO THE EMPLOYEE TABLE
## "All Employees — Plan Review"

*Scroll down. Point to the full data table.*

> "Now we get into the detail. This is every employee, their plan, their actual
> usage last month, and a utilization bar.
>
> The utilization bar is the key column. Red means they're using less than
> 30% of their plan's included data. Yellow is moderate. Green means they're
> using their plan efficiently."

*Point to a red bar row — e.g., Robert Landry.*

> "Red bars are waste. When I see a red bar on a Premium plan, that's $40 or
> more per month going to a carrier for nothing.
>
> I chose 30% as the downgrade threshold deliberately — and I'd defend that
> threshold in front of any auditor. It's not a gut feeling. It's an objective
> rule applied consistently across all 20 employees. Nobody can say the
> recommendations are biased or arbitrary, because every single person was
> measured against the same standard."

*Point to the Recommendation column on the right.*

> "The last column tells the manager exactly what to approve.
> 'Downgrade to Basic' — that means call the carrier, change the plan.
> Five minutes of administrative work. No device change. The employee doesn't
> even notice. But the savings show up on the next invoice.
>
> Karen Arsenault here — Basic plan, $40 a month, using 0.3 gigabytes — she's
> actually the most cost-efficient in terms of plan assignment even though her
> cost-per-GB is high, because Basic is already the lowest tier. There's nowhere
> to go. The flag doesn't fire on her. The system works correctly.
>
> That matters — a good analysis knows what NOT to flag, not just what to flag."

---

---

# SECTION 6 — THE BOTTOM TABLE
## "Right-Sizing Action Summary"

*Scroll to the bottom table.*

> "This is the memo in table form. This is what I'd attach to a formal
> recommendation going to a bureau director.
>
> Every flagged employee. The plan they're on now. The action — downgrade or
> upgrade. The monthly cost impact in green or red. And the annual number.
>
> Five downgrades — saving $40 a month each except Mary Violette who saves $20,
> for a gross saving of $180 a month.
>
> Two upgrades — Patricia Ouellete and Thomas Michaud — adding $28 a month
> combined. But they eliminate overage charges that are unpredictable and
> harder to reconcile on vendor invoices.
>
> Net result — bottom row: negative $152 a month. Negative $1,824 a year.
>
> A manager looks at this table and makes one decision. Approve or don't approve.
> The analyst's job is to make that decision as easy as possible. That's what
> this table does."

---

---

# THE CLOSING STATEMENT
## Say this after you finish the walkthrough

*Close the laptop screen slightly. Make eye contact.*

> "What I've shown you today is not a side project. It is the job description —
> executed.
>
> Cellphone management: I designed a system to audit it.
> Financial transaction review: I analyzed billing data and identified invoice
> discrepancies before payment.
> Cost-effectiveness analysis: I calculated cost per gigabyte and flagged waste.
> Data trends: I segmented by department, by tier, by utilization.
> Actionable recommendation: $1,824 in annual savings, ready to implement.
>
> I understand that public sector budgets are under pressure and every dollar that
> isn't wasted on a phone plan is a dollar that goes toward road maintenance or
> bridge repairs or keeping crews on the road in winter.
>
> That's why this work matters. And that's the mindset I'd bring to this bureau
> every day."

---

---

# IF THEY ASK FOLLOW-UP QUESTIONS

---

## Q: "How did you build this?"

> "I built the dataset in a CSV — 20 employees with realistic department
> assignments, plan tiers, and usage patterns including a few deliberate outliers.
> I wrote the analysis in Python using pandas for the data processing, and Flask
> to serve it as an interactive web dashboard with Chart.js for the visualizations.
> The whole thing runs locally — no cloud services, no external data.
> In a real setting, this would pull directly from the carrier's billing API
> or an exported invoice file."

---

## Q: "What if you only know Excel, not Python?"

> "The analysis logic is identical in Excel. Pivot table by department,
> calculated column for utilization percentage, conditional formatting for
> the red/yellow/green bars, a filter for the 30% threshold.
> Python just means it can be re-run automatically every month without
> rebuilding the spreadsheet. Either way, the judgment behind the analysis
> is the same."

---

## Q: "How would you handle a much larger fleet — 200 phones?"

> "The methodology scales exactly — the threshold rule doesn't care whether
> it's 20 employees or 200. What changes is the process for acting on it.
> With 200 devices, I'd work with the carrier account rep to do batch plan
> changes rather than one at a time. I'd also build a recurring monthly
> report so new outliers get caught within one billing cycle rather than
> accumulating for a year."

---

## Q: "What if an employee pushes back on a downgrade?"

> "That's a real scenario and worth planning for. My recommendation would be:
> downgrade with a 3-month review window. If the employee demonstrates usage
> above the Basic threshold within 90 days, they get upgraded back — no questions.
> That removes the objection and protects the employee. It also forces the question:
> if they never hit the threshold in 3 months, the data has answered itself."

---

## Q: "Have you worked in government or transportation before?"

> "Not directly in transportation — but I want to be honest about why I'm
> interested in MaineDOT specifically. I read through the department's history
> going back to the 1913 State Highway Commission. The founding mandate was to
> connect communities that were isolated because roads faded into dirt trails
> at town lines. That mission — using public resources as efficiently as possible
> to serve the widest number of people — that's exactly what a Finance and
> Administration bureau exists to protect. I find that meaningful. And I think
> the skills translate directly."

---

---

# THE SEVEN NUMBERS — MEMORIZE THESE

Write them on your hand if you need to. Know them cold.

```
$1,252   —  current monthly spend
$15,024  —  current annual spend
7        —  employees flagged
5        —  downgrade candidates
2        —  upgrade candidates
$1,824   —  net annual savings
12.1%    —  budget reduction
$160/GB  —  Robert Landry (your sharpest single data point)
```

---

# DAY-OF CHECKLIST

```
[ ]  Run:  python dashboard.py   (keep terminal open)
[ ]  Open: http://localhost:5000 in browser
[ ]  Print memo — one copy per panel member
[ ]  Arrive 10 minutes early — enough time to set up laptop
[ ]  Charger in bag
[ ]  Know the 7 numbers above without looking
[ ]  Know Robert Landry's story ($80/mo, 0.5 GB, $160/GB)
[ ]  Know Patricia Ouellete's story (overage victim, upgrade saves money)
```

---

# ONE SENTENCE — IF YOU FORGET EVERYTHING ELSE

> *"I defined the problem, gathered the data, set an objective threshold,
> ran the analysis, quantified the savings, and produced a recommendation
> a manager could sign today. That is this job."*

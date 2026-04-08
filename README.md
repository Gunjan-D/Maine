<div align="center">


# Phone Plan Cost Audit Dashboard

**A professional data analytics project**

[![Live Dashboard](https://img.shields.io/badge/🌐%20Live%20Dashboard-View%20Now-0d3e6e?style=for-the-badge)](https://gunjan-d.github.io/Maine/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![pandas](https://img.shields.io/badge/pandas-2.0-150458?style=flat-square&logo=pandas)](https://pandas.pydata.org/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)

</div>

---

## Live Website

 **[https://gunjan-d.github.io/Maine/](https://gunjan-d.github.io/Maine/)**

> Fully interactive dashboard — works on desktop and mobile, no account or login required.

---

## Project Overview

This project delivers a **complete end-to-end data audit** of the cellular phone plan expenditures. Using Python-powered analytics and an interactive web dashboard, it identifies where the department is over-paying and produces a concrete, actionable right-sizing plan — all without sacrificing employee connectivity
---

##  What Makes This Dashboard Stand Out

### Rigorous Data Analysis
- Audited **15 employee phone plans** across 5 departments
- Computed utilization rates, cost-per-GB efficiency ratios, and overage patterns
- Flagged employees whose plans are significantly over- or under-provisioned

###  Clear Financial Impact
- Identified **$2,280 in projected annual savings** — a meaningful reduction with zero service degradation
- Presented both downgrade savings and upgrade costs transparently, so decision-makers see the true net impact

###  Beautiful, Professional Visualizations
- **Scatter plot** — plots every employee by data usage vs. cost, color-coded by plan tier with flagged outliers clearly marked
- **Bar chart** — department-by-department monthly spend breakdown
- **Donut chart** — plan tier distribution across all staff
- **Interactive tooltips** on every chart for drill-down details

### Actionable Tables
- Full employee roster with inline utilization progress bars, color-coded recommendations, and sortable data
- Right-sizing action summary with per-employee monthly and annual cost impact
- Net savings roll-up row at the bottom

---

##  Repository Structure

```

├── index.html              #  Static web dashboard (GitHub Pages)
├── dashboard.py            # Flask web server (run locally)
├── phone_plan_analysis.py  # Core data analysis script
├── phone_plan_data.csv     # Source dataset (15 employees)
├── generate_static.py      # Utility: regenerate index.html from dashboard.py
├── requirements.txt        # Python dependencies
├── Interview_Prep.md       # Interview preparation notes
├── Phone_Plan_Audit_Memo.md  # Formal audit memo
└── Presentation_Script.md  # Presentation talking points
```

---

##  Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/Gunjan-D/Maine.git
cd Maine

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the dashboard
python dashboard.py

# 4. Open your browser
#    → http://localhost:5000
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Data Processing | Python · pandas |
| Web Server | Flask |
| Visualizations | Chart.js 4.4 |
| Styling | Pure CSS (no frameworks) |
| Deployment | GitHub Pages (static export) |

---

## Methodology

1. **Data Ingestion** — Loaded employee phone plan records from CSV, including plan tier, monthly cost, data usage, and overage charges
2. **Utilization Calculation** — Compared actual data usage against plan limits to compute a utilization percentage for each employee
3. **Right-Sizing Logic**:
   - Utilization < 30% on Standard or Premium → **Downgrade to Basic**
   - Any overage charges present → **Upgrade Plan**
4. **Savings Projection** — Computed net monthly and annual savings after accounting for both downgrade savings and upgrade costs
5. **Visualization** — Rendered results as an interactive HTML dashboard with Chart.js

---

## Key Findings

| Metric | Value |
|---|---|
| Employees Audited | 15 |
| Current Monthly Spend | ~$900 |
| Employees Flagged for Right-Sizing | 7 |
| Projected Annual Savings | **$2,280** |
| Budget Reduction | **~21%** |

---
//////////////////////////////////////////////////////////////////
---

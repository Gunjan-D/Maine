"""
MaineDOT Phone Plan Audit — Web Dashboard
Run:  python dashboard.py
Open: http://localhost:5000
"""

import os, sys
import pandas as pd
from flask import Flask, render_template_string

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Load & compute (same logic as phone_plan_analysis.py) ────────────────────
df = pd.read_csv(os.path.join(SCRIPT_DIR, "phone_plan_data.csv"))

PLAN_LIMITS_GB = {"Basic": 2, "Standard": 5, "Premium": 15}
PLAN_COST_MAP  = {"Basic": 40, "Standard": 60, "Premium": 80}

df["Plan_Limit_GB"]   = df["Plan_Tier"].map(PLAN_LIMITS_GB)
df["Utilization_Pct"] = (df["Data_GB"] / df["Plan_Limit_GB"] * 100).round(1)
df["Cost_Per_GB"]     = (df["Total_Monthly_Cost"] / df["Data_GB"]).round(2)
df["Annual_Cost"]     = df["Total_Monthly_Cost"] * 12

df["Recommendation"] = "No Change"
downgrade_mask = (df["Utilization_Pct"] < 30) & (df["Plan_Tier"].isin(["Premium","Standard"]))
df.loc[downgrade_mask, "Recommendation"] = "Downgrade to Basic"
df.loc[df["Overage_Cost"] > 0, "Recommendation"] = "Upgrade Plan"

current_monthly     = df["Total_Monthly_Cost"].sum()
current_annual      = df["Annual_Cost"].sum()

downgrade_df                  = df[df["Recommendation"] == "Downgrade to Basic"].copy()
downgrade_df["Savings_Month"] = downgrade_df["Plan_Cost"] - 40
total_savings_monthly         = downgrade_df["Savings_Month"].sum()

upgrade_df               = df[df["Recommendation"] == "Upgrade Plan"].copy()
UPGRADE_TARGET           = {"Basic": "Standard", "Standard": "Premium"}
upgrade_df["New_Plan"]   = upgrade_df["Plan_Tier"].map(UPGRADE_TARGET)
upgrade_df["New_Cost"]   = upgrade_df["New_Plan"].map(PLAN_COST_MAP)
upgrade_df["Extra_Month"]= upgrade_df["New_Cost"] - upgrade_df["Total_Monthly_Cost"]
total_upgrade_extra      = upgrade_df["Extra_Month"].sum()

net_savings_monthly = total_savings_monthly - total_upgrade_extra
net_savings_annual  = net_savings_monthly * 12
pct_reduction       = round(net_savings_annual / current_annual * 100, 1)

dept_spend = df.groupby("Department")["Total_Monthly_Cost"].sum().sort_values(ascending=False)

# ── Chart.js data ─────────────────────────────────────────────────────────────
# Scatter: all employees colored by tier
TIER_COLORS = {"Basic": "#1E88E5", "Standard": "#FFA726", "Premium": "#E53935"}

def scatter_datasets(dataframe):
    datasets = []
    for tier, grp in dataframe.groupby("Plan_Tier"):
        points = [{"x": round(row.Data_GB, 2),
                   "y": row.Total_Monthly_Cost,
                   "label": row.Name,
                   "flag": row.Recommendation}
                  for _, row in grp.iterrows()]
        datasets.append({
            "label": tier,
            "data": points,
            "backgroundColor": TIER_COLORS[tier],
        })
    return datasets

scatter_ds      = scatter_datasets(df)
dept_labels     = list(dept_spend.index)
dept_values     = list(dept_spend.values.tolist())
plan_counts     = df["Plan_Tier"].value_counts().reindex(["Basic","Standard","Premium"]).fillna(0).astype(int).tolist()

# Table rows
def row_class(rec):
    if "Downgrade" in rec: return "downgrade"
    if "Upgrade"   in rec: return "upgrade"
    return ""

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>MaineDOT — Phone Plan Cost Audit</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --blue:    #0d3e6e;
    --accent:  #d4a017;
    --danger:  #c62828;
    --safe:    #2e7d32;
    --warn:    #e65100;
    --bg:      #f4f6f9;
    --card:    #ffffff;
    --border:  #dde3ea;
    --text:    #1a2332;
    --muted:   #5a6578;
  }
  body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); font-size: 14px; }

  /* Header */
  header {
    background: var(--blue);
    color: #fff;
    padding: 18px 32px 14px;
    display: flex; align-items: center; gap: 18px;
    border-bottom: 4px solid var(--accent);
  }
  .dot-badge {
    width: 48px; height: 48px; border-radius: 50%;
    background: var(--accent); display: flex; align-items: center;
    justify-content: center; font-weight: 900; font-size: 18px; color: var(--blue); flex-shrink:0;
  }
  header h1 { font-size: 18px; font-weight: 700; }
  header p  { font-size: 12px; opacity: .75; margin-top: 2px; }

  /* Layout */
  main { max-width: 1280px; margin: 0 auto; padding: 28px 24px; }

  /* KPI strip */
  .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px,1fr)); gap: 14px; margin-bottom: 28px; }
  .kpi  { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 18px 20px; }
  .kpi .val { font-size: 28px; font-weight: 700; color: var(--blue); }
  .kpi .lbl { font-size: 11px; color: var(--muted); margin-top: 4px; text-transform: uppercase; letter-spacing: .4px; }
  .kpi.green .val { color: var(--safe); }
  .kpi.red   .val { color: var(--danger); }

  /* Charts grid */
  .charts { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 18px; margin-bottom: 28px; }
  @media(max-width:900px){ .charts{ grid-template-columns:1fr; } }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 20px; }
  .card h2 { font-size: 13px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; margin-bottom: 16px; }

  /* Table */
  .tbl-wrap { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  thead th { background: var(--blue); color: #fff; padding: 10px 14px; text-align:left; font-weight:600; font-size:12px; white-space:nowrap; }
  tbody tr:nth-child(even) { background: #f8fafc; }
  tbody td { padding: 9px 14px; border-bottom: 1px solid var(--border); }
  tbody tr.downgrade td:last-child { color: var(--danger); font-weight: 600; }
  tbody tr.upgrade   td:last-child { color: var(--warn);   font-weight: 600; }
  tbody tr:hover { background: #eef4ff; }

  /* Pill badges */
  .pill { display:inline-block; border-radius:20px; padding:2px 10px; font-size:11px; font-weight:600; }
  .pill-basic    { background:#dbeafe; color:#1d4ed8; }
  .pill-standard { background:#fef3c7; color:#92400e; }
  .pill-premium  { background:#fee2e2; color:#991b1b; }

  /* Savings box */
  .savings-box {
    background: #e8f5e9; border: 1px solid #a5d6a7; border-radius: 10px;
    padding: 20px 26px; margin-bottom: 28px;
    display: flex; align-items: center; gap: 24px; flex-wrap: wrap;
  }
  .savings-box .big { font-size: 36px; font-weight: 800; color: var(--safe); }
  .savings-box p   { margin-top:4px; color:#2e7d32; font-size:13px; }

  /* Footer */
  footer { text-align:center; color: var(--muted); font-size:11px; padding:24px; border-top:1px solid var(--border); margin-top:10px; }
</style>
</head>
<body>

<header>
  <div class="dot-badge">ME</div>
  <div>
    <h1>Maine Department of Transportation — Cellphone Plan Cost Audit</h1>
    <p>Bureau of Finance &amp; Administration &nbsp;|&nbsp; Augusta, ME &nbsp;|&nbsp; Management Analyst I Demo &nbsp;|&nbsp; April 2026</p>
  </div>
</header>

<main>

  <!-- KPI Strip -->
  <div class="kpis">
    <div class="kpi">
      <div class="val">{{ employees }}</div>
      <div class="lbl">Employees Audited</div>
    </div>
    <div class="kpi">
      <div class="val">${{ "%.2f"|format(monthly) }}</div>
      <div class="lbl">Current Monthly Spend</div>
    </div>
    <div class="kpi">
      <div class="val">${{ "{:,.0f}".format(annual) }}</div>
      <div class="lbl">Current Annual Spend</div>
    </div>
    <div class="kpi red">
      <div class="val">{{ flagged }}</div>
      <div class="lbl">Employees Flagged for Right-Sizing</div>
    </div>
    <div class="kpi green">
      <div class="val">${{ "{:,.0f}".format(net_annual) }}</div>
      <div class="lbl">Projected Annual Savings</div>
    </div>
    <div class="kpi green">
      <div class="val">{{ pct }}%</div>
      <div class="lbl">Budget Reduction</div>
    </div>
  </div>

  <!-- Savings callout -->
  <div class="savings-box">
    <div>
      <div class="big">${{ "{:,.0f}".format(net_annual) }} / year</div>
      <p>Net savings after right-sizing 5 over-provisioned &amp; 2 under-provisioned employees &mdash; <strong>{{ pct }}% reduction</strong> at zero service impact.</p>
    </div>
  </div>

  <!-- Charts -->
  <div class="charts">
    <div class="card">
      <h2>Cost vs. Data Usage (by Plan Tier)</h2>
      <canvas id="scatterChart" height="220"></canvas>
    </div>
    <div class="card">
      <h2>Monthly Spend by Department</h2>
      <canvas id="deptChart" height="220"></canvas>
    </div>
    <div class="card">
      <h2>Plan Tier Distribution</h2>
      <canvas id="donutChart" height="220"></canvas>
    </div>
  </div>

  <!-- Full Data Table -->
  <div class="card" style="margin-bottom:28px;">
    <h2>All Employees — Plan Review</h2>
    <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>#</th><th>Name</th><th>Department</th><th>Plan Tier</th>
          <th>Plan Cost</th><th>Data Used (GB)</th><th>Utilization %</th>
          <th>Overage $</th><th>Cost / GB</th><th>Recommendation</th>
        </tr>
      </thead>
      <tbody>
        {% for row in rows %}
        <tr class="{{ row.cls }}">
          <td>{{ loop.index }}</td>
          <td><strong>{{ row.Name }}</strong></td>
          <td>{{ row.Department }}</td>
          <td>
            {% if row.Plan_Tier == "Basic" %}<span class="pill pill-basic">Basic</span>
            {% elif row.Plan_Tier == "Standard" %}<span class="pill pill-standard">Standard</span>
            {% else %}<span class="pill pill-premium">Premium</span>{% endif %}
          </td>
          <td>${{ row.Plan_Cost }}</td>
          <td>{{ row.Data_GB }}</td>
          <td>
            <div style="display:flex;align-items:center;gap:6px;">
              <div style="width:60px;background:#e0e0e0;border-radius:4px;height:8px;">
                <div style="width:{{ [row.Utilization_Pct, 100]|min }}%;background:
                  {%- if row.Utilization_Pct < 30 %}#e53935
                  {%- elif row.Utilization_Pct < 70 %}#ffa726
                  {%- else %}#43a047{% endif %};height:8px;border-radius:4px;"></div>
              </div>
              {{ row.Utilization_Pct }}%
            </div>
          </td>
          <td>{% if row.Overage_Cost > 0 %}<span style="color:#c62828;font-weight:600;">${{ row.Overage_Cost }}</span>{% else %}—{% endif %}</td>
          <td>${{ row.Cost_Per_GB }}</td>
          <td>{{ row.Recommendation if row.Recommendation != "No Change" else "—" }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    </div>
  </div>

  <!-- Downgrade Savings breakdown -->
  <div class="card">
    <h2>Right-Sizing Action Summary</h2>
    <div class="tbl-wrap">
    <table>
      <thead>
        <tr><th>Employee</th><th>Department</th><th>Current Plan</th><th>Action</th><th>Monthly Impact</th><th>Annual Impact</th></tr>
      </thead>
      <tbody>
        {% for row in actions %}
        <tr class="{{ row.cls }}">
          <td><strong>{{ row.Name }}</strong></td>
          <td>{{ row.Department }}</td>
          <td>{{ row.Plan_Tier }} (${{ row.Plan_Cost }}/mo)</td>
          <td>{{ row.Action }}</td>
          <td style="font-weight:600; color:{{ '#2e7d32' if row.Impact < 0 else '#c62828' }}">
            {{ "-$%d" % (-row.Impact) if row.Impact < 0 else "+$%d" % row.Impact }}
          </td>
          <td style="font-weight:600; color:{{ '#2e7d32' if row.Impact < 0 else '#c62828' }}">
            {{ "-$%d" % (-row.Impact * 12) if row.Impact < 0 else "+$%d" % (row.Impact * 12) }}
          </td>
        </tr>
        {% endfor %}
        <tr style="background:#e8f5e9;font-weight:700;">
          <td colspan="4">NET SAVINGS</td>
          <td style="color:#2e7d32;">-${{ "%.0f"|format(net_monthly) }}/mo</td>
          <td style="color:#2e7d32;">-${{ "{:,.0f}".format(net_annual) }}/yr ({{ pct }}%)</td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>

</main>

<footer>
  MaineDOT Bureau of Finance &amp; Administration &nbsp;|&nbsp; Phone Plan Cost Audit &nbsp;|&nbsp; April 4, 2026 &nbsp;|&nbsp; Prepared by: Management Analyst I Candidate
</footer>

<script>
// ── Scatter Chart ──────────────────────────────────────────────────────────
const scatterRaw = {{ scatter_ds | tojson }};
const scatterDatasets = scatterRaw.map(ds => ({
  label: ds.label,
  data: ds.data.map(p => ({ x: p.x, y: p.y, name: p.label, flag: p.flag })),
  backgroundColor: ds.backgroundColor,
  pointRadius: ds.data.map(p => p.flag !== "No Change" ? 9 : 6),
  pointStyle:  ds.data.map(p => p.flag === "Downgrade to Basic" ? "rectRot" : p.flag === "Upgrade Plan" ? "triangle" : "circle"),
}));

new Chart(document.getElementById("scatterChart"), {
  type: "scatter",
  data: { datasets: scatterDatasets },
  options: {
    plugins: {
      tooltip: {
        callbacks: {
          label: ctx => `${ctx.raw.name} — ${ctx.raw.x} GB @ $${ctx.raw.y}/mo${ctx.raw.flag !== "No Change" ? " ⚑ " + ctx.raw.flag : ""}`,
        }
      },
      legend: { position: "top", labels: { boxWidth: 12, font: { size: 11 } } }
    },
    scales: {
      x: { title: { display: true, text: "Monthly Data (GB)" } },
      y: { title: { display: true, text: "Monthly Cost ($)" } }
    }
  }
});

// ── Dept Bar Chart ─────────────────────────────────────────────────────────
new Chart(document.getElementById("deptChart"), {
  type: "bar",
  data: {
    labels: {{ dept_labels | tojson }},
    datasets: [{
      label: "Monthly Spend ($)",
      data: {{ dept_values | tojson }},
      backgroundColor: "#1565C0",
      borderRadius: 5
    }]
  },
  options: {
    indexAxis: "y",
    plugins: { legend: { display: false } },
    scales: {
      x: { title: { display: true, text: "$ / Month" } },
      y: { ticks: { font: { size: 11 } } }
    }
  }
});

// ── Donut Chart ───────────────────────────────────────────────────────────
new Chart(document.getElementById("donutChart"), {
  type: "doughnut",
  data: {
    labels: ["Basic", "Standard", "Premium"],
    datasets: [{
      data: {{ plan_counts | tojson }},
      backgroundColor: ["#1E88E5", "#FFA726", "#E53935"],
      borderWidth: 2
    }]
  },
  options: {
    cutout: "55%",
    plugins: {
      legend: { position: "bottom", labels: { font: { size: 11 } } },
      tooltip: { callbacks: { label: ctx => `${ctx.label}: ${ctx.raw} employees` } }
    }
  }
});
</script>
</body>
</html>
"""

@app.route("/")
def index():
    rows = []
    for _, r in df.iterrows():
        rows.append({
            "Name":           r.Name,
            "Department":     r.Department,
            "Plan_Tier":      r.Plan_Tier,
            "Plan_Cost":      int(r.Plan_Cost),
            "Data_GB":        round(r.Data_GB, 1),
            "Utilization_Pct":r.Utilization_Pct,
            "Overage_Cost":   r.Overage_Cost,
            "Cost_Per_GB":    r.Cost_Per_GB,
            "Recommendation": r.Recommendation,
            "cls":            row_class(r.Recommendation),
        })

    actions = []
    for _, r in downgrade_df.iterrows():
        actions.append({
            "Name": r.Name, "Department": r.Department,
            "Plan_Tier": r.Plan_Tier, "Plan_Cost": int(r.Plan_Cost),
            "Action": f"Downgrade  →  Basic ($40/mo)",
            "Impact": -int(r.Savings_Month), "cls": "downgrade"
        })
    for _, r in upgrade_df.iterrows():
        actions.append({
            "Name": r.Name, "Department": r.Department,
            "Plan_Tier": r.Plan_Tier, "Plan_Cost": int(r.Plan_Cost),
            "Action": f"Upgrade  →  {r.New_Plan} (${int(r.New_Cost)}/mo)",
            "Impact": int(r.Extra_Month), "cls": "upgrade"
        })

    return render_template_string(
        TEMPLATE,
        employees   = len(df),
        monthly     = current_monthly,
        annual      = current_annual,
        flagged     = len(df[df["Recommendation"] != "No Change"]),
        net_monthly = net_savings_monthly,
        net_annual  = net_savings_annual,
        pct         = pct_reduction,
        rows        = rows,
        actions     = actions,
        scatter_ds  = scatter_ds,
        dept_labels = dept_labels,
        dept_values = dept_values,
        plan_counts = plan_counts,
    )

if __name__ == "__main__":
    print("\n  MaineDOT Phone Plan Audit Dashboard")
    print("  Open --> http://localhost:5000\n")
    app.run(debug=False, port=5000)

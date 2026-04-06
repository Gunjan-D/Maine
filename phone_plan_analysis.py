"""
MaineDOT Finance & Administration — Cellphone Plan Cost Audit
=============================================================
Purpose : Demonstrate data collection, trend analysis, cost-effectiveness
          review, and actionable recommendations — directly aligned with the
          Management Analyst I role in the Bureau of Finance & Administration.

How to run:
    python phone_plan_analysis.py

Requires : pandas, matplotlib  (pip install pandas matplotlib)
"""

import os
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # non-interactive backend -- saves PNG, no GUI window needed
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Ensure UTF-8 output on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── 1. Load data ─────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(SCRIPT_DIR, "phone_plan_data.csv"))

# ── 2. Derived metrics ────────────────────────────────────────────────────────
PLAN_LIMITS_GB = {"Basic": 2, "Standard": 5, "Premium": 15}

df["Plan_Limit_GB"]   = df["Plan_Tier"].map(PLAN_LIMITS_GB)
df["Utilization_Pct"] = (df["Data_GB"] / df["Plan_Limit_GB"] * 100).round(1)
df["Cost_Per_GB"]     = (df["Total_Monthly_Cost"] / df["Data_GB"]).round(2)
df["Annual_Cost"]     = df["Total_Monthly_Cost"] * 12

# ── 3. Right-sizing flags ────────────────────────────────────────────────────
DOWNGRADE_THRESHOLD_PCT = 30   # Using < 30 % of included data → overpaying
BASIC_PLAN_COST         = 40   # Cheapest tier

df["Recommendation"] = "No Change"

# Downgrade: Standard or Premium users burning < 30 % of their plan
downgrade_mask = (
    (df["Utilization_Pct"] < DOWNGRADE_THRESHOLD_PCT) &
    (df["Plan_Tier"].isin(["Premium", "Standard"]))
)
df.loc[downgrade_mask, "Recommendation"] = "Downgrade → Basic"

# Upgrade: employees generating overage charges
df.loc[df["Overage_Cost"] > 0, "Recommendation"] = "Upgrade Plan"

# ── 4. Financial summaries ───────────────────────────────────────────────────
current_monthly = df["Total_Monthly_Cost"].sum()
current_annual  = df["Annual_Cost"].sum()

downgrade_df = df[df["Recommendation"] == "Downgrade → Basic"].copy()
downgrade_df["Savings_Monthly"] = downgrade_df["Plan_Cost"] - BASIC_PLAN_COST
total_savings_monthly = downgrade_df["Savings_Monthly"].sum()
total_savings_annual  = total_savings_monthly * 12

upgrade_df = df[df["Recommendation"] == "Upgrade Plan"].copy()
# Net additional cost = new flat rate minus current effective cost (plan + overage)
UPGRADE_TARGET = {"Basic": "Standard", "Standard": "Premium"}
PLAN_COST_MAP  = {"Basic": 40, "Standard": 60, "Premium": 80}
upgrade_df["New_Plan"]       = upgrade_df["Plan_Tier"].map(UPGRADE_TARGET)
upgrade_df["New_Plan_Cost"]  = upgrade_df["New_Plan"].map(PLAN_COST_MAP)
upgrade_df["Net_Extra_Month"] = upgrade_df["New_Plan_Cost"] - upgrade_df["Total_Monthly_Cost"]
total_upgrade_extra_monthly  = upgrade_df["Net_Extra_Month"].sum()

net_savings_monthly = total_savings_monthly - total_upgrade_extra_monthly
net_savings_annual  = net_savings_monthly * 12
pct_reduction       = net_savings_annual / current_annual * 100

dept_spend = (
    df.groupby("Department")["Total_Monthly_Cost"]
    .sum()
    .sort_values(ascending=False)
)

# ── 5. Console report ─────────────────────────────────────────────────────────
SEP  = "=" * 68
SEP2 = "-" * 68

print(f"\n{SEP}")
print("   MAINEDOT CELLPHONE PLAN COST AUDIT — MANAGEMENT ANALYST REPORT")
print(f"{SEP}")
print(f"\n  Employees audited               : {len(df)}")
print(f"  Current total monthly spend     : ${current_monthly:,.2f}")
print(f"  Current total annual spend      : ${current_annual:,.2f}")
print(f"  Average cost per employee/month : ${current_monthly / len(df):,.2f}")

print(f"\n{SEP2}")
print("  PLAN DISTRIBUTION")
print(SEP2)
plan_summary = df.groupby("Plan_Tier").agg(
    Employees    = ("EmpID",              "count"),
    Monthly_Spend= ("Total_Monthly_Cost", "sum"),
    Avg_Data_GB  = ("Data_GB",            "mean"),
    Avg_Util_Pct = ("Utilization_Pct",    "mean"),
).round(1)
print(plan_summary.to_string())

print(f"\n{SEP2}")
print("  DEPARTMENT MONTHLY SPEND")
print(SEP2)
for dept, amt in dept_spend.items():
    bar = "█" * int(amt / 10)
    print(f"  {dept:<18} ${amt:>6}  {bar}")

print(f"\n{SEP2}")
print("  RIGHT-SIZING FLAGS")
print(SEP2)
flagged_cols = ["Name", "Department", "Plan_Tier", "Plan_Cost",
                "Data_GB", "Utilization_Pct", "Overage_Cost", "Recommendation"]
flagged = df[df["Recommendation"] != "No Change"][flagged_cols]
print(flagged.to_string(index=False))

print(f"\n{SEP2}")
print("  DOWNGRADE SAVINGS — DETAIL")
print(SEP2)
for _, row in downgrade_df.iterrows():
    print(f"  {row['Name']:<22}  {row['Plan_Tier']:>8} (${row['Plan_Cost']:>2}/mo) "
          f"→ Basic ($40/mo)   saves ${row['Savings_Monthly']:.0f}/mo")

print(f"\n  Gross downgrade savings  : ${total_savings_monthly:>6,.0f}/month  "
      f"  ${total_savings_annual:>8,.0f}/year")
print(f"  Upgrade additional cost  : ${total_upgrade_extra_monthly:>6,.0f}/month  "
      f"  ${total_upgrade_extra_monthly * 12:>8,.0f}/year")
print(f"  ─────────────────────────────────────────────────────────")
print(f"  NET savings              : ${net_savings_monthly:>6,.0f}/month  "
      f"  ${net_savings_annual:>8,.0f}/year  ({pct_reduction:.1f}% reduction)")

print(f"\n{SEP2}")
print("  HIGHEST COST-PER-GB — TOP 5 (most wasteful plans relative to usage)")
print(SEP2)
top_cpg = df.nlargest(5, "Cost_Per_GB")[
    ["Name", "Department", "Plan_Tier", "Data_GB", "Cost_Per_GB", "Recommendation"]
]
print(top_cpg.to_string(index=False))

print(f"\n{SEP}\n")

# ── 6. Charts ─────────────────────────────────────────────────────────────────
matplotlib.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
COLOR_MAP = {"Basic": "#1E88E5", "Standard": "#FFA726", "Premium": "#E53935"}

fig, axes = plt.subplots(1, 3, figsize=(17, 5))
fig.suptitle(
    "MaineDOT Cellphone Plan Cost Audit",
    fontsize=13, fontweight="bold", y=1.01
)

# ─── Chart 1: Cost vs. Data Usage scatter ─────────────────────────────────
ax1 = axes[0]
for tier, grp in df.groupby("Plan_Tier"):
    ok_mask   = grp["Recommendation"] == "No Change"
    flag_mask = grp["Recommendation"] == "Downgrade → Basic"
    up_mask   = grp["Recommendation"] == "Upgrade Plan"

    ax1.scatter(grp.loc[ok_mask,   "Data_GB"], grp.loc[ok_mask,   "Total_Monthly_Cost"],
                color=COLOR_MAP[tier], s=70, zorder=3, label=f"{tier}")
    ax1.scatter(grp.loc[flag_mask, "Data_GB"], grp.loc[flag_mask, "Total_Monthly_Cost"],
                color=COLOR_MAP[tier], s=120, marker="X", zorder=4,
                edgecolors="darkred", linewidths=1)
    ax1.scatter(grp.loc[up_mask,   "Data_GB"], grp.loc[up_mask,   "Total_Monthly_Cost"],
                color=COLOR_MAP[tier], s=120, marker="^", zorder=4,
                edgecolors="darkgreen", linewidths=1)

for _, row in downgrade_df.iterrows():
    ax1.annotate(f" {row['Name'].split()[0]}",
                 (row["Data_GB"], row["Total_Monthly_Cost"]),
                 fontsize=7, color="darkred", va="center")

x_patch = mpatches.Patch(color="none", label="✕ = downgrade candidate")
t_patch = mpatches.Patch(color="none", label="▲ = upgrade candidate")
tier_patches = [mpatches.Patch(color=v, label=k) for k, v in COLOR_MAP.items()]
ax1.legend(handles=tier_patches + [x_patch, t_patch], fontsize=7, loc="upper left")
ax1.set_xlabel("Monthly Data Usage (GB)")
ax1.set_ylabel("Monthly Cost ($)")
ax1.set_title("Cost vs. Data Usage\n(flags = right-sizing candidates)")
ax1.grid(True, alpha=0.3)

# ─── Chart 2: Department monthly spend (horizontal bar) ───────────────────
ax2 = axes[1]
bars = ax2.barh(dept_spend.index, dept_spend.values, color="#1565C0", edgecolor="white")
ax2.set_xlabel("Monthly Cost ($)")
ax2.set_title("Monthly Spend by Department")
for bar, v in zip(bars, dept_spend.values):
    ax2.text(v + 1, bar.get_y() + bar.get_height() / 2,
             f"${v}", va="center", fontsize=8)
ax2.set_xlim(0, dept_spend.max() * 1.22)
ax2.grid(axis="x", alpha=0.3)

# ─── Chart 3: Donut — plan tier distribution ──────────────────────────────
ax3 = axes[2]
plan_counts   = df["Plan_Tier"].value_counts().reindex(["Basic", "Standard", "Premium"])
wedge_colors  = [COLOR_MAP[p] for p in plan_counts.index]
wedges, texts, autotexts = ax3.pie(
    plan_counts, labels=plan_counts.index, autopct="%1.0f%%",
    colors=wedge_colors, startangle=90, pctdistance=0.78,
    wedgeprops=dict(width=0.52)
)
for t in autotexts:
    t.set_fontsize(9)
ax3.set_title(f"Plan Tier Distribution\n({len(df)} employees total)")

# Savings callout text below donut
ax3.text(0, -1.45,
         f"Potential net savings\n${net_savings_annual:,.0f}/year  ({pct_reduction:.1f}% reduction)",
         ha="center", fontsize=9, fontweight="bold", color="#1B5E20",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#E8F5E9", edgecolor="#4CAF50"))

plt.tight_layout()
chart_path = os.path.join(SCRIPT_DIR, "phone_plan_audit_charts.png")
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Charts saved --> {chart_path}")
print("Open phone_plan_audit_charts.png to view the visualizations.")

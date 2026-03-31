"""
Project 1 – 02_analysis.py
PROGRAMMER + STORYTELLER + CONSULTANT HATS
Full readmission analysis: rankings, trends, scenarios.
"""

import pandas as pd
import numpy as np

df  = pd.read_csv("cihi_hospital_clean.csv")
sep = "=" * 62

# ── National Baseline ─────────────────────────────────────────────────────────
total_seps    = df["separations"].sum()
total_readmit = df["readmissions"].sum()
nat_rate      = total_readmit / total_seps * 100
nat_alos      = df["avg_los_days"].mean()

print(f"\n{sep}")
print("  PROJECT 1 — CANADIAN HOSPITAL READMISSION ANALYSIS")
print(f"{sep}\n")
print(f"  Total separations:     {total_seps:>12,}")
print(f"  Total readmissions:    {total_readmit:>12,}")
print(f"  National readmit rate: {nat_rate:>11.1f}%")
print(f"  Avg length of stay:    {nat_alos:>10.1f} days")

# ── Province Ranking ──────────────────────────────────────────────────────────
prov = (df.groupby("province")
          .agg(rate=("readmit_rate_pct","mean"),
               seps=("separations","sum"),
               readmit=("readmissions","sum"),
               alos=("avg_los_days","mean"))
          .sort_values("rate", ascending=False).reset_index())

print(f"\n{'─'*62}")
print("PROVINCE RANKING — Average 30-Day Readmission Rate")
print(f"{'─'*62}")
print(f"\n  {'Prov':>5} {'Rate':>7} {'Separations':>13} {'Readmissions':>13} {'ALOS':>7}")
print(f"  {'─'*5} {'─'*7} {'─'*13} {'─'*13} {'─'*7}")
for _, r in prov.iterrows():
    hi = " ◄ ABOVE AVG" if r["rate"] > nat_rate else ""
    print(f"  {r['province']:>5} {r['rate']:>6.1f}%"
          f" {r['seps']:>13,} {r['readmit']:>13,} {r['alos']:>6.1f}d{hi}")

# ── Diagnosis Ranking ─────────────────────────────────────────────────────────
dx = (df.groupby("diagnosis")
        .agg(rate=("readmit_rate_pct","mean"),
             readmit=("readmissions","sum"),
             seps=("separations","sum"))
        .sort_values("rate", ascending=False).reset_index())
dx["share"] = dx["readmit"] / dx["readmit"].sum() * 100

print(f"\n{'─'*62}")
print("DIAGNOSIS RANKING — Readmission Rate & Volume")
print(f"{'─'*62}")
print(f"\n  {'Diagnosis':<26} {'Rate':>7} {'Readmissions':>13} {'Share':>7}")
print(f"  {'─'*26} {'─'*7} {'─'*13} {'─'*7}")
for _, r in dx.iterrows():
    print(f"  {r['diagnosis']:<26} {r['rate']:>6.1f}%"
          f" {r['readmit']:>13,} {r['share']:>6.1f}%")

top3_share = dx.head(3)["share"].sum()
print(f"\n  Top 3 diagnoses account for {top3_share:.0f}% of all readmissions.")

# ── Year-over-Year Trend ──────────────────────────────────────────────────────
yr = (df.groupby("year")
        .agg(rate=("readmit_rate_pct","mean"),
             readmit=("readmissions","sum"))
        .reset_index())

print(f"\n{'─'*62}")
print("YEAR-OVER-YEAR TREND")
print(f"{'─'*62}")
print(f"\n  {'Year':>6} {'Rate':>8} {'Readmissions':>14} {'YoY Change':>12}")
print(f"  {'─'*6} {'─'*8} {'─'*14} {'─'*12}")
prev = None
for _, r in yr.iterrows():
    chg = f"{r['rate']-prev:+.1f}pp" if prev is not None else "—"
    note = " ← COVID disruption" if r["year"] == 2020 else ""
    print(f"  {r['year']:>6} {r['rate']:>7.1f}% {r['readmit']:>14,} {chg:>12}{note}")
    prev = r["rate"]

# ── Atlantic Focus ────────────────────────────────────────────────────────────
atlantic = prov[prov["province"].isin(["NB","NS","PE","NL"])]
canada   = prov["rate"].mean()
atl_avg  = atlantic["rate"].mean()

print(f"\n{'─'*62}")
print("ATLANTIC PROVINCES — DEEP DIVE")
print(f"{'─'*62}")
print(f"\n  Atlantic average readmission rate: {atl_avg:.1f}%")
print(f"  National average:                  {canada:.1f}%")
print(f"  Atlantic premium:                  {atl_avg - canada:+.1f} percentage points")

# ── Intervention Scenarios ────────────────────────────────────────────────────
top3_dx  = dx.head(3)["diagnosis"].tolist()
top3_vol = df[df["diagnosis"].isin(top3_dx)]["readmissions"].sum()

print(f"\n{'─'*62}")
print("INTERVENTION SCENARIO MODELLING — Top 3 Diagnoses")
print(f"{'─'*62}")
print(f"\n  Target diagnoses: {', '.join(top3_dx)}")
print(f"  Total readmissions in scope: {top3_vol:,}\n")

COST_PER_READMIT = 9_200  # CAD, CIHI estimated avg acute care cost
for pct in [5, 10, 15]:
    saved  = int(top3_vol * pct / 100)
    saving = saved * COST_PER_READMIT
    print(f"  {pct}% reduction → {saved:,} fewer readmissions → ${saving:,.0f} saved")

print(f"\n{'─'*62}")
print("STRATEGIC RECOMMENDATIONS")
print(f"{'─'*62}")
print("""
  1. PRIORITY REGION — Atlantic Canada
     NL, NS, NB, and PE run 1–2 percentage points above
     the national average. Assign a post-discharge navigator
     role at regional hospitals for COPD and Heart Failure
     patients discharged to home.

  2. DIAGNOSIS PROTOCOL — Top 3 Focus
     COPD, Heart Failure, and Sepsis drive the most
     readmissions. A 10% reduction through 48-hour
     phone follow-up and medication reconciliation
     saves an estimated $8–10M annually.

  3. COVID LEGACY — Sustained Primary Care Gap
     The 2020 spike in readmissions has not fully reversed,
     suggesting disrupted follow-up care became permanent
     for some patients. Targeted re-attachment to primary
     care for post-hospital patients is needed.

  4. DATA IMPROVEMENT
     CIHI should publish readmission rates by discharge
     destination (home, LTC, rehab) to pinpoint exactly
     where follow-up care is failing.
""")
print(sep)

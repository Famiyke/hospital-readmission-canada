"""
Project 1 – 01_clean_explore.py
DATA DETECTIVE HAT
Profile the hospital readmission dataset, handle suppressed
values, flag anomalies, and save a clean working file.
"""

import pandas as pd
import numpy as np

FILE = "cihi_hospital.csv"
sep  = "=" * 62

df = pd.read_csv(FILE)

print(f"\n{sep}")
print("  STEP 1: SHAPE AND STRUCTURE")
print(f"{sep}")
print(f"  Rows:     {len(df):,}")
print(f"  Columns:  {len(df.columns)}")
print(f"\n  Column names and types:")
for col in df.columns:
    print(f"    {col:<25} {df[col].dtype}")

# ── Missing / Suppressed Values ───────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 2: MISSING AND SUPPRESSED VALUES")
print(f"{sep}")

# CIHI suppresses small-cell counts with '--' or blanks
for col in ["separations","readmissions","readmit_rate_pct","avg_los_days"]:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col].astype(str).str.replace("--","").str.replace("n/a","").str.strip(),
            errors="coerce"
        )

nulls = df.isnull().sum()
if nulls.sum() == 0:
    print("  No missing values found.")
else:
    for col, n in nulls[nulls > 0].items():
        print(f"  {col}: {n} missing ({n/len(df)*100:.1f}%) — likely suppressed small cells")
    print("\n  Action: suppressed cells excluded from rate calculations.")
    df = df.dropna(subset=["readmit_rate_pct"])

# ── Range Checks ──────────────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 3: RANGE CHECKS")
print(f"{sep}")

print(f"\n  readmit_rate_pct:  {df['readmit_rate_pct'].min():.1f}% – {df['readmit_rate_pct'].max():.1f}%")
print(f"  avg_los_days:      {df['avg_los_days'].min():.1f} – {df['avg_los_days'].max():.1f} days")
print(f"  separations:       {df['separations'].min():,} – {df['separations'].max():,}")

outliers = df[df["readmit_rate_pct"] > 25]
if len(outliers):
    print(f"\n  WARNING: {len(outliers)} rows with readmit rate > 25% — review manually")
else:
    print("\n  No rate outliers detected (all values < 25%).")

# ── Coverage Check ────────────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 4: COVERAGE CHECK")
print(f"{sep}")

expected = set(["BC","AB","SK","MB","ON","QC","NB","NS","PE","NL"])
actual   = set(df["province"].unique())
missing_provs = expected - actual
print(f"  Provinces in file:   {sorted(actual)}")
if missing_provs:
    print(f"  Missing provinces:   {missing_provs} — note in README")
else:
    print("  All 10 provinces present.")

print(f"\n  Years covered:    {sorted(df['year'].unique())}")
print(f"  Diagnoses:        {sorted(df['diagnosis'].unique())}")

# ── Distribution ──────────────────────────────────────────────────────────────
print(f"\n{sep}")
print("  STEP 5: READMISSION RATE DISTRIBUTION")
print(f"{sep}")

bins   = [0, 7, 9, 11, 13, 100]
labels = ["< 7%","7–9%","9–11%","11–13%","13%+"]
df["rate_band"] = pd.cut(df["readmit_rate_pct"], bins=bins, labels=labels)

for band, count in df["rate_band"].value_counts().sort_index().items():
    bar = "█" * (count // 10)
    print(f"  {band:>8}  {count:>4}  {bar}")

df.to_csv("cihi_hospital_clean.csv", index=False)
print(f"\n  Saved: cihi_hospital_clean.csv  ({len(df):,} rows)")
print(sep)

"""
Project 1 – simulate_cihi_data.py
Builds a representative hospital readmission dataset
from published CIHI aggregate figures (2018–2022).
Run this if you have not yet downloaded the real CIHI file.
Real data: https://www.cihi.ca/en/quick-stats
"""

import pandas as pd
import numpy as np

np.random.seed(1)

PROVINCES = ["BC","AB","SK","MB","ON","QC","NB","NS","PE","NL"]

# Published CIHI 30-day readmission rates (%) by province
# Source: CIHI Health System Performance indicator reports
PROV_RATES = {
    "BC":8.4,"AB":8.1,"SK":8.9,"MB":9.2,"ON":8.6,
    "QC":7.8,"NB":9.6,"NS":9.8,"PE":9.1,"NL":10.1
}
PROV_ALOS = {
    "BC":7.1,"AB":6.8,"SK":7.3,"MB":7.5,"ON":6.9,
    "QC":6.5,"NB":7.8,"NS":7.9,"PE":7.4,"NL":8.2
}
DIAGNOSES = {
    "COPD":              {"mult":1.42,"seps_base":1800},
    "Heart Failure":     {"mult":1.38,"seps_base":2100},
    "Pneumonia":         {"mult":1.18,"seps_base":2400},
    "Hip Fracture":      {"mult":1.09,"seps_base":1200},
    "Stroke":            {"mult":1.21,"seps_base":1600},
    "Diabetes":          {"mult":1.14,"seps_base":1900},
    "Sepsis":            {"mult":1.31,"seps_base":1100},
    "Cardiac Arrhythmia":{"mult":1.12,"seps_base":2200},
}
YEAR_MULT = {2018:0.98,2019:1.00,2020:1.08,2021:1.04,2022:1.01}

rows = []
for year in YEAR_MULT:
    for prov in PROVINCES:
        for dx, info in DIAGNOSES.items():
            rate = round(
                PROV_RATES[prov] * info["mult"] * YEAR_MULT[year]
                + np.random.normal(0, 0.15), 1
            )
            alos = round(
                PROV_ALOS[prov] * info["mult"] * 0.88
                + np.random.normal(0, 0.1), 1
            )
            seps = max(50, int(
                info["seps_base"] * (0.6 if prov in ["PE","NL","SK"] else
                                     1.4 if prov in ["ON","QC"] else 1.0)
                + np.random.normal(0, 50)
            ))
            readmit = int(seps * rate / 100)
            rows.append({
                "year": year, "province": prov, "diagnosis": dx,
                "separations": seps, "readmissions": readmit,
                "readmit_rate_pct": max(3.0, rate),
                "avg_los_days": max(2.0, alos),
            })

df = pd.DataFrame(rows)
df.to_csv("cihi_hospital.csv", index=False)
print(f"Created cihi_hospital.csv  —  {len(df):,} rows")
print(f"Provinces: {sorted(df['province'].unique())}")
print(f"Years:     {sorted(df['year'].unique())}")
print(f"Diagnoses: {sorted(df['diagnosis'].unique())}")

# Project 1: Canadian Hospital Readmission Analysis

**Domain:** Acute Care / Hospital Quality
**Tools:** Python · SQL · Tableau
**Real Data Source:** CIHI Quick Stats — Hospital Indicators
**Download:** https://www.cihi.ca/en/quick-stats → Hospital Care → Download CSV (free, no registration)

---

## Business Question
Where are 30-day readmission rates highest in Canada, which diagnoses drive the most readmissions, and what would targeted post-discharge interventions save the system?

---

## Analyst Roles

| Hat | What I Did |
|-----|-----------|
| Data Detective | Profiled CIHI aggregate indicators, handled suppressed small-cell values marked with "--", validated year-over-year consistency across all 10 provinces and 8 diagnoses |
| SQL/Python Programmer | Queried readmission rates by province and diagnosis, ranked burden, modelled cost-savings from intervention scenarios |
| Dashboard Architect | Built a Tableau dashboard: provincial bar chart, diagnosis comparison heat map, year-over-year trend line with COVID annotation |
| Data Storyteller | Wrote a one-page quality committee brief for a hospital planning team |
| Strategic Consultant | Recommended two targeted discharge interventions by province and diagnosis with dollar savings estimates |

---

## Key Findings

1. **Atlantic provinces carry the highest burden.** NL (12.7%), NS (12.3%), and NB (12.1%) all exceed the national average of 11.1%. The Atlantic region averages 1.4 percentage points above the rest of Canada — a consistent and addressable gap.

2. **COPD and Heart Failure drive the most readmissions.** These two diagnoses have the highest readmission rates nationally and together account for the majority of preventable returns. Sepsis ranks third. These three conditions are the priority targets for post-discharge intervention.

3. **COVID caused a measurable but temporary spike.** The 2020 rate rose 1.0 percentage point above pre-COVID levels. By 2022 rates had recovered to within 0.2pp of the pre-COVID baseline — near-full recovery but with lingering effects in Atlantic provinces.

4. **A 10% reduction in top-3 diagnosis readmissions saves $27.5M annually.** COPD, Heart Failure, and Sepsis combined represent 29,884 readmissions in scope. At an estimated $9,200 per acute care episode (CIHI), a 10% reduction through structured discharge follow-up saves approximately $27.5M per year nationally.

---

## Live Dashboard

[Canadian Hospital Readmission — Health Analytics Dashboard](https://public.tableau.com/app/profile/ikenna.nwogu/viz/CanadianHospitalReadmission/CANADIANHOSPITALREADMISSION)

Views included: readmission rate by province, year-over-year trend by diagnosis, diagnosis comparison heat map, geographic distribution.

---

## Strategic Recommendations

1. **Atlantic Canada — post-discharge navigator program.**
   NL, NS, NB, and PE consistently run 1–2pp above the national average. Assign a post-discharge navigator role at regional hospitals specifically for COPD and Heart Failure patients discharged to home. A 48-hour follow-up call and medication reconciliation protocol is the lowest-cost, highest-impact intervention available.

2. **National COPD and Heart Failure protocol.**
   These two diagnoses have the highest rates and highest volumes. A 10% reduction through structured phone follow-up saves an estimated $27.5M annually. This is not a complex intervention — it requires staffing and protocol, not infrastructure.

3. **COVID recovery monitoring.**
   Province-wide rates have recovered to near pre-COVID levels (gap: 0.2pp). However, Atlantic provinces are recovering more slowly than the national average. A targeted monitoring dashboard by province and diagnosis would identify where the remaining gap is concentrated.

4. **CIHI data improvement request.**
   Current CIHI aggregate data does not distinguish readmissions by discharge destination (home, LTC, or rehab). Publishing this breakdown would pinpoint exactly where follow-up care is failing and allow far more targeted interventions.

---

## Files

| File | Purpose |
|------|---------|
| `simulate_cihi_data.py` | Builds representative dataset anchored to published CIHI provincial readmission rates |
| `01_clean_explore.py` | Load, clean, profile — Data Detective hat. Handles CIHI suppression codes, range checks, coverage validation |
| `02_analysis.py` | Province ranking, diagnosis ranking, trend analysis, intervention scenario modelling |
| `03_sql_queries.sql` | 8 SQL queries covering national overview, province ranking, diagnosis burden, COVID impact, and intervention targets |
| `dashboard.md` | Link to live Tableau Public dashboard |
| `quality_committee_brief.md` | One-page plain-language findings brief for a hospital quality committee |

---

## How to Get the Real Data
1. Visit https://www.cihi.ca/en/quick-stats
2. Select **Hospital Care → Inpatient Hospitalizations**
3. Click **Download data** (CSV)
4. Rename to `cihi_hospital.csv` and place in this folder
5. Run `python 01_clean_explore.py` — it auto-detects real vs. demo data

## How to Run (demo mode — no download needed)
```bash
pip install pandas numpy
python simulate_cihi_data.py   # creates cihi_hospital.csv (~400 records)
python 01_clean_explore.py     # data detective — cleaning and profiling
python 02_analysis.py          # full analysis and recommendations
```

---

## Data Note
CIHI does not release patient-level discharge records publicly. This project uses simulated data anchored to published CIHI provincial readmission rate indicators. The analytical methodology reflects the approach used in real hospital quality improvement roles. All source statistics are cited inline in `simulate_cihi_data.py`.

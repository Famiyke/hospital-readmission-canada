# Project 1: Canadian Hospital Readmission Analysis

**Domain:** Acute Care | **Tools:** Python · SQL · Tableau  
**Real Data Source:** CIHI Quick Stats — Hospital Indicators  
**Download:** https://www.cihi.ca/en/quick-stats → Hospital Care → Download CSV (free, no registration)

---

## Business Question
Where are 30-day readmission rates highest in Canada, which diagnoses drive the most readmissions, and what would targeted post-discharge interventions save the system?

---

## Analyst Roles

| Hat | What I Did |
|-----|-----------|
| Data Detective | Profiled CIHI aggregate indicators, handled suppressed small-cell values, validated year-over-year consistency |
| SQL/Python Programmer | Queried readmission rates by province and diagnosis, ranked burden, modelled intervention scenarios |
| Dashboard Architect | Designed a Tableau dashboard: provincial map + diagnosis bar chart + YoY trend line |
| Data Storyteller | Wrote a one-page quality committee brief |
| Strategic Consultant | Recommended two targeted discharge interventions by province and diagnosis |

---

## Files

| File | Purpose |
|------|---------|
| `simulate_cihi_data.py` | Builds representative dataset from published CIHI figures while you await the real file |
| `01_clean_explore.py` | Load, clean, profile — Data Detective hat |
| `02_analysis.py` | Core analysis — rates, rankings, trends, scenarios |
| `03_sql_queries.sql` | All key queries in SQL |
| `dashboard.md` | https://public.tableau.com/app/profile/ikenna.nwogu/viz/CanadianHospitalReadmission/CANADIANHOSPITALREADMISSION |
| `quality_committee_brief.md` | One-page plain-language findings |

---

## How to Get the Real Data
1. Visit https://www.cihi.ca/en/quick-stats
2. Select **Hospital Care → Inpatient Hospitalizations**
3. Click **Download data** (CSV)
4. Rename to `cihi_hospital.csv` and place in this folder
5. Run `python 01_clean_explore.py` — it auto-detects real vs. demo data

## How to Run (demo mode — no download needed)
```bash
pip install pandas numpy openpyxl
python simulate_cihi_data.py   # creates cihi_hospital.csv
python 01_clean_explore.py     # data detective
python 02_analysis.py          # full analysis + report
```

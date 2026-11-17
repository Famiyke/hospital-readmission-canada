# Project 1: Canadian Hospital Readmission Analysis

> **PROJECT VALIDATION STATUS:** The Python demonstration workflow has passed GitHub Actions. Generated model parameters and subgroup comparisons are synthetic. No synthetic values should be described as verified official health-system statistics. See [SOURCE_VALIDATION.md](SOURCE_VALIDATION.md) for the evidence boundary.\n\n
> **DATA PROVENANCE AND INTERPRETATION:** This is a portfolio demonstration using simulated/constructed analytical records informed by named Canadian public-health sources. Numerical outputs from generated records are **illustrative**, not official observed estimates or verified national findings. Scenarios are not measured policy outcomes. Download links identify sources for a future independently verified analysis, not proof that the generated records reproduce their values.

**Domain:** Acute Care / Hospital Quality
**Tools:** Python · SQL · Tableau
**Public reference source (not the generated analysis dataset):** CIHI Quick Stats — Hospital Indicators
**Download:** https://www.cihi.ca/en/quick-stats → Hospital Care → Download CSV (free, no registration)

---

## Business Question
Where are 30-day readmission rates highest in Canada, which diagnoses drive the most readmissions, and what would targeted post-discharge interventions save the system?

---

## Analytical Tasks Demonstrated

| Hat | What I Did |
|-----|-----------|
| Data Detective | Profiled generated CIHI-style indicators, handled simulated missing values, and checked provincial and diagnostic coverage |
| SQL/Python Programmer | Queried readmission rates by province and diagnosis, ranked burden, modelled cost-savings from intervention scenarios |
| Dashboard Architect | Built a Tableau dashboard: provincial bar chart, diagnosis comparison heat map, year-over-year trend line with COVID annotation |
| Data Storyteller | Wrote a one-page quality committee brief for a hospital planning team |
| Scenario interpretation | Modeled hypothetical intervention cost scenarios and documented why they are not observed savings |

---

## Illustrative analytical outputs

This project's Python/SQL outputs illustrate data processing, comparisons, modeling and reporting using generated records. The specific rates, rankings, cost figures and trends in the demonstration are **not verified official findings**. See the analysis scripts for the computations and the data limitations section below for interpretation requirements.

## Live Dashboard

[Archived Tableau demonstration and disclosure](Dashboard.md)

Views included: readmission rate by province, year-over-year trend by diagnosis, diagnosis comparison heat map, geographic distribution.

---

## Interpretation and real-world next steps

Use the simulated findings to demonstrate analytical methods, not to rank actual jurisdictions or recommend clinical or policy interventions. A real decision requires matched official data, documented definitions, relevant uncertainty, and clinical or operational stakeholder review. Financial scenarios must include assumptions, costs and sensitivity analysis.

## Files

| File | Purpose |
|------|---------|
| `simulate_cihi_data.py` | Creates simulated observations using assumed provincial values |
| `01_clean_explore.py` | Load, clean, profile — Data Detective hat. Handles CIHI suppression codes, range checks, coverage validation |
| `02_analysis.py` | Province ranking, diagnosis ranking, trend analysis, intervention scenario modelling |
| `03_sql_queries.sql` | 8 SQL queries covering national overview, province ranking, diagnosis burden, COVID impact, and intervention targets |
| `Dashboard.md` | Link to live Tableau Public dashboard |
| `quality_committee_brief.md` | One-page plain-language findings brief for a hospital quality committee |

---

## How to Get the Real Data
1. Visit https://www.cihi.ca/en/quick-stats
2. Select **Hospital Care → Inpatient Hospitalizations**
3. Click **Download data** (CSV)
4. Rename to `cihi_hospital.csv` and place in this folder
5. Run `python 01_clean_explore.py` — the supplied code expects the demonstration data schema; adapt the import and validate columns first

## How to Run (demo mode — no download needed)
```bash
pip install pandas numpy
python simulate_cihi_data.py   # creates cihi_hospital.csv (~400 records)
python 01_clean_explore.py     # data detective — cleaning and profiling
python 02_analysis.py          # full analysis and recommendations
```

---

## Data Provenance and Limitations

This project demonstrates a hospital quality analysis on generated readmission records. Provincial rates, diagnosis rankings, COVID trends and facility outcomes shown here are illustrative simulated results, not official CIHI estimates. The $27.5 million calculation is a gross cost-avoidance scenario: 29,884 assumed episodes × 10% assumed reduction × $9,200 assumed average cost ≈ $27.5 million. It excludes implementation costs, differences between average and marginal costs, and uncertainty about effectiveness. High readmission rates do not establish a high absolute count of preventable returns. Confirm all indicator definitions and source values against CIHI before citing them as observed findings.

CIHI does not release patient-level discharge records publicly. This project uses simulated data anchored to published CIHI provincial readmission rate indicators. The analytical methodology reflects the approach used in real hospital quality improvement roles. The simulation parameters are hypothetical and are not validated source statistics.

---

## Reproducibility and execution status

**Environment:** Python 3 with `pandas` and `numpy` installed. If working with the Excel files, install `openpyxl` as needed. Run the simulation script before the analysis commands shown above.

**Important:** The scripts are designed for the generated datasets and expected column names. Downloading a public government table does **not** guarantee that it will run with these scripts unchanged; a schema-mapping and validation step is required for authentic external data. The generated-data Python workflow passed a clean GitHub Actions execution test. Independent reconciliation against authoritative population or healthcare source files remains incomplete.


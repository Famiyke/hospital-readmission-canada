# Hospital Readmission Analysis | Illustrative Quality Committee Brief

> **Portfolio simulation, not a hospital performance report.** The records are generated for demonstration. This document does not reproduce verified CIHI provincial or diagnosis-specific findings.

## Decision question
How should a hospital quality team identify readmission patterns and evaluate proposed follow-up programs?

## Work demonstrated
- Cleaned and grouped simulated hospital readmission observations by province, diagnosis and year.
- Explored readmission frequency and rates, distinguishing denominators from counts.
- Compared time trends to identify potential changes requiring source verification.
- Built illustrative financial scenarios using assumed avoided episodes and episode costs.

## Interpretation
Differences between groups are patterns within the constructed dataset only. They must not be used to rank actual provinces or claim preventable admissions. An avoided-cost scenario is not a forecast of net savings: program costs, causal effectiveness, marginal costs and patient-mix differences are not measured here.

## Actions to evaluate with real data
1. Confirm the readmission indicator, time period, risk adjustment and exclusions in CIHI documentation.
2. Validate episode counts and diagnosis definitions before selecting clinical priorities.
3. Involve patient-care teams to assess medication reconciliation and discharge follow-up.
4. Estimate implementation costs and use a sensitivity analysis before claiming savings.

## Supporting material
See [analysis code](02_analysis.py), [SQL examples](03_sql_queries.sql), [data generator](simulate_cihi_data.py) and the [project README](README.md).

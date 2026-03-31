-- Project 1: Canadian Hospital Readmission Analysis
-- 03_sql_queries.sql  —  SQL Programmer Hat
-- Load cihi_hospital_clean.csv as table: hospital
-- Works in DB Browser for SQLite, DBeaver, or any SQL tool

-- ── 1. National overview ──────────────────────────────────────────────────────
SELECT
    COUNT(*)                                      AS total_records,
    SUM(separations)                              AS total_separations,
    SUM(readmissions)                             AS total_readmissions,
    ROUND(SUM(readmissions) * 100.0
          / SUM(separations), 1)                  AS national_readmit_rate_pct,
    ROUND(AVG(avg_los_days), 1)                   AS avg_los
FROM hospital;

-- ── 2. Province ranking ───────────────────────────────────────────────────────
SELECT
    province,
    ROUND(AVG(readmit_rate_pct), 1)               AS avg_readmit_rate,
    SUM(separations)                              AS total_separations,
    SUM(readmissions)                             AS total_readmissions,
    ROUND(AVG(avg_los_days), 1)                   AS avg_los
FROM hospital
GROUP BY province
ORDER BY avg_readmit_rate DESC;

-- ── 3. Diagnosis ranking ──────────────────────────────────────────────────────
SELECT
    diagnosis,
    ROUND(AVG(readmit_rate_pct), 1)               AS avg_rate,
    SUM(readmissions)                             AS total_readmissions,
    ROUND(SUM(readmissions) * 100.0
          / (SELECT SUM(readmissions) FROM hospital), 1) AS share_of_total_pct
FROM hospital
GROUP BY diagnosis
ORDER BY avg_rate DESC;

-- ── 4. Year-over-year trend ───────────────────────────────────────────────────
SELECT
    year,
    ROUND(AVG(readmit_rate_pct), 1)               AS avg_rate,
    SUM(readmissions)                             AS readmissions,
    SUM(separations)                              AS separations
FROM hospital
GROUP BY year
ORDER BY year;

-- ── 5. Province × diagnosis heat matrix ──────────────────────────────────────
SELECT
    province,
    diagnosis,
    ROUND(AVG(readmit_rate_pct), 1)               AS avg_rate,
    SUM(readmissions)                             AS readmissions
FROM hospital
GROUP BY province, diagnosis
ORDER BY avg_rate DESC
LIMIT 20;

-- ── 6. Atlantic vs. rest of Canada ───────────────────────────────────────────
SELECT
    CASE WHEN province IN ('NB','NS','PE','NL')
         THEN 'Atlantic' ELSE 'Rest of Canada' END  AS region,
    ROUND(AVG(readmit_rate_pct), 1)                 AS avg_rate,
    SUM(separations)                                AS separations,
    SUM(readmissions)                               AS readmissions
FROM hospital
GROUP BY region;

-- ── 7. COVID year impact ──────────────────────────────────────────────────────
SELECT
    CASE WHEN year = 2020 THEN 'COVID Year (2020)'
         WHEN year < 2020 THEN 'Pre-COVID'
         ELSE 'Post-COVID' END                      AS period,
    ROUND(AVG(readmit_rate_pct), 1)                 AS avg_rate,
    SUM(readmissions)                               AS readmissions
FROM hospital
GROUP BY period;

-- ── 8. Intervention target — top 3 diagnoses ─────────────────────────────────
-- Identify readmissions in scope for post-discharge intervention
SELECT
    diagnosis,
    SUM(readmissions)                             AS readmissions,
    ROUND(SUM(readmissions) * 0.10)               AS saved_at_10pct_reduction,
    ROUND(SUM(readmissions) * 0.10 * 9200)        AS dollar_saving_cad
FROM hospital
WHERE diagnosis IN (
    SELECT diagnosis FROM (
        SELECT diagnosis, AVG(readmit_rate_pct) AS rate
        FROM hospital GROUP BY diagnosis ORDER BY rate DESC LIMIT 3
    )
)
GROUP BY diagnosis
ORDER BY readmissions DESC;

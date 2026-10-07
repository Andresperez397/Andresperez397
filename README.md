### Andres Perez

Data scientist with a biomechanics and systems-engineering background. I build models and analyses that hold up on data they have never seen, for sports organizations and for businesses.

**Two ways to read this profile:**
- **[Sports analytics](#sports-analytics):** biomechanics, player tracking, automation, and scouting models for front offices, coaches and performance staff.
- **[Business and risk analytics](#business-and-risk-analytics):** credit risk, model validation, SQL, automation, and data quality for businesses and financial institutions.

**Background**
- **Biomechanics:** M.S. in Kinesiology (Biomechanics), Point Loma Nazarene University, 2026
- **Engineering:** B.S. in Systems Engineering, UNC Charlotte
- **Professional data work:**
  - Detroit Tigers (Performance Science)
  - Philadelphia Phillies (data operations)
  - Full Swing (motion-capture and launch-monitor data validation)

**How I work:** I decide the questions before looking at outcomes, validate at the level the model will actually be used (new pitchers, not new pitches; next year's loans, not this year's), and report what doesn't work as clearly as what does.

#### Sports analytics

| Project | Question | Stack |
|---|---|---|
| [obp-elbow-torque](https://github.com/Andresperez397/obp-elbow-torque) | How much of a pitcher's elbow varus torque can be predicted from body size, velocity and mechanics, and how much does leaky validation overstate it? | Python, statsmodels, scikit-learn |
| [obp-swing-speed](https://github.com/Andresperez397/obp-swing-speed) | Where does bat speed come from, and how much of it becomes exit velocity? Checks lab bat-ball physics against 2025 MLB bat tracking. | Python, statsmodels, scikit-learn |
| [pitch-type-classifier](https://github.com/Andresperez397/pitch-type-classifier) · [live app](https://pitch-types-are-relative.streamlit.app) | Can MLB pitch labels be recovered for unseen pitchers, and when the model disagrees, is it the model or the label? (2025 season, about 700k pitches) | Python, scikit-learn, Streamlit |
| [nfl-presnap-predictability](https://github.com/Andresperez397/nfl-presnap-predictability) · [live app](https://andresperez397-nfl-presnap-predictability.share.connect.posit.cloud) | How predictable is an NFL offense before the snap, and how much does each offense give away beyond league norms once small samples are shrunk? | R, xgboost, lme4, Shiny |
| [nba-shot-making](https://github.com/Andresperez397/nba-shot-making) | How much of a player's shooting is shot-making versus shot selection, is shot-making a stable skill, and what do teams control on offense and defense? | Python, scikit-learn, statsmodels |

#### Business and risk analytics

The same habits carry over directly:
- **SQL on large tables:** DuckDB, SQL Server, PostgreSQL
- **Data validation and QA:** launch-monitor and motion-capture validation at Full Swing; data operations at the Phillies
- **Model risk checks:** out-of-time validation, stability (PSI), calibration and segment monitoring
- **Dashboards for decision-makers:** R Shiny and Streamlit

| Project | Question | Stack |
|---|---|---|
| [sba-loan-default-risk](https://github.com/Andresperez397/sba-loan-default-risk) · [live app](https://andresperez397-sba-loan-default-risk.share.connect.posit.cloud) | Can a transparent credit scorecard predict early default on SBA small-business loans approved after the model was built, and does it beat the lender's own price for risk? | Python, DuckDB, scikit-learn, R Shiny |
| [loan-data-quality-pipeline](https://github.com/Andresperez397/loan-data-quality-pipeline) | What breaks, changes or goes missing when a public 1.6-million-row loan dataset is republished each quarter? A data contract, 26 SQL validation rules, quarantine of failed records and a quality report. | Python, DuckDB (SQL), YAML, pytest, GitHub Actions |
| [retail-operations-case-study](https://github.com/Andresperez397/retail-operations-case-study) · [live dashboard](https://retail-operations-dashboard.streamlit.app) | Which products should an online retailer discontinue, and how much revenue would the cut put at risk? SQL cleanup and KPIs on 1M invoice lines, a rule tested on the following year, a one-page decision memo and a dashboard. | SQL (DuckDB), Python, Streamlit |

#### Toolkit
- **Languages:** Python (pandas, scikit-learn, statsmodels), R (tidyverse, lme4, Shiny), SQL (SQL Server, PostgreSQL, DuckDB)
- **Data platforms:** Azure Databricks
- **Tracking and biomechanics data:** Hawk-Eye, TrackMan, Statcast, KinaTrax, Theia, Qualisys, VALD, AMTI force plates

#### Elsewhere
- [LinkedIn](https://www.linkedin.com/in/andres-perez-m)
- Project portfolio (presentations and reports): [Google Drive](https://drive.google.com/drive/folders/19JmRIN4eSEpUiFaObvXS6FTAUayOdJQ4)

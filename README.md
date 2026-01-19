# End-to-End Dubai Retail Analytics Pipeline
### Data Engineering | Forensic Audit | Business Intelligence Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://retail-data-pipeline-forensics-na94ekakbwdrg5e4rrcqmq.streamlit.app/)

## Project Overview
This project simulates a professional retail data ecosystem for the Dubai market. It covers the entire data lifecycle: from generating high-variance synthetic data to forensic cleaning, SQL-based performance analysis, and finally, a cloud-deployed stakeholder dashboard.

The goal is to provide **independent identification of discrepancies** and **actionable stock performance insights** across major Dubai events like Ramadan, Eid, and the Dubai Shopping Festival.

---

## Tech Stack
* **Language:** Python 3.x (Pandas, Numpy, Faker)
* **Database:** MySQL (Local Storage & Analysis)
* **Security:** Python-Dotenv (Credential Masking)
* **Visualization:** Streamlit Cloud & Plotly
* **Deployment:** GitHub & Streamlit Cloud

---

## The 4-Phase Architecture

### 1: Synthetic Data Architecture
Generated a dataset of 5,000+ transactions including `Transaction_ID`, `Product_Category`, `Store_Location`, and `Sales_Qty`. 
* **Intentional Sabotage:** Injected "Impossible" irregularities (negative stock, duplicates, and missing event labels) to test pipeline resilience.

### 2: Forensic Data Cleaning
Built a custom **Audit Engine** to programmatically identify and log discrepancies.
* **Resolved:** 100+ duplicate records.
* **Corrected:** 51 instances of negative stock.
* **Standardized:** 1,000+ missing event tags, ensuring 100% data integrity for reporting.

### 3: SQL Intelligence & Stock Performance
Migrated cleaned data to a relational MySQL database to run complex KPI queries.
* **Stock Turnover Analysis:** Identified high-velocity products during "Black Friday" and "Ramadan."
* **Demographic Insights:** Analyzed "Basket Value" across key locations (Mall of the Emirates vs. Dubai Marina).

### 4: Stakeholder Reporting (Streamlit)
Deployed a live, interactive dashboard that allows non-technical stakeholders to filter performance by event and location.
* **Live Dashboard:** [https://retail-data-pipeline-forensics-na94ekakbwdrg5e4rrcqmq.streamlit.app/]

---

## Key Business Insights
* **Stock-out Risk:** "Smart Watch Ultra" turnover rate exceeds safety thresholds by 70% during Black Friday.
* **Location Strategy:** Mall of the Emirates shows a 15% higher average basket value for luxury goods compared to other locations.
* **Event Impact:** Dubai Shopping Festival (DSF) drives the highest volume of "Limited Edition Sneaker" sales.

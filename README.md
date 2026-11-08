
# Product Margin & Leakage Audit

An automated, reproducible financial audit pipeline analyzing margin erosion, category profitability, and discounting leakage across multi-regional sales operations.

---

## Executive Summary

- **Portfolio Health:** Aggregate sales demonstrate resilient demand, but blended gross margin experiences structural degradation in specific product segments.
- **Leakage Vulnerability:** Discounts $>15\%$ in the **Electronics** and **Furniture** categories account for significant margin decay without proportional volume elasticity.
- **Recommended Remediation:** Implement algorithmic discount caps at 10% across APAC and LATAM to reclaim an estimated **3.4% blended margin**.

---

## Analytical Architecture
Raw Data (.parquet) ──► DuckDB Engine ──► Quarto (.qmd) ──► Self-Contained HTML


- **Data Ingestion & OLAP:** DuckDB processes parquet files directly in-memory via high-throughput columnar SQL queries.
- **Reporting & Visualization:** Quarto compiles structured markdown, DuckDB query layers, and Plotly graphics into a single portable, standalone HTML document (`embed-resources: true`).

---

## Quickstart & Reproduction

To reproduce this audit locally:

```bash
# 1. Clone the repository
git clone [https://github.com/](https://github.com/)<your-username>/margin-audit.git
cd margin-audit

# 2. Set up virtual environment and dependencies
python -m venv .venv
source .venv/bin/activate       # Fish shell: source .venv/bin/activate.fish
pip install -r requirements.txt # or: pip install duckdb pandas plotly pyarrow jupyter

# 3. Generate data & compile report
python generate_data.py
quarto render margin-audit.qmd

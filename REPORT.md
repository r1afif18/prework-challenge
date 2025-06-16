# Caprae Capital Prework Challenge – Solution Report

## 1. Objective

Develop a modular tool that simulates a business lead generation workflow—scraping, enrichment, and export—adaptable for real sales/ops use cases.

---

## 2. Approach

- **Scraping:**  
  - For demo reliability, the pipeline uses dummy hardcoded leads instead of live scraping (as most modern business directories block bots).  
  - The scraping logic is modular—`scrape_leads()` can easily be replaced with real web scraping, Selenium, or an API in production.
- **Enrichment:**  
  - Each lead is enriched with a dummy email and LinkedIn URL, demonstrating pipeline extensibility.
- **Export:**  
  - Results are exported as CSV, universally compatible with sales/CRM tools.

---

## 3. Business Value

- **Sales/ops ready:** This pipeline is directly usable for enrichment and lead preparation, or for integration into automated outreach workflows.
- **Extensible:** Easily adaptable to real data and future business logic (deduplication, enrichment via API, CRM integration).
- **Why dummy data?** Ensures a working demo that demonstrates understanding of business logic, despite real-world anti-bot restrictions.

---

## 4. Next Steps / Improvements

- Swap in real web scraping (using Selenium/official APIs).
- Add deduplication/validation.
- Advanced enrichment (public APIs/email finder).
- Extend UI (Streamlit search/filter, CRM integration).

---

## 5. Files Delivered

- `dashboard.py` (Streamlit app)
- `src/scraper.py`, `src/enrich.py`
- `data/leads.csv`
- `README.md`, `REPORT.md`, `SCOPE.md`

---

*Developed and deployed by Rafif Sudanta on Linux VPS for Caprae Capital, June 2025.*

# Caprae Capital Prework Challenge – Project Scope

## Objective

Develop a simple, modular pipeline that simulates a business lead generation workflow:
- Generate (scrape) business leads
- Enrich leads with additional data (email, LinkedIn)
- Export to CSV

---

## Features in Scope

- Dummy lead generator (`scraper.py`)  
  *Reason: Many business directories block automated scraping; dummy data ensures robust demo pipeline.*
- Enrichment module (`enrich.py`)  
  *Adds sample email and LinkedIn data; demonstrates pipeline extensibility.*
- CSV export (in `dashboard.py` and `app.py`)
- Streamlit dashboard for UX/UI demo (dashboard.py)
- Option to upload user CSV and preview/download in app

---

## Out of Scope

- Live web scraping from production directories (due to anti-bot protection)
- Advanced enrichment (public email/phone lookups)
- CRM integration, deduplication (could be added in future iterations)

---

## Deliverables

- Source code: `dashboard.py`, `src/scraper.py`, `src/enrich.py`
- Output sample: `data/leads.csv`
- Documentation: `README.md`, `REPORT.md`, `SCOPE.md`

---

*Developed by Rafif Sudanta for Caprae Capital Prework – June 2025*

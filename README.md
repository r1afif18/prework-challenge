# 🚀 Lead Generation Pipeline – Caprae Capital Prework Challenge

A simple, modular pipeline to generate, enrich, and export business leads—built and tested as a technical assignment for Caprae Capital.  
**Developed and deployed on a Linux VPS (Ubuntu) for real-world, production-ready demonstration.**

---

## ✨ Features

- **Generate Demo Leads:** Dummy data to simulate company leads scraping.
- **Enrichment:** Automatically adds sample email & LinkedIn for each lead.
- **Export to CSV:** Download results instantly, ready for CRM/sales workflow.
- **Upload:** Preview and export your own CSV leads.
- **Production-ready:** Developed, tested, and deployed on a Linux VPS, demonstrating real industry implementation.

---

## 🌐 Live Demo

**Try the app:**  
[https://prework-challenge.streamlit.app/](https://prework-challenge.streamlit.app/)

---

## 🛠️ How to Run Locally (or on a VPS/Linux)

```bash
# 1. Clone the repository
git clone https://github.com/r1afif18/prework-challenge.git
cd prework-challenge

# 2. Set up the environment (recommended: Linux or VPS, e.g., Ubuntu)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit dashboard
streamlit run dashboard.py
```
The app runs on port 8501 by default. On a VPS, open the port in your firewall and access via http://[your-vps-ip]:8501


---

## 📂 Project Structure
```
prework-challenge/
├── src/
│   ├── scraper.py         # Dummy lead generator
│   ├── enrich.py          # Enrichment logic 
│   └── __init__.py
├── dashboard.py           # Streamlit web dashboard
├── app.py                 # CLI runner 
├── data/
│   └── leads.csv          # Example output
├── requirements.txt
├── README.md
├── REPORT.md
└── SCOPE.md
```

---

## 📑 Approach
This tool simulates a real-world lead generation pipeline:

Generate Leads: Scraping is simulated with hardcoded sample leads (ensures demo always works and is robust).

Enrichment: Adds dummy emails and LinkedIn URLs to each lead.

Export: Results can be previewed and downloaded as CSV.

Upload: Upload and view your own CSV leads in-app.

Note:
For demo purposes, scraping uses dummy data to avoid anti-bot protections present in most business directories.
The pipeline is modular—scrape_leads() can be replaced with real scraping, API, or enrichment logic as needed.

---

## 💡 Linux VPS/Production Notes
This project was developed and run entirely on a Linux VPS (Ubuntu 22.04) to demonstrate real-world readiness and deployment skills.

The workflow is tested for stability in cloud and remote server environments.

Steps to open firewall for Streamlit (example for Ubuntu):

```bash

sudo ufw allow 8501
sudo ufw reload
```
For cloud providers (AWS, Azure, GCP), ensure port 8501 is open for public access.


---

### 👤 Author
Developed by Rafif Sudanta
For Caprae Capital Prework Technical Challenge — June 2025

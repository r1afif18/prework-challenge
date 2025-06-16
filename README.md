# 🚀 Lead Generation Pipeline – Caprae Capital Prework Challenge

A simple, modular pipeline to generate, enrich, and export business leads—built and tested as a technical assignment for Caprae Capital.  
**Developed and deployed on a Linux VPS (Ubuntu) for a real-world, production-ready demonstration. Now includes a Jupyter Notebook walkthrough for transparent, step-by-step review.**

---

## ✨ Features

- **Generate Demo Leads:** Dummy data simulates company leads scraping.
- **Enrichment:** Automatically adds sample email & LinkedIn for each lead.
- **Export to CSV:** Download results instantly—ready for CRM/sales workflow.
- **Upload:** Preview and export your own CSV leads.
- **Jupyter Notebook Walkthrough:** Transparent, cell-by-cell demo of the pipeline.
- **Production-ready:** Developed, tested, and deployed on a Linux VPS.

---

## 🌐 Live Demo

**Try the app:**  
[https://prework-challenge.streamlit.app/](https://prework-challenge.streamlit.app/)

---

## 🛠️ Getting Started

### Run Locally (or on a VPS/Linux)

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

# 5. (Optional) Run the Jupyter Notebook walkthrough
jupyter notebook leadgen_walkthrough.ipynb

```
> By default, the app runs on port 8501.On a VPS, open the port in your firewall and access via http://[your-vps-ip]:8501.
---


## 📓 Jupyter Notebook Walkthrough

- **See:** [`leadgen_walkthrough.ipynb`](./leadgen_walkthrough.ipynb) for a cell-by-cell demo of the pipeline:
  - **Step-by-step demonstration:** Generate, enrich, export
  - **Transparent business/data logic:** Easy to review and adapt
  - **Reproducible:** Rerun or modify as needed for your own use case

---

## 📂 Project Structure


```
prework-challenge/
├── src/
│ ├── scraper.py   # Dummy lead generator
│ ├── enrich.py    # Enrichment logic
│ └── init.py
├── dashboard.py   # Streamlit web dashboard
├── app.py         # CLI runner
├── data/
│ └── leads.csv    # Example output
├── requirements.txt
├── README.md
├── REPORT.md
└── SCOPE.md
```

---

## 📝 Approach

- **This tool simulates a real-world lead generation pipeline:**
  - **Generate Leads:**  
    Scraping is simulated with hardcoded sample leads (ensures demo always works and is robust)
  - **Enrichment:**  
    Adds dummy emails and LinkedIn URLs to each lead
  - **Export:**  
    Results can be previewed and downloaded as CSV
  - **Upload:**  
    Upload and view your own CSV leads in-app
- **Note:**
  - For demo purposes, scraping uses dummy data to avoid anti-bot protections in business directories
  - The pipeline is modular—`scrape_leads()` can be replaced with real scraping, API, or enrichment logic as needed

---

## 🖥️ Linux VPS/Production Notes

- **Developed and run entirely on a Linux VPS (Ubuntu 22.04)** to demonstrate real-world deployment and readiness
- **Workflow tested for stability in cloud and remote server environments**
- **Open firewall for Streamlit (Ubuntu example):**

```bash

sudo ufw allow 8501
sudo ufw reload
```
For cloud providers (AWS, Azure, GCP), ensure port 8501 is open for public access.


---

### 👤 Author
- **Developed by Rafif Sudanta**
- **For Caprae Capital Prework Technical Challenge — June 2025**

from src.scraper import scrape_leads
from src.enrich import enrich_contacts

def main():
    criteria = {'industry': 'Any', 'location': 'Any'}
    raw = scrape_leads(criteria)
    print(raw)  # Print hasil scraping
    df = enrich_contacts(raw)
    print(df.head())  # Print hasil enrichment
    df.to_csv('data/leads.csv', index=False)
    print("Saved to data/leads.csv")

if __name__ == '__main__':
    main()

import pandas as pd

def enrich_contacts(raw_leads):
    """
    Enrich leads: tambahkan dummy email dan LinkedIn url
    """
    for lead in raw_leads:
        if lead["name"]:
            # Email dummy dari nama
            lead["email"] = lead["name"].replace(" ", "").lower() + "@example.com"
            lead["linkedin"] = "https://www.linkedin.com/in/" + lead["name"].replace(" ", "").lower()
        else:
            lead["email"] = ""
            lead["linkedin"] = ""
    return pd.DataFrame(raw_leads)

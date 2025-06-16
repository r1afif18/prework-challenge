import streamlit as st
import pandas as pd
from src.scraper import scrape_leads
from src.enrich import enrich_contacts

st.set_page_config(
    page_title="Lead Generation Pipeline – Demo",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🚀 Lead Generation Demo – Caprae Prework")
st.write("Simple pipeline to generate, enrich, and export business leads. Built for Caprae Capital technical challenge.")

st.header("1. Generate Leads (Dummy Demo)")
if st.button("Generate Sample Leads"):
    criteria = {'industry': 'Any', 'location': 'Any'}
    raw = scrape_leads(criteria)
    df = enrich_contacts(raw)
    st.session_state['df'] = df
    st.success("Leads generated!")

# Show leads if available
df = st.session_state.get('df') if 'df' in st.session_state else None
if df is not None and not df.empty:
    st.header("2. Preview & Export")
    st.dataframe(df, use_container_width=True)
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="leads.csv",
        mime="text/csv"
    )
else:
    st.info("Click 'Generate Sample Leads' to start, or upload your own CSV.")

st.header("3. Or Upload Your Own Leads")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    df_upload = pd.read_csv(uploaded_file)
    st.dataframe(df_upload, use_container_width=True)
    st.download_button(
        label="Download Uploaded CSV",
        data=df_upload.to_csv(index=False),
        file_name="uploaded_leads.csv",
        mime="text/csv"
    )

st.markdown("---")
st.caption("Demo by Rafif Sudanta | For Caprae Capital Prework Challenge")

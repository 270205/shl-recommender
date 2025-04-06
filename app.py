import streamlit as st  # ✅ Always import this first!

# Set Streamlit page configuration
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

# Standard path setup to access engine/
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'engine')))
sys.path.append('.')

# Imports from custom modules
from engine.utils import load_catalog, clean_text
from engine.matcher import keyword_match

# Load the catalog CSV
catalog = load_catalog()

# Show the number of rows loaded
st.write("📦 Catalog loaded with", len(catalog), "rows.")

# App Title and Description
st.title("🔍 SHL Assessment Recommendation Engine")
st.write("Enter a job role or key traits (comma-separated), and get SHL assessments that match!")

# Input box
user_input = st.text_input("Job Role or Traits (comma-separated)", placeholder="e.g., Problem Solving, Leadership")

# Recommendation logic
if user_input:
    results = keyword_match(user_input, catalog)

    if not results.empty:
        st.success(f"✅ Found {len(results)} matching assessments:")
        for _, row in results.iterrows():
            st.markdown(f"""
            ### 🧪 {row['Assessment Name']}
            **Description:** {row['Description']}  
            **Traits:** {row['Traits']}  
            **Suitable For Roles:** {row['Suitable For Roles']}  
            """)
    else:
        st.warning("No matching assessments found. Try different keywords.")

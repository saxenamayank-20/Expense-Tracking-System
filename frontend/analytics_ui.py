import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


# Override with an API_URL secret on Streamlit Cloud.
API_URL = os.getenv("API_URL", "https://expense-tracking-system-gj39.onrender.com")
# Render free tier can take ~60s to wake up from sleep.
TIMEOUT = 90


def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        try:
            response = requests.post(f"{API_URL}/analytics/", json=payload, timeout=TIMEOUT)
        except requests.RequestException:
            st.error("Could not reach the backend. Please try again in a minute.")
            return
        if response.status_code != 200:
            st.error("Failed to retrieve analytics from the backend.")
            return
        response = response.json()
        if not response:
            st.info("No expenses found for the selected date range.")
            return

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }


        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)

        
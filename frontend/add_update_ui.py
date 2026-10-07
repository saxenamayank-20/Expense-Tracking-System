import streamlit as st
from datetime import datetime
import requests
import os

# Override with an API_URL secret on Streamlit Cloud.
API_URL = os.getenv("API_URL", "https://expense-tracking-system-wx6y.onrender.com")
# Render free tier can take ~60s to wake up from sleep.
TIMEOUT = 90


def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2025, 1, 1), label_visibility="collapsed")
    try:
        response = requests.get(f"{API_URL}/expenses/{selected_date}", timeout=TIMEOUT)
    except requests.RequestException:
        response = None
    if response is not None and response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses. The backend may be waking up or its database is unreachable.")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]["category"]
                if category not in categories:
                    category = "Other"
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=10.0, value=amount, key=f"amount_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button("Submit", type="primary")
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            try:
                response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses,
                                         timeout=TIMEOUT)
            except requests.RequestException:
                response = None
            if response is not None and response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")
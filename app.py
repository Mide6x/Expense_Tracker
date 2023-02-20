import pandas as pd
import calendar
from datetime import datetime

import streamlit as st
import plotly.graph_objects as go

# variables
incomes = ["Salary", "Blog", "Social Media", "Sponsorships", "Other Sources" ]
expenses = ["Food", "Mobile Top-up", "House Bills", "Entertainment", "Others"]
currency = "NGN"
page_title = "Income Expense Tracker"
page_icon = ":money_with_wings:"
layout = "Centered"

st.set_page_config(page_title=page_title, page_icon=page_icon)
st.title(page_title + "" + page_icon)


#----import input fields----#
years = [datetime.today().year -1, datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

#--- first page ---#
st.subheader(f"Data entry in {currency}")

with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month: ", months, key="month")
    col2.selectbox("Select Year: ", years, key="year")

    "---"

    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}: ", min_value=0, format="%i", key=income, step=10)
    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}: ", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Notes"):
        notes = st.text_input("Anything you'd love to remember?", placeholder="Type in a note here")

    
    "---"

    submitted = st.form_submit_button("Give me visuals bro")

    
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        # TODO: Add contents to database
        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")

        st.success("Data Saved!")

    #plot periods

st.header("Data Visualization")
with st.form("saved_periods"):
     # TODO: get periods from database
     period = st.selectbox("Select Period: ", ["2023_March"])
     submitted = st.form_submit_button("Plot Period")
     if submitted:
    # TODO: Get data from database
        comment = "Omo, I spent a lot this month. Nigeria showed me shege!"
        incomes = {'Salary': 60000, 'Blog': 0, 'Other Income': 35000}
        expenses = {'Rent': 45000, 'Utilities': 5600, 'Groceries': 4500} 

        #Create Metrics
        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        remaining_metrics = total_income - total_expense

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"{total_income} {currency}")
        col2.metric("Total Expenses", f"{total_expense} {currency}")
        col3.metric("Balance", f"{remaining_metrics} {currency}")
        st.text(f"Comment: {comment}")
                



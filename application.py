import streamlit as st
from datetime import datetime

# Title
st.title("Date Difference Calculator")

# Date inputs

start_date = st.date_input("Start Date", datetime(2022, 1, 1))
end_date = st.date_input("End Date", datetime.today())

# Ensure the end date is after the start date
if end_date >= start_date:
    # Calculate the exact difference in years and months
    total_days = (end_date - start_date).days
    total_years = total_days / 365.25  # Account for leap years
    total_months = total_days / 30.44  # Average month length

    # Display the results
    st.write(f"Start Date: {start_date}")
    st.write(f"End Date: {end_date}")
    st.write(f"Number of years (up to 1 decimal place): **{total_years:.1f}**")
    st.write(f"Number of months (up to 1 decimal place): **{total_months:.1f}**")
    st.write(f"Number of days (up to 1 decimal place): **{total_days:.1f}**")
else:
    st.error("End Date must be after Start Date.")
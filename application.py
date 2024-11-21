import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from pandas.tseries.offsets import BDay

# Title
st.title("📅 Date Difference Calculator")

# Sidebar for Inputs
st.sidebar.header("Input Dates")
start_date = st.sidebar.date_input("Start Date", datetime(2022, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.today())

# Sidebar for Options
st.sidebar.header("Options")
include_dates = st.sidebar.checkbox("Include both Start Date and End Date in the calculation", value=True)
business_days_only = st.sidebar.checkbox("Calculate Business Days (Exclude weekends)", value=False)

# Main Section
st.header("Results")

if end_date >= start_date:
    if business_days_only:
        # Generate a range of business days
        date_range = pd.date_range(start=start_date, end=end_date, freq=BDay())

        # Adjust for inclusivity
        if not include_dates:
            date_range = date_range[1:-1]  # Exclude start and end dates

        total_business_days = len(date_range)

        # Display Results
        st.subheader("Business Days")
        st.write(f"Start Date: **{start_date.strftime('%Y-%m-%d')}**")
        st.write(f"End Date: **{end_date.strftime('%Y-%m-%d')}**")
        st.write(f"Include Start and End Date: **{'Yes' if include_dates else 'No'}**")
        st.success(f"Total Business Days (Excluding weekends): **{total_business_days}**")
    else:
        # Calculate total days
        total_days = (end_date - start_date).days
        if include_dates:
            total_days += 1
        else:
            total_days -= 1

        # Calculate years and months
        total_years = total_days / 365.25
        total_months = total_days / 30.44

        # Display Results
        st.subheader("Regular Days")
        st.write(f"Start Date: **{start_date.strftime('%Y-%m-%d')}**")
        st.write(f"End Date: **{end_date.strftime('%Y-%m-%d')}**")
        st.write(f"Include Start and End Date: **{'Yes' if include_dates else 'No'}**")
        st.success(f"Total Days: **{total_days}**")
        st.info(f"Total Years: **{total_years:.1f}**, Months: **{total_months:.1f}**")
else:
    st.error("End Date must be after Start Date.")

# Footer Section: Lunch Countdown
st.markdown("---")
st.header("🍴 Countdown to Lunch")

# Calculate time remaining until 12 PM
now = datetime.now()  # User's local time
lunch_time = now.replace(hour=12, minute=0, second=0, microsecond=0)

# If lunch time has passed today, calculate for tomorrow
if now > lunch_time:
    lunch_time += timedelta(days=1)

time_remaining = lunch_time - now
hours, remainder = divmod(time_remaining.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Display time remaining
st.write(
    f"Time left until lunch at 12:00 PM: **{hours} hours, {minutes} minutes, {seconds} seconds**"
)
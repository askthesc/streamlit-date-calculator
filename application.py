import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from pandas.tseries.offsets import BDay
import pytz
import time
from streamlit_autorefresh import st_autorefresh


# Title
st.title("📅 Date Difference Calculator")

# Sidebar for Inputs
st.sidebar.header("Input Dates")
start_date = st.sidebar.date_input("Start Date", datetime(2024, 11, 20))
end_date = st.sidebar.date_input("End Date", datetime.today())

# Sidebar for Options
st.sidebar.header("Options")
include_dates = st.sidebar.checkbox("Include both Start Date and End Date in the calculation", value=True)
business_days_only = st.sidebar.checkbox("Calculate Business Days (Exclude weekends)", value=False)

# Main Section


if end_date >= start_date:
    if business_days_only:
        # Generate a range of business days
        date_range = pd.date_range(start=start_date, end=end_date, freq=BDay())

        # Adjust for inclusivity
        if not include_dates:
            if len(date_range) > 1:
                date_range = date_range[1:-1]
            elif len(date_range) == 1:
                date_range = date_range
            elif len(date_range) == 1:
                date_range = []  # Exclude start and end dates
      

        total_business_days = len(date_range)
        total_biz_years = total_business_days / 365.25
        total_biz_months = total_business_days / 30.44

        # Display Results
        st.subheader("Business Days")
        st.write(f"Start Date: **{start_date.strftime('%Y-%m-%d')}**")
        st.write(f"End Date: **{end_date.strftime('%Y-%m-%d')}**")
        st.write(f"Include Start and End Date: **{'Yes' if include_dates else 'No'}**")
        st.success(f"Total Business Days (Excluding weekends): **{total_biz_years:.1f}**")
        st.success(f"Total Business Months (Excluding weekends): **{total_biz_months:.1f}**")
        st.success(f"Total Business Years (Excluding weekends): **{total_business_days:.1f}**")
    else:
        # Calculate total days
        total_days = (end_date - start_date).days
        if include_dates:
            total_days += 1
        elif total_days >0:
            pass
        else:
            total_days = 0 

        # Calculate years and months
        total_years = total_days / 365.25
        total_months = total_days / 30.44

        # Display Results
       
        st.write(f"Start Date: **{start_date.strftime('%Y-%m-%d')}**")
        st.write(f"End Date: **{end_date.strftime('%Y-%m-%d')}**")
        st.write(f"Include Start and End Date: **{'Yes' if include_dates else 'No'}**")
  
        st.success(f"Total Years: **{total_years:.1f}**")
        st.success(f"Total Months: **{total_months:.1f}**")
        st.success(f"Total Days: **{total_days}**")
else:
    st.error("End Date must be after Start Date.")


# Auto-refresh every second
st_autorefresh(interval=1000)  # Refresh every 1000ms (1 second)


# Footer Section: Lunch Countdown
st.markdown("---")
st.header("🍴 Countdown to Lunch")

# Get current time in Los Angeles
la_tz = pytz.timezone("America/Los_Angeles")
now = datetime.now(la_tz)
lunch_time = now.replace(hour=12, minute=0, second=0, microsecond=0)

# If lunch time has passed today, calculate for tomorrow
if now > lunch_time:
    lunch_time += timedelta(days=1)

time_remaining = lunch_time - now
hours, remainder = divmod(time_remaining.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Display time remaining
st.write(
    f"Time left until lunch at 12:00 PM (Los Angeles Time): **{hours} hours, {minutes} minutes, {seconds} seconds**"
)
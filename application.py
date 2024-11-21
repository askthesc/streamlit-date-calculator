import streamlit as st
from datetime import datetime
import pandas as pd
from pandas.tseries.offsets import BDay

# Title
st.title("Date Difference Calculator")

# Date inputs
start_date = st.date_input("Start Date", datetime(2022, 1, 1))
end_date = st.date_input("End Date", datetime.today())

# Checkbox for inclusion of start and end dates (checked by default)
include_dates = st.checkbox("Include both Start Date and End Date in the calculation", value=True)

# Checkbox to calculate business days (unchecked by default)
business_days_only = st.checkbox("Calculate Business Days (Exclude weekends)", value=False)

# Ensure the end date is after the start date
if end_date >= start_date:
    if business_days_only:
        # Generate a range of business days
        date_range = pd.date_range(start=start_date, end=end_date, freq=BDay())
        total_business_days = len(date_range)

        # Adjust for inclusivity
        if not include_dates:
            total_business_days -= 1  # Exclude the end date if "Include Both" is unchecked

        # Display results for business days
        st.write(f"Start Date: {start_date}")
        st.write(f"End Date: {end_date}")
        st.write(f"Include Start and End Date: **{'Yes' if include_dates else 'No'}**")
        st.write(f"Business Days (excluding weekends): **{total_business_days}**")
    else:
        # Calculate total days difference
        total_days = (end_date - start_date).days
        if include_dates:
            total_days += 1  # Add 1 day if inclusive

        # Calculate the total years and months for regular day count
        total_years = total_days / 365.25  # Account for leap years
        total_months = total_days / 30.44  # Average month length

        # Display the results
        st.write(f"Start Date: {start_date}")
        st.write(f"End Date: {end_date}")
        st.write(f"Include Start and End Date: **{'Yes' if include_dates else 'No'}**")
        st.write(f"Number of years (up to 1 decimal place): **{total_years:.1f}**")
        st.write(f"Number of months (up to 1 decimal place): **{total_months:.1f}**")
        st.write(f"Number of days: **{total_days}**")
else:
    st.error("End Date must be after Start Date.")
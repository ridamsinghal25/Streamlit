import datetime
import streamlit as st

st.title("Age Calculator")

today = datetime.datetime.now().year

st.text(f"Today is {today}")

dob = st.date_input("Select your date of birth", datetime.date(2023, 7, 1)).year

st.text(f"Your age is {today - dob} years")




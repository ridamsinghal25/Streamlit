import streamlit as st

st.title("Favourite programming language picker")

st.text("This is my first app.")

st.write("Choose your favourite programming language:")

language = st.selectbox("Select the lanuage", ["JavaScript", "C++", "Java", "Python", "Assembly"])

st.write(f"Your favourite language is {language}.")
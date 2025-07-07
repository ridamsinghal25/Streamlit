import streamlit as st

st.title("Hello Chai app")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app.")
st.write("Choose your favourite variety of chai")

chai = st.selectbox("Your favourite chai", ["Masala Chai", "Lemon Chai", "Adrak Chai", "Kesar Chai"])

st.write(f"You choose {chai}. Excellent choice")

st.success("Your chai has been brewed")
import streamlit as st

st.title("Tip Calculator")

bill_val = st.number_input("Enter the bill amount:")
tip_val = st.number_input("Enter the tipping amount:")
num_ppl = st.number_input("Enter the number of people:")

if st.button("Calculate"):
    st.header(f"Each person has to pay: {str(round((bill_val + tip_val) / num_ppl, 2))}")

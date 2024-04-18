import streamlit as st
from datetime import date

from BeefyAlgorithm import beefy_algorithm

st.title('Beefy Algorithm App')

a_date: date = st.date_input("Date for Beefy Algorithm")

btn_pressed: bool = st.button('Run Beefy Algorithm')
if btn_pressed:
    with st.spinner("Computing..."):
        df = beefy_algorithm(a_date)
    st.subheader('Results:')
    st.write(df.head())

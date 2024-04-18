import streamlit as st

st.title('Beefy Algorithm App')

some_date = st.date_input("Some date:")

btn_pressed: bool = st.button('Run Algorithm')
if btn_pressed:
    st.write("Date selected: ", some_date)

import streamlit as st

st.title("Portfolio")

ticker = st.text_input("Ticker")

shares = st.number_input("Shares")

buy_price = st.number_input("Buy Price")

if st.button("Save Holding"):
    st.success("Holding saved")

import streamlit as st

st.set_page_config(
    page_title="Stock Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Intelligence Platform")

st.markdown("""
Long-term investing dashboard.

Use the sidebar to navigate:
- Portfolio
- Screener
- Watchlist
- Alerts
""")

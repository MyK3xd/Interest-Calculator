import streamlit as st

pg = st.navigation([
    st.Page("pages/simple_interest.py", title="Simple Interest Calculator"),
    st.Page("pages/compound_interest.py", title="Compound Interest Calculator")
])

pg.run()
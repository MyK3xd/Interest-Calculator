import streamlit as st

pg = st.navigation([st.Page("main.py", title="Simple Interest Calculator"), st.Page("page_2.py")])
pg.run()
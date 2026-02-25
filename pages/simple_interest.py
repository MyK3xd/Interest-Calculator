import streamlit as st
import pandas as pd

def calculate_simple_interest(principal, rate_percent, time, rate_unit="month", time_unit="month"):

    rate = rate_percent / 100

    if rate_unit == "month" and time_unit == "year":
        time = time * 12

    elif rate_unit == "year" and time_unit == "month":
        time = time / 12

    return principal * rate * time

def reset_inputs():
        for key in ["principal", "rate", "time"]:
            if key in st.session_state:
                st.session_state[key] = 0.0

def simple_interest_calculator():

    col1, col2 = st.columns(2)

    with col1:
        principal = st.number_input("Principal", key="principal", step=1.0) #principal input

        r_col1, r_col2 = st.columns(2)

        with r_col1:
            rate = st.number_input("Rate (%)", key="rate", step=0.5) #interest rate input

        with r_col2:
            rate_select = st.selectbox("Interest Type", ["per Month", "per Year"], key="rate_type", index=1)

            rate_unit = "month" if rate_select == "per Month" else "year"    

        t_col1, t_col2 = st.columns(2)

        with t_col1:
            time = st.number_input("Time (Years)", key="time", step=1) #time input

        with t_col2:
            time_select = st.selectbox("Time Type", ["Months", "Years"], key="time_type", index=1)

            time_unit = "month" if time_select == "Months" else "year"

    with col2:
        st.subheader("Results", text_alignment="center")
        interest = calculate_simple_interest(principal, rate, time, rate_unit=rate_unit, time_unit=time_unit)
        st.metric("Total Interest", f"${interest:,.2f}")
        st.metric("Total Amount", f"${principal + interest:,.2f}")

    st.button("Reset", on_click=reset_inputs)

    return principal, rate, time, rate_unit, time_unit

def sched_table_generator(principal, rate, time, rate_unit, time_unit):
    data = []

    # number of rows depends on user-selected term
    periods = int(time) if float(time) > 0 else 1

    # column label changes based on selected time unit
    time_label = "Month" if time_unit == "month" else "Year"

    for period in range(1, periods + 1):
        interest = calculate_simple_interest(principal, rate, period, rate_unit=rate_unit, time_unit=time_unit)
        total_amount = principal + interest
        data.append({
            time_label: period, 
            "Interest": f"${interest:,.2f}", 
            "Total Amount": f"${total_amount:,.2f}", 
            "Principal": f"${principal:,.2f}"
            })

    return pd.DataFrame(data)

def line_graph(data):
    # determine time column name (Month or Year)
    time_col = "Year" if "Year" in data.columns else "Month" if "Month" in data.columns else data.columns[0]

    df_plot = data.copy()
    # clean Total Amount column and convert to numeric
    df_plot["Total Amount"] = df_plot["Total Amount"].str.replace("$", "").str.replace(",", "").astype(float)

    df_plot = df_plot.set_index(time_col).sort_index()
    st.line_chart(df_plot[["Total Amount"]])
    
#-------------------------------------- Main App --------------------------------------    

st.title("Simple Interest Calculator")

simple_interest_calculator()

p = st.session_state.get("principal", 0.0)
r = st.session_state.get("rate", 0.0)
t = st.session_state.get("time", 1)
r_unit = st.session_state.get("rate_type", "per Year").split()[-1].lower()
t_unit = st.session_state.get("time_type", "Years")[:-1].lower()

df = sched_table_generator(p, r, t, r_unit, t_unit)

st.divider()

graph_col, table_col = st.columns(2)
with graph_col:
    st.write("### Growth Over Time")
    line_graph(df)
    
with table_col:
    st.write("### Schedule")
    st.write(df)
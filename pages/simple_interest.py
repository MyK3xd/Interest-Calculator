import streamlit as st

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
#-------------------------------------- Main App --------------------------------------    

st.title("Simple Interest Calculator")


simple_interest_calculator()
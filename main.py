import streamlit as st

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def reset_inputs():
        for key in ["principal", "rate", "time"]:
            if key in st.session_state:
                st.session_state[key] = 0.0

def simple_interest_calculator():
    
    col1, col2, col3 = st.columns(3)

    with col1:
        principal = st.number_input("Principal", key="principal", step=1.0)

    with col2:
        rate = st.number_input("Rate (%)", key="rate", step=0.1)

    with col3:
        time = st.number_input("Time (Years)", key="time", step=0.1)

    col1, col2 = st.columns(2 )

    with col1:
        st.metric("Simple Interest", f"${calculate_simple_interest(principal, rate, time):,.2f}")
    with col2:
        st.metric("Total Amount", f"${principal + calculate_simple_interest(principal, rate, time):,.2f}")

    st.button("Reset", on_click=reset_inputs)

#------------------- Main App -------------------    

st.title("Interest Calculator")

interest_type = st.selectbox("Select Interest Type", ["Simple Interest", "Compound Interest"],
                           index = None,
                           placeholder = "Select Interest Type")

if interest_type == "Simple Interest":
    container = st.container(border=True)
    with container:
        simple_interest_calculator()
else:
    st.info("Compound Interest Calculator is under development. Please check back later.")
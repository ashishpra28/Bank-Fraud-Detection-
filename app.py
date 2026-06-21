# Import libraries
import streamlit as st
import requests
import joblib

# API 
API_URL = "http://api:8000/predict"

st.set_page_config(
    page_title="FraudShield",
    page_icon="🛡️",
    layout="centered"
)

st.markdown(
"""
<h1 style='text-align:center;'>
🛡️ FraudShield
</h1>

<p style='text-align:center;
font-size:20px;
color:gray;'>

AI-powered Bank Fraud Detection System to identify suspicious transactions in real time

</p>
""",
unsafe_allow_html=True
)

st.divider()

# Define user inputs    
hour = st.slider("Transaction Hour",min_value=0,max_value=23,value=12)
st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","CASH_IN","DEBIT"])
st.divider()

st.markdown("Transaction Amount")
amount = st.number_input("Total Amount", min_value=0.0, value=1000.0)
st.divider()

st.markdown("Sender Account")
col3, col4 = st.columns(2)
with col3:
    oldbalanceOrg = st.number_input(
        "Balance Before",
        min_value=0.0,
        value=0.0,
        step=100.0,
        format="%.2f",
        key="sender_before"
    )
with col4:
    newbalanceOrig = st.number_input(
        "Balance After",
        min_value=0.0,
        value=0.0,
        step=100.0,
        format="%.2f",
        key="sender_after"
    )
st.divider()

st.markdown("Receiver Account")
col5, col6 = st.columns(2)
with col5:
    oldbalanceDest = st.number_input(
        "Balance Before",
        min_value=0.0,
        value=0.0,
        step=100.0,
        format="%.2f",
        key="receiver_before"
    )
with col6:
    newbalanceDest = st.number_input(
        "Balance After",
        min_value=0.0,
        value=0.0,
        step=100.0,
        format="%.2f",
        key="receiver_after"
    )
st.divider() 

# Prediction button 
if st.button("Predict Fraud"): 

    # Feature Engineering 
    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    # Final input dataframe 
    input_data = {
        "hour":hour,
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }

    st.divider() 
    st.subheader("Prediction Result")

    try:
        response = requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result = response.json() 
            if result['prediction'] == 1:
                st.error(
                    f"⚠️ Potential Fraudulent Transaction Detected\n\n"
                    f"Fraud Probability: {result['fraud_probability']:.2%}"
                    )
            else:
                st.success(
                    f"✅ Legitimate Transaction\n\n"
                    f"Fraud Probability: {result['fraud_probability']:.2%}"
                )
            
            # Risk level 
            if result['fraud_probability'] >= 0.8:
                st.error("🔴 High Risk")
            elif result['fraud_probability'] >= 0.4:
                st.warning("🟠 Medium Risk")
            else:
                st.success("🟢 Low Risk")
        else: 
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError: 
        st.error("Could not connect on the FastAPI server. Make sure it is connected on port 8000")



   

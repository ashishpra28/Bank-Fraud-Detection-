# Import libraries 
import streamlit as st 
import pandas as pd 
import joblib 

# Import model 
model = joblib.load("artifacts/model.pkl")

# Page configuration
st.set_page_config(
    page_title="Bank Fraud Detection",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Bank Fraud Detection System")

st.markdown(
    "Enter transaction details to predict whether the transaction is Fraud or Not."
)

st.divider()

# Define user inputs    
transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","CASH_IN","DEBIT"])
hour = st.slider("Transaction Hour",min_value=0,max_value=23,value=12)
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Sender Balance",min_value=0.0,value=0.0)
newbalanceOrig = st.number_input("New Sender Balance",min_value=0.0,value=0.0)
oldbalanceDest = st.number_input("Old Receiver Balance",min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Receiver Balance",min_value=0.0, value=0.0)

# Prediction button 
if st.button("Predict Fraud"): 

    # Feature Engineering 
    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    # Final input dataframe 
    input_data = pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "balanceDiffOrig": balanceDiffOrig,
        "balanceDiffDest": balanceDiffDest,
        "hour": hour
    }])

    # Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider() 
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(
            f"⚠️ Fraudulent Transaction Detected\n\n"
            f"Fraud Probability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Legitimate Transaction\n\n"
            f"Fraud Probability: {probability:.2%}"
        )

    # Risk level 
    if probability >= 0.8:
        st.error("🔴 High Risk")
    elif probability >= 0.4:
        st.warning("🟠 Medium Risk")
    else:
        st.success("🟢 Low Risk")

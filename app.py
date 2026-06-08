import streamlit as st
import pandas as pd
import joblib
model=joblib.load("first_model.joblib")
st.set_page_config(page_title="Churn Prediction")
st.title("Customer Churn Prediction")
# st.write("Predict whethe a customer is likely to churn")
# st.markdown("--")
gender=st.selectbox("Gender",["Male","Female"])
SeniorCitizen=st.selectbox("Senior Citizen",[0,1])
Partner=st.selectbox("Partner",["Yes","No"])
Dependents=st.selectbox("Dependents",["Yes","No"])
tenure=st.slider("tenure",0,72,12)
PhoneService=st.selectbox("Phone Service",["Yes","No"])
MultipleLines=st.selectbox("Multi Plelines",["Yes","No","No Phone Service"])
InternetService=st.selectbox("Internet Service",["DSL","Fibre optic","No"])
OnlineSecurity=st.selectbox("Online Security",["Yes","No","No internet service"])
OnlineBackup=st.selectbox("Online Backup",["Yes","No","No ineternet service"])
DeviceProtection=st.selectbox("Device Protection",["Yes","No","ineternet service"])
TechSupport=st.selectbox("Tech Support",["Yes","No","No internet servce"])
StreamingTV=st.selectbox("Streaming TV",["Yes","No","internet service "])
StreamingMovies=st.selectbox("Streaming Movies",["Yes","No","internet service"])
PaperlessBilling=st.selectbox("Paperless Billing",["Yes","No"])
PaymentMethod=st.selectbox("Payment methods",["Electronic check","Mailed check","Bank transfer(automatic)","credit card(automatic)"])
MonthlyCharges=st.number_input("Monthly Charges",min_value=0.0)
TotalCharges=st.number_input("Total Charges",min_value=0.0)
Contract=st.selectbox("Contract Type",["Month-to-month","One-year","Two-year"])
input_data=pd.DataFrame({
    "gender":[gender],
    "SeniorCitizen":[SeniorCitizen],
    "Partner":[Partner],
    "Dependents":[Dependents],
    "tenure":[tenure],
    "PhoneService":[PhoneService],
    "MultipleLines":[MultipleLines],
    "InternetService":[InternetService],
    "OnlineSecurity":[OnlineSecurity],
    "OnlineBackup":[OnlineBackup],
    "DeviceProtection":[DeviceProtection],
    "TechSupport":[TechSupport],
    "StreamingTV":[StreamingTV],
    "StreamingMovies":[StreamingMovies],
    "PaperlessBilling":[PaperlessBilling],
    "PaymentMethod":[PaymentMethod],
    "MonthlyCharges":[MonthlyCharges],
    "TotalCharges":[TotalCharges],
    "Contract":[Contract]                       
})
if st.button("Predict"):
    prediction=model.predict(input_data)
    probability=model.predict_proba(input_data)
    churn_prob=probability[0][1]
    st.subheader("Prediction Result")
    if prediction[0]==1:
        st.error(
            f"Customer likely to churn. \n"
            f"Probability:{churn_prob:.2f}"
        )
    else:
        st.sucess(
            f"Customer likely to stay .\n"
            f"Pobability:{churn_prob:.2f}"
        )
  

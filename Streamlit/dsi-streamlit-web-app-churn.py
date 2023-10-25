# Improt libraries
import streamlit as st
import pandas as pd
import joblib

# load our model pipeline object
model = joblib.load("churn_model.joblib")

# insert a title for the app and instructions

st.title("Customer Churn Prediction Model")
st.subheader("Enter customer information and submit for likelihood of churn")


# chest pain input form

SeniorCitizen = st.number_input(
    label = "Enter whether the customer is a senior citizen [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )

tenure = st.number_input(
    label = "Enter the customers's tenure status [1-72]",
    min_value = 1,
    max_value = 72,
    value = 12,
    )

MonthlyCharges = st.number_input(
    label = "Enter the customers's monthly charge amount [0-150]",
    min_value = 0.00,
    max_value = 150.00,
    value = 75.00,
    step=0.01,
    format="%0.2f"
    )

TotalCharges = st.number_input(
    label = "Enter the customers's total charge value [0-9000]",
    min_value = 0.00,
    max_value = 9000.00,
    value = 4500.00,
    step=0.01,
    format="%0.2f"
    )

gender_Male = st.number_input(
    label = "Enter whether the customer is male [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
Partner_Yes = st.number_input(
    label = "Enter whether the customer has a partner [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
Dependents_Yes = st.number_input(
    label = "Enter whether the customer has dependents [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
PhoneService_Yes = st.number_input(
    label = "Enter whether the customer has phone service [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
MultipleLines_No_phone_service = st.number_input(
    label = "Enter whether the customer has multiple phone lines [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 
 = st.number_input(
    label = "Enter the customers's recorded MDVP:Fo(Hz) [0-1]",
    min_value = 0,
    max_value = 1,
    value = 1,
    )
 


({"SeniorCitizen" :[SeniorCitizen],
"tenure" : [tenure],
"MonthlyCharges" : [MonthlyCharges],
"TotalCharges" :[TotalCharges],
"gender_Male" : [gender_Male],
"Partner_Yes" : [Partner_Yes],
"Dependents_Yes" : [Dependents_Yes],
"PhoneService_Yes" : [PhoneService_Yes],
"MultipleLines_No phone service" : [MultipleLines_No_phone_service],
"MultipleLines_Yes" : [MultipleLines_Yes],
"InternetService_Fiber optic" : [InternetService_Fiber_optic],
"InternetService_No" : [InternetService_No],
"OnlineSecurity_No internet service" : [OnlineSecurity_No_internet_service],
"OnlineSecurity_Yes" : [OnlineSecurity_Yes],
"OnlineBackup_No internet service" : [OnlineBackup_No_internet_service],
"OnlineBackup_Yes" : [OnlineBackup_Yes],
"DeviceProtection_No internet service" : [DeviceProtection_No_internet_service],
"DeviceProtection_Yes" : [DeviceProtection_Yes],
"TechSupport_No internet service" : [TechSupport_No_internet_service],
"TechSupport_Yes" : [TechSupport_Yes],
"StreamingTV_No internet service" : [StreamingTV_No_internet_service],
"StreamingTV_Yes" : [StreamingTV_Yes],
"StreamingMovies_No internet service" : [StreamingMovies_No_internet_service],
"StreamingMovies_Yes" : [StreamingMovies_Yes],
"Contract_One year" : [Contract_One_year],
"Contract_Two year" : [Contract_Two_year],
"PaperlessBilling_Yes" : [PaperlessBilling_Yes],
"PaymentMethod_Credit card (automatic)" : [PaymentMethod_Credit_card_automatic],
"PaymentMethod_Electronic check" : [PaymentMethod_Electronic_check],
"PaymentMethod_Mailed check" : [PaymentMethod_Mailed_check],
"tenure_cohort_12-24 months" : [tenure_cohort_12_24_months],
"tenure_cohort_24-48 months" : [tenure_cohort_24_48_months],
"tenure_cohort_over 48 months" : [tenure_cohort_over_48_months]})


# submit inputs to model

if st.button("Submit For Prediction"):
    # store data into df for prediction
    new_data = pd.DataFrame({"SeniorCitizen" :[SeniorCitizen],
    "tenure" : [tenure],
    "MonthlyCharges" : [MonthlyCharges],
    "TotalCharges" :[TotalCharges],
    "gender_Male" : [gender_Male],
    "Partner_Yes" : [Partner_Yes],
    "Dependents_Yes" : [Dependents_Yes],
    "PhoneService_Yes" : [PhoneService_Yes],
    "MultipleLines_No phone service" : [MultipleLines_No_phone_service],
    "MultipleLines_Yes" : [MultipleLines_Yes],
    "InternetService_Fiber optic" : [InternetService_Fiber_optic],
    "InternetService_No" : [InternetService_No],
    "OnlineSecurity_No internet service" : [OnlineSecurity_No_internet_service],
    "OnlineSecurity_Yes" : [OnlineSecurity_Yes],
    "OnlineBackup_No internet service" : [OnlineBackup_No_internet_service],
    "OnlineBackup_Yes" : [OnlineBackup_Yes],
    "DeviceProtection_No internet service" : [DeviceProtection_No_internet_service],
    "DeviceProtection_Yes" : [DeviceProtection_Yes],
    "TechSupport_No internet service" : [TechSupport_No_internet_service],
    "TechSupport_Yes" : [TechSupport_Yes],
    "StreamingTV_No internet service" : [StreamingTV_No_internet_service],
    "StreamingTV_Yes" : [StreamingTV_Yes],
    "StreamingMovies_No internet service" : [StreamingMovies_No_internet_service],
    "StreamingMovies_Yes" : [StreamingMovies_Yes],
    "Contract_One year" : [Contract_One_year],
    "Contract_Two year" : [Contract_Two_year],
    "PaperlessBilling_Yes" : [PaperlessBilling_Yes],
    "PaymentMethod_Credit card (automatic)" : [PaymentMethod_Credit_card_automatic],
    "PaymentMethod_Electronic check" : [PaymentMethod_Electronic_check],
    "PaymentMethod_Mailed check" : [PaymentMethod_Mailed_check],
    "tenure_cohort_12-24 months" : [tenure_cohort_12_24_months],
    "tenure_cohort_24-48 months" : [tenure_cohort_24_48_months],
    "tenure_cohort_over 48 months" : [tenure_cohort_over_48_months]})
    
    # apply model pipeline to the input data and extract probability prediction
    pred_proba = model.predict_proba(new_data)[0][1]
    
    # output prediction
    st.subheader(f"Based on these customer attributes, our model predicts a parkinson's disease probability of {pred_proba: .0%}")
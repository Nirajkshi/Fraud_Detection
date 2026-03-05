import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model/logistic_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection Dashboard")

st.write("Enter transaction details to check fraud probability")

# Transaction inputs
time = st.number_input("Transaction Time")
amount = st.number_input("Transaction Amount")

# PCA features
features = []
for i in range(1, 29):
    value = st.number_input(f"V{i}")
    features.append(value)

if st.button("Check Fraud"):

    input_data = np.array([[time, amount] + features])

    input_scaled = scaler.transform(input_data)

    fraud_prob = model.predict_proba(input_scaled)[0][1]

    st.subheader("Fraud Probability")

    st.write(fraud_prob)

    if fraud_prob > 0.59:
        st.error("⚠️ High Risk Transaction")
    else:
        st.success("✅ Normal Transaction")
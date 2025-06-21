import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('salary_prediction.pkl')

st.title("💼 Salary Prediction App")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
experience = st.slider("Years of Experience", 0, 40, 2)

# Manually map to encoded values used during training
gender_mapping = {
    "Female": 0,
    "Male": 1,
    "Other": 2
}

education_mapping = {
    "Bachelor's": 0,      # replace with correct number used during training
    "Master's": 1,        # replace with correct number used during training
    "PhD": 2              # replace with correct number used during training
}

# When button is clicked
if st.button("Predict Salary"):
    try:
        gender_encoded = gender_mapping[gender]
        education_clean = {
            "Bachelor's": "Bachelor's Degree",
            "Master's": "Master's Degree",
            "PhD": "PHD"
        }[education]
        
        # Adjust the education mapping if actual values were different
        education_encoded = education_mapping[education]

        # Final feature array
        features = np.array([[age, gender_encoded, education_encoded, experience]])

        # Predict
        prediction = model.predict(features)[0]
        st.success(f"💰 Estimated Salary: ${prediction:,.2f}")

    except KeyError as e:
        st.error(f"Invalid input: {e}")

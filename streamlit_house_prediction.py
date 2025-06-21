import streamlit as st
import joblib
import numpy as np

# Set Streamlit page config
st.set_page_config(page_title="🏠 House Price Predictor", layout="centered")

# Load model and encoder
model = joblib.load("house_price_prediction.pkl")
label_encoder = joblib.load("house_price_encoder.pkl")

# Title
st.title("🏡 House Price Prediction App")
st.markdown("Fill out the form below to predict the price of a house in ₹ (INR).")

# Furnishing status mapping (if needed)
furnishing_map = {
    "Unfurnished": 0,
    "Semi-furnished": 1,
    "Furnished": 2
}

# House detail input form
with st.form("prediction_form"):
    st.header("📝 Enter House Details")
    
    area = st.number_input("Area (in sqft)", min_value=500, max_value=10000, step=100, value=1500)
    bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
    bathrooms = st.slider("Number of Bathrooms", 1, 10, 2)
    stories = st.slider("Number of Stories", 1, 5, 2)
    
    mainroad = st.radio("Is there access to main road?", ["Yes", "No"])
    guestroom = st.radio("Is there a guest room?", ["Yes", "No"])
    basement = st.radio("Does it have a basement?", ["Yes", "No"])
    hotwaterheating = st.radio("Has hot water heating?", ["Yes", "No"])
    airconditioning = st.radio("Air conditioning available?", ["Yes", "No"])
    parking = st.slider("Number of Parking Spaces", 0, 5, 1)
    prefarea = st.radio("Is it in a preferred area?", ["Yes", "No"])
    
    furnishingstatus = st.selectbox("Furnishing Status", list(furnishing_map.keys()))

    submit = st.form_submit_button("🔍 Predict Price")

if submit:
    try:
        # Prepare input data
        input_data = [[
            area,
            bedrooms,
            bathrooms,
            stories,
            1 if mainroad == "Yes" else 0,
            1 if guestroom == "Yes" else 0,
            1 if basement == "Yes" else 0,
            1 if hotwaterheating == "Yes" else 0,
            1 if airconditioning == "Yes" else 0,
            parking,
            1 if prefarea == "Yes" else 0,
            furnishing_map[furnishingstatus]
        ]]
        
        # Prediction
        predicted_price = model.predict(input_data)[0]
        st.success(f"💰 **Predicted House Price: ₹{predicted_price:,.2f}**")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

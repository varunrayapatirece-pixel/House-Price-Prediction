
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Predict California house prices using Machine Learning.")

st.subheader("Enter Property Details")

col1, col2 = st.columns(2)

with col1:
    med_inc = st.number_input("Median Income", value=3.0)
    house_age = st.number_input("House Age", value=20.0)
    ave_rooms = st.number_input("Average Rooms", value=5.0)
    ave_bedrms = st.number_input("Average Bedrooms", value=1.0)

with col2:
    population = st.number_input("Population", value=1000.0)
    ave_occup = st.number_input("Average Occupancy", value=3.0)
    latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=34.0)
    longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, value=-118.0)

if st.button("Predict House Price"):

    input_data = pd.DataFrame([{
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated House Price: ${prediction * 100000:,.2f}")

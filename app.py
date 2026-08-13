import streamlit as st
import pandas as pd
import pickle

# Load model
pipe = pickle.load(open("model.pkl", "rb"))

st.title("Food Delivery Time Prediction")

# Inputs
delivery_person_age = st.number_input("Delivery Person Age", 18, 60, 25)

delivery_person_ratings = st.number_input(
    "Delivery Person Ratings",
    min_value=1.0,
    max_value=5.0,
    value=4.5
)

distance_km = st.number_input(
    "Distance (km)",
    min_value=0.1,
    value=5.0
)

road_traffic_density = st.selectbox(
    "Road Traffic Density",
    ["Low", "Medium", "High", "Jam"]
)

weatherconditions = st.selectbox(
    "Weather Conditions",
    ["Sunny", "Cloudy", "Fog", "Stormy", "Windy", "Sandstorms"]
)

type_of_vehicle = st.selectbox(
    "Type of Vehicle",
    ["Bike", "Scooter", "Motorcycle", "Electric Scooter"]
)

order_hour = st.slider(
    "Order Hour",
    min_value=0,
    max_value=23,
    value=12
)

# Prediction
if st.button("Predict Delivery Time"):

    input_df = pd.DataFrame({
        "delivery_person_age": [delivery_person_age],
        "delivery_person_ratings": [delivery_person_ratings],
        "distance_km": [distance_km],
        "road_traffic_density": [road_traffic_density],
        "weatherconditions": [weatherconditions],
        "type_of_vehicle": [type_of_vehicle],
        "order_hour": [order_hour]
    })

    prediction = pipe.predict(input_df)

    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} minutes")
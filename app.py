import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="Smart Electricity Bill Predictor",
    page_icon="⚡",
    layout="centered"
)

# Title
st.title("⚡ Smart Electricity Bill Predictor")

st.write("Predict your monthly electricity bill using AI")

st.divider()

# Inputs
units = st.number_input("Units Consumed", min_value=0)

lights = st.slider("Number of Lights", 0, 20, 4)
light_hours = st.slider("Light Usage Hours", 0, 24, 6)

fans = st.slider("Number of Fans", 0, 10, 3)
fan_hours = st.slider("Fan Usage Hours", 0, 24, 8)

ac = st.slider("Number of ACs", 0, 5, 1)
ac_hours = st.slider("AC Usage Hours", 0, 24, 3)

fridge = st.slider("Fridge Count", 0, 5, 1)

tv = st.slider("Number of TVs", 0, 5, 1)
tv_hours = st.slider("TV Usage Hours", 0, 24, 4)

washing_machine = st.slider("Washing Machines", 0, 3, 1)
washing_hours = st.slider("Washing Machine Hours", 0, 10, 1)

inverter = st.selectbox(
    "Inverter Available?",
    ["No", "Yes"]
)

geyser = st.slider("Number of Geysers", 0, 3, 0)
geyser_hours = st.slider("Geyser Usage Hours", 0, 10, 0)

season = st.selectbox(
    "Season",
    ["Winter/Rainy", "Summer"]
)

# Convert categorical values
inverter_value = 1 if inverter == "Yes" else 0
season_value = 1 if season == "Summer" else 0

st.divider()

# Predict button
if st.button("🔮 Predict Electricity Bill"):

    input_data = np.array([[
        units,
        lights,
        light_hours,
        fans,
        fan_hours,
        ac,
        ac_hours,
        fridge,
        tv,
        tv_hours,
        washing_machine,
        washing_hours,
        inverter_value,
        geyser,
        geyser_hours,
        season_value
    ]])

    prediction = model.predict(input_data)

    bill = prediction[0]

    st.success(f"Estimated Monthly Bill: ₹{bill:.2f}")

    # Bill category
    if bill < 2000:
        st.info("Low Electricity Usage")

    elif bill < 5000:
        st.warning("Medium Electricity Usage")

    else:
        st.error("High Electricity Usage")

st.divider()

st.caption("Built using Machine Learning and Random Forest")

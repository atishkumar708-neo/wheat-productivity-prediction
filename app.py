# ============================================================
# Wheat Productivity Prediction App
# ============================================================

import streamlit as st
import pandas as pd
import joblib

# ------------------------------------------------------------
# Load Saved Model
# ------------------------------------------------------------

model = joblib.load("rf_productivity.pkl")

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------

st.title("🌾 Wheat Productivity Prediction")

st.write(
    "Predict wheat productivity using climate and irrigation data."
)

# ------------------------------------------------------------
# User Inputs
# ------------------------------------------------------------

zone = st.selectbox(

    "Select Zone",

    [

        "Ambala",

        "Gurgaon",

        "Hisar",

        "Jind",

        "Karnal",

        "Rohtak"

    ]

)

year = st.number_input(

    "Year",

    min_value=1965,

    max_value=2050,

    value=2019

)

tmax_crop = st.number_input(

    "Crop Tmax"

)

tmax_lean = st.number_input(

    "Lean Tmax"

)

tmin_crop = st.number_input(

    "Crop Tmin"

)

tmin_lean = st.number_input(

    "Lean Tmin"

)

rf_crop = st.number_input(

    "Crop Rainfall"

)

rf_lean = st.number_input(

    "Lean Rainfall"

)

irrigation = st.number_input(

    "Irrigation (%)"

)

# ------------------------------------------------------------
# Prediction Button
# ------------------------------------------------------------

if st.button("Predict"):

    input_df = pd.DataFrame({

        "Year":[year],

        "Zone":[zone],

        "Tmax_Crop":[tmax_crop],

        "Tmax_Lean":[tmax_lean],

        "Tmin_Crop":[tmin_crop],

        "Tmin_Lean":[tmin_lean],

        "RF_Crop":[rf_crop],

        "RF_Lean":[rf_lean],

        "Irrigation_Percent":[irrigation]

    })

    prediction = model.predict(input_df)[0]

    st.success(

        f"Predicted Wheat Productivity : {prediction:.2f} kg/ha"

    )
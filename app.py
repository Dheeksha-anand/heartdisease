import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Heart Disease Prediction App")
st.write("Enter the required details below to check the risk of developing heart disease.")

# User inputs
male = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
age = st.number_input("Age", min_value=20, max_value=100, step=1)
education = st.selectbox("Education Level", [1, 2, 3, 4])
currentSmoker = st.selectbox("Current Smoker?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, max_value=50, step=1)
BPMeds = st.selectbox("On BP Medication?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
prevalentStroke = st.selectbox("Had a Stroke?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
prevalentHyp = st.selectbox("Has Hypertension?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
diabetes = st.selectbox("Has Diabetes?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=600, step=1)
sysBP = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=250, step=1)
diaBP = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=50, max_value=150, step=1)
BMI = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, step=0.1)
heartRate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, step=1)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, step=1)

# Create input dataframe
input_data = pd.DataFrame([[male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]],
                          columns=["male", "age", "education", "currentSmoker", "cigsPerDay", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "⚠️ Likely to develop Heart Disease" if prediction == 1 else "✅ Unlikely to develop Heart Disease"
    
    # Display result
    st.subheader(f"Prediction Result:")
    st.markdown(f"### {result}")

    if prediction == 1:
        st.warning("It's recommended to consult a doctor and maintain a healthy lifestyle.")
    else:
        st.success("Keep maintaining a healthy lifestyle!")

# Run this file using: `streamlit run filename.py`

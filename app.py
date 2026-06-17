import streamlit as st
import pandas as pd
import pickle

with open("models/student_model.pkl", "rb") as f:
    model = pickle.load(f)
st.title("Student Math Score Predictor")
reading = st.number_input("Reading Score", 0, 100, 50)
writing = st.number_input("Writing Score", 0, 100, 50)
if st.button("Predict"):
    data = pd.DataFrame({
        "reading score": [reading],
        "writing score": [writing]
    })
    result = model.predict(data)
    st.success(f"Predicted Math Score: {result[0]:.2f}")
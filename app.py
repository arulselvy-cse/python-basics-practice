import streamlit as st 
import joblib
import numpy as np 

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Purchase Prediction")
st.write("Enter customer details:")

age = st.number_input("Age",min_value=19,max_value=92)
salary = st.number_input("Salary",min_value=20000,max_value=50000)

if st.button("Predict"):
 input_data = np.array([[age,salary]])
 input_scaled = scaler.transform(input_data)
 prediction = model.predict(input_scaled)

 if prediction [0]==1:
    st.success("Customer is likely to purchase")
 else:
    st.warning("Customer is not likely to Purchase")
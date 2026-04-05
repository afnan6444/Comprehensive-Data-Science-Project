import streamlit as st
import pandas as pd
import requests

st.title('Sales Forecast Dashboard')

# User inputs
product = st.selectbox('Select Product', ['Product A', 'Product B', 'Product C'])
region = st.selectbox('Select Region', ['North', 'South', 'East', 'West'])
quantity = st.number_input('Quantity', min_value=1, max_value=1000, value=10)

# Prepare input data
input_data = {
    'Product': product,
    'Region': region,
    'Quantity': quantity
}

if st.button('Predict Sales'):
    response = requests.post('http://localhost:5000/predict', json=input_data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Sales: {result['predicted_sales']}")
    else:
        st.error('Prediction failed. Please try again.')

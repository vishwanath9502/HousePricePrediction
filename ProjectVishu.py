import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


# Display title
st.image(r"D:\Vishu\My\Innomatics\New\Innomatics Logo.png")
st.title("House Price Prediction")

# Load the pre-trained model
try:
    model = pickle.load(open(r"C:\Users\gorla\lr.pkl", "rb"))
    model_loaded = True
except Exception as e:
    st.error(f"Error loading model: {e}")
    model_loaded = False

# Sidebar content
st.sidebar.header("Model Information")
st.sidebar.markdown(
    """
    The model used for prediction is a Linear Regression model trained on a dataset of house prices. 
    It considers the following features:
    - Size of the house in square feet
    - Number of bedrooms
    - Number of bathrooms
    - Neighborhood (Rural, Urban, Suburb)
    - Year of construction
    """
)

st.sidebar.header("Instructions")
st.sidebar.markdown(
    """
    Use the inputs on the main page to enter the details of the house for which you want to predict the price. 
    After entering the details, click on the "Predict Price" button to see the predicted price.
    """
)

# Main page content
if model_loaded:
    st.success("Model loaded successfully!")

    # User inputs
    st.header("Enter House Details")
    SquareFeet = st.number_input("Size of the house (in square feet)", min_value=800, max_value=6000, step=50)
    Bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=5, step=1)
    Bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=5, step=1)
    Neighborhood = st.radio("Neighborhood", ['Rural', 'Urban', 'Suburb'])
    YearBuilt = st.number_input("Year of Construction", min_value=1900, max_value=2050, step=1)

    # Convert neighborhood to numerical value
    neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3

    # Predict price on button click
    if st.button("Predict Price"):
        try:
            price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])[0]
            st.success(f"The predicted price for the house with given details is Rs. {price:,.2f}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")


# Footer
st.markdown(
    """
    <div class="footer">
    Developed by Vishu | Innomatics Research Labs
    </div>
    """,
    unsafe_allow_html=True
)
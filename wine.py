import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Load the trained KMeans model and the scaler
# Note: Adjust the paths accordingly to where your model and scaler are saved
model_path = "./main/kmeans_wine_clustering.joblib"
model = joblib.load(model_path)

# Streamlit title and description
st.title("Wine Cluster Prediction")
st.write("Discover what type of wine you might prefer based on alcohol content and color intensity.")

# User input for alcohol content and color intensity
alcohol_content = st.number_input("Enter the alcohol content (typical range: 11-15):", min_value=11.0, max_value=15.0, step=0.1)
color_intensity = st.number_input("Enter the color intensity (typical range: 1-13):", min_value=1.0, max_value=13.0, step=0.1)

# Create an input array with the user data
input_array = np.array([[alcohol_content, color_intensity]])

# Button to trigger the prediction
if st.button('Check Your Wine Preference'):
    # Scale the input
    input_array_scaled = scaler.transform(input_array)
    
    # Predict the cluster
    predicted_cluster = model.predict(input_array_scaled)[0]
    
    # Map the cluster to a description
    cluster_descriptions = {
        0: "You are a casual drinker. You seem to enjoy light, refreshing wines with bold color and acidity. You likely prefer crisp and lively wines.",
        1: "You are an experienced drinker. You have the refined palate of a connoisseur! You enjoy balanced, flavorful, and structured wines with higher alcohol content.",
        2: "You are health-conscious or an occasional drinker. You likely lean towards wines that are subtle and easy-going."
    }

    # Output the result
    cluster_description = cluster_descriptions.get(predicted_cluster, "Unknown Cluster")
    st.write(f"### {cluster_description}")


import sys
sys.path.append('.')
from theme import apply_theme, page_header, metric_card, sec_head
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
import os

st.set_page_config(page_title="Land Price Prediction", page_icon="🏠", layout="wide")
apply_theme()

page_header("🏠", "Land Price Prediction", "Predict land prices using Machine Learning based on various features.")

# Generate synthetic Indian land data
@st.cache_data
def generate_data():
    np.random.seed(42)
    n = 1000
    
    states = ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Delhi', 'Gujarat', 
              'Rajasthan', 'Uttar Pradesh', 'West Bengal', 'Telangana', 'Odisha']
    land_types = ['Agricultural', 'Residential', 'Commercial', 'Industrial']
    zones = ['Urban', 'Semi-Urban', 'Rural']
    
    data = {
        'area_sqft': np.random.randint(500, 50000, n),
        'distance_city_km': np.random.randint(1, 100, n),
        'road_connectivity': np.random.randint(1, 10, n),
        'water_availability': np.random.randint(1, 10, n),
        'electricity_supply': np.random.randint(1, 10, n),
        'soil_quality': np.random.randint(1, 10, n),
        'flood_risk': np.random.randint(1, 10, n),
        'market_demand': np.random.randint(1, 10, n),
        'state': np.random.choice(states, n),
        'land_type': np.random.choice(land_types, n),
        'zone': np.random.choice(zones, n),
    }
    
    df = pd.DataFrame(data)
    
    # Price logic based on features
    base_price = df['area_sqft'] * 500
    city_factor = (100 - df['distance_city_km']) * 1000
    infra_factor = (df['road_connectivity'] + df['water_availability'] + 
                    df['electricity_supply']) * 5000
    
    zone_multiplier = df['zone'].map({'Urban': 3.0, 'Semi-Urban': 1.8, 'Rural': 1.0})
    type_multiplier = df['land_type'].map({
        'Commercial': 4.0, 'Industrial': 3.0, 
        'Residential': 2.0, 'Agricultural': 1.0
    })
    
    noise = np.random.normal(0, 50000, n)
    
    df['price_inr'] = ((base_price + city_factor + infra_factor) * 
                        zone_multiplier * type_multiplier + noise).astype(int)
    df['price_inr'] = df['price_inr'].clip(lower=100000)
    
    return df

# Train model
@st.cache_resource
def train_model(df):
    df_encoded = pd.get_dummies(df, columns=['state', 'land_type', 'zone'])
    X = df_encoded.drop('price_inr', axis=1)
    y = df_encoded['price_inr']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    return model, X.columns.tolist(), r2, mae

# Load data and train
df = generate_data()
model, feature_cols, r2, mae = train_model(df)

# Model performance
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Model", "Random Forest")
with col2:
    st.metric("R² Score", f"{r2:.2f}")
with col3:
    st.metric("Mean Absolute Error", f"₹{mae:,.0f}")

st.markdown("---")

# Input form
st.subheader("🔍 Enter Land Details")

col1, col2, col3 = st.columns(3)

with col1:
    area_sqft = st.number_input("Area (sq ft)", min_value=100, max_value=100000, value=1000)
    distance_city = st.slider("Distance from City (km)", 1, 100, 10)
    road_connectivity = st.slider("Road Connectivity (1-10)", 1, 10, 7)
    water_availability = st.slider("Water Availability (1-10)", 1, 10, 7)

with col2:
    electricity_supply = st.slider("Electricity Supply (1-10)", 1, 10, 8)
    soil_quality = st.slider("Soil Quality (1-10)", 1, 10, 6)
    flood_risk = st.slider("Flood Risk (1=High, 10=Low)", 1, 10, 8)
    market_demand = st.slider("Market Demand (1-10)", 1, 10, 7)

with col3:
    state = st.selectbox("State", ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Delhi', 
                                    'Gujarat', 'Rajasthan', 'Uttar Pradesh', 
                                    'West Bengal', 'Telangana', 'Odisha'])
    land_type = st.selectbox("Land Type", ['Agricultural', 'Residential', 'Commercial', 'Industrial'])
    zone = st.selectbox("Zone", ['Urban', 'Semi-Urban', 'Rural'])

# Predict button
if st.button("🔮 Predict Price", type="primary"):
    input_data = {
        'area_sqft': area_sqft,
        'distance_city_km': distance_city,
        'road_connectivity': road_connectivity,
        'water_availability': water_availability,
        'electricity_supply': electricity_supply,
        'soil_quality': soil_quality,
        'flood_risk': flood_risk,
        'market_demand': market_demand,
        'state': state,
        'land_type': land_type,
        'zone': zone
    }
    
    input_df = pd.DataFrame([input_data])
    input_encoded = pd.get_dummies(input_df, columns=['state', 'land_type', 'zone'])
    
    # Add missing columns
    for col in feature_cols:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[feature_cols]
    
    predicted_price = model.predict(input_encoded)[0]
    
    st.markdown("---")
    st.success(f"### 💰 Predicted Land Price: ₹{predicted_price:,.0f}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Price per sq ft", f"₹{predicted_price/area_sqft:,.0f}")
    with col2:
        st.metric("Price in Lakhs", f"₹{predicted_price/100000:.2f}L")
    with col3:
        st.metric("Price in Crores", f"₹{predicted_price/10000000:.3f}Cr")
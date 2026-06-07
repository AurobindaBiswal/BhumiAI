import sys
sys.path.append('.')
from theme import apply_theme, page_header, sec_head
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Location Map Visualizer", page_icon="🗺️", layout="wide")
apply_theme()
page_header("🗺️", "Land Location Intelligence Map", "Visualize land prices, investment potential, and development zones across Odisha.")

# Odisha cities/areas data
@st.cache_data
def get_odisha_land_data():
    data = {
        'location': [
            'Bhubaneswar - Patia', 'Bhubaneswar - Chandrasekharpur', 
            'Bhubaneswar - Nalco Nagar', 'Bhubaneswar - Niladri Vihar',
            'Bhubaneswar - Infocity', 'Bhubaneswar - Jaydev Vihar',
            'Bhubaneswar - Nayapalli', 'Bhubaneswar - Saheed Nagar',
            'Cuttack - Badambadi', 'Cuttack - Buxi Bazar',
            'Cuttack - Chauliaganj', 'Cuttack - Mangalabag',
            'Puri - Sea Beach Road', 'Puri - VIP Road',
            'Rourkela - Sector 1', 'Rourkela - Uditnagar',
            'Sambalpur - Ainthapali', 'Sambalpur - Budharaja',
            'Berhampur - Bada Bazar', 'Berhampur - Gandhi Nagar',
            'Balasore - Town Area', 'Kendrapara - Main Town',
            'Brahmapur - New Colony', 'Khordha - Main Area',
            'Jajpur - Industrial Area', 'Angul - Industrial Zone',
        ],
        'lat': [
            20.3548, 20.3433, 20.3201, 20.3301,
            20.3467, 20.3389, 20.2897, 20.2634,
            20.4625, 20.4698, 20.4534, 20.4412,
            19.8135, 19.8234, 22.2604, 22.2534,
            21.4669, 21.4534, 19.3149, 19.3267,
            21.4942, 20.6256, 19.3067, 20.1834,
            20.8389, 20.8534,
        ],
        'lon': [
            85.8245, 85.8123, 85.8034, 85.8156,
            85.8312, 85.8198, 85.8467, 85.8389,
            85.8830, 85.8756, 85.8634, 85.8512,
            85.8312, 85.8423, 84.8536, 84.8412,
            83.9812, 83.9698, 84.7941, 84.8056,
            86.9334, 86.7123, 84.7823, 85.6234,
            86.3389, 85.1023,
        ],
        'price_per_sqft': [
            3200, 2800, 2400, 2600,
            3500, 3100, 2900, 3300,
            1800, 2100, 1600, 1900,
            4200, 3800, 1200, 1100,
            900, 850, 800, 750,
            600, 500, 700, 1400,
            650, 700,
        ],
        'investment_score': [
            88, 82, 75, 78,
            92, 85, 80, 86,
            70, 72, 65, 68,
            85, 80, 60, 58,
            55, 52, 50, 48,
            45, 42, 47, 65,
            55, 58,
        ],
        'zone_type': [
            'IT/Residential', 'Residential', 'Residential', 'Residential',
            'IT/Commercial', 'Commercial', 'Residential', 'Commercial',
            'Commercial', 'Commercial', 'Residential', 'Residential',
            'Tourism', 'Tourism/Residential', 'Industrial', 'Residential',
            'Commercial', 'Residential', 'Commercial', 'Residential',
            'Commercial', 'Agricultural', 'Residential', 'Residential',
            'Industrial', 'Industrial',
        ],
        'development_stage': [
            'Developed', 'Developed', 'Developing', 'Developing',
            'Developed', 'Developed', 'Developed', 'Developed',
            'Developed', 'Developed', 'Developing', 'Developing',
            'Developed', 'Developing', 'Developed', 'Developing',
            'Developing', 'Developing', 'Developing', 'Developing',
            'Developing', 'Underdeveloped', 'Developing', 'Developing',
            'Developed', 'Developing',
        ]
    }
    return pd.DataFrame(data)

df = get_odisha_land_data()

st.markdown("---")

# Filters
col1, col2, col3 = st.columns(3)
with col1:
    map_type = st.selectbox("Map View", [
        "💰 Price per sq ft", 
        "📊 Investment Score",
        "🏗️ Zone Type",
        "🔨 Development Stage"
    ])
with col2:
    min_price, max_price = st.slider(
        "Filter by Price Range (₹/sqft)", 
        int(df['price_per_sqft'].min()), 
        int(df['price_per_sqft'].max()),
        (int(df['price_per_sqft'].min()), int(df['price_per_sqft'].max()))
    )
with col3:
    min_score = st.slider("Minimum Investment Score", 0, 100, 0)

# Filter data
filtered_df = df[
    (df['price_per_sqft'] >= min_price) & 
    (df['price_per_sqft'] <= max_price) &
    (df['investment_score'] >= min_score)
]

st.markdown(f"**Showing {len(filtered_df)} locations**")

# Map
if map_type == "💰 Price per sq ft":
    fig = px.scatter_mapbox(
        filtered_df, lat='lat', lon='lon',
        color='price_per_sqft',
        size='price_per_sqft',
        hover_name='location',
        hover_data={'price_per_sqft': True, 'investment_score': True, 'zone_type': True},
        color_continuous_scale='RdYlGn',
        size_max=25,
        zoom=7,
        title="Odisha — Land Price per sq ft Map",
        mapbox_style="open-street-map"
    )

elif map_type == "📊 Investment Score":
    fig = px.scatter_mapbox(
        filtered_df, lat='lat', lon='lon',
        color='investment_score',
        size='investment_score',
        hover_name='location',
        hover_data={'investment_score': True, 'price_per_sqft': True, 'zone_type': True},
        color_continuous_scale='RdYlGn',
        size_max=25,
        zoom=7,
        title="Odisha — Investment Score Map",
        mapbox_style="open-street-map"
    )

elif map_type == "🏗️ Zone Type":
    fig = px.scatter_mapbox(
        filtered_df, lat='lat', lon='lon',
        color='zone_type',
        size='price_per_sqft',
        hover_name='location',
        hover_data={'zone_type': True, 'price_per_sqft': True, 'investment_score': True},
        size_max=25,
        zoom=7,
        title="Odisha — Zone Type Map",
        mapbox_style="open-street-map"
    )

else:
    fig = px.scatter_mapbox(
        filtered_df, lat='lat', lon='lon',
        color='development_stage',
        size='price_per_sqft',
        hover_name='location',
        hover_data={'development_stage': True, 'price_per_sqft': True, 'investment_score': True},
        size_max=25,
        zoom=7,
        title="Odisha — Development Stage Map",
        mapbox_style="open-street-map"
    )

fig.update_layout(height=550, margin={"r":0,"t":40,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Stats and table
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Top 5 Investment Locations")
    top5 = filtered_df.nlargest(5, 'investment_score')[
        ['location', 'investment_score', 'price_per_sqft', 'zone_type']
    ].reset_index(drop=True)
    top5.index += 1
    st.dataframe(top5, use_container_width=True)

with col2:
    st.subheader("💰 Price Distribution by City")
    filtered_df['city'] = filtered_df['location'].str.split(' - ').str[0]
    city_avg = filtered_df.groupby('city')['price_per_sqft'].mean().reset_index()
    city_avg.columns = ['City', 'Avg Price/sqft']
    city_avg = city_avg.sort_values('Avg Price/sqft', ascending=False)
    
    fig2 = px.bar(city_avg, x='City', y='Avg Price/sqft',
                  color='Avg Price/sqft', color_continuous_scale='RdYlGn',
                  title="Average Land Price by City")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Location details
st.subheader("🔍 Location Details Table")
display_df = filtered_df[['location', 'price_per_sqft', 'investment_score', 
                           'zone_type', 'development_stage']].reset_index(drop=True)
display_df.index += 1
display_df.columns = ['Location', 'Price/sqft (₹)', 'Investment Score', 'Zone Type', 'Development Stage']
st.dataframe(display_df, use_container_width=True)
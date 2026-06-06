import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Development Potential", page_icon="🏗️", layout="wide")

st.title("🏗️ Land Development Potential Analyzer")
st.write("Analyze the development potential of land parcels using AI and zoning intelligence.")

def analyze_development_potential(inputs):
    results = {}

    # Suitable development types
    development_types = {}

    # Residential
    res_score = 0
    res_score += inputs['water_supply'] * 10
    res_score += inputs['electricity'] * 10
    res_score += inputs['road_access'] * 8
    res_score += inputs['nearby_schools'] * 7
    res_score += inputs['nearby_hospitals'] * 6
    res_score += (10 - inputs['noise_level']) * 5
    res_score += (10 - inputs['pollution']) * 4
    development_types['Residential'] = min(100, res_score)

    # Commercial
    com_score = 0
    com_score += inputs['footfall_potential'] * 15
    com_score += inputs['road_access'] * 12
    com_score += inputs['market_proximity'] * 10
    com_score += inputs['parking_space'] * 8
    com_score += inputs['electricity'] * 7
    development_types['Commercial'] = min(100, com_score)

    # Agricultural
    agr_score = 0
    agr_score += inputs['soil_quality'] * 15
    agr_score += inputs['water_supply'] * 12
    agr_score += inputs['sunlight_exposure'] * 10
    agr_score += (10 - inputs['pollution']) * 8
    agr_score += inputs['flat_terrain'] * 7
    development_types['Agricultural'] = min(100, agr_score)

    # Industrial
    ind_score = 0
    ind_score += inputs['road_access'] * 10
    ind_score += inputs['electricity'] * 12
    ind_score += inputs['water_supply'] * 8
    ind_score += inputs['flat_terrain'] * 10
    ind_score += (10 - inputs['nearby_schools']) * 5
    ind_score += inputs['market_proximity'] * 7
    development_types['Industrial'] = min(100, ind_score)

    # Mixed Use
    mix_score = (development_types['Residential'] + development_types['Commercial']) / 2
    development_types['Mixed Use'] = mix_score

    results['development_types'] = development_types

    # Best use
    best_use = max(development_types, key=development_types.get)
    results['best_use'] = best_use
    results['best_score'] = development_types[best_use]

    # ROI estimation
    roi_multipliers = {
        'Residential': 2.5, 'Commercial': 3.8,
        'Agricultural': 1.4, 'Industrial': 2.8, 'Mixed Use': 3.2
    }
    results['estimated_roi'] = roi_multipliers[best_use]

    # Timeline
    timelines = {
        'Residential': '2-3 years', 'Commercial': '1-2 years',
        'Agricultural': 'Immediate', 'Industrial': '3-4 years', 'Mixed Use': '2-4 years'
    }
    results['development_timeline'] = timelines[best_use]

    # Challenges
    challenges = []
    if inputs['flood_risk'] > 6:
        challenges.append("⚠️ High flood risk — drainage infrastructure needed")
    if inputs['road_access'] < 4:
        challenges.append("⚠️ Poor road access — connectivity improvement required")
    if inputs['water_supply'] < 4:
        challenges.append("⚠️ Water supply issues — borewell or pipeline needed")
    if inputs['electricity'] < 4:
        challenges.append("⚠️ Electricity supply weak — grid connection required")
    if inputs['soil_quality'] < 4:
        challenges.append("⚠️ Poor soil quality — foundation work may be costly")
    if not challenges:
        challenges.append("✅ No major challenges detected")

    results['challenges'] = challenges

    return results

st.markdown("---")

tab1, tab2 = st.tabs(["📝 Analyze Land", "🧪 Demo — Bhubaneswar Plot"])

with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**🌍 Physical Features**")
        soil_quality = st.slider("Soil Quality (1-10)", 1, 10, 7)
        flat_terrain = st.slider("Flat Terrain (1-10)", 1, 10, 8)
        flood_risk = st.slider("Flood Risk (1=Low, 10=High)", 1, 10, 3)
        sunlight_exposure = st.slider("Sunlight Exposure (1-10)", 1, 10, 8)
        noise_level = st.slider("Noise Level (1=Low, 10=High)", 1, 10, 3)
        pollution = st.slider("Pollution Level (1=Low, 10=High)", 1, 10, 2)

    with col2:
        st.write("**🏗️ Infrastructure**")
        road_access = st.slider("Road Access (1-10)", 1, 10, 8)
        electricity = st.slider("Electricity Supply (1-10)", 1, 10, 9)
        water_supply = st.slider("Water Supply (1-10)", 1, 10, 8)
        parking_space = st.slider("Parking Space Available (1-10)", 1, 10, 6)

    with col3:
        st.write("**📍 Location & Market**")
        nearby_schools = st.slider("Nearby Schools (1-10)", 1, 10, 7)
        nearby_hospitals = st.slider("Nearby Hospitals (1-10)", 1, 10, 6)
        footfall_potential = st.slider("Footfall Potential (1-10)", 1, 10, 7)
        market_proximity = st.slider("Market Proximity (1-10)", 1, 10, 7)

    if st.button("🔍 Analyze Development Potential", type="primary"):
        inputs = {
            'soil_quality': soil_quality, 'flat_terrain': flat_terrain,
            'flood_risk': flood_risk, 'sunlight_exposure': sunlight_exposure,
            'noise_level': noise_level, 'pollution': pollution,
            'road_access': road_access, 'electricity': electricity,
            'water_supply': water_supply, 'parking_space': parking_space,
            'nearby_schools': nearby_schools, 'nearby_hospitals': nearby_hospitals,
            'footfall_potential': footfall_potential, 'market_proximity': market_proximity
        }

        results = analyze_development_potential(inputs)

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🏆 Best Use", results['best_use'])
        with col2:
            st.metric("📈 Estimated ROI", f"{results['estimated_roi']}x")
        with col3:
            st.metric("⏱️ Timeline", results['development_timeline'])

        col1, col2 = st.columns(2)

        with col1:
            dev_df = pd.DataFrame({
                'Type': list(results['development_types'].keys()),
                'Score': list(results['development_types'].values())
            }).sort_values('Score', ascending=True)

            fig = px.bar(dev_df, x='Score', y='Type', orientation='h',
                        title="Development Suitability by Type",
                        color='Score', color_continuous_scale='RdYlGn')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("⚠️ Development Challenges")
            for challenge in results['challenges']:
                st.write(challenge)

            st.subheader("📋 Suitability Scores")
            for dev_type, score in results['development_types'].items():
                icon = "🟢" if score >= 70 else "🟡" if score >= 50 else "🔴"
                st.write(f"{icon} **{dev_type}:** {score:.1f}/100")

with tab2:
    st.info("Demo: Patia, Bhubaneswar — Mixed Residential Plot")

    if st.button("🚀 Run Demo Analysis", type="primary"):
        demo_inputs = {
            'soil_quality': 7, 'flat_terrain': 8, 'flood_risk': 3,
            'sunlight_exposure': 9, 'noise_level': 4, 'pollution': 3,
            'road_access': 8, 'electricity': 9, 'water_supply': 8,
            'parking_space': 6, 'nearby_schools': 8, 'nearby_hospitals': 7,
            'footfall_potential': 7, 'market_proximity': 7
        }

        results = analyze_development_potential(demo_inputs)

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🏆 Best Use", results['best_use'])
        with col2:
            st.metric("📈 Estimated ROI", f"{results['estimated_roi']}x")
        with col3:
            st.metric("⏱️ Timeline", results['development_timeline'])

        col1, col2 = st.columns(2)

        with col1:
            dev_df = pd.DataFrame({
                'Type': list(results['development_types'].keys()),
                'Score': list(results['development_types'].values())
            }).sort_values('Score', ascending=True)

            fig = px.bar(dev_df, x='Score', y='Type', orientation='h',
                        title="Patia Plot — Development Suitability",
                        color='Score', color_continuous_scale='RdYlGn')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("⚠️ Development Challenges")
            for challenge in results['challenges']:
                st.write(challenge)

            st.subheader("📋 Suitability Scores")
            for dev_type, score in results['development_types'].items():
                icon = "🟢" if score >= 70 else "🟡" if score >= 50 else "🔴"
                st.write(f"{icon} **{dev_type}:** {score:.1f}/100")
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Investment Score", page_icon="📊", layout="wide")

st.title("📊 Land Investment Score Analyzer")
st.write("Get a comprehensive AI-powered investment score for any land parcel.")

def calculate_investment_score(inputs):
    scores = {}

    # Location Score (0-100)
    location = 0
    location += (10 - inputs['distance_city']) * 8
    location += inputs['road_connectivity'] * 5
    location += inputs['public_transport'] * 4
    location += inputs['nearby_schools'] * 3
    location += inputs['nearby_hospitals'] * 3
    scores['Location Score'] = min(100, max(0, location))

    # Infrastructure Score
    infra = 0
    infra += inputs['electricity'] * 8
    infra += inputs['water_supply'] * 8
    infra += inputs['sewage_system'] * 6
    infra += inputs['internet_connectivity'] * 5
    scores['Infrastructure Score'] = min(100, max(0, infra))

    # Market Score
    market = 0
    market += inputs['price_appreciation'] * 8
    market += inputs['market_demand'] * 7
    market += inputs['rental_yield'] * 6
    market += (10 - inputs['market_competition']) * 4
    scores['Market Score'] = min(100, max(0, market))

    # Legal Score
    legal = 0
    legal += inputs['clear_title'] * 20
    legal += inputs['no_disputes'] * 20
    legal += inputs['registered_doc'] * 15
    legal += inputs['govt_approved'] * 15
    scores['Legal Score'] = min(100, max(0, legal))

    # Risk Score (higher = lower risk)
    risk = 0
    risk += (10 - inputs['flood_risk']) * 6
    risk += (10 - inputs['earthquake_risk']) * 5
    risk += (10 - inputs['pollution_level']) * 5
    risk += inputs['soil_stability'] * 6
    scores['Risk Score'] = min(100, max(0, risk))

    # Overall weighted score
    overall = (
        scores['Location Score'] * 0.30 +
        scores['Infrastructure Score'] * 0.20 +
        scores['Market Score'] * 0.25 +
        scores['Legal Score'] * 0.15 +
        scores['Risk Score'] * 0.10
    )
    scores['Overall Score'] = round(overall, 1)

    return scores

def get_recommendation(score):
    if score >= 80:
        return "🟢 EXCELLENT INVESTMENT", "Strong buy recommendation. High returns expected.", "green"
    elif score >= 65:
        return "🔵 GOOD INVESTMENT", "Recommended for investment with good growth potential.", "blue"
    elif score >= 50:
        return "🟡 MODERATE INVESTMENT", "Acceptable investment. Do thorough due diligence.", "orange"
    elif score >= 35:
        return "🟠 RISKY INVESTMENT", "High risk. Not recommended without expert advice.", "orange"
    else:
        return "🔴 POOR INVESTMENT", "Avoid this investment. Multiple risk factors detected.", "red"

st.markdown("---")
st.subheader("🔍 Enter Land Details for Investment Analysis")

tab1, tab2 = st.tabs(["📝 Manual Input", "🧪 Demo Analysis"])

with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**📍 Location Factors**")
        distance_city = st.slider("Distance from City (1=Far, 10=Close)", 1, 10, 6)
        road_connectivity = st.slider("Road Connectivity (1-10)", 1, 10, 7)
        public_transport = st.slider("Public Transport Access (1-10)", 1, 10, 6)
        nearby_schools = st.slider("Nearby Schools (1-10)", 1, 10, 7)
        nearby_hospitals = st.slider("Nearby Hospitals (1-10)", 1, 10, 6)

    with col2:
        st.write("**🏗️ Infrastructure & Market**")
        electricity = st.slider("Electricity Supply (1-10)", 1, 10, 8)
        water_supply = st.slider("Water Supply (1-10)", 1, 10, 7)
        sewage_system = st.slider("Sewage System (1-10)", 1, 10, 6)
        internet_connectivity = st.slider("Internet Connectivity (1-10)", 1, 10, 7)
        price_appreciation = st.slider("Price Appreciation Rate (1-10)", 1, 10, 7)
        market_demand = st.slider("Market Demand (1-10)", 1, 10, 6)
        rental_yield = st.slider("Rental Yield Potential (1-10)", 1, 10, 6)
        market_competition = st.slider("Market Competition (1=Low, 10=High)", 1, 10, 5)

    with col3:
        st.write("**⚖️ Legal & Risk Factors**")
        clear_title = st.checkbox("Clear Title Document", value=True)
        no_disputes = st.checkbox("No Legal Disputes", value=True)
        registered_doc = st.checkbox("Registered Documents", value=True)
        govt_approved = st.checkbox("Government Approved Layout", value=False)
        flood_risk = st.slider("Flood Risk (1=Low, 10=High)", 1, 10, 3)
        earthquake_risk = st.slider("Earthquake Risk (1=Low, 10=High)", 1, 10, 2)
        pollution_level = st.slider("Pollution Level (1=Low, 10=High)", 1, 10, 3)
        soil_stability = st.slider("Soil Stability (1-10)", 1, 10, 7)

    if st.button("📊 Calculate Investment Score", type="primary"):
        inputs = {
            'distance_city': distance_city, 'road_connectivity': road_connectivity,
            'public_transport': public_transport, 'nearby_schools': nearby_schools,
            'nearby_hospitals': nearby_hospitals, 'electricity': electricity,
            'water_supply': water_supply, 'sewage_system': sewage_system,
            'internet_connectivity': internet_connectivity,
            'price_appreciation': price_appreciation, 'market_demand': market_demand,
            'rental_yield': rental_yield, 'market_competition': market_competition,
            'clear_title': int(clear_title), 'no_disputes': int(no_disputes),
            'registered_doc': int(registered_doc), 'govt_approved': int(govt_approved),
            'flood_risk': flood_risk, 'earthquake_risk': earthquake_risk,
            'pollution_level': pollution_level, 'soil_stability': soil_stability
        }

        scores = calculate_investment_score(inputs)
        label, advice, color = get_recommendation(scores['Overall Score'])

        st.markdown("---")
        st.markdown(f"## {label}")
        st.info(f"💡 {advice}")

        col1, col2 = st.columns(2)

        with col1:
            # Radar chart
            categories = ['Location', 'Infrastructure', 'Market', 'Legal', 'Risk']
            values = [
                scores['Location Score'], scores['Infrastructure Score'],
                scores['Market Score'], scores['Legal Score'], scores['Risk Score']
            ]

            fig = go.Figure(data=go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                line_color='blue'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                title="Investment Score Radar Chart"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📋 Detailed Scores")
            for category, score in scores.items():
                if category != 'Overall Score':
                    bar_color = "🟢" if score >= 70 else "🟡" if score >= 50 else "🔴"
                    st.write(f"{bar_color} **{category}:** {score:.1f}/100")
                    st.progress(int(score))

            st.markdown("---")
            st.metric("🏆 Overall Investment Score", f"{scores['Overall Score']}/100")

with tab2:
    st.info("Demo: Bhubaneswar Residential Plot Analysis")

    if st.button("🚀 Run Demo Analysis", type="primary"):
        demo_inputs = {
            'distance_city': 7, 'road_connectivity': 8, 'public_transport': 7,
            'nearby_schools': 8, 'nearby_hospitals': 7, 'electricity': 9,
            'water_supply': 8, 'sewage_system': 7, 'internet_connectivity': 8,
            'price_appreciation': 8, 'market_demand': 7, 'rental_yield': 7,
            'market_competition': 4, 'clear_title': 1, 'no_disputes': 1,
            'registered_doc': 1, 'govt_approved': 1, 'flood_risk': 2,
            'earthquake_risk': 2, 'pollution_level': 3, 'soil_stability': 8
        }

        scores = calculate_investment_score(demo_inputs)
        label, advice, color = get_recommendation(scores['Overall Score'])

        st.markdown(f"## {label}")
        st.info(f"💡 {advice}")

        categories = ['Location', 'Infrastructure', 'Market', 'Legal', 'Risk']
        values = [
            scores['Location Score'], scores['Infrastructure Score'],
            scores['Market Score'], scores['Legal Score'], scores['Risk Score']
        ]

        col1, col2 = st.columns(2)

        with col1:
            fig = go.Figure(data=go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                line_color='blue'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                title="Bhubaneswar Plot — Investment Radar"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📋 Detailed Scores")
            for category, score in scores.items():
                if category != 'Overall Score':
                    bar_color = "🟢" if score >= 70 else "🟡" if score >= 50 else "🔴"
                    st.write(f"{bar_color} **{category}:** {score:.1f}/100")
                    st.progress(int(score))

            st.markdown("---")
            st.metric("🏆 Overall Investment Score", f"{scores['Overall Score']}/100")
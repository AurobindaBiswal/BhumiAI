import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Negotiation Strategy", page_icon="📊", layout="wide")

st.title("📊 AI-Powered Land Negotiation Strategy")
st.write("Get data-driven negotiation strategies to get the best deal on land purchases.")

def generate_negotiation_strategy(inputs):
    results = {}

    # Calculate fair market value
    base_price = inputs['asking_price']
    
    # Market adjustments
    adjustments = []
    adjustment_total = 0

    if inputs['days_on_market'] > 90:
        adj = -base_price * 0.08
        adjustments.append(("Days on Market > 90 days", adj, "Seller is motivated"))
        adjustment_total += adj
    elif inputs['days_on_market'] > 60:
        adj = -base_price * 0.05
        adjustments.append(("Days on Market > 60 days", adj, "Slight seller motivation"))
        adjustment_total += adj

    if inputs['price_vs_market'] > 10:
        adj = -base_price * 0.10
        adjustments.append(("Price above market rate", adj, "Overpriced listing"))
        adjustment_total += adj
    elif inputs['price_vs_market'] > 5:
        adj = -base_price * 0.05
        adjustments.append(("Price slightly above market", adj, "Room for negotiation"))
        adjustment_total += adj

    if inputs['legal_issues'] > 0:
        adj = -base_price * (inputs['legal_issues'] * 0.05)
        adjustments.append(("Legal issues detected", adj, "Risk discount applicable"))
        adjustment_total += adj

    if inputs['infrastructure_gaps'] > 3:
        adj = -base_price * 0.07
        adjustments.append(("Poor infrastructure", adj, "Development cost discount"))
        adjustment_total += adj

    if inputs['motivated_seller']:
        adj = -base_price * 0.08
        adjustments.append(("Motivated seller", adj, "Urgent sale situation"))
        adjustment_total += adj

    results['adjustments'] = adjustments
    results['fair_value'] = max(base_price + adjustment_total, base_price * 0.6)

    # Negotiation prices
    results['opening_offer'] = results['fair_value'] * 0.85
    results['target_price'] = results['fair_value'] * 0.92
    results['walkaway_price'] = results['fair_value'] * 1.05

    # Negotiation tactics
    tactics = []

    if inputs['days_on_market'] > 60:
        tactics.append({
            'tactic': '⏰ Time Leverage',
            'description': f'Property has been on market for {inputs["days_on_market"]} days. Mention you are aware of this and have other options.',
            'strength': 'High'
        })

    if inputs['price_vs_market'] > 5:
        tactics.append({
            'tactic': '📊 Market Comparison',
            'description': 'Present comparable properties in the area at lower prices. Use data to justify your offer.',
            'strength': 'High'
        })

    if inputs['legal_issues'] > 0:
        tactics.append({
            'tactic': '⚖️ Legal Risk Discount',
            'description': f'Highlight {inputs["legal_issues"]} legal issue(s) found in document verification. Request price reduction for risk.',
            'strength': 'Very High'
        })

    if inputs['infrastructure_gaps'] > 3:
        tactics.append({
            'tactic': '🏗️ Infrastructure Cost',
            'description': 'Present estimated cost of infrastructure development needed. Deduct from asking price.',
            'strength': 'Medium'
        })

    tactics.append({
        'tactic': '💰 Cash Payment Advantage',
        'description': 'Offer quick cash settlement in exchange for price reduction of 5-8%.',
        'strength': 'Medium'
    })

    tactics.append({
        'tactic': '🏠 Multiple Property Interest',
        'description': 'Show interest in multiple properties to create competition and reduce seller leverage.',
        'strength': 'Medium'
    })

    results['tactics'] = tactics

    # Negotiation phases
    results['phases'] = [
        {
            'phase': 'Phase 1 — Opening Offer',
            'price': results['opening_offer'],
            'action': 'Start low but reasonable. Justify with market data and property issues.'
        },
        {
            'phase': 'Phase 2 — Counter Response',
            'price': (results['opening_offer'] + results['target_price']) / 2,
            'action': 'Move slightly. Show willingness but emphasize constraints.'
        },
        {
            'phase': 'Phase 3 — Target Price',
            'price': results['target_price'],
            'action': 'This is your ideal price. Hold firm here with strong justification.'
        },
        {
            'phase': 'Phase 4 — Walk Away Price',
            'price': results['walkaway_price'],
            'action': 'Maximum you should pay. If seller exceeds this, walk away.'
        }
    ]

    # Overall negotiation power
    power_score = 50
    if inputs['days_on_market'] > 60: power_score += 15
    if inputs['price_vs_market'] > 5: power_score += 15
    if inputs['legal_issues'] > 0: power_score += 20
    if inputs['motivated_seller']: power_score += 15
    if inputs['infrastructure_gaps'] > 3: power_score += 10
    results['negotiation_power'] = min(100, power_score)

    return results

st.markdown("---")

tab1, tab2 = st.tabs(["📝 Analyze Deal", "🧪 Demo Analysis"])

with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**💰 Price Information**")
        asking_price = st.number_input("Seller's Asking Price (₹)", min_value=100000, max_value=100000000, value=5000000, step=100000)
        price_vs_market = st.slider("Price Above Market Rate (%)", 0, 50, 10)
        days_on_market = st.number_input("Days Property on Market", min_value=1, max_value=365, value=75)

    with col2:
        st.write("**⚠️ Property Issues**")
        legal_issues = st.slider("Number of Legal Issues Found", 0, 5, 1)
        infrastructure_gaps = st.slider("Infrastructure Gaps (1-10)", 1, 10, 4)
        motivated_seller = st.checkbox("Seller Appears Motivated (urgent sale)", value=True)

    with col3:
        st.write("**📍 Market Context**")
        market_trend = st.selectbox("Current Market Trend", ["Rising", "Stable", "Declining"])
        buyer_competition = st.slider("Other Buyers Competing (0=None, 10=Many)", 0, 10, 2)
        your_urgency = st.selectbox("Your Purchase Urgency", ["Low", "Medium", "High"])

    if st.button("🎯 Generate Negotiation Strategy", type="primary"):
        inputs = {
            'asking_price': asking_price,
            'price_vs_market': price_vs_market,
            'days_on_market': days_on_market,
            'legal_issues': legal_issues,
            'infrastructure_gaps': infrastructure_gaps,
            'motivated_seller': motivated_seller,
        }

        results = generate_negotiation_strategy(inputs)

        st.markdown("---")

        # Power score
        power = results['negotiation_power']
        power_color = "🟢" if power >= 70 else "🟡" if power >= 40 else "🔴"
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Asking Price", f"₹{asking_price:,.0f}")
        with col2:
            st.metric("Fair Market Value", f"₹{results['fair_value']:,.0f}")
        with col3:
            st.metric("Your Target Price", f"₹{results['target_price']:,.0f}")
        with col4:
            st.metric("Negotiation Power", f"{power_color} {power}/100")

        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            # Negotiation phases chart
            phases_df = pd.DataFrame(results['phases'])
            fig = px.bar(
                x=[p['phase'] for p in results['phases']],
                y=[p['price'] for p in results['phases']],
                title="Negotiation Price Phases",
                color=[p['price'] for p in results['phases']],
                color_continuous_scale='RdYlGn'
            )
            fig.add_hline(y=asking_price, line_dash="dash", line_color="red",
                         annotation_text="Asking Price")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📋 Negotiation Phases")
            for phase in results['phases']:
                st.write(f"**{phase['phase']}:** ₹{phase['price']:,.0f}")
                st.caption(phase['action'])
                st.markdown("---")

        st.subheader("🎯 Recommended Negotiation Tactics")
        for tactic in results['tactics']:
            strength_color = "🔴" if tactic['strength'] == 'Very High' else "🟠" if tactic['strength'] == 'High' else "🟡"
            with st.expander(f"{tactic['tactic']} — Strength: {strength_color} {tactic['strength']}"):
                st.write(tactic['description'])

        if results['adjustments']:
            st.subheader("💡 Price Adjustment Justifications")
            for adj_name, adj_value, reason in results['adjustments']:
                st.write(f"• **{adj_name}:** ₹{adj_value:,.0f} ({reason})")

with tab2:
    st.info("Demo: Negotiating a plot near Patia, Bhubaneswar")
    if st.button("🚀 Run Demo", type="primary"):
        demo_inputs = {
            'asking_price': 4500000,
            'price_vs_market': 12,
            'days_on_market': 95,
            'legal_issues': 1,
            'infrastructure_gaps': 4,
            'motivated_seller': True,
        }
        results = generate_negotiation_strategy(demo_inputs)

        power = results['negotiation_power']
        power_color = "🟢" if power >= 70 else "🟡" if power >= 40 else "🔴"

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Asking Price", "₹45,00,000")
        with col2:
            st.metric("Fair Market Value", f"₹{results['fair_value']:,.0f}")
        with col3:
            st.metric("Your Target Price", f"₹{results['target_price']:,.0f}")
        with col4:
            st.metric("Negotiation Power", f"{power_color} {power}/100")

        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            fig = px.bar(
                x=[p['phase'] for p in results['phases']],
                y=[p['price'] for p in results['phases']],
                title="Bhubaneswar Plot — Negotiation Phases",
                color=[p['price'] for p in results['phases']],
                color_continuous_scale='RdYlGn'
            )
            fig.add_hline(y=4500000, line_dash="dash", line_color="red",
                         annotation_text="Asking Price")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📋 Negotiation Phases")
            for phase in results['phases']:
                st.write(f"**{phase['phase']}:** ₹{phase['price']:,.0f}")
                st.caption(phase['action'])
                st.markdown("---")

        st.subheader("🎯 Recommended Tactics")
        for tactic in results['tactics']:
            strength_color = "🔴" if tactic['strength'] == 'Very High' else "🟠" if tactic['strength'] == 'High' else "🟡"
            with st.expander(f"{tactic['tactic']} — {strength_color} {tactic['strength']}"):
                st.write(tactic['description'])
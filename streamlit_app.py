import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

# Page config
st.set_page_config(
    page_title="AT Market Intelligence",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for glossy styling
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .metric-title {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-subtitle {
        font-size: 0.85rem;
        opacity: 0.8;
    }
    
    .health-indicator {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
    }
    
    .health-green { background-color: #27ae60; }
    .health-amber { background-color: #f39c12; }
    .health-red { background-color: #e74c3c; }
    
    .trend-up { color: #27ae60; }
    .trend-down { color: #e74c3c; }
    .trend-neutral { color: #f39c12; }
    
    .warning-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
        color: #856404;
    }
    
    .innovation-tag {
        background-color: #e8f4fd;
        color: #2980b9;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        margin: 2px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Sample data generation
def generate_sample_data():
    """Generate realistic sample data for the AT market"""
    
    # Market segments
    segments = [
        "Mobility Aids", "Communication Devices", "Vision Equipment", 
        "Hearing Equipment", "Personal Care", "Home Modifications",
        "Vehicle Modifications", "Prosthetics", "Orthotics",
        "Workplace Equipment", "Recreation Equipment", "Smart Home Tech", "Therapy Equipment"
    ]
    
    # Generate market data
    market_data = []
    for segment in segments:
        data = {
            'segment': segment,
            'market_value': np.random.randint(50, 600),  # Million dollars
            'growth_rate': np.random.uniform(-2, 15),
            'participants': np.random.randint(5000, 95000),
            'wait_days': np.random.randint(12, 35),
            'price_inflation': np.random.uniform(-1, 8),
            'provider_count': np.random.randint(45, 400),
            'satisfaction': np.random.uniform(3.5, 4.8),
            'return_rate': np.random.uniform(0.5, 3.2),
            'safety_incidents': np.random.uniform(0.1, 1.5),
            'new_products': np.random.randint(5, 50),
            'market_concentration': np.random.randint(25, 75),
            'metro_pct': np.random.randint(65, 85),
            'regional_pct': np.random.randint(15, 30),
            'atsi_pct': np.random.randint(5, 15)
        }
        market_data.append(data)
    
    return pd.DataFrame(market_data)

def get_health_status(value, thresholds, reverse=False):
    """Determine health status based on thresholds"""
    if reverse:
        if value <= thresholds[0]:
            return "green", "🟢"
        elif value <= thresholds[1]:
            return "amber", "🟡"
        else:
            return "red", "🔴"
    else:
        if value >= thresholds[1]:
            return "green", "🟢"
        elif value >= thresholds[0]:
            return "amber", "🟡"
        else:
            return "red", "🔴"

def create_trend_chart(data, title):
    """Create a mini trend chart"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(len(data))),
        y=data,
        mode='lines+markers',
        line=dict(color='#3498db', width=3),
        marker=dict(size=6, color='white', line=dict(color='#3498db', width=2)),
        fill='tonexty',
        fillcolor='rgba(52, 152, 219, 0.1)'
    ))
    
    fig.update_layout(
        height=120,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

# Main app
def main():
    # Header with dynamic segment title
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); 
                padding: 2rem; margin: -1rem -1rem 2rem -1rem; color: white;'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <h1 style='margin: 0; font-size: 2.5rem;'>{selected_segment} Market Overview</h1>
                <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Q2 2025 • {segment_subcategories.get(selected_segment, "Assistive Technology Segment")}</p>
            </div>
            <div style='background: #9b59b6; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold;'>
                NDIS
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    df = generate_sample_data()
    
    # Sidebar for segment selection
    st.sidebar.header("Market Segment")
    selected_segment = st.sidebar.selectbox(
        "Choose AT Market Segment:",
        df['segment'].tolist(),
        index=0
    )
    
    # Filter data for selected segment
    segment_data = df[df['segment'] == selected_segment].iloc[0]
    
    # Get segment-specific subcategories for display
    segment_subcategories = {
        "Mobility Aids": "Wheelchairs, Scooters, Walking Aids, Standing Frames",
        "Communication Devices": "Speech Devices, Tablets, Communication Apps, Voice Output",
        "Vision Equipment": "Magnifiers, Screen Readers, Navigation Aids, Smart Glasses",
        "Hearing Equipment": "Hearing Aids, FM Systems, Assistive Listening, Cochlear Implants",
        "Personal Care": "Bathroom Aids, Dressing Aids, Eating Utensils, Hygiene Products",
        "Home Modifications": "Ramps, Rails, Accessible Fixtures, Door Modifications",
        "Vehicle Modifications": "Hand Controls, Wheelchair Lifts, Pedal Extensions, Steering Aids",
        "Prosthetics": "Upper Limb, Lower Limb, Myoelectric, Cosmetic Prosthetics",
        "Orthotics": "Braces, Supports, Therapeutic Footwear, Spinal Orthoses",
        "Workplace Equipment": "Ergonomic Aids, Computer Access, Desk Modifications, Seating",
        "Recreation Equipment": "Sports Wheelchairs, Adaptive Sports, Exercise Equipment, Games",
        "Smart Home Tech": "IoT Devices, Home Automation, Environmental Controls, Safety Systems",
        "Therapy Equipment": "Exercise Equipment, Positioning Aids, Sensory Tools, Mobility Training"
    }
    
    # Add export options
    st.sidebar.markdown("---")
    st.sidebar.header("Export Options")
    if st.sidebar.button("📊 Export to PDF"):
        st.sidebar.success("PDF export initiated!")
    if st.sidebar.button("📈 Export Data"):
        st.sidebar.download_button(
            label="Download CSV",
            data=df.to_csv(index=False),
            file_name=f"at_market_data_{datetime.date.today()}.csv",
            mime="text/csv"
        )
    
    # Main dashboard layout
    col1, col2, col3 = st.columns(3)
    
    # Row 1: Market Size, Participants, Service Delivery
    with col1:
        health_color, health_icon = get_health_status(segment_data['growth_rate'], [5, 10])
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Market Value</div>
            <div class="metric-value">${segment_data['market_value']}M</div>
            <div class="metric-subtitle trend-{'up' if segment_data['growth_rate'] > 0 else 'down'}">
                {'↗' if segment_data['growth_rate'] > 0 else '↘'} {segment_data['growth_rate']:.1f}% growth YoY
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Mini trend chart
        trend_data = [segment_data['market_value'] * (1 + np.random.uniform(-0.1, 0.1)) for _ in range(5)]
        fig = create_trend_chart(trend_data, "Market Growth")
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        health_color, health_icon = get_health_status(segment_data['participants'], [20000, 50000])
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Active Participants</div>
            <div class="metric-value">{segment_data['participants']:,}</div>
            <div class="metric-subtitle">
                Metro: {segment_data['metro_pct']}% | Regional: {segment_data['regional_pct']}%<br>
                ATSI: {segment_data['atsi_pct']}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Geographic breakdown pie chart
        geo_fig = go.Figure(data=[go.Pie(
            labels=['Metro', 'Regional', 'Remote'],
            values=[segment_data['metro_pct'], segment_data['regional_pct'], 100-segment_data['metro_pct']-segment_data['regional_pct']],
            hole=0.6,
            marker=dict(colors=['#3498db', '#e74c3c', '#f39c12'])
        )])
        geo_fig.update_layout(height=120, margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
        st.plotly_chart(geo_fig, use_container_width=True, config={'displayModeBar': False})
    
    with col3:
        health_color, health_icon = get_health_status(segment_data['wait_days'], [21, 14], reverse=True)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Service Delivery</div>
            <div class="metric-value">{segment_data['wait_days']:.0f} days</div>
            <div class="metric-subtitle">
                Avg. approval to delivery<br>Target: 14 days
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if segment_data['wait_days'] > 21:
            st.markdown("""
            <div class="warning-box">
                ⚠️ Delivery delays above target - investigate supply chain
            </div>
            """, unsafe_allow_html=True)
    
    # Row 2: Price Trends, Competition, Quality
    col4, col5, col6 = st.columns(3)
    
    with col4:
        health_color, health_icon = get_health_status(segment_data['price_inflation'], [2, 4], reverse=True)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Price Trends</div>
            <div class="metric-value trend-{'up' if segment_data['price_inflation'] > 0 else 'down'}">
                {'+' if segment_data['price_inflation'] > 0 else ''}{segment_data['price_inflation']:.1f}%
            </div>
            <div class="metric-subtitle">
                Inflation rate (12 months)<br>CPI: +4.1%
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        health_color, health_icon = get_health_status(segment_data['market_concentration'], [50, 70], reverse=True)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Market Competition</div>
            <div class="metric-value">{segment_data['provider_count']}</div>
            <div class="metric-subtitle">
                Active providers<br>Top 5 = {segment_data['market_concentration']}% market share
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if segment_data['market_concentration'] > 60:
            st.markdown("""
            <div class="warning-box">
                ⚠️ High market concentration - monitor for competition issues
            </div>
            """, unsafe_allow_html=True)
    
    with col6:
        health_color, health_icon = get_health_status(segment_data['satisfaction'], [3.5, 4.0])
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Quality & Satisfaction</div>
            <div class="metric-value">{segment_data['satisfaction']:.1f}</div>
            <div class="metric-subtitle">
                Satisfaction (out of 5)<br>
                Return rate: {segment_data['return_rate']:.1f}%
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quality metrics gauge
        quality_fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = segment_data['satisfaction'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Satisfaction"},
            gauge = {
                'axis': {'range': [None, 5]},
                'bar': {'color': "#27ae60"},
                'steps': [
                    {'range': [0, 2.5], 'color': "#e74c3c"},
                    {'range': [2.5, 3.5], 'color': "#f39c12"},
                    {'range': [3.5, 5], 'color': "#27ae60"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 4.0
                }
            }
        ))
        quality_fig.update_layout(height=120, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(quality_fig, use_container_width=True, config={'displayModeBar': False})
    
    # Row 3: Innovation, Benchmarking, Outlook
    col7, col8, col9 = st.columns(3)
    
    with col7:
        health_color, health_icon = get_health_status(segment_data['new_products'], [10, 25])
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{health_icon} Innovation Trends</div>
            <div class="metric-value">{segment_data['new_products']}</div>
            <div class="metric-subtitle">
                New products this quarter<br>
                15% feature smart technology
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Innovation tags
        innovation_tags = ["IoT Sensors", "AI Integration", "App Connectivity", "Predictive Analytics"]
        tags_html = "".join([f'<span class="innovation-tag">{tag}</span>' for tag in innovation_tags])
        st.markdown(f'<div style="margin-top: 10px;">{tags_html}</div>', unsafe_allow_html=True)
    
    with col8:
        benchmark_status = "Above" if np.random.random() > 0.5 else "Below"
        benchmark_color = "trend-down" if benchmark_status == "Above" else "trend-up"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🌏 Global Benchmark</div>
            <div class="metric-value {benchmark_color}">+12%</div>
            <div class="metric-subtitle">
                {benchmark_status} UK NHS prices<br>
                On par with US Medicare
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Benchmark comparison chart
        countries = ['Australia', 'UK', 'US', 'Canada']
        prices = [100, 88, 102, 95]  # Index: Australia = 100
        
        benchmark_fig = go.Figure(data=[
            go.Bar(x=countries, y=prices, marker_color=['#e74c3c', '#27ae60', '#f39c12', '#3498db'])
        ])
        benchmark_fig.update_layout(
            height=120, 
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=False,
            yaxis=dict(showgrid=False, showticklabels=False),
            xaxis=dict(showgrid=False)
        )
        st.plotly_chart(benchmark_fig, use_container_width=True, config={'displayModeBar': False})
    
    with col9:
        outlook = np.random.choice(["Strong", "Stable", "Cautious"])
        outlook_color = {"Strong": "trend-up", "Stable": "trend-neutral", "Cautious": "trend-down"}[outlook]
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🔮 Market Outlook</div>
            <div class="metric-value {outlook_color}">{outlook}</div>
            <div class="metric-subtitle">
                Growing demand<br>
                Stable supply chain
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Outlook indicators
        outlook_items = [
            "✓ New provider entries",
            "✓ Innovation investment up 23%", 
            "⚠ Skills shortage in regional areas"
        ]
        for item in outlook_items:
            color = "#27ae60" if item.startswith("✓") else "#f39c12"
            st.markdown(f'<div style="font-size: 0.8rem; color: {color}; margin: 2px 0;">{item}</div>', 
                       unsafe_allow_html=True)
    
    # Market comparison section
    st.markdown("---")
    st.header("📊 Cross-Segment Comparison")
    
    # Create comparison metrics
    comparison_metrics = st.columns(4)
    
    with comparison_metrics[0]:
        st.metric("Market Value Rank", "3rd", "↑ 1 position")
    
    with comparison_metrics[1]:
        st.metric("Growth Rate Rank", "5th", "↓ 2 positions") 
    
    with comparison_metrics[2]:
        st.metric("Satisfaction Rank", "2nd", "↑ 3 positions")
    
    with comparison_metrics[3]:
        st.metric("Innovation Rank", "7th", "→ No change")
    
    # Market comparison chart
    fig_comparison = px.scatter(
        df, 
        x='market_value', 
        y='growth_rate',
        size='participants',
        color='satisfaction',
        hover_name='segment',
        title="Market Size vs Growth Rate (Bubble size = Participants, Color = Satisfaction)",
        labels={
            'market_value': 'Market Value ($M)',
            'growth_rate': 'Growth Rate (%)',
            'satisfaction': 'Satisfaction Score'
        }
    )
    
    # Highlight selected segment
    fig_comparison.add_scatter(
        x=[segment_data['market_value']], 
        y=[segment_data['growth_rate']],
        mode='markers',
        marker=dict(size=20, color='red', symbol='star'),
        name=f'{selected_segment} (Selected)',
        showlegend=True
    )
    
    fig_comparison.update_layout(height=500)
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Data table
    with st.expander("📋 Detailed Market Data"):
        st.dataframe(df.round(2))

if __name__ == "__main__":
    main()

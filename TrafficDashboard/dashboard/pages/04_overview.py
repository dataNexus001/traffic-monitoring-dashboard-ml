import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Overview', layout='wide')

st.markdown("""
<style>
[data-testid='stSidebar'] { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); }
[data-testid='stSidebarNav'] a { color: #ffffff !important; font-size: 15px !important;
    font-weight: 500; padding: 10px 15px; border-radius: 8px; text-transform: capitalize; }
[data-testid='stSidebarNav'] a:hover { background: rgba(0,212,255,0.15) !important; color: #00d4ff !important; }
[data-testid='stSidebarNav'] a[aria-selected='true'] { background: rgba(0,212,255,0.2) !important; border-left: 3px solid #00d4ff; }
.block-container { padding: 2rem 3rem; }
.page-title { font-size: 2em; font-weight: 800; color: #00d4ff; margin-bottom: 5px; }
.section-title { color: #aaaaaa; font-size: 1em; margin-bottom: 25px; }
.metric-card { background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid rgba(0,212,255,0.2); border-radius: 15px;
    padding: 20px; text-align: center; margin-bottom: 20px; }
.metric-card h2 { color: #00d4ff; font-size: 2em; margin: 0; }
.metric-card p { color: #888; font-size: 0.85em; margin: 5px 0 0 0; }
</style>
""", unsafe_allow_html=True)

df = pd.read_csv('data/traffic_cleaned.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

st.markdown('<div class="page-title">Full Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Everything at a glance</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-card"><h2>{len(df):,}</h2><p>Total Records</p></div>',
                unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><h2>{df["traffic_volume"].mean():.0f}</h2><p>Avg Volume</p></div>',
                unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><h2>{df["traffic_volume"].max():,}</h2><p>Peak Volume</p></div>',
                unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="metric-card"><h2>{df["hour"].mode()[0]}</h2><p>Busiest Hour</p></div>',
                unsafe_allow_html=True)

st.markdown('---')
col1, col2 = st.columns(2)
with col1:
    hourly = df.groupby('hour')['traffic_volume'].mean().reset_index()
    fig = px.line(hourly, x='hour', y='traffic_volume', title='Traffic by Hour',
                  markers=True, template='plotly_dark')
    fig.update_traces(line_color='#00d4ff')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
with col2:
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    daily = df.groupby('day_of_week')['traffic_volume'].mean().reset_index()
    daily['day'] = daily['day_of_week'].apply(lambda x: days[x])
    fig = px.bar(daily, x='day', y='traffic_volume', title='Traffic by Day',
                 color='traffic_volume', color_continuous_scale='Blues', template='plotly_dark')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    weather_df = df.groupby('weather_main')['traffic_volume'].mean().reset_index()
    fig = px.bar(weather_df, x='weather_main', y='traffic_volume', title='Traffic by Weather',
                 color='traffic_volume', color_continuous_scale='RdYlGn', template='plotly_dark')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
with col4:
    monthly = df.groupby('month')['traffic_volume'].mean().reset_index()
    fig = px.line(monthly, x='month', y='traffic_volume', title='Traffic by Month',
                  markers=True, template='plotly_dark')
    fig.update_traces(line_color='#7b2ff7')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

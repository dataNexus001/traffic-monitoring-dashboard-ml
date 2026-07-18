import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Home', layout='wide')

st.markdown("""
<style>
[data-testid='stSidebar'] { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); }
[data-testid='stSidebarNav'] a { color: #ffffff !important; font-size: 15px !important;
    font-weight: 500; padding: 10px 15px; border-radius: 8px; text-transform: capitalize; }
[data-testid='stSidebarNav'] a:hover { background: rgba(0,212,255,0.15) !important; color: #00d4ff !important; }
[data-testid='stSidebarNav'] a[aria-selected='true'] { background: rgba(0,212,255,0.2) !important; border-left: 3px solid #00d4ff; }
.block-container { padding: 2rem 3rem; }
.metric-card { background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid rgba(0,212,255,0.2); border-radius: 15px;
    padding: 25px; text-align: center; margin-bottom: 20px; }
.metric-card h2 { color: #00d4ff; font-size: 2.2em; margin: 0; }
.metric-card p { color: #888; font-size: 0.9em; margin: 5px 0 0 0; }
.page-title { font-size: 2em; font-weight: 800; color: #00d4ff; margin-bottom: 5px; }
.section-title { color: #aaaaaa; font-size: 1em; margin-bottom: 25px; }
</style>
""", unsafe_allow_html=True)

df = pd.read_csv('data/traffic_cleaned.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

st.markdown('<div class="page-title">Traffic Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Live metrics from Metro Interstate Traffic Volume dataset</div>',
            unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="metric-card"><h2>{len(df):,}</h2><p>Total Records</p></div>',
                unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><h2>{df["traffic_volume"].mean():.0f}</h2><p>Avg Traffic Volume</p></div>',
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
    fig = px.line(hourly, x='hour', y='traffic_volume',
                  title='Average Traffic Volume by Hour',
                  labels={'hour': 'Hour of Day', 'traffic_volume': 'Avg Volume'},
                  markers=True, template='plotly_dark')
    fig.update_traces(line_color='#00d4ff')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    daily = df.groupby('day_of_week')['traffic_volume'].mean().reset_index()
    daily['day'] = daily['day_of_week'].apply(lambda x: days[x])
    fig2 = px.bar(daily, x='day', y='traffic_volume',
                  title='Average Traffic by Day of Week',
                  labels={'day': 'Day', 'traffic_volume': 'Avg Volume'},
                  template='plotly_dark', color='traffic_volume',
                  color_continuous_scale='Blues')
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

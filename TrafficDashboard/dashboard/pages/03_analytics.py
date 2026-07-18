import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Analytics', layout='wide')

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
</style>
""", unsafe_allow_html=True)

df = pd.read_csv('data/traffic_cleaned.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

st.markdown('<div class="page-title">Traffic Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Explore traffic patterns across time and weather</div>',
            unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(['By Day', 'By Weather', 'By Month', 'Weekend vs Weekday'])

with tab1:
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    daily = df.groupby('day_of_week')['traffic_volume'].mean().reset_index()
    daily['day'] = daily['day_of_week'].apply(lambda x: days[x])
    fig = px.bar(daily, x='day', y='traffic_volume',
                 title='Average Traffic Volume by Day of Week',
                 color='traffic_volume', color_continuous_scale='Blues', template='plotly_dark')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    weather = df.groupby('weather_main')['traffic_volume'].mean().reset_index()
    weather = weather.sort_values('traffic_volume', ascending=False)
    fig = px.bar(weather, x='weather_main', y='traffic_volume',
                 title='Average Traffic Volume by Weather Condition',
                 color='traffic_volume', color_continuous_scale='RdYlGn', template='plotly_dark')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    monthly = df.groupby('month')['traffic_volume'].mean().reset_index()
    fig = px.line(monthly, x='month', y='traffic_volume',
                  title='Average Traffic Volume by Month',
                  markers=True, template='plotly_dark')
    fig.update_traces(line_color='#00d4ff')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    weekend = df.groupby('is_weekend')['traffic_volume'].mean().reset_index()
    weekend['type'] = weekend['is_weekend'].map({0: 'Weekday', 1: 'Weekend'})
    fig = px.bar(weekend, x='type', y='traffic_volume',
                 title='Weekday vs Weekend Traffic Volume',
                 color='type',
                 color_discrete_map={'Weekday':'#00d4ff','Weekend':'#7b2ff7'},
                 template='plotly_dark')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
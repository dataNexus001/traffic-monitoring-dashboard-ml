import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title='Prediction', layout='wide')

st.markdown("""
<style>
[data-testid='stSidebar'] { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); }
[data-testid='stSidebarNav'] a {
    color: #ffffff !important;
    font-size: 15px !important;
    font-weight: 500;
    padding: 10px 15px;
    border-radius: 8px;
    text-transform: capitalize;
}
[data-testid='stSidebarNav'] a:hover { background: rgba(0,212,255,0.15) !important; color: #00d4ff !important; }
[data-testid='stSidebarNav'] a[aria-selected='true'] { background: rgba(0,212,255,0.2) !important; border-left: 3px solid #00d4ff; }
.block-container { padding: 2rem 3rem; }
.page-title { font-size: 2em; font-weight: 800; color: #00d4ff; margin-bottom: 5px; }
.section-title { color: #aaaaaa; font-size: 1em; margin-bottom: 25px; }
.result-box {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid rgba(0, 212, 255, 0.3);
    border-radius: 15px;
    padding: 40px;
    text-align: center;
    margin-top: 20px;
}
.result-number { font-size: 3.5em; font-weight: 800; color: #00d4ff; }
.result-label { color: #888; font-size: 1em; margin-top: 5px; }
.status-heavy { color: #ff4444; font-size: 1.5em; font-weight: bold; margin-top: 15px; }
.status-moderate { color: #ffaa00; font-size: 1.5em; font-weight: bold; margin-top: 15px; }
.status-light { color: #00ff88; font-size: 1.5em; font-weight: bold; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

with open('models/traffic_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('models/le_weather.pkl', 'rb') as f:
    le_weather = pickle.load(f)

st.markdown('<div class="page-title">Traffic Volume Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Adjust the parameters to get an instant prediction</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('##### Input Parameters')
    hour = st.slider('Hour of Day', 0, 23, 8)
    day = st.selectbox('Day of Week', ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
    month = st.slider('Month', 1, 12, 6)
    weather = st.selectbox('Weather Condition', le_weather.classes_)
    temp = st.slider('Temperature (Kelvin)', 240, 320, 280)
    rain = st.slider('Rain 1h (mm)', 0.0, 10.0, 0.0)
    snow = st.slider('Snow 1h (mm)', 0.0, 1.0, 0.0)
    clouds = st.slider('Cloud Cover (%)', 0, 100, 40)

with col2:
    st.markdown('##### Prediction Result')
    day_map = {'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}
    is_weekend = 1 if day in ['Sat','Sun'] else 0
    weather_enc = le_weather.transform([weather])[0]
    features = [[hour, day_map[day], month, is_weekend,
                 temp, rain, snow, clouds, weather_enc, 0]]
    prediction = model.predict(features)[0]

    if prediction > 4000:
        status = '<div class="status-heavy">Heavy Traffic</div>'
    elif prediction > 2000:
        status = '<div class="status-moderate">Moderate Traffic</div>'
    else:
        status = '<div class="status-light">Light Traffic</div>'

    st.markdown(f'''
    <div class="result-box">
        <div class="result-number">{prediction:.0f}</div>
        <div class="result-label">Predicted Vehicles / Hour</div>
        <br>{status}
    </div>''', unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    st.info(f'{day} at {hour:02d}:00 — {weather} weather — {"Weekend" if is_weekend else "Weekday"}')
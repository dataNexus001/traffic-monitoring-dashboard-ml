import streamlit as st

st.set_page_config(
    page_title='Traffic Monitoring Dashboard',
    page_icon='🚦',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
}
[data-testid="stSidebarNav"] a {
    color: #ffffff !important;
    font-size: 15px !important;
    font-weight: 500;
    padding: 10px 15px;
    border-radius: 8px;
    text-transform: capitalize;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(0, 212, 255, 0.15) !important;
    color: #00d4ff !important;
}
.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
.full-page {
    height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.hero {
    background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #0f3460 100%);
    padding: 40px 40px;
    margin: 20px;
    border-radius: 15px;
    border: 1px solid rgba(0, 212, 255, 0.15);
    text-align: center;
    border-bottom: 1px solid rgba(0, 212, 255, 0.2);
    width: 100%;
    animation: fadeInDown 1s ease;
}
.hero h1 {
    font-size: 3em;
    font-weight: 800;
    background: linear-gradient(90deg, #00d4ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}
.hero p { color: #aaaaaa; font-size: 1.2em; margin: 5px 0; }
.cards-wrapper {
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 30px 40px;
    width: 100%;
}
.nav-card {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid rgba(0, 212, 255, 0.15);
    border-radius: 12px;          /* ← add this */
    padding: 40px 20px;
    text-align: center;
    flex: 1;
    cursor: pointer;
    text-decoration: none !important;
    display: block;
    transition: all 0.3s ease;
}
.nav-card:hover {
    background: linear-gradient(135deg, #0f3460, #1a1a2e);
    box-shadow: inset 0 -3px 0 #00d4ff;
}
.nav-card h3 { color: #00d4ff; margin: 0 0 8px 0; font-size: 1.2em; }
.nav-card p { color: #888; font-size: 0.85em; margin: 0; }
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>

<div class="full-page">
    <div class="hero">
        <h1>Traffic Monitoring Dashboard</h1>
        <p>Predictive Traffic Analysis using Machine Learning</p>
        <p style="color:#555; font-size:0.85em; margin-top:8px;">Metro Interstate Traffic Volume — Real Data Analysis</p>
    </div>
    <div class="cards-wrapper">
        <a href="/home" target="_self" class="nav-card">
            <h3>Home</h3>
            <p>Live metrics and traffic overview</p>
        </a>
        <a href="/prediction" target="_self" class="nav-card">
            <h3>Prediction</h3>
            <p>Predict traffic volume with ML</p>
        </a>
        <a href="/analytics" target="_self" class="nav-card">
            <h3>Analytics</h3>
            <p>Explore patterns and trends</p>
        </a>
        <a href="/overview" target="_self" class="nav-card">
            <h3>Overview</h3>
            <p>Full dashboard at a glance</p>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
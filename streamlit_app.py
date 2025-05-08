import streamlit as st

# --- MUST BE FIRST Streamlit command ---
st.set_page_config(page_title="Josue Ordonez - Portfolio", layout="centered")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #212529; font-size: 16px;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: auto;
    }
    .section-title {
        color: #003366;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .section-content {
        margin-bottom: 20px;
    }
    .project-link {
        color: #003366;
        text-decoration: none;
        font-weight: bold;
    }
    .project-link:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# --- Page Title ---
st.title("Josue Ordonez - Portfolio")

# --- Professional Summary ---
st.markdown("<div class='section-title'>Professional Summary</div>", unsafe_allow_html=True)
st.markdown("<div class='section-content'>Experienced sales manager and options trader with over 22 years in customer relations, team management, and data analysis. Skilled in building automated solutions using Python and Streamlit to streamline processes and enhance decision-making. Currently transitioning to a tech-focused role to leverage expertise in data analysis and financial trading.</div>", unsafe_allow_html=True)

# --- Skills and Technologies ---
st.markdown("<div class='section-title'>Skills and Technologies</div>", unsafe_allow_html=True)
st.markdown("""<div class='section-content'>
<ul>
    <li>Python, Pandas, Streamlit, Matplotlib</li>
    <li>API Integrations and Data Automation</li>
    <li>Options Trading Strategies and Data Analysis</li>
    <li>Customer Relationship Management</li>
    <li>Web App Development and Data Visualization</li>
</ul>
</div>""", unsafe_allow_html=True)

# --- Projects Section ---
st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)
st.markdown("""<div class='section-content'>
<ul>
    <li><a href='https://conferencecall.streamlit.app' class='project-link'>Conference Call App</a>: Manage and track conference calls with automated scheduling and tracking features.</li>
    <li><a href='https://wzmetrics.streamlit.app' class='project-link'>WZ Metrics Dashboard</a>: Visualize and analyze sales performance metrics with dynamic data insights.</li>
    <li><a href='https://spywheelscreener.streamlit.app' class='project-link'>SPY Wheel Screener</a>: Identify optimal SPY wheel strategy setups with data filtering and screening tools.</li>
</ul>
</div>""", unsafe_allow_html=True)

# --- Career Goals ---
st.markdown("<div class='section-title'>Career Goals</div>", unsafe_allow_html=True)
st.markdown("""<div class='section-content'>
<p>Transitioning to a data-focused role where I can build and manage automated systems for financial trading and business analytics. Seeking opportunities to apply skills in data analysis, Python, and options trading to drive actionable insights and operational efficiency.</p>
</div>""", unsafe_allow_html=True)

# --- Contact Information ---
st.markdown("<div class='section-title'>Contact Information</div>", unsafe_allow_html=True)
st.markdown("""<div class='section-content'>
<ul>
    <li>ð§ Email: ordonezjosue@gmail.com</li>
    <li>ð LinkedIn: <a href='https://www.linkedin.com/in/josue-ordonez-7843192a' class='project-link'>Connect with me on LinkedIn</a></li>
</ul>
</div>""", unsafe_allow_html=True)

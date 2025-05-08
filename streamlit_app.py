import streamlit as st

# --- MUST BE FIRST Streamlit command ---
st.set_page_config(page_title="Josue Ordonez - Portfolio", layout="centered")

# --- Page Title ---
st.title("Josue Ordonez - Portfolio")

# --- Professional Summary ---
st.header("Professional Summary")
st.write("""
Experienced sales manager and options trader with over 22 years in customer relations, 
team management, and data analysis. Skilled in building automated solutions using Python 
and Streamlit to streamline processes and enhance decision-making. Currently transitioning 
to a tech-focused role to leverage expertise in data analysis and financial trading.
""")

# --- Skills and Technologies ---
st.header("Skills and Technologies")
st.write("""
- Python, Pandas, Streamlit, Matplotlib  
- API Integrations and Data Automation  
- Options Trading Strategies and Data Analysis  
- Customer Relationship Management  
- Web App Development and Data Visualization  
""")

# --- Projects Section ---
st.header("Projects")
st.write("""
- [Conference Call App](https://conferencecall.streamlit.app): Manage and track conference calls with automated scheduling and tracking features.  
- [WZ Metrics Dashboard](https://wzmetrics.streamlit.app): Visualize and analyze sales performance metrics with dynamic data insights.  
- [SPY Wheel Screener](https://spywheelscreener.streamlit.app): Identify optimal SPY wheel strategy setups with data filtering and screening tools.  
""")

# --- Career Goals ---
st.header("Career Goals")
st.write("""
Transitioning to a data-focused role where I can build and manage automated systems for financial 
trading and business analytics. Seeking opportunities to apply skills in data analysis, Python, 
and options trading to drive actionable insights and operational efficiency.
""")

# --- Contact Information ---
st.header("Contact Information")
st.write("""
- 📧 Email: ordonezjosue@gmail.com  
- 🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/josue-ordonez-7843192a)  
""")
import streamlit as st
from streamlit.web.server import Server

# Your existing page setup
home_page = st.Page("st_pages/home.py", title="Home", icon="🏠")
tools_page = st.Page("st_pages/tools.py", title="Tools", icon="🪛")
analysis_page = st.Page("st_pages/stats.py", title="Stats", icon="📊")

pg = st.navigation([home_page, tools_page, analysis_page])
st.set_page_config(
    page_title="COCO-ML-TOOLBOX",
    page_icon=":rocket",
)

# Override headers AFTER initializing the app
def override_headers():
    server = Server.get_current()
    if server is not None:
        server._headers = {
            "X-Frame-Options": "ALLOW-FROM https://data-up.io",
            "Content-Security-Policy": "frame-ancestors 'self' https://data-up.io;",
        }

# Call the function after setup
override_headers()

# Run the app
pg.run()
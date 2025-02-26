import streamlit as st
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

# --------------------------------------------------------
# Middleware to override headers
# --------------------------------------------------------
class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Frame-Options"] = "ALLOW-FROM https://data-up.io/"
        response.headers["Content-Security-Policy"] = "frame-ancestors 'self' https://data-up.io/;"
        return response

# Add middleware to Streamlit's FastAPI app
st.runtime.add_middleware(CustomHeaderMiddleware)
# --------------------------------------------------------

# Your existing Streamlit code
home_page = st.Page("st_pages/home.py", title="Home", icon="🏠")
tools_page = st.Page("st_pages/tools.py", title="Tools", icon="🪛")
analysis_page = st.Page("st_pages/stats.py", title="Stats", icon="📊")

pg = st.navigation([home_page, tools_page, analysis_page])
st.set_page_config(
    page_title="COCO-ML-TOOLBOX",
    page_icon=":rocket",
)

pg.run()
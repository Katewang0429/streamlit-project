import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title = "NASTAR", page_icon=":tada:", layout="wide" )

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load assets
lottie_coding = "https://lottie.host/9a4b412d-9cf6-45ad-8812-7ea1fed64004/3KToPQDHXa.json"
image__rescue = Image.open("images/rescuer_3.jpg")
# Header Section
with st.container():

    st.title("🛰️ NATSAR Search & Rescue Simulation Hub")  
    # st.header("Search and Rescue Sentinel")
    st.image(image__rescue)
    st.subheader("Exploring SAR Scenarios with Interactive Demos")
    st.markdown("""
                Welcome to the **NATSAR Simulation Hub**, a platform showcasing interactive 
                search and rescue (SAR) demonstrations.  
                This app highlights how technology can support SAR teams in real-world 
                scenarios through simulation, detection, and real-time alerting.  
                """)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        
# --- Brief about scenarios ---
        st.markdown("### 🚨 Scenarios to Explore")
        st.markdown("""
                - 🌊 **Lost at Sea** — Simulate maritime rescue challenges and visualize detection in open water.  
                - 🌲 **Bushland Beacon** — Track emergency signals and beacon detection in rugged bushland environments.  
                - 🔥 **Heat Signature Hunt** — Detect and analyze thermal heat signatures using multimodal inputs.  
                - 📡 **Real-Time Alerting** — Experience a live-style SAR dashboard for rapid decision-making and response.  
                """)

# --- Call to Action ---
    st.markdown("---")
    st.success("👉 Use the sidebar to navigate through the simulations and explore each scenario.")

with right_column:
     st_lottie(lottie_coding, height=300, key= "coding" )




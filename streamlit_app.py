import streamlit as st

# --- Global Config ---
st.set_page_config(page_title="SAR Object Detection", layout="centered")
# --- Landing Page Content ---
st.title("🌐 Welcome to SAR Vision Tools")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/9e/SAR_drone.jpg",
    caption="Aerial view used in SAR missions",
    width='content'
)

st.markdown("""
   
This web application helps *search and rescue teams* and *researchers* detect critical objects from images captured via *drones, bodycams, or other camera systems*.

Using computer vision, the app can:
- 🔍 Detect people, backpacks, vehicles, and equipment
- 📸 Process uploaded images from field cameras
- 📈 Display detection confidence for each object
- 💾 Optionally save results for analysis

---

### 🚀 How to Get Started

1. Go to the *Detection* page (in the sidebar)
2. Upload an image from your camera or device
3. Click "Run Detection"
4. View results with bounding boxes and confidence levels
""")

st.markdown("---")
st.markdown("© 2025 SAR Vision Tools | ")
import streamlit as st
from PIL import Image, ImageDraw
import random

# --- Page Config ---
st.set_page_config(page_title="Detection", layout="wide")
st.title("🔍 SAR Object Detection")

# --- Sidebar ---
st.sidebar.header("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

st.sidebar.header("Detection Settings")
confidence_threshold = st.sidebar.slider("Minimum Confidence", 0.0, 1.0, 0.5)
run_detection = st.sidebar.button("🔍 Run Detection")

# --- Main UI Logic ---
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width='content')

    if run_detection:
        # --- MOCK DETECTION RESULTS ---
        st.subheader("🎯 Detection Results")

        draw = ImageDraw.Draw(image)
        mock_detections = [
            {"label": "Person", "confidence": round(random.uniform(0.6, 0.95), 2), "box": [50, 50, 200, 300]},
            {"label": "Backpack", "confidence": round(random.uniform(0.5, 0.8), 2), "box": [220, 120, 320, 250]},
        ]

        filtered = [d for d in mock_detections if d["confidence"] >= confidence_threshold]

        for det in filtered:
            x1, y1, x2, y2 = det["box"]
            draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
            draw.text((x1, y1 - 10), f"{det['label']} ({det['confidence']})", fill="red")

        st.image(image, caption="Detections", use_column_width=True)

        st.markdown("#### 📋 Detected Objects")
        st.table([
            {"Label": d["label"], "Confidence": d["confidence"]}
            for d in filtered
        ])
    else:
        st.info("Click 'Run Detection' to start processing the image.")
else:
    st.warning("Please upload an image to begin.")

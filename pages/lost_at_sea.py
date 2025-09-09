# app.py
import streamlit as st
import cv2, numpy as np, pandas as pd, time

import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from ultralytics import YOLO
from utils.video_io import frame_generator, VideoWriter
from utils.ir_sim import to_ir
from utils.overlays import draw_boxes, draw_hud
from utils.inference import Detector, CachedDetections
from utils.cache import hash_config

st.set_page_config(page_title="Lost at Sea Demo", layout="wide")

# Sidebar controls
src = st.sidebar.selectbox("Video source", ["Sample 1", "Sample 2", "Upload"])
model_name = st.sidebar.selectbox("Model", ["yolov8n.pt"])
conf_thr = st.sidebar.slider("Confidence", 0.05, 0.9, 0.35, 0.01)
iou_thr  = st.sidebar.slider("NMS IoU",   0.2, 0.9, 0.5, 0.05)
stride   = st.sidebar.slider("Frame stride", 1, 5, 2, 1)
show_boxes = st.sidebar.checkbox("Show boxes", True)
show_scores = st.sidebar.checkbox("Show labels+scores", True)
show_ir = st.sidebar.checkbox("IR layer (simulated)")
low_vis = st.sidebar.checkbox("Simulate low-visibility")
trigger_alerts = st.sidebar.checkbox("Alerts", True)


# --- Resolve video path (Samples or Upload) ---
from pathlib import Path
import uuid

APP_ROOT = Path(__file__).resolve().parent.parent  # project root (one level above /pages)
DATA_DIR = APP_ROOT / "data" / "videos"
RAW_DIR = DATA_DIR / "raw"
TMP_DIR = DATA_DIR / "tmp"
RAW_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)

# Map your sample names to files you place under data/videos/raw/
SAMPLES = {
    "Sample 1": RAW_DIR / "sample1.mp4",   # <-- put a file with this name here
    "Sample 2": RAW_DIR / "sample2.mp4",   
}

uploaded_file = None
if src == "Upload":
    uploaded_file = st.sidebar.file_uploader(
        "Upload a video (mp4/mov/avi/mkv)", type=["mp4", "mov", "avi", "mkv"]
    )

# Decide the path
video_path = None
if src in ("Sample 1", "Sample 2"):
    candidate = SAMPLES[src]
    if candidate.exists():
        video_path = str(candidate)
    else:
        st.error(f"Missing sample file: {candidate.name} in {RAW_DIR}. "
                 f"Add a video there or use Upload.")
        st.stop()
elif src == "Upload":
    if uploaded_file is None:
        st.info("Upload a video from the sidebar to start.")
        st.stop()
    # Save uploaded bytes to a temp file so OpenCV can read it
    tmp_name = TMP_DIR / f"upload_{uuid.uuid4().hex}.mp4"
    with open(tmp_name, "wb") as f:
        f.write(uploaded_file.read())
    video_path = str(tmp_name)
else:
    st.error("Unknown source selection.")
    st.stop()

# Optional: ensure the selected model file exists (for custom)
# model_path = model_name
# if model_name == "custom_lifejacket.pt":
#     custom_path = APP_ROOT / "models" / "custom_lifejacket.pt"
#     if not custom_path.exists():
#         st.warning("custom_lifejacket.pt not found. Falling back to yolov8n.pt.")
#         model_path = "yolov8n.pt"

# Rebuild the detector with the resolved model path 
# Detector (with optional cache)
det = Detector(model_name, conf_thr, iou_thr)
cache = CachedDetections()

placeholder = st.empty()
events = []

fps = 0.0; last = time.time()
for i, frame in enumerate(frame_generator(video_path, stride=stride)):
    raw = frame.copy()

    # Simulate conditions
    if low_vis:
        frame = cv2.GaussianBlur(frame, (5,5), 0)
        frame = cv2.convertScaleAbs(frame, alpha=0.8, beta=-20)  # lower contrast/brightness

    view = to_ir(frame) if show_ir else frame

    # Inference (cached by video+config hash)
    key = hash_config(video_path, model_name, conf_thr, iou_thr, stride, low_vis, show_ir)
    dets = cache.get(key, i)
    if dets is None:
        dets = det.predict(view)  # returns list of (cls, conf, xyxy)
        cache.put(key, i, dets)

    # Alerts
    # (Simple example: if any person/raft/life_jacket above conf_thr, log an event)
    if trigger_alerts and any(c in ("person","raft","life_jacket") for c,_,_ in dets):
        events.append({"frame": i, "ts": time.time(), "note": "Target detected"})

    # Draw overlays
    out = view.copy()
    if show_boxes:
        out = draw_boxes(out, dets, show_scores=show_scores)
    out = draw_hud(out, fps=fps, model=model_name)

    # Show
    placeholder.image(out, channels="BGR", width='content')

    # FPS calc
    now = time.time(); fps = 1.0 / max(1e-6, (now - last)); last = now

import streamlit as st
import requests

from PIL import Image
from pathlib import Path

st.title("Lost at sea")
image__lost_at_sea = Image.open(Path(__file__).parent.parent / "images" / "rescuer.jpg")

with st.container():
    st.image(image__lost_at_sea)
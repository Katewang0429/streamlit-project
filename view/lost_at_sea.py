import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.title("Lost at sea")


image__lost_at_sea = Image.open("images/rescuer.jpg")

with st.container():
    st.image(image__lost_at_sea)
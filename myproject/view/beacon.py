import streamlit as st
from PIL import Image
from pathlib import Path

st.title("Bushland Beacon")
image__bushland_Beacon = Image.open(Path(__file__).parent.parent / "images" / "rescuer_2.jpg")

# Image display
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((2, 1))
   
    with image_column:
        st.image(image__bushland_Beacon)

    with text_column:
        st.subheader("Some header")
        st.write("""Some description """)
        st.markdown("[Video Link]")
            


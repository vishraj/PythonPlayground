import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # open the camera app on your machine
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert the image to grayscale
    gray_image = img.convert("L")

    # render the grayscale image
    st.image(gray_image)

uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_image = img.convert("L")
    st.image(gray_image)

import streamlit as st
from PIL import Image

def generate_caption(image):
    return "A person riding a motorcycle on a street."

st.set_page_config(page_title="Image Captioning Demo", layout="centered")
st.title("🖼️ Image Captioning Demo")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    caption = generate_caption(image)
    st.markdown(f"**Generated Caption:** {caption}")
else:
    st.info("Please upload an image to see the caption.")

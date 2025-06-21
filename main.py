import streamlit as st
from PIL import Image
import os

# Set Streamlit page config
st.set_page_config(layout="wide")
st.title("🧪 Clinical Trials Model Dashboard")

# Correct folder name from your project
image_folder = "dashboard_images"
image_files = sorted(os.listdir(image_folder))[:20]  # show up to 20 images

for img_file in image_files:
    feature_name = os.path.splitext(img_file)[0].replace("_", " ").title()
    st.subheader(f"🧬 Feature: {feature_name}")
    image_path = os.path.join(image_folder, img_file)
    st.image(Image.open(image_path), use_container_width=True)


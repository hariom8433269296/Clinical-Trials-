import streamlit as st
from PIL import Image
import os

# Streamlit page config
st.set_page_config(layout="wide")
st.title("🧪 Clinical Trials Model Dashboard")

# Folder containing images
image_folder = "dashboard_images"

# List only valid image files
valid_extensions = (".png", ".jpg", ".jpeg")
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
)[:20]

# Display images
for img_file in image_files:
    feature_name = os.path.splitext(img_file)[0].replace("_", " ").title()
    st.subheader(f"📊 Feature: {feature_name}")
    image_path = os.path.join(image_folder, img_file)
    st.image(Image.open(image_path), use_container_width=True)

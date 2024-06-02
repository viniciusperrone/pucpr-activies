import streamlit as st
from PIL import Image

from utils.import_static_files import get_image_path
from cards import generate_cards

image_path = get_image_path('logo-pucpr.png')

image = Image.open(image_path)

def home_page():
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(image, use_column_width=False, width=180)

    with col2:
        st.title("Sistema Acadêmico")

    generate_cards()

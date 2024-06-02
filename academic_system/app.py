import streamlit as st
from PIL import Image
import os

from cards import generate_cards
from utils.import_static_files import get_image_path

current_dir = os.path.dirname(__file__)

css_path = os.path.join(current_dir, 'assets', 'css', 'global.css')

image_path = get_image_path('logo-pucpr.png')

image = Image.open(image_path)

st.set_page_config(
    page_title="PUCPR | Sistema Acadêmico",
    page_icon='📚'
)

with open(css_path) as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.image(image, use_column_width=False, width=180)

with col2:
    st.title("Sistema Acadêmico")

generate_cards()

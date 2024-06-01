import streamlit as st
from PIL import Image
import os

current_dir = os.path.dirname(__file__)

css_path = os.path.join(current_dir, 'assets', 'css', 'global.css')

image_path = os.path.join(os.path.dirname(current_dir), 'logo-pucpr.png')

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
    st.image(image, use_column_width=False)

with col2:
    st.title("Sistema Acadêmico")

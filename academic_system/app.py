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

def create_card(title, description):
    card_html = f"""
    <div style="height: 280px; background-color: transparent; border: 1px solid #f6f6f6; border-radius: 10px; padding: 8px; text-align: center; margin-bottom: 30px">
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

col1_card, col2_card = st.columns(2)

col3_card, col4_card = st.columns(2)

with col1_card:
    create_card("Alunos", "Módulo de Alunos")

with col2_card:
    create_card("Professores", "Módulo de Alunos")

with col3_card:
    create_card("Disciplinas", "Módulo de Alunos")

with col4_card:
    create_card("Turmas", "Módulo de Alunos")

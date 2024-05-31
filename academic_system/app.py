import streamlit as st
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logo-pucpr.png')

image = Image.open(image_path)

st.set_page_config(
    page_title="PUCPR | Sistema Acadêmico",
    page_icon='📚',
)

col1, col2 = st.columns([1, 3])

with col1:
    st.image(image, use_column_width=False)

with col2:
    st.title("Sistema Acadêmico")

def create_card(title, description):
    st.write(f"### {title}")
    st.write(description)

col1_card, col2_card, col3_card, col4_card = st.columns(4)

with col1_card:
    create_card("Alunos", "Módulo de Alunos")

with col2_card:
    create_card("Professores", "Módulo de Alunos")

with col3_card:
    create_card("Disciplinas", "Módulo de Alunos")

with col4_card:
    create_card("Turmas", "Módulo de Alunos")

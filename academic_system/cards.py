import streamlit as st

from utils.import_static_files import get_image_path
from utils.encode_image import generate_encoded_image

def create_card(title: str, encoded_image: str):
    card_html = f"""
    <div style="height: 200px; margin-top: 24px; padding: 8px; background-color: transparent; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); display: flex; flex-direction: column; align-items: center;">
        <h3 style="font-size: 24px; color: #8c1717;">{title}</h3>
        <img src="data:image/svg;base64,{encoded_image}" alt="Icon" width="100">
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)

def generate_cards():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        image_path = get_image_path("student.png")

        encoded_image = generate_encoded_image(image_path)

        create_card("Alunos", encoded_image)
    
    with col2:
        image_path = get_image_path("teacher.png")

        encoded_image = generate_encoded_image(image_path)

        create_card("Professores", encoded_image)

    with col3:
        image_path = get_image_path("subject.png")

        encoded_image = generate_encoded_image(image_path)
        
        create_card("Disciplinas", encoded_image)

    with col4:
        image_path = get_image_path("school_class.png")

        encoded_image = generate_encoded_image(image_path)

        create_card("Turmas", encoded_image)
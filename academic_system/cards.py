import streamlit as st

from utils.import_static_files import get_image_path
from utils.encode_image import generate_encoded_image

def create_card(title: str, encoded_image: str, page_key: str):
    def handle_click():
        st.session_state.page = page_key

    # st.button('Clique no cartão', key=page_key, on_click=handle_click)

    card = st.write(f"""
        <style>
            .card {{
                height: 200px;
                margin-top: 24px;
                padding: 8px;
                background-color: transparent;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                display: flex;
                cursor: pointer;
                flex-direction: column;
                align-items: center;
                transition: transform 0.2s, box-shadow 0.2s;
            }}
            .card:hover {{
                transform: scale(1.05);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }}
            .card h3 {{
                font-size: 24px;
                color: #8c1717;
            }}
        </style>
        <div id="card-btn-{page_key}" class="card">
            <h3>{title}</h3>
            <img src="data:image/png;base64,{encoded_image}" alt="Icon" width="100">
        </div>
    """, unsafe_allow_html=True)

    if card:
        print("Clickou")

def generate_cards():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        image_path = get_image_path("student.png")

        encoded_image = generate_encoded_image(image_path)

        create_card("Alunos", encoded_image, "Estudante")
    
    with col2:
        image_path = get_image_path("teacher.png")

        encoded_image = generate_encoded_image(image_path)

        create_card("Professores", encoded_image, "Professor")

    with col3:
        image_path = get_image_path("subject.png")

        encoded_image = generate_encoded_image(image_path)
        
        create_card("Disciplinas", encoded_image, "Disciplina")

    with col4:
        image_path = get_image_path("school_class.png")

        encoded_image = generate_encoded_image(image_path)

        create_card("Turmas", encoded_image, "Turma")
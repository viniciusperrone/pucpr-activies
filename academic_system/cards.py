import streamlit as st

def create_card(title: str):
    card_html = f"""
    <div style="height: 200px; padding: 8px; background-color: transparent; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); display: flex; justify-content: center;">
        <h3 style="font-size: 24px; color: #8c1717;">{title}</h3>
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)

def generate_cards():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        create_card("Alunos")
    
    with col2:
        create_card("Professores")

    with col3:
        create_card("Disciplinas")

    with col4:
        create_card("Turmas")
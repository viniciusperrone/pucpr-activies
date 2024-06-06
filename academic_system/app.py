import streamlit as st
from PIL import Image
import os

from pages.home import home_page
from pages.student import student_page
from pages.tearcher import teacher_page
from pages.subject import subject_page
from pages.school_class import school_class_page

current_dir = os.path.dirname(__file__)

css_path = os.path.join(current_dir, 'assets', 'css', 'global.css')

st.set_page_config(
    page_title="PUCPR | Sistema Acadêmico",
    page_icon='📚',
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
    """,
    unsafe_allow_html=True,
)

with open(css_path) as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Home"

query_params = st.query_params

if 'page' in query_params:
    st.session_state.page = query_params['page'][0]

if st.session_state.page == "Home":
    home_page()

elif st.session_state.page == "Estudante":
    student_page()

elif st.session_state.page == "Professor":
    teacher_page()

elif st.session_state.page == "Disciplina":
    subject_page()

elif st.session_state.page == "Turma":
    school_class_page()
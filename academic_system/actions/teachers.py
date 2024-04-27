from teacher import Teacher
from subject import Subject

from typing import List

def create_teacher(list_teachers: List[Teacher], list_subjects: List[Subject]) -> None:
    name_teacher = input("Digite o nome: ")
    age_teacher = int(input("Digite a idade: "))
    gender_teacher = input("Digite o sexo: ")
    choose_subject = ""

    for subject in list_subjects:
        print(f"\nDisciplina: {subject}")

        add_subject = input("\nAdicionar disciplina (S/N): ").upper()

        if(add_subject == 'S'):
            choose_subject = subject.name

            print("\nDisciplina adicionada.")

            break

    teacher = Teacher(name_teacher, age_teacher, gender_teacher, choose_subject)

    list_teachers.append(teacher)

def list_teachers(list_teachers: List[Teacher]) -> None:
    print("Lista de Professores.\n")
    for index, teacher in enumerate(list_teachers):
        print(f"{index + 1}. Professor")
        print(f"Nome: {teacher.name}")
        print(f"Idade: {teacher.age}")
        print(f"Sexo: {teacher.gender}")
        print(f"Disciplina: {teacher.subject}\n")

def delete_teacher(list_teacher: List[Teacher]) -> None:
    print("Lista de Professores.\n")
    for index, teacher in enumerate(list_teacher):
        print(f"[{index + 1}] - {teacher.name}\n")
    
    index_teacher = int(input("Digite o número do professor que deseja excluir: "))

    teacher = list_teacher[index_teacher - 1]

    if index_teacher > len(list_teacher) or index_teacher < len(list_teacher):
        print("Número de professor errado ou não existe!\n")

    list_teacher.remove(teacher)
    print("\nProfessor removido.")


def update_teacher(list_teacher: List[Teacher]) -> None:
    print("Lista de Professores.\n")
    for index, teacher in enumerate(list_teacher):
        print(f"[{index + 1}] - {teacher.name}\n")

    index_teacher = int(input("Digite o número do estudante que deseja atualizar: "))

    teacher = list_teacher[index_teacher - 1]

    if index_teacher > len(list_teacher) or index_teacher < len(list_teacher):
        print("Número de professor errado ou não existe!\n")

    name_teacher = input("Digite o novo nome: ")
    age_teacher = int(input("Digite a nova idade: "))

    teacher.name = name_teacher
    teacher.age = age_teacher
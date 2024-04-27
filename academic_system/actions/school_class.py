from student import Student
from teacher import Teacher
from school_class import SchoolClass

from menu import menu_update_school_class

from typing import List

def create_school_class(list_students: List[Student], list_teachers: List[Teacher], list_school_class: List[SchoolClass]) -> None:
    list_selected_students = []
    choose_teacher = ''
    choose_subject = ''

    for student in list_students:
        print(student)

        add_student = input("\nAdicionar aluno a turma (S/N): ").upper()

        if(add_student == 'S'):
            list_selected_students.append(student.name)
        
        pass

    for teacher in list_teachers:
        print(teacher)

        add_teacher = input("\nAdicionar professor a turma (S/N): ").upper()

        if(add_teacher == 'S'):
            choose_teacher = teacher.name
            choose_subject = teacher.subject

        pass

    school_class_item = SchoolClass(list_selected_students, choose_teacher, choose_subject)

    list_school_class.append(school_class_item)

def list_school_class(list_school_class: List[SchoolClass]) -> None:
    print("Lista de Turmas.\n")

    for index, school_class in enumerate(list_school_class):
        print(school_class)

        print("\nAlunos:\n")

        for index, student in enumerate(school_class.students):
            print(f"[{index + 1}] - {student}")

            if index == len(school_class.students):
                print("\n")

        if(index != len(list_school_class) - 1):
            print("\n")

def delete_school_class(list_school_class: List[SchoolClass]) -> None:
    print("Lista de Turmas.\n")

    for index, school_class in enumerate(list_school_class):
        print(f"[{index + 1}] - {school_class}")

        if(index != len(list_school_class) - 1):
            print("\n")
    
    index_school_class = int(input("Digite o número do professor que deseja excluir: "))

    school_class = list_school_class[index_school_class - 1]

    if index_school_class > len(list_school_class) or index_school_class < len(list_school_class):
        print("Número de turma errado ou não existe!\n")

    list_school_class.remove(school_class)
    print("\Turma removida.")

def update_school_class(list_school_class: List[SchoolClass], list_students: List[Student], list_teachers: List[Teacher]) -> None:
    print("Lista de Turmas.\n")

    for index, school_class in enumerate(list_school_class):
        print(f"[{index + 1}] - {school_class}")

    index_school_class = int(input("Digite o número do turma que deseja atualizar: "))

    school_class = list_school_class[index_school_class - 1]

    if index_school_class > len(list_school_class) or index_school_class < len(list_school_class):
        print("Número de turma errado ou não existe!\n")


    choose_option = menu_update_school_class()

    match choose_option:
        case 1:
            students_updated = []

            for index, student in enumerate(school_class.students):
                print(f"[{index + 1}] - {student}")

            index_student_remove = int(input("Digite o número do estudante que deseja remover: "))

            student = school_class.students[index_student_remove - 1]

            if student is None:
                print("Número de estudante errado ou estudante não existe!\n")

                return

            students_updated = [value for value in school_class.students if value != student]

            school_class.students = students_updated

            print("\nEstudantes atualizado.")
        
        case 2:
            unselected_list = [item for item in list_students if item.name not in school_class.students]

            for index, unselected_student in enumerate(unselected_list):
                print(f"{index + 1} - {unselected_student.name}")
                
                add_student = input("\nAdicionar aluno a turma (S/N): ").upper()

                if(add_student == 'S'):
                    school_class.students.append(unselected_student.name)

                pass

            print("\nEstudantes atualizados.")
        
        case 3:
            print("Lista de Professores\n")

            for teacher in list_teachers:
                print(teacher)

                select_teacher = input("Adicionar professor (S/N): ")

                if(select_teacher == 'S'):
                    school_class.teacher = teacher.name
                    school_class.subject = teacher.subject

                    break

        case _:
            pass


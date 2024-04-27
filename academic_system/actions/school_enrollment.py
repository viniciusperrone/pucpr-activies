from student import Student
from school_enrollment import SchoolEnrollment

from typing import List

def create_school_enrollment(list_students: List[Student], list_school_enrollment: List[SchoolEnrollment]) -> None:
    student_choose = ''

    for student in list_students:
        print(f"\n{student}")

        add_student = input("\nMatricular este aluno (S/N): ").upper()

        if(add_student == 'S'):
            student_choose = student.name
            
            break

    school_enrollment_item = SchoolEnrollment(student_choose)

    list_school_enrollment.append(school_enrollment_item)

    print(f"\nMatrícula Criada: {school_enrollment_item}")

def list_school_enrollment(list_school_enrollment: List[SchoolEnrollment]) -> None:
    print("\nLista de Matrículas.\n")
    
    for school_enrollment in list_school_enrollment:
        print(school_enrollment)

def delete_school_enrollment(list_school_enrollment: List[SchoolEnrollment]) -> None:
    print("\nLista de Matrículas.\n")

    for index, student in enumerate(list_school_enrollment):
        print(f"[{index + 1}] - {student}\n")
    
    index_school_enrollment = int(input("Digite o número a matrícula que deseja excluir: "))

    school_enrollment_item = list_school_enrollment[index_school_enrollment - 1]

    if school_enrollment_item is None:
        print("Número de matricula errado ou estudante não existe!\n")

        return

    list_school_enrollment.remove(school_enrollment_item)
    print("\nMatrícula removida.")


def update_school_enrollment(list_school_enrollment: List[SchoolEnrollment]) -> None:
    print("\nLista de Matrículas.\n")

    for index, student in enumerate(list_school_enrollment):
        print(f"[{index + 1}] - {student}\n")
    
    index_school_enrollment = int(input("Digite o número a matrícula que deseja atualizar: "))

    school_enrollment_item = list_school_enrollment[index_school_enrollment - 1]

    if school_enrollment_item is None:
        print("Número de matricula errado ou estudante não existe!\n")

        return
    

    school_enrollment_item.regenerate_identifier()

    print(f"Matrícula atualizada: {school_enrollment_item}")
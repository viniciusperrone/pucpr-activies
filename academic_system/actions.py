from student import Student
from typing import List

def created_student(list_students: List[Student]) -> None:
    name_student = input("Digite o nome: ")
    age_student = int(input("Digite a idade: "))
    gender_student = input("Digite o sexo: ")

    student = Student(name_student, age_student, gender_student)

    list_students.append(student)

def list_student(list_students: List[Student]) -> None:
    print("Lista de Estudantes.\n")
    for index, student in enumerate(list_students):
        print(f"Aluno [{index + 1}]")
        print(f"Nome: {student.name}")
        print(f"Idade: {student.age}")
        print(f"Sexo: {student.gender}\n")

def delete_student(list_students: List[Student]) -> None:
    print("Lista de Estudantes.\n")
    for index, student in enumerate(list_students):
        print(f"[{index + 1}] - {student.name}\n")
    
    index_student = int(input("Digite o número do estudante que deseja excluir: "))

    student = list_students[index_student - 1]

    if index_student > len(list_students) or index_student < len(list_students):
        print("Número de estudante errado ou estudante não existe!\n")

    list_students.remove(student)
    print("\nEstudante removido.")


def update_student(list_students: List[Student]) -> None:
    print("Lista de Estudantes.\n")
    for index, student in enumerate(list_students):
        print(f"[{index + 1}] - {student.name}\n")

    index_student = int(input("Digite o número do estudante que deseja atualizar: "))

    student = list_students[index_student - 1]

    if index_student > len(list_students) or index_student < len(list_students):
        print("Número de estudante errado ou estudante não existe!\n")

    name_student = input("Digite o novo nome: ")
    age_student = int(input("Digite a nova idade: "))

    student.name = name_student
    student.age = age_student
import json
from typing import List

options_text_main = ['1. Estudante', '2. Disciplina', '3. Professor', '4. Turma', '5. Matrícula', '6. Sair']
options_text_module = ['1. Incluir', '2. Listar', '3. Excluir', '4. Alterar']

choose_option = 1

# Classes

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def convert_to_dict(self):
        return { "name": self.name, "age": self.age, "gender": self.gender }

    def __str__(self):
        return self.name


# VARIAVEIS

students: List[Student] = []

# Funções

def created_student(list_students: List[Student]) -> None:
    name_student = input("\nDigite o nome: ")
    age_student = int(input("Digite a idade: "))
    gender_student = input("Digite o sexo: ")

    student = Student(name_student, age_student, gender_student)

    list_students.append(student)

    print(f"\nAluno {student} criado com sucesso!")

def list_student(list_students: List[Student]) -> None:
    if len(list_students) == 0:
        print("\n Sem Estudantes cadastrados.")

        return
    
    print("Lista de Estudantes.\n")

    for index, student in enumerate(list_students):
        print(f"Aluno [{index + 1}]")
        print(f"Nome: {student.name}")
        print(f"Idade: {student.age}")
        print(f"Sexo: {student.gender}\n")

def delete_student(list_students: List[Student]) -> None:
    if len(list_students) == 0:
        print("\n Sem Estudantes cadastrados.")

        return
    
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
    if len(list_students) == 0:
        print("\n Sem Estudantes cadastrados.")

        return
    
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

    print("\nEstudante atualizado com sucesso!")

# Gerar JSON    

def save_data(list_students: List[Student]):
    students_to_dict = [student.convert_to_dict() for student in list_students]

    data = {
        "students": students_to_dict
    }
    
    with open("data.json", "w") as file:
        json.dump(data, file)

# ESTRUTURA DE REPETIÇÃO

while choose_option != 6:
    print("\n------------Sistema PUC------------\n")

    for option in options_text_main:
        print(option)

    choose_option = int(input("\nDigite sua opção: "))

    if choose_option not in [1, 2, 3, 4, 5, 6]:
        print("\nOpção inválida!")

    if choose_option == 6:
                
        break

    else:
        print("\n------------Sistema PUC------------\n")

        for option in options_text_module:
            print(option)

        choose_option_module = int(input("\nDigite sua opção: "))

        if choose_option_module not in [1, 2, 3, 4]:
            print("\nOpção inválida!")

        else:
            if choose_option == 1:
                match choose_option_module:
                    case 1:
                        created_student(students)

                    case 2:
                        list_student(students)

                    case 3: 
                        delete_student(students)
                    
                    case 4: 
                        update_student(students)

                    case _:
                        print("\nOpção inválida!")
        

save_data(students)
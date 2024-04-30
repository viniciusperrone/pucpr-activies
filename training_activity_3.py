from typing import List

options_text_main = ['1. Estudante', '2. Disciplina', '3. Professor', '4. Turma', '5. Matrícula', '6. Sair']
options_text_module = ['1. Incluir', '2. Listar', '3. Excluir', '4. Alterar']

choose_option = 1

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

# ESTRUTURA DE REPETIÇÃO

while choose_option != 6:
    print("\n------------Sistema PUC------------\n")

    for option in options_text_main:
        print(option)

    choose_option = int(input("\nDigite sua opção: "))

    if choose_option not in [1, 2, 3, 4, 5, 6]:
        print("\nOpção inválida!")

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
                        name = input("Digite o nome do aluno")
                        age = int(input("Digite a idade do aluno: "))
                        gender = input("Digite o sexo do aluno")

                        student = Student(name, age, gender)

                        print(f"Aluno {student} criado com sucesso!")

                        break

                    case 2:
                        if len(students) == 0:
                            print("\n Sem Estudantes cadastrados.")

                            break
                        
                        for student in students:
                            print(f"Aluno: {student.name}")

                    case 3: 
                        if len(students) == 0:
                            print("\n Sem Estudantes cadastrados.")

                            break

                        for index, student in enumerate(students):
                            print(f"{index + 1}. {student}")

                        index_student = int(input("\nSelecione o número do estudante que deseja excluir: "))

                        student = students[index_student - 1]

                        if student is None:
                            print("\nEstudante não existe ou número inválido!")

                            break

                        students.remove(student)

                        print("\nEstudante removido com sucesso!")
                    
                    case 4: 
                        if len(students) == 0:
                            print("\n Sem Estudantes cadastrados.")

                            break

                        for index, student in enumerate(students):
                            print(f"{index + 1}. {student}")

                        index_student = int(input("\nSelecione o número do estudante que deseja editar: "))

                        student = students[index_student - 1]

                        if student is None:
                            print("\nEstudante não existe ou número inválido!")

                            break

                        name = input("Digite o nome do aluno")
                        age = int(input("Digite a idade do aluno: "))
                        gender = input("Digite o sexo do aluno")

                        student.name = name
                        student.age = age
                        student.gender = gender

                        print("\nEstudante atualizado com sucesso!")

                    case _:
                        print("\nOpção inválida!")

                        break


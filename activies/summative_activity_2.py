import json
import random
from typing import List

options_text_main = ['1. Estudante', '2. Disciplina', '3. Professor', '4. Turma', '5. Matrícula', '6. Sair']
options_text_module = ['1. Incluir', '2. Listar', '3. Excluir', '4. Alterar']

choose_option = 1

# CLASSES

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def convert_to_dict(self):
        return { "name": self.name, "age": self.age, "gender": self.gender }

    def __str__(self):
        return self.name

class Subject:
    def __init__(self, name, workload):
        self.name = name
        self.workload = workload

    def convert_to_dict(self):
        return { "name": self.name, "workload": self.workload }
    
    def __str__(self) -> str:
        return self.name

class Teacher:
    def __init__(self, name, age, gender, subject):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject

    def convert_to_dict(self):
        return { "name": self.name, "age": self.age, "gender": self.gender, "subject": self.subject }

    def __str__(self):
        return self.name

class SchoolClass:
    def __init__(self, students: List[str], teacher: str, subject: str):
        self.students = students
        self.identifier = 'C' + str(self.generate_random_identifier())
        self.teacher = teacher
        self.subject = subject
    
    def generate_random_identifier(self):
        return random.randint(1000, 9999)

    def convert_to_dict(self):
        return { "students": self.students, "identifier": self.identifier, "teacher": self.teacher, "subject": self.subject }

    def __str__(self) -> str:
        return f"{self.identifier} - {self.subject} ({self.teacher})"

class SchoolEnrollment:
    def __init__(self, student: str):
        self.student = student
        self.identifier = 'A' + str(self.generate_random_identifier())

    def regenerate_identifier(self):
        self.identifier = 'A' + str(self.generate_random_identifier())
    
    def generate_random_identifier(self):
        return random.randint(1000, 9999)

    def convert_to_dict(self):
        return { "student": self.student, "identifier": self.identifier }
    
    def __str__(self) -> str:
        return f"{self.identifier} - {self.student}"
    
# VARIAVEIS

students: List[Student] = []
subjects: List[Teacher] = []
teachers: List[Subject] = []
school_class: List[SchoolClass] = []
school_enrollment: List[SchoolEnrollment] = []

# FUNÇÕES

def menu_update_school_class():
    options_text = ['1. Remover alunos', '2. Adicionar alunos', '3. Atualizar professor']

    print("\n------------Sistema PUC------------\n")

    for index, option in enumerate(options_text):
        print(f"{index + 1}. {option}\n")

    choose_item = int(input("\nDigite sua opção: "))

    return choose_item

"""
    1. Estudante

        - Incluir
        - Listar
        - Deletar
        - Atualizar
"""

def create_student(list_students: List[Student]) -> None:
    name_student = input("\nDigite o nome: ")
    age_student = int(input("Digite a idade: "))
    gender_student = input("Digite o sexo: ")

    student = Student(name_student, age_student, gender_student)

    list_students.append(student)

    print(f"\nAluno {student} criado com sucesso!")

def list_student(list_students: List[Student]) -> None:
    if len(list_students) == 0:
        print("\nSem Estudantes cadastrados.")

        return
    
    print("\nLista de Estudantes.\n")

    for index, student in enumerate(list_students):
        print(f"Aluno [{index + 1}]")
        print(f"Nome: {student.name}")
        print(f"Idade: {student.age}")
        print(f"Sexo: {student.gender}\n")

def delete_student(list_students: List[Student]) -> None:
    if len(list_students) == 0:
        print("\nSem Estudantes cadastrados.")

        return
    
    print("\nLista de Estudantes.\n")

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
        print("\nSem Estudantes cadastrados.")

        return
    
    print("\nLista de Estudantes.\n")

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

"""
    2. Disciplina

        - Incluir
        - Listar
        - Deletar
        - Atualizar
"""

def create_subject(list_subject: List[Subject]) -> None:
    name_subject = input("Digite o nome: ")
    name_workload = input("Digite a carga horária: ")

    subject = Subject(name_subject, name_workload)

    list_subject.append(subject)

def list_subjects(list_subject: List[Subject]) -> None:
    print("\nLista de Disciplinas.\n")

    for index, subject in enumerate(list_subject):
        print(f"[{index + 1}] - Disciplina")
        print(f"Nome: {subject.name}")
        print(f"Carga Horária: {subject.workload}\n")

def delete_subject(list_subject: List[Subject]) -> None:
    print("\nLista de Disciplinas.\n")

    for index, subject in enumerate(list_subject):
        print(f"[{index + 1}] - {subject.name}\n")
    
    index_subject = int(input("Digite o número da disciplina que deseja excluir: "))

    subject = list_subject[index_subject - 1]

    if index_subject > len(list_subject) or index_subject < len(list_subject):
        print("Número de estudante errado ou estudante não existe!\n")

    list_subject.remove(subject)
    print("\nDisciplina removido.")


def update_subject(list_subject: List[Subject]) -> None:
    print("\nLista de Disciplina.\n")

    for index, subject in enumerate(list_subject):
        print(f"[{index + 1}] - {subject.name}\n")

    index_subject = int(input("Digite o número da disciplina que deseja atualizar: "))

    subject = list_subject[index_subject - 1]

    if index_subject > len(list_subject) or index_subject < len(list_subject):
        print("Número de disciplina errado ou não existe!\n")

    name_subject = input("Digite o novo nome: ")
    workload_subject = input("Digite a nova carga horária: ")

    subject.name = name_subject
    subject.workload = workload_subject

"""
    3. Professor

        - Incluir
        - Listar
        - Deletar
        - Atualizar
"""

def create_teacher(list_teachers: List[Teacher], list_subjects: List[Subject]) -> None:
    name_teacher = input("Digite o nome: ")
    age_teacher = int(input("Digite a idade: "))
    gender_teacher = input("Digite o sexo: ")
    choose_subject = ""

    if len(list_subjects) == 0:
        print("\nSem Disciplinas cadastrados.")

        return

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
    if len(list_teachers) == 0:
        print("\nSem Professores cadastrados.")

        return
    
    print("\nLista de Professores.\n")

    for index, teacher in enumerate(list_teachers):
        print(f"{index + 1}. Professor")
        print(f"Nome: {teacher.name}")
        print(f"Idade: {teacher.age}")
        print(f"Sexo: {teacher.gender}")
        print(f"Disciplina: {teacher.subject}\n")

def delete_teacher(list_teacher: List[Teacher]) -> None:
    if len(list_teachers) == 0:
        print("\nSem Professores cadastrados.")

        return
    
    print("\nLista de Professores.\n")
    for index, teacher in enumerate(list_teacher):
        print(f"[{index + 1}] - {teacher.name}\n")
    
    index_teacher = int(input("Digite o número do professor que deseja excluir: "))

    teacher = list_teacher[index_teacher - 1]

    if index_teacher > len(list_teacher) or index_teacher < len(list_teacher):
        print("Número de professor errado ou não existe!\n")

    list_teacher.remove(teacher)
    print("\nProfessor removido.")


def update_teacher(list_teacher: List[Teacher]) -> None:
    if len(list_teachers) == 0:
        print("\nSem Professores cadastrados.")

        return
    
    print("\nLista de Professores.\n")

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

"""
    4. Turma

        - Incluir
        - Listar
        - Deletar
        - Atualizar
"""

def create_school_class(list_students: List[Student], list_teachers: List[Teacher], list_school_class: List[SchoolClass]) -> None:
    list_selected_students = []
    choose_teacher = ''
    choose_subject = ''

    if len(list_students) == 0:
        print("\nSem Estudantes cadastrados.")

        return

    if len(list_teachers) == 0:
        print("\nSem Professores cadastrados.")

        return

    for student in list_students:
        print(f"\n{student}")

        add_student = input("\nAdicionar aluno a turma (S/N): ").upper()

        if(add_student == 'S'):
            list_selected_students.append(student.name)
        
        pass

    if list_selected_students == []:
        print("\nNenhum estudante selecionado.\n")


    for teacher in list_teachers:
        print(f"\n{teacher}")

        add_teacher = input("\nAdicionar professor a turma (S/N): ").upper()

        if(add_teacher == 'S'):
            choose_teacher = teacher.name
            choose_subject = teacher.subject

            break

        pass

    if choose_teacher == '':
        print("\nNenhum professor selecionado.\n")

    school_class_item = SchoolClass(list_selected_students, choose_teacher, choose_subject)

    list_school_class.append(school_class_item)

def list_school_class(list_school_class: List[SchoolClass]) -> None:
    print("\nLista de Turmas.\n")

    if len(list_school_class) == 0:
        print("\nSem Turmas cadastrados.")

        return

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
    if len(list_school_class) == 0:
        print("\nSem Turmas cadastrados.")

        return

    print("\nLista de Turmas.\n")

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
    if len(list_school_class) == 0:
        print("\nSem Turmas cadastrados.")

        return
    
    print("\nLista de Turmas.\n")

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
            print("\nLista de Professores\n")

            for teacher in list_teachers:
                print(teacher)

                select_teacher = input("Adicionar professor (S/N): ")

                if(select_teacher == 'S'):
                    school_class.teacher = teacher.name
                    school_class.subject = teacher.subject

                    break

        case _:
            pass

"""
    5. Matrícula

        - Incluir
        - Listar
        - Deletar
        - Atualizar
"""

def create_school_enrollment(list_students: List[Student], list_school_enrollment: List[SchoolEnrollment]) -> None:
    student_choose = ''

    if len(list_students) == 0:
        print("\nSem Estudantes cadastrados.")

        return

    for student in list_students:
        print(f"\n{student}")

        add_student = input("\nMatricular este aluno (S/N): ").upper()

        if(add_student == 'S'):
            student_choose = student.name
            
            break

    if student_choose == '':
        print("\nNenhum aluno foi adicionado\n")

        return

    school_enrollment_item = SchoolEnrollment(student_choose)

    list_school_enrollment.append(school_enrollment_item)

    print(f"\nMatrícula Criada: {school_enrollment_item}")

def list_school_enrollment(list_school_enrollment: List[SchoolEnrollment]) -> None:
    if len(list_school_enrollment) == 0:
        print("\nSem Matriculas cadastradas.")

        return

    print("\nLista de Matrículas.\n")
    
    for school_enrollment in list_school_enrollment:
        print(school_enrollment)

def delete_school_enrollment(list_school_enrollment: List[SchoolEnrollment]) -> None:
    if len(list_school_enrollment) == 0:
        print("\nSem Matriculas cadastradas.")

        return

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
    if len(list_school_enrollment) == 0:
        print("\nSem Matriculas cadastradas.")

        return
    
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

# GERAR JSON    

def save_data():
    students_to_dict = [student.convert_to_dict() for student in students]
    subject_to_dict = [subject.convert_to_dict() for subject in subjects]
    tearchers_to_dict = [teacher.convert_to_dict() for teacher in teachers]
    school_class_to_dict = [school_class_item.convert_to_dict() for school_class_item in school_class]
    school_enrollment_to_dict = [school_enrollment_item.convert_to_dict() for school_enrollment_item in school_enrollment]

    data = {
        "students": students_to_dict,
        "subjects": subject_to_dict,
        "teachers": tearchers_to_dict,
        "school_class": school_class_to_dict,
        "school_enrollment": school_enrollment_to_dict
    }
    
    with open("data.json", "w") as file:
        json.dump(data, file)

# ESTRUTURA DE REPETIÇÃO

while choose_option != 6:
    print("\n------------Sistema PUC------------\n")

    for option in options_text_main:
        print(option)

    try:
        choose_option = int(input("\nDigite sua opção: "))
    except:
        print("\nOpção inválida.\n")

        break

    if choose_option not in [1, 2, 3, 4, 5, 6]:
        print("\nOpção inválida!")

    if choose_option == 6:
                
        break

    else:
        print("\n------------Sistema PUC------------\n")

        for option in options_text_module:
            print(option)

        try:
            choose_option_module = int(input("\nDigite sua opção: "))

        except:
            print("\nOpção inválida.\n")

            break

        if choose_option_module not in [1, 2, 3, 4]:
            print("\nOpção inválida!")

        else:
            if choose_option == 1:
                match choose_option_module:
                    case 1:
                        create_student(students)

                    case 2:
                        list_student(students)

                    case 3: 
                        delete_student(students)
                    
                    case 4: 
                        update_student(students)

                    case _:
                        print("\nOpção inválida!")

            if choose_option == 2:
                match choose_option_module:
                    case 1:
                        create_subject(subjects)

                    case 2:
                        list_subjects(subjects)

                    case 3: 
                        delete_subject(subjects)
                    
                    case 4: 
                        update_subject(subjects)

                    case _:
                        print("\nOpção inválida!")

            if choose_option == 3:
                match choose_option_module:
                    case 1:
                        create_teacher(teachers, subjects)

                    case 2:
                        list_teachers(teachers)

                    case 3: 
                        delete_teacher(teachers)
                    
                    case 4: 
                        update_teacher(teachers)

                    case _:
                        print("\nOpção inválida!")
            
            if choose_option == 4:
                match choose_option_module:
                    case 1:
                        create_school_class(students, teachers, school_class)

                    case 2:
                        list_school_class(school_class)

                    case 3: 
                        delete_school_class(school_class)
                    
                    case 4: 
                        update_school_class(school_class, students, teachers)

                    case _:
                        print("\nOpção inválida!")

            if choose_option == 5:
                match choose_option_module:
                    case 1:
                        create_school_enrollment(students, school_enrollment)

                    case 2:
                        list_school_enrollment(school_enrollment)

                    case 3: 
                        delete_school_enrollment(school_enrollment)
                    
                    case 4: 
                        update_school_enrollment(school_enrollment)

                    case _:
                        print("\nOpção inválida!")
        

save_data()
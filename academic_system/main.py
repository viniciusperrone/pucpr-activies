from student import Student
from teacher import Teacher
from subject import Subject

from menu import menu_main

students = []
subjects = []
teachers = []

continuous = 'S'

while continuous == 'S':
    answer_menu = menu_main()

    match answer_menu:
        case 1:
            name_student = input("Digite o nome: ")
            age_student = int(input("Digite a idade: "))
            gender_student = input("Digite o sexo: ")

            student = Student(name_student, age_student, gender_student)

            students.append(student.convert_to_dict())

        case 2:
            name_subject = input("Digite o nome: ")
            name_workload = input("Digite a carga horária: ")

            subject = Subject(name_subject, name_workload)

            subjects.append(subject.convert_to_dict())

        case 3:
            name_teacher = input("Digite o nome: ")
            age_student = int(input("Digite a idade: "))
            gender_student = input("Digite o sexo: ")
            subject_teacher = input("Digite a disciplina: ")

            teacher = Teacher(name_teacher, age_student, gender_student, subject_teacher)

            teachers.append(teacher.convert_to_dict())
        case _:
            pass


    continuous = input("Deseja continuar (S/N)? ").upper()

print(students)
print(subjects)
print(teachers)
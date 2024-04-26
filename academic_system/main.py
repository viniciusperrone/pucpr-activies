from student import Student
from teacher import Teacher
from subject import Subject
from school_class import SchoolClass
from school_enrollment import SchoolEnrollment

from menu import menu_main

students = []
subjects = []
teachers = []
school_class = []
school_enrollment = []

continuous = 'S'

while continuous == 'S':
    answer_menu = menu_main()

    match answer_menu:
        case 1:
            name_student = input("Digite o nome: ")
            age_student = int(input("Digite a idade: "))
            gender_student = input("Digite o sexo: ")

            student = Student(name_student, age_student, gender_student)

            students.append(student)

        case 2:
            name_subject = input("Digite o nome: ")
            name_workload = input("Digite a carga horária: ")

            subject = Subject(name_subject, name_workload)

            subjects.append(subject)

        case 3:
            name_teacher = input("Digite o nome: ")
            age_student = int(input("Digite a idade: "))
            gender_student = input("Digite o sexo: ")
            choose_subject = ""

            print("\n")
            for subject in subjects:
                print(f"Disciplina: {subject}")

                add_subject = input("\nAdicionar disciplina (S/N):").upper()

                if(add_subject == 'S'):
                    choose_subject = subject.name

                    print("\nDisciplina adicionada.")

                    break

            teacher = Teacher(name_teacher, age_student, gender_student, choose_subject)

            teachers.append(teacher)
        
        case 4:
            list_students = []
            choose_teacher = ''
            choose_subject = ''

            print("\n")
            for student in students:
                print(student)

                add_student = input("\nAdicionar aluno a turma (S/N): ").upper()

                if(add_student == 'S'):
                    list_students.append(student.name)

            print("\n")
            for teacher in teachers:
                print(teacher)

                add_teacher = input("\nAdicionar professor a turma (S/N): ").upper()

                if(add_student == 'S'):
                    choose_teacher = teacher.name
                    choose_subject = teacher.subject

                    break
                
            school_class_item = SchoolClass(list_students, choose_teacher, choose_subject)

            school_class.append(school_class_item)
        
        case 5:
            student_choose = ''

            print("\n")
            for student in students:
                print(student)

                add_student = input("\nMatricular este aluno (S/N)?").upper()

                if(add_student == 'S'):
                    student_choose = student.name

            school_enrollment_item = SchoolEnrollment(student_choose)

            school_enrollment.append(school_enrollment_item)

            print(school_enrollment_item)

        case _:
            pass


    continuous = input("Deseja continuar (S/N)? ").upper()
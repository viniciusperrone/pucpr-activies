from student import Student
from teacher import Teacher
from subject import Subject
from school_class import SchoolClass
from school_enrollment import SchoolEnrollment

from menu import menu_main, menu_item

from actions.student import created_student, list_student, delete_student, update_student
from actions.subject import created_subject, list_subjects, delete_subject, update_subject
from actions.teachers import create_teacher, list_teachers

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
            continuos_item = 'S'

            while continuos_item == 'S':
                answer_item = menu_item()

                match answer_item:
                    case 1:
                        created_student(students)

                    case 2:
                        list_student(students)
                    
                    case 3: 
                        delete_student(students)
                    
                    case 4:
                        update_student(students)

                    case _:
                        pass

                continuos_item = input("\nDeseja continuar neste módulo (S/N)? ").upper()

        case 2:
            continuos_item = 'S'

            while continuos_item == 'S':
                answer_item = menu_item()

                match answer_item:
                    case 1:
                        created_subject(subjects)
                    
                    case 2:
                        list_subjects(subjects)
                    
                    case 3:
                        delete_subject(subjects)

                    case 4:
                        update_subject(subjects)
                    case _:
                        pass

                continuos_item = input("\nDeseja continuar neste módulo (S/N)? ").upper()

        case 3:
            continuos_item = 'S'

            match continuos_item:
                case 1:
                    create_teacher(teachers)

                case 2:
                    list_teachers(teachers)
                    
                case _:
                    pass

            name_teacher = input("Digite o nome: ")
            age_student = int(input("Digite a idade: "))
            gender_student = input("Digite o sexo: ")
            choose_subject = ""

            for subject in subjects:
                print(f"\nDisciplina: {subject}")

                add_subject = input("\nAdicionar disciplina (S/N): ").upper()

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

            for student in students:
                print(student)

                add_student = input("\nAdicionar aluno a turma (S/N): ").upper()

                if(add_student == 'S'):
                    list_students.append(student.name)

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

            for student in students:
                print(student)

                add_student = input("\nMatricular este aluno (S/N): ").upper()

                if(add_student == 'S'):
                    student_choose = student.name
                    
                    break

            school_enrollment_item = SchoolEnrollment(student_choose)

            school_enrollment.append(school_enrollment_item)

            print(school_enrollment_item)

        case _:
            pass


    continuous = input("\nDeseja continuar (S/N)? ").upper()
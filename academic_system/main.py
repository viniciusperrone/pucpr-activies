from typing import List

from student import Student
from teacher import Teacher
from subject import Subject
from academic_system.models.school_class import SchoolClass
from school_enrollment import SchoolEnrollment

from menu import menu_main, menu_item

from actions.student import created_student, list_student, delete_student, update_student
from actions.subject import created_subject, list_subjects, delete_subject, update_subject
from actions.teachers import create_teacher, list_teachers, delete_teacher, update_teacher
from actions.school_class import create_school_class, list_school_class, delete_school_class, update_school_class
from actions.school_enrollment import create_school_enrollment, list_school_enrollment, delete_school_enrollment, update_school_enrollment

from save_data import save_data

students: List[Student] = []
subjects: List[Teacher] = []
teachers: List[Subject] = []
school_class: List[SchoolClass] = []
school_enrollment: List[SchoolEnrollment] = []

student_1 = Student("Vinicius", 22, "M")
student_2 = Student("Will", 22, "M")
student_3 = Student("Lorenzo", 22, "M")

subject_1 = Subject("LTP", "60h")
subject_2 = Subject("LPI", "60h")

teacher_1 = Teacher("Marden", 48, "M", "LTP")
teacher_2 = Teacher("Renan", 48, "M", "LPI")

students.append(student_1)
students.append(student_2)
students.append(student_3)

subjects.append(subject_1)
subjects.append(subject_2)

teachers.append(teacher_1)
teachers.append(teacher_2)

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

            while continuos_item == 'S':
                answer_item = menu_item()

                match answer_item:
                    case 1:
                        create_teacher(teachers, subjects)

                    case 2:
                        list_teachers(teachers)
                        
                    case 3: 
                        delete_teacher(teachers)
                    
                    case 4:
                        update_teacher(teachers)

                    case _:
                        pass
                
                continuos_item = input("\nDeseja continuar neste módulo (S/N)? ").upper()
        
        case 4:
            continuos_item = 'S'

            while continuos_item == 'S':
                answer_item = menu_item()

                match answer_item:
                    case 1:
                        create_school_class(students, teachers, school_class)

                    case 2:
                        list_school_class(school_class)

                    case 3:
                        delete_school_class(school_class)

                    case 4:
                        update_school_class(school_class, students, teachers)

                    case _:
                        pass
                
                continuos_item = input("\nDeseja continuar neste módulo (S/N)? ").upper()
        
        case 5:
            continuos_item = 'S'

            while continuos_item == 'S':
                answer_item = menu_item()

                match answer_item:
                    case 1:
                        create_school_enrollment(students, school_enrollment)

                    case 2:
                        list_school_enrollment(school_enrollment)

                    case 3:
                        delete_school_enrollment(school_enrollment)
                    
                    case 4:
                        update_school_enrollment(school_enrollment)

                    case _:
                        pass

                continuos_item = input("\nDeseja continuar neste módulo (S/N)? ").upper()


        case _:
            pass


    continuous = input("\nDeseja continuar no sistema (S/N)? ").upper()

students_convert_to_dict = [student.convert_to_dict() for student in students]
subjects_convert_to_dict = [subject.convert_to_dict() for subject in subjects]
teachers_convert_to_dict = [teacher.convert_to_dict() for teacher in teachers]
school_class_convert_to_dict = [school_class_item.convert_to_dict() for school_class_item in school_class]
school_enrollment_convert_to_dict = [school_enrollment_item.convert_to_dict() for school_enrollment_item in school_enrollment]

save_data(students_convert_to_dict, subjects_convert_to_dict, teachers_convert_to_dict, school_class_convert_to_dict, school_enrollment_convert_to_dict)
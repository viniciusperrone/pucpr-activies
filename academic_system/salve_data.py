import json

from typing import List

from student import Student
from subject import Subject
from teacher import Teacher
from school_class import SchoolClass
from school_enrollment import SchoolEnrollment

def salve_data(students: List[Student], subjects: List[Subject], teachers: List[Teacher], school_class: List[SchoolClass], school_enrollment: List[SchoolEnrollment]):
    with open("students.json", "w") as file:
        json.dump(students, file)

    with open("subjects.json", "w") as file:
        json.dump(subjects, file)

    with open("teachers.json", "w") as file:
        json.dump(teachers, file)

    with open("school_class.json", "w") as file:
        json.dump(school_class, file)

    with open("school_class.json", "w") as file:
        json.dump(school_enrollment, file)
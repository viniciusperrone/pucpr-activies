import json

from typing import List

from student import Student
from subject import Subject
from teacher import Teacher
from school_class import SchoolClass
from school_enrollment import SchoolEnrollment

def save_data(students: List[Student], subjects: List[Subject], teachers: List[Teacher], school_class: List[SchoolClass], school_enrollment: List[SchoolEnrollment]):
    data = {
        "students": students,
        "subjects": subjects,
        "teachers": teachers,
        "school_class": school_class,
        "school_enrollment": school_enrollment
    }
    
    with open("data.json", "w") as file:
        json.dump(data, file)
        
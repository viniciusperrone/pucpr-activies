
"""
    The SchoolClass class will have following fields:
        - Students
        - Identifier
        - Teacher
        - Subject
"""

import random

class SchoolClass:
    def __init__(self, students, teachers, subject):
        self.students = students
        self.identifier = 'C' + str(self.generate_random_identifier())
        self.teachers = teachers
        self.subject = subject
    
    def generate_random_identifier(self):
        return random.randint(1000, 9999)

    def convert_to_dict(self):
        return { "students": self.students, "identifier": self.identifier, "teachers": self.teachers, "subject": self.subject }

    def __str__(self) -> str:
        return f"{self.identifier} - {self.subject}"
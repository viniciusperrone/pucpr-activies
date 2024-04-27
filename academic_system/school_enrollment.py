
"""
    The SchoolEnrollment class will have following fields:
        - Student
        - Identifier
"""

import random

class SchoolEnrollment:
    def __init__(self, student: str):
        self.student = student
        self.identifier = 'A' + str(self.generate_random_identifier())

    def regenerate_identifier(self):
        self.identifier = 'A' + str(self.generate_random_identifier())
    
    def generate_random_identifier(self):
        return random.randint(1000, 9999)
    
    def __str__(self) -> str:
        return f"{self.identifier} - {self.student}"
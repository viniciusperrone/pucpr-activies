
"""
    The SchoolEnrollment class will have following fields:
        - Student
        - Identifier
"""

import random

class SchoolEnrollment:
    def __init__(self, student):
        self.student = student
        self.identifier = 'A' + str(self.generate_random_identifier())
    
    def generate_random_identifier(self):
        return random.randint(1000, 9999)
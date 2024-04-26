
"""
    The Student class will have following fields:
        - Full Name
        - Age
        - Gender
"""

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def convert_to_dict(self):
        return { "name": self.name, "age": self.age, "gender": self.gender }

    def __str__(self):
        return self.name
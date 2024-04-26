
"""
    The Teacher class will have following fields:
        - Full Name
        - Age
        - Gender
        - Subject
"""

class Teacher:
    def __init__(self, name, age, gender, subject):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject

    def convert_to_dict(self):
        return { "name": self.name, "age": self.age, "gender": self.gender, "subject": self.subject }

    def __str__(self):
        return self.name
        

 
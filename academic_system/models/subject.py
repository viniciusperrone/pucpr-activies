
"""
    The Subject class will have following fields:
        - Name
        - Workload
"""

class Subject:
    def __init__(self, name, workload):
        self.name = name
        self.workload = workload

    def convert_to_dict(self):
        return { "name": self.name, "workload": self.workload }
    
    def __str__(self) -> str:
        return self.name

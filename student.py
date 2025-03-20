import json

class Student:
    def __init__(self, roll_number, name, age, department):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.department = department

    def __str__(self):
        return f"Roll No: {self.roll_number}, Name: {self.name}, Age: {self.age}, Department: {self.department}"

    def to_dict(self):
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "age": self.age,
            "department": self.department
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['roll_number'], data['name'], data['age'], data['department'])

import json
from student import Student

class StudentManagementSystem:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Student.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump([student.to_dict() for student in self.students], file)

    def add_student(self, roll_number, name, age, department):
        new_student = Student(roll_number, name, age, department)
        self.students.append(new_student)
        self.save_data()

    def display_students(self):
        if not self.students:
            print("No students found.")
        for student in self.students:
            print(student)

    def search_student(self, roll_number=None, name=None):
        for student in self.students:
            if student.roll_number == roll_number or student.name == name:
                print(student)
                return
        print("Student not found.")

    def update_student(self, roll_number, name=None, age=None, department=None):
        for student in self.students:
            if student.roll_number == roll_number:
                if name: student.name = name
                if age: student.age = age
                if department: student.department = department
                self.save_data()
                print("Student details updated.")
                return
        print("Student not found.")

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                self.save_data()
                print("Student deleted.")
                return
        print("Student not found.")

def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            system.add_student(roll_number, name, age, department)
        elif choice == '2':
            system.display_students()
        elif choice == '3':
            roll_number = input("Enter Roll Number or Name to search: ")
            system.search_student(roll_number=roll_number)
        elif choice == '4':
            roll_number = input("Enter Roll Number to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            age = input("Enter new Age (leave blank to keep current): ")
            department = input("Enter new Department (leave blank to keep current): ")
            age = int(age) if age else None
            system.update_student(roll_number, name or None, age, department or None)
        elif choice == '5':
            roll_number = input("Enter Roll Number to delete: ")
            system.delete_student(roll_number)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

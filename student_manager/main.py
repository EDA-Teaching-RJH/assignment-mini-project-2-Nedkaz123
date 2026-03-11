# main.py

# This is the main program file.
# It shows a menu and allows the user to interact with the system.

from student import Student
from validator import validate_email, validate_phone, validate_student_id
from file_handler import save_student, load_students

def add_student():

    name = input("Enter name: ")

    email = input("Enter email: ")
    if not validate_email(email):
        print("Invalid email format")
        return
    
    phone = input("Enter phone number: ")
    if not validate_phone(phone):
        print("Invalid phone format")
        return
    
    student_id = input("Enter student ID (ST12345): ")
    if not validate_student_id(student_id):
        print("Invalid student ID format")
        return
    
    course = input("Enter course: ")

    student = Student(name, email, phone, student_id, course)

    save_student(student)

    print("Student saved successfully")

def view_students():

    students = load_students()

    for s in students:
        print(s)

def search_student():

    keyword = input("Eter name or ID to search: ")

    students = load_students()

    for student in students:

        if keyword.lower() in student[0].lower() or keyword in student[3]:
                print(student)

def menu():

    while True:

        print("\nStudent Contact Manager")
        print("1 - Add Student")
        print("2 - View Students")
        print("3 - Search Student")
        print("4 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            break

        else:
            print("Invalid option")

menu()
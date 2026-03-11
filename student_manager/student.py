# student.py

# This file contains the classes used in the program.
# I created a Person class first and then a Student class that inherits from it.

from datetime import datetime

class Person:

    # Basic Person class
    # Stores common details like name, email and phone.

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Student(Person):

    # Student class inherits from Person
    # It adds a student ID and course

    def __init__(self, name, email, phone, student_id, course):

        super().__init__(name, email, phone)

        self.student_id = student_id
        self.course = course

        self.date_added = datetime.now()

    def to_list(self):

        # Convert the student object into a list so it can saved to a CSV file.

        return [
            self.name,
            self.email,
            self.phone,
            self.student_id,
            self.course,
            self.date_added
        ]
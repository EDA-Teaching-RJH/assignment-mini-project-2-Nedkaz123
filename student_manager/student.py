# student.py

from datetime import datetime

class Person:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Student(Person):

    def __init__(self, name, email, phone, student_id, course):

        super().__init__(name, email, phone)

        self.student_id = student_id
        self.course = course

        self.date_added = datetime.now()

    def to_list(self):

        return [
            self.name,
            self.email,
            self.phone,
            self.student_id,
            self.course,
            self.date_added
        ]
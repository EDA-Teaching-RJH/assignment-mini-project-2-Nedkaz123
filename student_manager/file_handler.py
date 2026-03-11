# file_handler.py

import csv

FILE_NAME = "contacts.csv"

def save_student(student):

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(student.to_list())

def load_students():

    students = []

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            for row in reader: 
                students.append(row)

    except FileNotFoundError:
        print("No data file found yet.")

    return students
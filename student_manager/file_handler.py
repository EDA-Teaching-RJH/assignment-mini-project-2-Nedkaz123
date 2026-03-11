# file_handler.py

# This file is responsible for reading and writing student data to a CSV file.

import csv

FILE_NAME = "contacts.csv"

def save_student(student):

    # Saves a student to a CSV file.

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(student.to_list())

def load_students():

    # Loads students from CSV file.

    students = []

    try:

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            for row in reader: 
                students.append(row)

    except FileNotFoundError:
        print("No data file found yet.")

    return students
# validator.py

# The file contains functions used to validate user input.
# Regular expressions are used to check if the data format is correct.

import re

def validate_email(email):

    # Checks if email format is valid.

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)

def validate_phone(phone):

    # Validates UK mobile phone numbers.

    pattern = r'^(\+44|0)7\d{9}$'

    return re.match(pattern, phone)

def validate_student_id(student_id):

    # Checks student ID format.

    pattern = r'^ST\d{5}$'

    return re.match(pattern, student_id)
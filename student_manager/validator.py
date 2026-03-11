# validator.py

import re

def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)

def validate_phone(phone):

    pattern = r'^(\+44|0)7\d{9}$'

    return re.match(pattern, phone)

def validate_student_id(student_id):

    pattern = r'^ST\d{5}$'

    return re.match(pattern, student_id)
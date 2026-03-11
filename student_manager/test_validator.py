# test_validator.py

import unittest
from validator import validate_email, validate_phone, validate_student_id

class TestValidator(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email("test@email.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("invalidemail"))

    def test_valid_phone(self):
        self.assertTrue(validate_phone("07123456789"))

    def test_invalid_phone(self):
        self.assertFalse(validate_phone("123"))

    def test_valid_student_id(self):
        self.assertTrue(validate_student_id("ST12345"))

    def test_invalid_student_id(self):
        self.assertFalse(validate_student_id("12345"))

if __name__ == "__main__":
    unittest.main()
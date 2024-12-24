from django.test import TestCase
from .models import Student, Attendance

class AttendanceModelTests(TestCase):

    def setUp(self):
        self.student = Student.objects.create(name="John Doe", roll_number="12345")

    def test_student_creation(self):
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.roll_number, "12345")

    def test_attendance_record(self):
        attendance_record = Attendance.objects.create(student=self.student, date="2023-10-01", status="Present")
        self.assertEqual(attendance_record.student, self.student)
        self.assertEqual(attendance_record.status, "Present")
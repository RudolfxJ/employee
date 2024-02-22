# tests/test_employee_model.py
from django.test import TestCase
from .models import Employee, Skill

class EmployeeModelTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            contact_number='1234567890',
            date_of_birth='1990-01-01',
            street_address='123 Main St',
            city='New York',
            postal_code='1001',
            country='USA'
        )

        self.python_skill = Skill.objects.create(
            name='Python',
            employee=self.employee,
            years_experience=5,
            seniority_rating='Expert'
        )
        self.cs_skill = Skill.objects.create(
            name='C#',
            employee=self.employee,
            years_experience=3,
            seniority_rating='Intermediate'
        )
        
    def test_employee_creation(self):
        self.assertEqual(self.employee.employee_code.__len__(), 6)

    def test_employee_str_method(self):
        self.assertEqual(str(self.employee), 'John Doe')

    def test_skill_creation(self):
        self.assertEqual(self.python_skill.name, 'Python')
        self.assertEqual(self.python_skill.years_experience, 5)
        self.assertEqual(self.python_skill.seniority_rating, 'Expert')

        self.assertEqual(self.cs_skill.name, 'C#')
        self.assertEqual(self.cs_skill.years_experience, 3)
        self.assertEqual(self.cs_skill.seniority_rating, 'Intermediate')

    def test_skill_association_with_employee(self):
        self.assertEqual(self.python_skill.employee, self.employee)
        self.assertEqual(self.cs_skill.employee, self.employee)

    def test_employee_email(self):
        self.assertEqual(self.employee.email, 'john@example.com')

    def test_employee_contact_number(self):
        self.assertEqual(self.employee.contact_number, '1234567890')

    def test_employee_address(self):
        self.assertEqual(self.employee.street_address, '123 Main St')
        self.assertEqual(self.employee.city, 'New York')
        self.assertEqual(self.employee.postal_code, '10001')
        self.assertEqual(self.employee.country, 'USA')


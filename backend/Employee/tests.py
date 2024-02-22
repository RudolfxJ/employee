from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

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
        self.assertEqual(self.employee.postal_code, '1001')
        self.assertEqual(self.employee.country, 'USA')

class EmployeeTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

        # Create test data
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            contact_number="1234567890",
            date_of_birth="1990-01-01",
            street_address="123 Main St",
            city="Anytown",
            postal_code="1234",
            country="Country",
        )
        self.skill = Skill.objects.create(
            name="Python",
            employee=self.employee,
            years_experience=5,
            seniority_rating="Expert"
        )

    def test_get_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming this is the only employee

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "contact_number": "0987654321",
            "date_of_birth": "1995-02-02",
            "street_address": "456 Main St",
            "city": "Anytown",
            "postal_code": "4321",
            "country": "Country",
            "skill": [{
                "name": "Django",
                "years_experience": 3,
                "seniority_rating": "Intermediate"
            }]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_employee_with_skills(self):
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})
        data = {
            "first_name": "John Updated",
            "last_name": "Doe Updated",
            "skill": [{
                "name": "Python",
                "years_experience": 5,
                "seniority_rating": "Expert"
            }, {
                "name": "Django",
                "years_experience": 3,
                "seniority_rating": "Intermediate"
            }]
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.get(pk=self.employee.pk).first_name, "John Updated")

    def test_update_employee_without_skills(self):
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})
        data = {
            "first_name": "John Updated",
            "last_name": "Doe Updated",
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.get(pk=self.employee.pk).first_name, "John Updated")

    def test_delete_employee(self):
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())


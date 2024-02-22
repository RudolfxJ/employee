from django.core.management.base import BaseCommand
from Employee.models import Employee, Skill

class Command(BaseCommand):
    employees = [
        {
        "first_name": "John",
        "last_name": "Doe",
        "contact_number": "1234567890",
        "email": "qOqQH@example.com",
        "date_of_birth": "1990-01-01",
        "street_address": "123 Any Street",
        "city": "Anytown",
        "postal_code": "1235",
        "country": "USA",
        "skills": [
            {
            "name": "Programming",
            "years_experience": "5",
            "seniority_rating": "Advanced",
            },
        ],
        },
        {
        "first_name": "Jane",
        "last_name": "Ploe",
        "contact_number": "0987654321",
        "email": "aBaBZ@example.com",
        "date_of_birth": "1992-02-02",
        "street_address": "456 Any Avenue",
        "city": "Anytown",
        "postal_code": "5421",
        "country": "USA",
        "skills": [
            {
            "name": "Design",
            "years_experience": "3",
            "seniority_rating": "Beginner",
            },
        ],
        },
        {
        "first_name": "Jim",
        "last_name": "Koe",
        "contact_number": "1122334455",
        "email": "xYxYZ@example.com",
        "date_of_birth": "1994-03-03",
        "street_address": "789 Any Boulevard",
        "city": "Anytown",
        "postal_code": "6789",
        "country": "USA",
        "skills": [
            {
            "name": "Project Management",
            "years_experience": "2",
            "seniority_rating": "Expert",
            },
        ],
        },
    ]

    def handle(self, *args, **kwargs):
        Employee.objects.all().delete()
        for employee in self.employees:
            data = employee
            skills = data.pop("skills")
            employee_obj = Employee.objects.create(**employee)
            for skill in skills:
                skill['employee'] = employee_obj
                Skill.objects.create(**skill)

        return
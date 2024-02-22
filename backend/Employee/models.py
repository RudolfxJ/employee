import random
import string
from django.db import models

class Employee(models.Model):
    """
    The Employee model represents an employee in the company.
    Each employee has a first name, last name, email, contact number, date of birth, and address details.
    """
    employee_code = models.CharField(max_length=6)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    
    date_of_birth = models.DateField()
    
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=4)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
    @staticmethod
    def generate_employee_code():
        """
        Each ID should be 2 random uppercased letters 
        followed by 4 random numbers.
        """
        return ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=4))

    def save(self, *args, **kwargs):
        if not self.employee_code:
            self.employee_code = Employee.generate_employee_code()
        return super().save(*args, **kwargs)
    

class Skill(models.Model):
    """
    The Skill model represents a skill that an employee may have.
    Each skill has a name, is associated with an employee, has a years of experience and a seniority rating.
    """
    SENIORITY_RATING = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'), 
        ('Expert', 'Expert')
        ]
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_skills")
    years_experience = models.IntegerField()
    seniority_rating = models.CharField(max_length=100, choices=SENIORITY_RATING)

    def __str__(self):
        return self.name
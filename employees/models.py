from django.db import models

from department.models import Area, Department

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    hire_date = models.DateField()
    position = models.CharField(max_length=100)  # Job title
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from django.db import models

from django.db import models
from employees.models import Employee  # Importando o modelo Employee
from trg_trainingmanagement.models import Training

class Participant(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="participant", verbose_name="Employee")
    trainings = models.OneToOneField(Training,on_delete=models.CASCADE, related_name="participants", verbose_name="Trainings")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"


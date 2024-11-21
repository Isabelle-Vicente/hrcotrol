from django.db import models

from employees.models import Employee

class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('EPI', 'Personal Protective Equipment'),
        ('EPC', 'Collective Protective Equipment'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(choices=EQUIPMENT_TYPES, max_length=3)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    acquisition_date = models.DateField()

    def __str__(self):
        return self.name


class MaintenanceInspection(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='inspections')
    date = models.DateField()
    status = models.CharField(max_length=50)  # Example: 'Good Condition', 'Needs Repair', etc.
    observations = models.TextField()

    def __str__(self):
        return f'{self.equipment.name} - {self.date}'
    

class EPIDistribution(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    distribution_date = models.DateField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.employee} - {self.equipment.name}'

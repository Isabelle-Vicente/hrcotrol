from django.db import models
from employees.models import Employee  
class Benefit(models.Model):
    BENEFIT_TYPES = [
        ('Health Insurance', 'Health Insurance'),
        ('Meal Voucher', 'Meal Voucher'),
        ('Transport Voucher', 'Transport Voucher'),
        ('Gym Membership', 'Gym Membership'),
        ('Other', 'Other'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='benefits')
    benefit_type = models.CharField(max_length=50, choices=BENEFIT_TYPES)
    value = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly benefit value")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  
    notes = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"{self.benefit_type} - {self.employee.first_name} {self.employee.last_name}"

    class Meta:
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

from django.db import models
from django.core.validators import MinValueValidator
from employees.models import Employee  

class Contract(models.Model):
    CONTRACT_TYPES = [
        ('CLT', 'CLT'),
        ('Temporary', 'Temporary'),
        ('Internship', 'Internship'),
        ('Freelancer', 'Freelancer'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='contracts')
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # For contracts without a fixed term
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when the record is updated
    document = models.FileField(upload_to='contract_documents/', null=True, blank=True)

    def __str__(self):
        return f"Contract for {self.employee.first_name} {self.employee.last_name} - {self.contract_type}"

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

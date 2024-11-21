from django.db import models

from employees.models import Employee

class IncidentReport(models.Model):
    # Informações do incidente
    name = models.CharField(max_length=100)  # Nome da pessoa
    address = models.CharField(max_length=100)  # Endereço da pessoa
    age = models.IntegerField()  # Idade da pessoa
    identification_number = models.CharField(max_length=20)  # Número de identificação (pode ser CPF ou outro documento)
    identification_document = models.CharField(max_length=100)  # Tipo de documento de identificação (ex: CPF, RG, passaporte)

    # Detalhes do acidente
    type_accident  = models.CharField(max_length=20, choices=[
        ('typical', 'Typical'),
        ('atypical', 'Atypical'),
        ('path', 'Path'),
        ('occupational', 'Occupational'),
    ], default='atypical')
    accident_location = models.CharField(max_length=100)  # Local do acidente (ex: rua, empresa, residência, etc.)
    type_injury = models.CharField(max_length=100)  # Tipo de lesão (ex: fratura, corte, contusão, etc.)
    time_away = models.IntegerField()  # Tempo afastado do trabalho (em dias)
    severity = models.CharField(max_length=50, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    reported_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    # Informações do médico
    doctor_name = models.CharField(max_length=100)  # Nome do médico
    doctor_crm = models.CharField(max_length=10)  # Número do CRM do médico

    def __str__(self):
        return f"Incidente: {self.name} - {self.type_accident} ({self.accident_location})"

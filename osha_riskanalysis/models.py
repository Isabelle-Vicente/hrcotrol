from django.db import models
from department.models import Area

class RiskIdentification(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    number_of_employees = models.IntegerField()
    area_description = models.TextField()
    equipment_description = models.TextField()

    def __str__(self):
        return f'Risk Identification in {self.area.name}'

class RiskAssessment(models.Model):
    risk_identification = models.ForeignKey(RiskIdentification, on_delete=models.CASCADE)
    ergonomic = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('None', 'None')])
    biological = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('None', 'None')])
    chemical = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('None', 'None')])
    physical = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('None', 'None')])
    accident = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('None', 'None')])

    def __str__(self):
        return f'Risk Assessment: {self.risk_identification}'

class RiskControl(models.Model):
    risk_assessment = models.ForeignKey(RiskAssessment, on_delete=models.CASCADE)
    mitigation = models.TextField()

    def __str__(self):
        return f'Risk Control for {self.risk_assessment}'
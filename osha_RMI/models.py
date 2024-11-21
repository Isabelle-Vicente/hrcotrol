from django.db import models

from django.db import models

from employees.models import Employee

# Model for recording security inspections
class SafetyInspection(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    auditor = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Associate with the user who performed the inspection
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    inspected_areas = models.TextField()

    def __str__(self):
        return f"Inspection {self.name} - {self.status}"

# Model for monitoring medical exams
class MedicalExam(models.Model):
    employee_name =models.ForeignKey(Employee, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=100, choices=[('Audiometry', 'Audiometry'), ('Spirometry', 'Spirometry'), ('Blood Test', 'Blood Test')])
    exam_date = models.DateField()
    result = models.TextField()
    recommendations = models.TextField()
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"Exam of {self.employee_name} - {self.exam_type}"
    
# Model for occupational health monitoring
class OccupationalHealthMonitoring(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Associate with the employee
    exams = models.ManyToManyField(MedicalExam)
    monitoring_start_date = models.DateField()
    last_update = models.DateField()

    def __str__(self):
        return f"Health Monitoring - {self.employee.username}"

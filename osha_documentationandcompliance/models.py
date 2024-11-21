from django.db import models

from employees.models import Employee

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('legal', 'Legal'),
        ('normative', 'Normative'),
        ('regulatory', 'Regulatory'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
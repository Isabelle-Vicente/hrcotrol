from django.db import models


class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)  
    portfolio = models.FileField(upload_to='portfolios/', blank=True, null=True)  
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('interview', 'Interview'), ('hired', 'Hired'), ('rejected', 'Rejected')], default='pending')
    image = models.ImageField(upload_to='applicant_images/', null=True, blank=True)
    about = models.TextField()
    education = models.TextField()
    skills  = models.CharField(max_length=500, null=True) 
    interactions = models.TextField(blank=True, null=True)  


    def __str__(self):
        return f"{self.first_name} {self.last_name} "

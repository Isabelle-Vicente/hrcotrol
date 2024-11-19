from django.db import models
from django.utils.translation import gettext_lazy as _

CATEGORY_CHOICES = [
    ('technology', 'Technology'),
    ('finance', 'Finance'),
    # Adicione mais opções aqui
]

class JobStatus(models.TextChoices):
    OPEN = 'open', _('Open')
    CLOSED = 'closed', _('Closed')

class JobDetails(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.CharField(max_length=500)
    education = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100, blank=True, null=True)
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=6, choices=JobStatus.choices, default=JobStatus.OPEN)    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_requirements_list(self):
            return self.requirements.split(', ')
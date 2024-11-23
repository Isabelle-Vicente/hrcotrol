from django.db import models

class Training(models.Model):
    title = models.CharField(max_length=200, verbose_name="Training Title")
    description = models.TextField(verbose_name="Training Description", blank=True, null=True)
    type = models.CharField(
        max_length=50,
        choices=[('onsite', 'Onsite'), ('online', 'Online'), ('hybrid', 'Hybrid')],
        default='onsite',
        verbose_name="Training Type"
    )
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

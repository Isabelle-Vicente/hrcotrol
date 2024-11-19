from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return self.name
from django.db import models

class SafetyPolicy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OperationalProcedure(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    policy = models.ForeignKey(SafetyPolicy, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class EmergencyPlan(models.Model):
    emergency_type = models.CharField(max_length=100)  # Fire, Chemical spill, etc.
    description = models.TextField()
    procedure = models.ForeignKey(OperationalProcedure, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Plan for {self.emergency_type}"

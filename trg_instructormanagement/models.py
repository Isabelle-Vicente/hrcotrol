from django.db import models

from trg_trainingmanagement.models import Training

class Instructor(models.Model):
    name = models.CharField(max_length=150, verbose_name="Instructor Name")
    specialization = models.CharField(max_length=200, verbose_name="Specialization")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    trainings = models.OneToOneField(Training, on_delete=models.CASCADE, related_name="instructors", verbose_name="Trainings")

    def __str__(self):
        return self.name


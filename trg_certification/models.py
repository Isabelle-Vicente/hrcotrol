from django.db import models
from trg_participantmanagement.models import Participant
from trg_trainingmanagement.models import Training

class Certificate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="certificates", verbose_name="Participant")
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name="certificates", verbose_name="Training")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Issue Date")
    validation_code = models.CharField(max_length=50, unique=True, verbose_name="Validation Code")

    def __str__(self):
        return f"Certificate for {self.participant} - {self.training}"

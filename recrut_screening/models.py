from django.db import models
from django.forms import ValidationError
from recrut_applicant.models import Applicant
from recrut_vacancymanagement.models import JobDetails
from django.db.models.signals import pre_save
from django.dispatch import receiver

class ApplicantScreening(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='screenings')
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE, related_name='screenings')
    score_skills = models.IntegerField(default=0)
    score_experience = models.IntegerField(default=0)
    score_compatibility = models.IntegerField(default=0)
    comments = models.TextField(blank=True, null=True)
    screening_date = models.DateField(auto_now_add=True)
    reviewer = models.CharField(max_length=100)  
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')

    def __str__(self):
        return f"Screening for {self.applicant} - {self.job.title}"
    
    def calculate_skill_score(self):
        applicant_skills = self.applicant.skills.split(',') if self.applicant.skills else []
        job_requirements = self.job.requirements.split(',') if self.job.requirements else []
        matching_skills = [skill for skill in applicant_skills if skill.strip().lower() in [r.strip().lower() for r in job_requirements]]
        
        skill_percentage = (len(matching_skills) / len(job_requirements) * 100) if job_requirements else 0
        return skill_percentage

    def total_score(self):
        return self.score_skills + self.score_experience + self.score_compatibility

    def save(self, *args, **kwargs):
        self.score_skills = self.calculate_skill_score()
        super().save(*args, **kwargs)


class ApplicantTesting(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='testings')
    screening = models.OneToOneField(ApplicantScreening, on_delete=models.CASCADE)
    test_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
         ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    feedback = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.applicant} - Test - {self.get_status_display()}"
    
    def clean(self):
        if self.screening.status != 'approved':
            raise ValidationError("Screening must be passed before proceeding to testing.")


class ApplicantInterviewing(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='interviews')
    testing = models.OneToOneField(ApplicantTesting, on_delete=models.CASCADE)
    interview_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    scheduled_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    feedback = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.applicant} - Interview - {self.get_status_display()}"
    
    def clean(self):
        if self.testing.status != 'approved':
            raise ValidationError("The test must be passed before proceeding to the interview.")
   



def can_proceed_to_next_stage(applicant, current_stage):
    if current_stage == 'testing':
        screening = ApplicantScreening.objects.filter(applicant=applicant, status='approved').first()
        return screening is not None
    elif current_stage == 'interviewing':
        testing = ApplicantTesting.objects.filter(applicant=applicant, status='approved').first()
        return testing is not None
    return False




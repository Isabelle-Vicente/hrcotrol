from django import forms
from recrut_screening.models import ApplicantInterviewing, ApplicantScreening, ApplicantTesting


class ApplicantScreeningForm(forms.ModelForm):

    class Meta:
        model = ApplicantScreening
        fields = '__all__'

class ApplicantTestingForm(forms.ModelForm):
    class Meta:
        model = ApplicantTesting
        fields = ['applicant', 'screening', 'test_score', 'feedback', 'status']

class ApplicantInterviewingForm(forms.ModelForm):
    class Meta:
        model = ApplicantInterviewing
        fields = ['applicant', 'testing', 'interview_score', 'scheduled_date', 'feedback', 'status']
from django import forms
from recrut_applicant.models import Applicant


class ApplicantForm(forms.ModelForm):

    class Meta:
        model = Applicant
        fields = '__all__'
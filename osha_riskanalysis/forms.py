from django import forms
from .models import RiskIdentification, RiskAssessment, RiskControl

class RiskIdentificationForm(forms.ModelForm):
    class Meta:
        model = RiskIdentification
        fields = ['area', 'number_of_employees', 'area_description', 'equipment_description']

class RiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = RiskAssessment
        fields = ['risk_identification', 'ergonomic', 'biological', 'chemical', 'physical', 'accident']

class RiskControlForm(forms.ModelForm):
    class Meta:
        model = RiskControl
        fields = ['risk_assessment', 'mitigation']

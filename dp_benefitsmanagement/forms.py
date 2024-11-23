from django import forms
from .models import Benefit

class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = ['employee', 'benefit_type', 'value', 'start_date', 'end_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'employee': 'Employee',
            'benefit_type': 'Benefit Type',
            'value': 'Monthly Value',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'notes': 'Notes',
        }

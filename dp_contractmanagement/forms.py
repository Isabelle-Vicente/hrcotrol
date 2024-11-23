from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'employee', 
            'contract_type', 
            'start_date', 
            'end_date', 
            'salary', 
            'is_active', 
            'document'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(attrs={'step': '0.01'}),
        }

        labels = {
            'employee': 'Employee',
            'contract_type': 'Contract Type',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'salary': 'Salary',
            'is_active': 'Is Active',
            'document': 'Contract Document',
        }

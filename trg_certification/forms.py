from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['participant', 'training', 'validation_code']
        widgets = {
            'participant': forms.Select(attrs={'class': 'form-control'}),
            'training': forms.Select(attrs={'class': 'form-control'}),
            'validation_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Validation Code'}),
        }
        labels = {
            'participant': 'Participant',
            'training': 'Training',
            'validation_code': 'Validation Code',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant'].queryset = self.fields['participant'].queryset.select_related('employee')
        self.fields['training'].queryset = self.fields['training'].queryset.all()

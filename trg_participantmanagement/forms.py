from django import forms

from employees.models import Employee
from trg_trainingmanagement.models import Training
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['employee', 'trainings']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'trainings': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'employee': 'Employee',
            'trainings': 'Trainings',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.all()
        self.fields['trainings'].queryset = Training.objects.all()

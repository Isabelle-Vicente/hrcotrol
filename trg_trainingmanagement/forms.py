
from django import forms

from trg_trainingmanagement.models import Training


class  TrainingForm(forms.ModelForm):
    class Meta :
        model = Training
        fields = ['title', 'description', 'type', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}), 
        }
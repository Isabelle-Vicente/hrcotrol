from django import forms
from .models import TrainingReport

class TrainingReportForm(forms.ModelForm):
    class Meta:
        model = TrainingReport
        fields = ['title', 'report_type', 'training', 'data', 'created_by']
        widgets = {
            'data': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'created_by': forms.TextInput(attrs={'placeholder': 'Generated by'}),
        }
        labels = {
            'title': 'Report Title',
            'report_type': 'Type of Report',
            'training': 'Related Training',
            'data': 'Report Data (JSON)',
            'created_by': 'Created By',
        }

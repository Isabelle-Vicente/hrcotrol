from django import forms
from .models import SafetyInspection, MedicalExam, OccupationalHealthMonitoring

class SafetyInspectionForm(forms.ModelForm):
    class Meta:
        model = SafetyInspection
        fields = ['name', 'description', 'date', 'auditor', 'status', 'inspected_areas']

class MedicalExamForm(forms.ModelForm):
    class Meta:
        model = MedicalExam
        fields = ['employee_name', 'exam_type', 'exam_date', 'result', 'recommendations', 'status']

class OccupationalHealthMonitoringForm(forms.ModelForm):
    class Meta:
        model = OccupationalHealthMonitoring
        fields = ['employee', 'exams', 'monitoring_start_date', 'last_update']


from django import forms
from .models import SafetyPolicy, OperationalProcedure, EmergencyPlan

class SafetyPolicyForm(forms.ModelForm):
    class Meta:
        model = SafetyPolicy
        fields = ['name', 'description', 'active']


class OperationalProcedureForm(forms.ModelForm):
    class Meta:
        model = OperationalProcedure
        fields = ['title', 'description', 'policy', 'active']


class EmergencyPlanForm(forms.ModelForm):
    class Meta:
        model = EmergencyPlan
        fields = ['emergency_type', 'description', 'procedure', 'active']
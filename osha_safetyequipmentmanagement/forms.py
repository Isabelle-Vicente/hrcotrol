from django import forms
from .models import Equipment, MaintenanceInspection, EPIDistribution

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'type', 'description', 'quantity', 'acquisition_date']

class MaintenanceInspectionForm(forms.ModelForm):
    class Meta:
        model = MaintenanceInspection
        fields = ['equipment', 'date', 'status', 'observations']

class EPIDistributionForm(forms.ModelForm):
    class Meta:
        model = EPIDistribution
        fields = ['employee', 'equipment', 'distribution_date', 'quantity']

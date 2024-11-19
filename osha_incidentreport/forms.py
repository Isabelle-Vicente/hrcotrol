from django import forms
from osha_incidentreport.models import IncidentReport

class IncidentReportForm(forms.ModelForm):

    class Meta:
        model = IncidentReport
        fields = '__all__'


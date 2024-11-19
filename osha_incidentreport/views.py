from django.shortcuts import get_object_or_404, redirect, render
from osha_incidentreport.forms import IncidentReportForm
from osha_incidentreport.models import IncidentReport

def incident_report_list(request):
    incidentreport = IncidentReport.objects.all()
    return render(request, 'incident_report_list.html', {'incidentreport': incidentreport})

def incident_report_create(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_report_list')  
    else:
        form = IncidentReportForm() 
    return render(request, 'incident_report_form.html', {'form': form})

def incident_report_update(request, pk):
    incidentreport = get_object_or_404(IncidentReport, pk=pk)
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, instance=incidentreport)
        if form.is_valid():
            form.save()
            return redirect('incident_report_list')
        else:
            form = IncidentReportForm(instance=incidentreport)
        return render(request, 'incident_report_form.html', {'form': form})

def incident_report_delete(request, pk):
    incidentreport = get_object_or_404(IncidentReport, pk=pk)
    if request.method == 'POST':
        incidentreport.delete()
        return redirect('incident_report_list')
    return render(request, 'incident_report_confirm_delete.html', {'incidentreport': incidentreport})
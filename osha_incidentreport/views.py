from django.shortcuts import get_object_or_404, redirect, render
from osha_incidentreport.forms import IncidentReportForm
from osha_incidentreport.models import IncidentReport
from django.core.paginator import Paginator


def incident_report_list(request):
    incidentreports_list = IncidentReport.objects.all()
    paginator = Paginator(incidentreports_list, 4)  

    page_number = request.GET.get('page')
    incidentreports = paginator.get_page(page_number)

    return render(request, 'incident_report_list.html', {'incidentreports': incidentreports})

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
    incident_report = get_object_or_404(IncidentReport, pk=pk)

    if request.method == 'POST':
        form = IncidentReportForm(request.POST, instance=incident_report)
        if form.is_valid():
            form.save()
            return redirect('incident_report_list')
    else:
        form = IncidentReportForm(instance=incident_report)

    return render(request, 'incident_report_form.html', {'form': form, 'incident_report': incident_report})

def incident_report_delete(request, pk):
    incidentreport = get_object_or_404(IncidentReport, pk=pk)
    if request.method == 'POST':
        incidentreport.delete()
        return redirect('incident_report_list')
    return render(request, 'incident_report_confirm_delete.html', {'incidentreport': incidentreport})
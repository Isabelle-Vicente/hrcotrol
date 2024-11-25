from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, redirect, render
from osha_RMI.forms import MedicalExamForm, OccupationalHealthMonitoringForm, SafetyInspectionForm
from osha_RMI.models import MedicalExam, OccupationalHealthMonitoring, SafetyInspection

# Paginação - Função Genérica
def paginate_objects(request, objects_list, per_page=4):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

# Safety Inspection Views
def safety_inspection_list(request):
    safetyinspections = SafetyInspection.objects.all()
    safetyinspections_paginated = paginate_objects(request, safetyinspections)
    return render(request, 'safety_inspection_list.html', {'safetyinspections': safetyinspections_paginated})

def safety_inspection_create(request):
    if request.method == 'POST':
        form = SafetyInspectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('safety_inspection_list')
    else:
        form = SafetyInspectionForm()
    return render(request, 'safety_inspection_form.html', {'form': form})

def safety_inspection_update(request, pk):
    safetyinspection = get_object_or_404(SafetyInspection, pk=pk)
    if request.method == 'POST':
        form = SafetyInspectionForm(request.POST, instance=safetyinspection)
        if form.is_valid():
            form.save()
            return redirect('safety_inspection_list')
    else:
        form = SafetyInspectionForm(instance=safetyinspection)
    return render(request, 'safety_inspection_form.html', {'form': form})

def safety_inspection_delete(request, pk):
    safetyinspection = get_object_or_404(SafetyInspection, pk=pk)
    if request.method == 'POST':
        safetyinspection.delete()
        return redirect('safety_inspection_list')
    return render(request, 'safety_inspection_confirm_delete.html', {'safetyinspection': safetyinspection})

# Medical Exam Views
def medical_exam_list(request):
    medicalexams_list = MedicalExam.objects.all()
    medicalexams_paginated = paginate_objects(request, medicalexams_list)
    return render(request, 'medical_exam_list.html', {'medicalexams': medicalexams_paginated})

def medical_exam_create(request):
    if request.method == 'POST':
        form = MedicalExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_exam_list')
    else:
        form = MedicalExamForm()
    return render(request, 'medical_exam_form.html', {'form': form})

def medical_exam_update(request, pk):
    medicalexam = get_object_or_404(MedicalExam, pk=pk)
    if request.method == 'POST':
        form = MedicalExamForm(request.POST, instance=medicalexam)
        if form.is_valid():
            form.save()
            return redirect('medical_exam_list')
    else:
        form = MedicalExamForm(instance=medicalexam)
    return render(request, 'medical_exam_form.html', {'form': form})

def medical_exam_delete(request, pk):
    medicalexam = get_object_or_404(MedicalExam, pk=pk)
    if request.method == 'POST':
        medicalexam.delete()
        return redirect('medical_exam_list')
    return render(request, 'medical_exam_confirm_delete.html', {'medicalexam': medicalexam})

# Occupational Health Monitoring Views
def occupational_health_monitoring_list(request):
    occupationalhealthmonitorings = OccupationalHealthMonitoring.objects.all()
    return render(request, 'occupational_health_monitoring_list.html', {'occupationalhealthmonitorings': occupationalhealthmonitorings})

def occupational_health_monitoring_create(request):
    if request.method == 'POST':
        form = OccupationalHealthMonitoringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('occupational_health_monitoring_list')
    else:
        form = OccupationalHealthMonitoringForm()
    return render(request, 'occupational_health_monitoring_form.html', {'form': form})

def occupational_health_monitoring_update(request, pk):
    occupationalhealthmonitoring = get_object_or_404(OccupationalHealthMonitoring, pk=pk)
    if request.method == 'POST':
        form = OccupationalHealthMonitoringForm(request.POST, instance=occupationalhealthmonitoring)
        if form.is_valid():
            form.save()
            return redirect('occupational_health_monitoring_list')
    else:
        form = OccupationalHealthMonitoringForm(instance=occupationalhealthmonitoring)
    return render(request, 'occupational_health_monitoring_form.html', {'form': form})

def occupational_health_monitoring_delete(request, pk):
    occupationalhealthmonitoring = get_object_or_404(OccupationalHealthMonitoring, pk=pk)
    if request.method == 'POST':
        occupationalhealthmonitoring.delete()
        return redirect('occupational_health_monitoring_list')
    return render(request, 'occupational_health_monitoring_confirm_delete.html', {'occupationalhealthmonitoring': occupationalhealthmonitoring})

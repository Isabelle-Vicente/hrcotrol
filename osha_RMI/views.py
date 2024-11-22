from django.shortcuts import get_object_or_404, redirect, render
from osha_RMI.forms import MedicalExamForm, OccupationalHealthMonitoringForm, SafetyInspectionForm
from osha_RMI.models import MedicalExam, OccupationalHealthMonitoring, SafetyInspection

def safety_inspection_list(request):
    safetyinspections = SafetyInspection.objects.all() 
    return render(request, 'safety_inspection_list.html', {'safetyinspections': safetyinspections})  

def safety_inspection_create(request):
    if request.method == 'POST':
        form = SafetyInspectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('safety_inspection_list')
        else:
            print(form.errors)  
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

#----------------------------------------------------------------------------------------------------------

def medical_exam_list(request):
    medicalexams = MedicalExam.objects.all()  
    return render(request, 'medical_exam_list.html', {'medicalexams': medicalexams})  

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

#----------------------------------------------------------------------------------------------------------

def occupational_health_monitoring_list(request):
    occupationalhealthmonitoring = OccupationalHealthMonitoring.objects.all()
    return render(request, 'occupational_health_monitoring_list.html', {'occupationalhealthmonitoring': occupationalhealthmonitoring})

def occupational_health_monitoring_create(request):
    if request.method == 'POST':
        form = OccupationalHealthMonitoring(request.POST)
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
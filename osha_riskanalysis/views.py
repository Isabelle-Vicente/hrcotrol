from django.shortcuts import render, get_object_or_404, redirect
from .models import RiskIdentification, RiskAssessment, RiskControl
from .forms import RiskIdentificationForm, RiskAssessmentForm, RiskControlForm

def dashboard(request):
    assessments = RiskAssessment.objects.all()
    return render(request, 'dashboard.html', {'assessments': assessments})

# Risk Identification CRUD
def risk_identification_list(request):
    risks = RiskIdentification.objects.all()
    return render(request, 'risk_identification_list.html', {'risks': risks})

def risk_identification_create(request):
    if request.method == 'POST':
        form = RiskIdentificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('risk_identification_list')
    else:
        form = RiskIdentificationForm()
    return render(request, 'risk_identification_form.html', {'form': form})

def risk_identification_update(request, pk):
    risk = get_object_or_404(RiskIdentification, pk=pk)
    if request.method == 'POST':
        form = RiskIdentificationForm(request.POST, instance=risk)
        if form.is_valid():
            form.save()
            return redirect('risk_identification_list')
    else:
        form = RiskIdentificationForm(instance=risk)
    return render(request, 'risk_identification_form.html', {'form': form})

def risk_identification_delete(request, pk):
    risk = get_object_or_404(RiskIdentification, pk=pk)
    if request.method == 'POST':
        risk.delete()
        return redirect('risk_identification_list')
    return render(request, 'risk_identification_confirm_delete.html', {'risk': risk})

# Risk Assessment CRUD
def risk_assessment_list(request):
    assessments = RiskAssessment.objects.all()
    return render(request, 'risk_assessment_list.html', {'assessments': assessments})

def risk_assessment_create(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('risk_assessment_list')
    else:
        form = RiskAssessmentForm()
    return render(request, 'risk_assessment_form.html', {'form': form})

def risk_assessment_update(request, pk):
    assessment = get_object_or_404(RiskAssessment, pk=pk)
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            return redirect('risk_assessment_list')
    else:
        form = RiskAssessmentForm(instance=assessment)
    return render(request, 'risk_assessment_form.html', {'form': form})

def risk_assessment_delete(request, pk):
    assessment = get_object_or_404(RiskAssessment, pk=pk)
    if request.method == 'POST':
        assessment.delete()
        return redirect('risk_assessment_list')
    return render(request, 'risk_assessment_confirm_delete.html', {'assessment': assessment})

# Risk Control CRUD
def risk_control_list(request):
    controls = RiskControl.objects.all()
    return render(request, 'risk_control_list.html', {'controls': controls})

def risk_control_create(request):
    if request.method == 'POST':
        form = RiskControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('risk_control_list')
    else:
        form = RiskControlForm()
    return render(request, 'risk_control_form.html', {'form': form})

def risk_control_update(request, pk):
    control = get_object_or_404(RiskControl, pk=pk)
    if request.method == 'POST':
        form = RiskControlForm(request.POST, instance=control)
        if form.is_valid():
            form.save()
            return redirect('risk_control_list')
    else:
        form = RiskControlForm(instance=control)
    return render(request, 'risk_control_form.html', {'form': form})

def risk_control_delete(request, pk):
    control = get_object_or_404(RiskControl, pk=pk)
    if request.method == 'POST':
        control.delete()
        return redirect('risk_control_list')
    return render(request, 'risk_control_confirm_delete.html', {'control': control})

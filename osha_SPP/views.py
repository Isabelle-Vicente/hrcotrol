from django.shortcuts import get_object_or_404, redirect, render
from osha_SPP.forms import SafetyPolicyForm, OperationalProcedureForm, EmergencyPlanForm
from osha_SPP.models import SafetyPolicy, OperationalProcedure, EmergencyPlan

def safetypolicy_list(request):
    safetypolicy = SafetyPolicy.objects.all()
    return render(request, 'safetypolicy_list.html', {'safetypolicy': safetypolicy})

def safetypolicy_create(request):
    if request.method == 'POST':
        form = SafetyPolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('safetypolicy_list')  
    else:
        form = SafetyPolicyForm() 
    return render(request, 'safetypolicy_form.html', {'form': form})

def safetypolicy_update(request, pk):
    safetypolicy = get_object_or_404(SafetyPolicy, pk=pk)
    if request.method == 'POST':
        form = SafetyPolicyForm(request.POST, instance=safetypolicy)
        if form.is_valid():
            form.save()
            return redirect('safetypolicy_list')
        else:
            form = SafetyPolicyForm(instance=safetypolicy)
        return render(request, 'safetypolicy_form.html', {'form': form})

def safetypolicy_delete(request, pk):
    safetypolicy = get_object_or_404(SafetyPolicy, pk=pk)
    if request.method == 'POST':
        safetypolicy.delete()
        return redirect('safetypolicy_list')
    return render(request, 'safetypolicy_confirm_delete.html', {'safetypolicy': safetypolicy})


# --------------------------------------------------------------------------------------

def operational_procedure_list(request):
    operationalprocedure = OperationalProcedure.objects.all()
    return render(request, 'operational_procedure_list.html', {'operationalprocedure': operationalprocedure})

def operational_procedure_create(request):
    if request.method == 'POST':
        form = OperationalProcedureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operational_procedure_list')  
    else:
        form = OperationalProcedureForm() 
    return render(request, 'operational_procedure_form.html', {'form': form})

def operational_procedure_update(request, pk):
    operationalprocedure = get_object_or_404(OperationalProcedure, pk=pk)
    if request.method == 'POST':
        form = OperationalProcedureForm(request.POST, instance=operationalprocedure)
        if form.is_valid():
            form.save()
            return redirect('operational_procedure_list')
        else:
            form = OperationalProcedureForm(instance=operationalprocedure)
        return render(request, 'operational_procedure_form.html', {'form': form})

def operational_procedure_delete(request, pk):
    operationalprocedure = get_object_or_404(OperationalProcedure, pk=pk)
    if request.method == 'POST':
        operationalprocedure.delete()
        return redirect('operational_procedure_list')
    return render(request, 'operational_procedure_confirm_delete.html', {'operationalprocedure': operationalprocedure})

# --------------------------------------------------------------------------------------

def emergency_plan_list(request):
    emergencyplan = EmergencyPlan.objects.all()
    return render(request, 'emergency_plan_list.html', {'emergencyplan': emergencyplan})

def emergency_plan_create(request):
    if request.method == 'POST':
        form = EmergencyPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emergency_plan_list')  
    else:
        form = EmergencyPlanForm() 
    return render(request, 'emergency_plan_form.html', {'form': form})

def emergency_plan_update(request, pk):
    emergencyplan = get_object_or_404(EmergencyPlan, pk=pk)
    if request.method == 'POST':
        form = EmergencyPlanForm(request.POST, instance=emergencyplan)
        if form.is_valid():
            form.save()
            return redirect('emergency_plan_list')
        else:
            form = EmergencyPlanForm(instance=emergencyplan)
        return render(request, 'emergency_plan_form.html', {'form': form})

def emergency_plan_delete(request, pk):
    emergencyplan = get_object_or_404(EmergencyPlan, pk=pk)
    if request.method == 'POST':
        emergencyplan.delete()
        return redirect('emergency_plan_list')
    return render(request, 'emergency_plan_confirm_delete.html', {'emergencyplan': emergencyplan})
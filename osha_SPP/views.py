from django.shortcuts import get_object_or_404, redirect, render
from osha_SPP.forms import SafetyPolicyForm, OperationalProcedureForm, EmergencyPlanForm
from osha_SPP.models import SafetyPolicy, OperationalProcedure, EmergencyPlan
from django.core.paginator import Paginator


def safetypolicy_list(request):
    safetypolicys = SafetyPolicy.objects.all()
    paginator = Paginator(safetypolicys, 4)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'safetypolicy_list.html', {'page_obj': page_obj})


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

from django.core.paginator import Paginator

def operational_procedure_list(request):
    operationalprocedures = OperationalProcedure.objects.all()  # Obtendo todos os procedimentos operacionais
    paginator = Paginator(operationalprocedures, 4)  # Dividindo em páginas de 4 itens
    page_number = request.GET.get('page')  # Obtendo o número da página a partir da URL
    page_obj = paginator.get_page(page_number)  # Pagina os resultados

    return render(request, 'operational_procedure_list.html', {'page_obj': page_obj})  # Passando a página paginada para o template


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

from django.core.paginator import Paginator

def emergency_plan_list(request):
    # Obter todos os planos de emergência
    emergencyplans = EmergencyPlan.objects.all()

    # Configurar a paginação (4 planos por página, por exemplo)
    paginator = Paginator(emergencyplans, 4)

    # Obter o número da página a partir dos parâmetros da URL
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'emergency_plan_list.html', {'page_obj': page_obj})


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
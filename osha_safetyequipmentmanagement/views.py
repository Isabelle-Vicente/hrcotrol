from django.shortcuts import get_object_or_404, redirect, render
from .forms import EquipmentForm, MaintenanceInspectionForm, EPIDistributionForm
from .models import Equipment, MaintenanceInspection, EPIDistribution
from django.core.paginator import Paginator


def equipment_list(request):
    equipments = Equipment.objects.all()  # Obter todos os equipamentos
    paginator = Paginator(equipments, 4)  # 10 equipamentos por página
    page_number = request.GET.get('page')  # Pega o número da página da URL
    page_obj = paginator.get_page(page_number)  # Obtém os objetos para a página
    return render(request, 'equipment_list.html', {'page_obj': page_obj})


def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')  
    else:
        form = EquipmentForm() 
    return render(request, 'equipment_form.html', {'form': form})

def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
        else:
            form = EquipmentForm(instance=equipment)
        return render(request, 'equipment_form.html', {'form': form})

def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'equipment_confirm_delete.html', {'equipment': equipment})

# --------------------------------------------------------------------------------------

def maintenance_inspection_list(request):
    maintenanceinspections = MaintenanceInspection.objects.all()  # Obter todas as inspeções de manutenção
    paginator = Paginator(maintenanceinspections, 4)  # 10 itens por página
    page_number = request.GET.get('page')  # Pega o número da página da URL
    page_obj = paginator.get_page(page_number)  # Obtém os objetos para a página
    return render(request, 'maintenance_inspection_list.html', {'page_obj': page_obj})

def maintenance_inspection_create(request):
    if request.method == 'POST':
        form = MaintenanceInspectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_inspection_list')  
    else:
        form = MaintenanceInspectionForm() 
    return render(request, 'maintenance_inspection_form.html', {'form': form})

def maintenance_inspection_update(request, pk):
    maintenanceinspection = get_object_or_404(MaintenanceInspection, pk=pk)
    if request.method == 'POST':
        form = MaintenanceInspectionForm(request.POST, instance=maintenanceinspection)
        if form.is_valid():
            form.save()
            return redirect('maintenance_inspection_list')
        else:
            form = MaintenanceInspectionForm(instance=maintenanceinspection)
        return render(request, 'maintenance_inspection_form.html', {'form': form})

def maintenance_inspection_delete(request, pk):
    maintenanceinspection = get_object_or_404(MaintenanceInspection, pk=pk)
    if request.method == 'POST':
        maintenanceinspection.delete()
        return redirect('maintenance_inspection_list')
    return render(request, 'maintenance_inspection_confirm_delete.html', {'maintenanceinspection': maintenanceinspection})

# --------------------------------------------------------------------------------------


def epi_distribution_list(request):
    epidistributions = EPIDistribution.objects.all()  # Obter todas as distribuições de EPI
    paginator = Paginator(epidistributions, 4)  # 10 itens por página
    page_number = request.GET.get('page')  # Pega o número da página da URL
    page_obj = paginator.get_page(page_number)  # Obtém os objetos para a página
    return render(request, 'epi_distribution_list.html', {'page_obj': page_obj})

def epi_distribution_create(request):
    if request.method == 'POST':
        form = EPIDistributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('epi_distribution_list')  
    else:
        form = EPIDistributionForm() 
    return render(request, 'epi_distribution_form.html', {'form': form})

def epi_distribution_update(request, pk):
    epidistribution = get_object_or_404(EPIDistribution, pk=pk)
    if request.method == 'POST':
        form = EPIDistributionForm(request.POST, instance=epidistribution)
        if form.is_valid():
            form.save()
            return redirect('epi_distribution_list')
        else:
            form = EPIDistributionForm(instance=epidistribution)
        return render(request, 'epi_distribution_form.html', {'form': form})

def epi_distribution_delete(request, pk):
    epidistribution = get_object_or_404(EPIDistribution, pk=pk)
    if request.method == 'POST':
        epidistribution.delete()
        return redirect('epi_distribution_list')
    return render(request, 'epi_distribution_confirm_delete.html', {'epidistribution': epidistribution})
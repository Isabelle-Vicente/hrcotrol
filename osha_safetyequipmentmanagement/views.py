from django.shortcuts import get_object_or_404, redirect, render
from .forms import EquipmentForm, MaintenanceInspectionForm, EPIDistributionForm
from .models import Equipment, MaintenanceInspection, EPIDistribution

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment})

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
    maintenanceinspection = MaintenanceInspection.objects.all()
    return render(request, 'maintenance_inspection_list.html', {'maintenanceinspection': maintenanceinspection})

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
    epidistribution = EPIDistribution.objects.all()
    return render(request, 'epi_distribution_list.html', {'epidistribution': epidistribution})

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
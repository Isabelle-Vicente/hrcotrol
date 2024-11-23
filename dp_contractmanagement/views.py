from django.shortcuts import get_object_or_404, render, redirect
from dp_contractmanagement.models import Contract
from .forms import ContractForm


def contract_list(request):
    contract = Contract.objects.all()
    return render(request, 'contract_list.html', {'contract': contract})

def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contract_list')  
    else:
        form = ContractForm()
    return render(request, 'contract_form.html', {'form': form})

def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')  
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contract_form.html', {'form': form})
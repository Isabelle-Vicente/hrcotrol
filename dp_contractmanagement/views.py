from django.shortcuts import get_object_or_404, render, redirect
from dp_contractmanagement.models import Contract
from .forms import ContractForm
from django.core.paginator import Paginator

def contract_list(request):
    contracts_list = Contract.objects.all()
    paginator = Paginator(contracts_list, 4)  
    page_number = request.GET.get('page')
    contracts = paginator.get_page(page_number)
    return render(request, 'contract_list.html', {'contracts': contracts})



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
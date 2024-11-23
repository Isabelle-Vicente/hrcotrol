from django.shortcuts import get_object_or_404, render, redirect
from dp_benefitsmanagement.forms import BenefitForm
from .models import Benefit

def benefit_list(request):
    benefit = Benefit.objects.all()
    return render(request, 'benefit_list.html', {'benefit': benefit})

def benefit_create(request):
    if request.method == 'POST':
        form = BenefitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('benefit_list')  
    else:
        form = BenefitForm()
    return render(request, 'benefit_form.html', {'form': form})

def benefit_update(request, pk):
    benefit = get_object_or_404(Benefit, pk=pk)
    if request.method == 'POST':
        form = BenefitForm(request.POST, instance=benefit)
        if form.is_valid():
            form.save()
            return redirect('benefit_list')
    else:
        form = BenefitForm(instance=benefit)
    return render(request, 'benefit_form.html', {'form': form})
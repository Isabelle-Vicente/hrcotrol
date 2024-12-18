from django.shortcuts import get_object_or_404, redirect, render
from trg_trainingmanagement.forms import TrainingForm
from trg_trainingmanagement.models import Training

from django.core.paginator import Paginator
from trg_trainingmanagement.models import Training

def training_list(request):
    trainings = Training.objects.all()
    paginator = Paginator(trainings, 4)  

    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)  

    return render(request, 'training_list.html', {'page_obj': page_obj})


def training_create(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm()  # Formulário instanciado para uma requisição GET
    
    return render(request, 'training_form.html', {'form': form})

    
def training_update(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')  
    else:
        form = TrainingForm(instance=training)
    
    return render(request, 'training_form.html', {'form': form})

    
def training_delete(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        training.delete()
        return redirect('training_list')
    return render(request, 'training_confirm_delete.html', {'training':training})


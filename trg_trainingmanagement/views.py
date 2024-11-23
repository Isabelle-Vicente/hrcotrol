from django.shortcuts import get_object_or_404, redirect, render
from trg_trainingmanagement.forms import TrainingForm
from trg_trainingmanagement.models import Training

def training_list(request):
    training = Training.objects.all()
    return render(request, 'training_list.html', {'training': training})

def training_create(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
        else:
            form = TrainingForm()
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


from django.shortcuts import get_object_or_404, redirect, render

from trg_participantmanagement.forms import ParticipantForm
from trg_participantmanagement.models import Participant

def participant_list(request):
    participants = Participant.objects.prefetch_related('trainings').select_related('employee')
    return render(request, 'participant_list.html', {'participants': participants})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')  
    else:
        form = ParticipantForm()  
    return render(request, 'participant_form.html', {'form': form})
    

def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participant_form.html', {'form': form})

    

def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'participant_confirm_delete.html', {'participant':participant})


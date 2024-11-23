from django.shortcuts import get_object_or_404, redirect, render
from trg_instructormanagement.forms import InstructorForm
from trg_instructormanagement.models import Instructor

def instructor_list(request):
    instructor = Instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructor': instructor})

def instructor_create(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor_list') 
    else:
        form = InstructorForm()
    
    return render(request, 'instructor_form.html', {'form': form})
    
def instructor_update(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')
        else:
            form = InstructorForm(instance=instructor)
        return render(request, 'instructor_form.html', {'form': form})
    
def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.delete()
        return redirect('instructor_list')
    return render(request, 'instructor_confirm_delete.html', {'instructor':instructor})


from django.shortcuts import get_object_or_404, redirect, render
from trg_instructormanagement.forms import InstructorForm
from trg_instructormanagement.models import Instructor
from django.core.paginator import Paginator


def instructor_list(request):
    instructors = Instructor.objects.all()

    paginator = Paginator(instructors, 4)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'instructor_list.html', {'page_obj': page_obj})

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


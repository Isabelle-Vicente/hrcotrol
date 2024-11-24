from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from recrut_vacancymanagement.models import JobDetails
from recrut_vacancymanagement.forms import JobDetailsForm  

def jobdetails_list(request):
    job_list = JobDetails.objects.all()

    title_filter = request.GET.get('title')
    if title_filter:
        job_list = job_list.filter(title__icontains=title_filter)

    job_list = job_list.order_by('title')
    paginator = Paginator(job_list, 4)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    return render(request, 'jobdetails/jobdetails_list.html', {
        'jobs': jobs,
    })

# Criar uma nova vaga
def jobdetails_create(request):
    if request.method == 'POST':
        form = JobDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobdetails_list')
    else:
        form = JobDetailsForm()
    return render(request, 'jobdetails/jobdetails_form.html', {'form': form})

# Atualizar uma vaga existente
def jobdetails_update(request, pk):
    job_detail = get_object_or_404(JobDetails, pk=pk)
    if request.method == "POST":
        form = JobDetailsForm(request.POST, instance=job_detail)
        if form.is_valid():
            form.save()
            return redirect('jobdetails_list')
    else:
        form = JobDetailsForm(instance=job_detail)
    
    requirements_list = job_detail.requirements.split(',') if job_detail.requirements else []
    
    return render(request, 'jobdetails/jobdetails_edit.html', {
        'form': form,
        'requirements_list': requirements_list
    })

# Excluir uma vaga
def jobdetails_delete(request, pk):
    job = get_object_or_404(JobDetails, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('jobdetails_list')
    return render(request, 'jobdetails/jobdetails_confirm_delete.html', {'job': job})

# Detalhes de uma vaga em JSON
def jobdetails_detail(request, pk):
    job = get_object_or_404(JobDetails, pk=pk)
    data = {
        'title': job.title,
        'description': job.description,
        'requirements': job.requirements,
        'education': job.education,
        'category': job.category,
        'location': job.location,
        'salary_range': job.salary_range,
        'status': job.status,
    }
    return JsonResponse(data)

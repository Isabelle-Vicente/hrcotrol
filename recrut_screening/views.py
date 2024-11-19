from pyexpat.errors import messages
from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import ApplicantScreening
from .forms import ApplicantScreeningForm
from .models import ApplicantTesting
from .forms import ApplicantTestingForm
from .models import ApplicantInterviewing
from .forms import ApplicantInterviewingForm

# Listar triagens de candidatos
def applicant_screening_list(request):
    screenings = ApplicantScreening.objects.all()
    
    # Filtrar pelo status (opcional)
    status_filter = request.GET.get('status')
    if status_filter:
        screenings = screenings.filter(status=status_filter)
    
    paginator = Paginator(screenings, 4)  
    page_number = request.GET.get('page')
    screenings_page = paginator.get_page(page_number)
    
    return render(request, 'applicant_screening/applicant_screening_list.html', {
        'screenings': screenings_page,
    })

# Criar uma nova triagem de candidato
def applicant_screening_create(request):
    if request.method == 'POST':
        form = ApplicantScreeningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applicant_screening_list')
    else:
        form = ApplicantScreeningForm()
    return render(request, 'applicant_screening/applicant_screening_form.html', {'form': form})

# Atualizar uma triagem existente
def applicant_screening_update(request, pk):
    screening = get_object_or_404(ApplicantScreening, pk=pk)
    if request.method == 'POST':
        form = ApplicantScreeningForm(request.POST, instance=screening)
        if form.is_valid():
            form.save()
            return redirect('applicant_screening_list')
    else:
        form = ApplicantScreeningForm(instance=screening)
    
    return render(request, 'applicant_screening/applicant_screening_form.html', {
        'form': form,
    })

# Excluir uma triagem
def applicant_screening_delete(request, pk):
    screening = get_object_or_404(ApplicantScreening, pk=pk)
    if request.method == 'POST':
        screening.delete()
        return redirect('applicant_screening_list')
    return render(request, 'applicant_screening/applicant_screening_confirm_delete.html', {'screening': screening})

# Detalhes de uma triagem em JSON
def applicant_screening_detail(request, pk):
    screening = get_object_or_404(ApplicantScreening, pk=pk)
    data = {
        'applicant_first_name': screening.applicant.first_name,
        'applicant_last_name': screening.applicant.last_name,
        'applicant_email': screening.applicant.email,
        'job': screening.job.title,
        'score_skills': screening.score_skills,
        'score_experience': screening.score_experience,
        'score_compatibility': screening.score_compatibility,
        'comments': screening.comments,
        'screening_date': screening.screening_date,
        'reviewer': screening.reviewer,
        'status': screening.status,
    }
    return JsonResponse(data)

def applicant_testing_list(request):
    testings = ApplicantTesting.objects.all()
    status_filter = request.GET.get('status')
    if status_filter:
        testings = testings.filter(status=status_filter)
    
    paginator = Paginator(testings, 4)
    page_number = request.GET.get('page')
    testings_page = paginator.get_page(page_number)
    
    return render(request, 'applicant_testing/applicant_testing_list.html', {
        'testings': testings_page,
    })

# Criar um novo teste para candidato
def applicant_testing_create(request):
    if request.method == 'POST':
        form = ApplicantTestingForm(request.POST)
        if form.is_valid():
            testing = form.save(commit=False)
            try:
                if testing.screening.status == 'approved':
                    testing.full_clean()  
                    testing.save()
                    return redirect('applicant_testing_list')
                else:
                    messages.error(request, "Screening must be passed before proceeding to testing.")
                    return redirect('applicant_screening_list')
            except ValidationError as e:
                messages.error(request, e.message_dict.get('__all__')[0])  
                return redirect('applicant_screening_list')
    else:
        form = ApplicantTestingForm()
    return render(request, 'applicant_testing/applicant_testing_form.html', {'form': form})



# Atualizar um teste existente
def applicant_testing_update(request, pk):
    testing = get_object_or_404(ApplicantTesting, pk=pk)
    if request.method == 'POST':
        form = ApplicantTestingForm(request.POST, instance=testing)
        if form.is_valid():
            form.save()
            return redirect('applicant_testing_list')
    else:
        form = ApplicantTestingForm(instance=testing)
    
    return render(request, 'applicant_testing/applicant_testing_form.html', {
        'form': form,
    })

# Excluir um teste
def applicant_testing_delete(request, pk):
    testing = get_object_or_404(ApplicantTesting, pk=pk)
    if request.method == 'POST':
        testing.delete()
        return redirect('applicant_testing_list')
    return render(request, 'applicant_testing/applicant_testing_confirm_delete.html', {'testing': testing})

# Detalhes de um teste em JSON
def applicant_testing_detail(request, pk):
    testing = get_object_or_404(ApplicantTesting, pk=pk)
    data = {
        'applicant_first_name': testing.applicant.first_name,
        'applicant_last_name': testing.applicant.last_name,
        'applicant_email': testing.applicant.email,
        'test_score': testing.test_score,
        'feedback': testing.feedback,
        'status': testing.status,
    }
    return JsonResponse(data)

# Listar entrevistas de candidatos
def applicant_interviewing_list(request):
    interviews = ApplicantInterviewing.objects.all().order_by('scheduled_date')  

    # Filtro de status (se houver)
    status_filter = request.GET.get('status')
    if status_filter:
        interviews = interviews.filter(status=status_filter)

    # Paginação
    paginator = Paginator(interviews, 4)  
    page_number = request.GET.get('page')
    interviews_page = paginator.get_page(page_number)

    return render(request, 'applicant_interviewing/applicant_interviewing_list.html', {
        'interviewings': interviews_page,
    })


# Criar uma nova entrevista para candidato
def applicant_interviewing_create(request):
    if request.method == 'POST':
        form = ApplicantInterviewingForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            try:
                if interview.testing.status == 'approved':
                    interview.full_clean()  
                    interview.save()
                    return redirect('applicant_interview_list')
                else:
                    messages.error(request, "Testing not approved yet. Cannot proceed to interview.")
                    return redirect('applicant_testing_list')
            except ValidationError as e:
                messages.error(request, e.message_dict.get('__all__')[0])  
                return redirect('applicant_testing_list')
    else:
        form = ApplicantInterviewingForm()
    return render(request, 'applicant_interviewing/applicant_interviewing_form.html', {'form': form})



# Atualizar uma entrevista existente
def applicant_interviewing_update(request, pk):
    interview = get_object_or_404(ApplicantInterviewing, pk=pk)
    if request.method == 'POST':
        form = ApplicantInterviewingForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return redirect('applicant_interviewing_list')
    else:
        form = ApplicantInterviewingForm(instance=interview)
    
    return render(request, 'applicant_interviewing/applicant_interviewing_form.html', {
        'form': form,
    })

# Excluir uma entrevista
def applicant_interviewing_delete(request, pk):
    interview = get_object_or_404(ApplicantInterviewing, pk=pk)
    if request.method == 'POST':
        interview.delete()
        return redirect('applicant_interviewing_list')
    return render(request, 'applicant_interviewing/applicant_interviewing_confirm_delete.html', {'interview': interview})

# Detalhes de uma entrevista em JSON
def applicant_interviewing_detail(request, pk):
    interview = get_object_or_404(ApplicantInterviewing, pk=pk)
    data = {
        'applicant_first_name': interview.applicant.first_name,
        'applicant_last_name': interview.applicant.last_name,  
        'applicant_email': interview.applicant.email,
        'testing': interview.testing.feedback,
        'interview_score': interview.interview_score,
        'scheduled_date': interview.scheduled_date,
        'feedback': interview.feedback,
        'status': interview.status,
    }
    return JsonResponse(data)

from django.core.paginator import Paginator  
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from recrut_applicant.filters import ApplicantFilter
from recrut_applicant.forms import ApplicantForm
from recrut_applicant.models import Applicant
from django.db.models import Q

def filter_applicants(keywords, minimum_education, minimum_experience):
    query = Q()
    for keyword in keywords:
        query |= Q(skills__icontains=keyword) | Q(education__icontains=keyword)
    
    filtered_applicants = Applicant.objects.filter(query, education__icontains=minimum_education)
    
    if minimum_experience:
        filtered_applicants = filtered_applicants.filter(experience__gte=minimum_experience)
    
    return filtered_applicants


def applicant_list(request):
    # Pega todos os candidatos inicialmente
    applicant_list = Applicant.objects.all()

    # Aplica o filtro por nome
    applicant_filter = ApplicantFilter(request.GET, queryset=applicant_list)

    # Ordenação por nome e paginação
    filtered_list = applicant_filter.qs.order_by('first_name')
    paginator = Paginator(filtered_list, 4)
    page_number = request.GET.get('page')
    applicants = paginator.get_page(page_number)

    # Passa o filtro para o contexto
    return render(request, 'applicant/applicant_list.html', {
        'applicants': applicants,
        'filter': applicant_filter,  # Adicione o filtro aqui
    })


def create_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('applicant_list')  
    else:
        form = ApplicantForm()
    return render(request, 'applicant/applicant_form.html', {'form': form})

def applicant_update(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('applicant_list')  
    else:
        form = ApplicantForm(instance=applicant)
    return render(request, 'applicant/applicant_form.html', {'form': form})

def applicant_delete(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == 'POST':
        applicant.delete()
        return redirect('applicant_list')  
    return render(request, 'applicant/applicant_confirm_delete.html', {'applicant': applicant})

def applicant_detail(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    data = {
        'first_name': applicant.first_name,
        'last_name': applicant.last_name,
        'email': applicant.email,
        'phone': applicant.phone,
        'salary': applicant.salary,
        'status': applicant.status,
        'application_date': applicant.application_date.strftime('%Y-%m-%d'),
        'image': applicant.image.url if applicant.image else None,
        'resume': applicant.resume.url if applicant.resume else None,
        'cover_letter': applicant.cover_letter.url if applicant.cover_letter else None,
        'portfolio': applicant.portfolio.url if applicant.portfolio else None,
        'about': applicant.about,
        'education': applicant.education,
        'skills': applicant.skills,
    }
    return JsonResponse(data)


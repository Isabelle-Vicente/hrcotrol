from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from trg_certification.forms import CertificateForm
from django.core.paginator import Paginator
from trg_certification.models import Certificate

def certificate_list(request):
    certificates = Certificate.objects.all()

    paginator = Paginator(certificates, 4)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    return render(request, 'certificate_list.html', {'page_obj': page_obj})


def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')  
    else:
        form = CertificateForm()
    
    return render(request, 'certificate_form.html', {'form': form})
    
def certificate_update(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
        else:
            form = CertificateForm(instance=certificate)
        return render(request, 'certificate_form.html', {'form': form})
    
def certificate_delete(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        certificate.delete()
        return redirect('certificate_list')
    return render(request, 'certificate_confirm_delete.html', {'certificate':certificate})



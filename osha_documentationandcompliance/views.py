from django.shortcuts import get_object_or_404, render, redirect
from .forms import DocumentForm
from .models import Document

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.responsible = request.user
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document_form.html', {'form': form})

def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk)  
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)  
        if form.is_valid():
            form.save()  
            return redirect('document_list')  
    else:
        form = DocumentForm(instance=document)  
    return render(request, 'document_form.html', {'form': form})  

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'document_confirm_delete.html', {'document': document})

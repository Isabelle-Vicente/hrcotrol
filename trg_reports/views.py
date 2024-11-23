from django.shortcuts import render, redirect, get_object_or_404
from trg_reports.forms import TrainingReportForm
from .models import TrainingReport

def report_list(request):
    reports = TrainingReport.objects.all().order_by('-generated_at') 
    return render(request, 'report_list.html', {'reports': reports})

def create_report(request):
    if request.method == 'POST':
        form = TrainingReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')  
    else:
        form = TrainingReportForm()
    return render(request, 'report_form.html', {'form': form})

def update_report(request, pk):
    report = get_object_or_404(TrainingReport, pk=pk)
    if request.method == 'POST':
        form = TrainingReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_detail', pk=pk)  # Redireciona para os detalhes do relatório atualizado
    else:
        form = TrainingReportForm(instance=report)
    return render(request, 'report_form.html', {'form': form})

def report_detail(request, pk):
    report = get_object_or_404(TrainingReport, pk=pk)
    return render(request, 'report_detail.html', {'report': report})

def delete_report(request, pk):
    report = get_object_or_404(TrainingReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')  # Redireciona para a lista após a exclusão
    return render(request, 'report_confirm_delete.html', {'report': report})

from django.shortcuts import render
from recrut_applicant.models import Applicant
from recrut_screening.models import ApplicantScreening
from recrut_screening.models import ApplicantInterviewing, ApplicantTesting
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models import Count
from recrut_vacancymanagement.models import JobDetails

def reports_metrics(request):
    jobs = JobDetails.objects.all()
    labels_candidates = []
    data_candidates = []

    for job in jobs:
        candidate_count = ApplicantScreening.objects.filter(job=job).values('applicant').distinct().count()
        labels_candidates.append(job.title)
        data_candidates.append(candidate_count)

    applicants = Applicant.objects.all()
    labels_scores = []
    data_scores = []

    for applicant in applicants:
        screening_score = ApplicantScreening.objects.filter(applicant=applicant).aggregate(total=Sum('score_skills'))['total'] or 0
        testing_score = ApplicantTesting.objects.filter(applicant=applicant).aggregate(total=Sum('test_score'))['total'] or 0
        interview_score = ApplicantInterviewing.objects.filter(applicant=applicant).aggregate(total=Sum('interview_score'))['total'] or 0

        total_score = float(screening_score) + float(testing_score) + float(interview_score)  
        if total_score > 0:
            labels_scores.append(f"{applicant.first_name} {applicant.last_name}")
            data_scores.append(total_score)

    statuses = ['pending', 'interview', 'hired', 'rejected']
    data_status = [Applicant.objects.filter(status=status).count() for status in statuses]
    labels_status = ['Pending', 'Interview', 'Hired', 'Rejected']

   # Gráfico 4: Número de candidatos cadastrados por mês
    monthly_data = Applicant.objects.annotate(month=TruncMonth('application_date')).values('month').annotate(count=Count('id')).order_by('month')
    labels_months = [data['month'].strftime('%B %Y') for data in monthly_data]
    data_months = [data['count'] for data in monthly_data]

    context = {
        'labels_candidates': labels_candidates,
        'data_candidates': data_candidates,
        'labels_scores': labels_scores,
        'data_scores': data_scores,
        'labels_status': labels_status,
        'data_status': data_status,
        'labels_months': labels_months,
        'data_months': data_months,
    }

    return render(request, 'recrut_reportsmetrics/reportsmetrics.html', context)


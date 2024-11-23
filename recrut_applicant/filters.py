import django_filters
from .models import Applicant

class ApplicantFilter(django_filters.FilterSet):
    class Meta:
        model = Applicant
        fields = {
            "first_name": ["icontains"]
        }
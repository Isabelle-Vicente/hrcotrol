from django.urls import path
from . import views

urlpatterns = [
    path('reports-metrics/', views.reports_metrics, name='reports_metrics'),
]

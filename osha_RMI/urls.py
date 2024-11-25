from django.urls import path
from osha_RMI import views

urlpatterns = [
    # Safety Inspection URLs
    path('safety_inspections/', views.safety_inspection_list, name='safety_inspection_list'),
    path('safety_inspections/create/', views.safety_inspection_create, name='safety_inspection_create'),
    path('safety_inspections/update/<int:pk>/', views.safety_inspection_update, name='safety_inspection_update'),
    path('safety_inspections/delete/<int:pk>/', views.safety_inspection_delete, name='safety_inspection_delete'),

    # Medical Exam URLs
    path('medical_exams/', views.medical_exam_list, name='medical_exam_list'),
    path('medical_exams/create/', views.medical_exam_create, name='medical_exam_create'),
    path('medical_exams/update/<int:pk>/', views.medical_exam_update, name='medical_exam_update'),
    path('medical_exams/delete/<int:pk>/', views.medical_exam_delete, name='medical_exam_delete'),

    # Occupational Health Monitoring URLs
    path('regular-monitoring-inspections/occupational_health_monitoring/', views.occupational_health_monitoring_list, name='occupational_health_monitoring_list'),
    path('regular-monitoring-inspections/occupational_health_monitoring/create/', views.occupational_health_monitoring_create, name='occupational_health_monitoring_create'),
    path('regular-monitoring-inspections/occupational_health_monitoring/update/<int:pk>/', views.occupational_health_monitoring_update, name='occupational_health_monitoring_update'),
    path('regular-monitoring-inspections/occupational_health_monitoring/delete/<int:pk>/', views.occupational_health_monitoring_delete, name='occupational_health_monitoring_delete'),
]

from django.urls import path
from . import views

urlpatterns = [

    path('safety_inspection/', views.safety_inspection_list, name='safety_inspection_list'), 
    path('safety_inspection/create/', views.safety_inspection_create, name='safety_inspection_create'),
    path('safety_inspection/update/<int:pk>/', views.safety_inspection_update, name='safety_inspection_update'),
    path('safety_inspection/delete/<int:pk>/', views.safety_inspection_delete, name='safety_inspection_delete'),

    path('medical_exam/', views.medical_exam_list, name='medical_exam_list'), 
    path('medical_exam/create/', views.medical_exam_create, name='medical_exam_create'),
    path('medical_exam/update/<int:pk>/', views.medical_exam_update, name='medical_exam_update'),
    path('medical_exam/delete/<int:pk>/', views.medical_exam_delete, name='maintenance_inspection_delete'),

    path('occupational_health_monitoring/', views.occupational_health_monitoring_list, name='occupational_health_monitoring_list'), 
    path('occupational_health_monitoring/create/', views.occupational_health_monitoring_create, name='occupational_health_monitoring_create'),
    path('occupational_health_monitoring/update/<int:pk>/', views.occupational_health_monitoring_update, name='occupational_health_monitoring_update'),
    path('occupational_health_monitoring/delete/<int:pk>/', views.occupational_health_monitoring_delete, name='occupational_health_monitoring_delete'),
]





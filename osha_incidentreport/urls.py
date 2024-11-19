from django.urls import path
from . import views

urlpatterns = [

    path('incident-report/', views.incident_report_list, name='incident_report_list'), 
    path('incident-report/create/', views.incident_report_create, name='incident_report_create'),
    path('incident-report/update/<int:pk>/', views.incident_report_update, name='incident_report_update'),
    path('incident-report/delete/<int:pk>/', views.incident_report_delete, name='incident_report_delete'),
]


from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    # RiskIdentification URLs
    path('risk-identification/', views.risk_identification_list, name='risk_identification_list'),  # Corrigido aqui
    path('risk-identification/create/', views.risk_identification_create, name='risk_identification_create'),
    path('risk-identification/update/<int:pk>/', views.risk_identification_update, name='risk_identification_update'),
    path('risk-identification/delete/<int:pk>/', views.risk_identification_delete, name='risk_identification_delete'),

    # RiskAssessment URLs
    path('risk-assessment/', views.risk_assessment_list, name='risk_assessment_list'),
    path('risk-assessment/create/', views.risk_assessment_create, name='risk_assessment_create'),
    path('risk-assessment/update/<int:pk>/', views.risk_assessment_update, name='risk_assessment_update'),
    path('risk-assessment/delete/<int:pk>/', views.risk_assessment_delete, name='risk_assessment_delete'),

    # RiskControl URLs
    path('risk-control/', views.risk_control_list, name='risk_control_list'),
    path('risk-control/create/', views.risk_control_create, name='risk_control_create'),
    path('risk-control/update/<int:pk>/', views.risk_control_update, name='risk_control_update'),
    path('risk-control/delete/<int:pk>/', views.risk_control_delete, name='risk_control_delete'),
]


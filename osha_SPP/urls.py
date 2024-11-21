from django.urls import path
from . import views

urlpatterns = [

    path('safety-policy/', views.safetypolicy_list, name='safetypolicy_list'), 
    path('safety-policy/create/', views.safetypolicy_create, name='safetypolicy_create'),
    path('safety-policy/update/<int:pk>/', views.safetypolicy_update, name='safetypolicy_update'),
    path('safety-policy/delete/<int:pk>/', views.safetypolicy_delete, name='safetypolicy_delete'),

    path('operational-procedure/', views.operational_procedure_list, name='operational_procedure_list'), 
    path('operational-procedure/create/', views.operational_procedure_create, name='operational_procedure_create'),
    path('operational-procedure/update/<int:pk>/', views.operational_procedure_update, name='operational_procedure_update'),
    path('operational-procedure/delete/<int:pk>/', views.operational_procedure_delete, name='operational_procedure_delete'),

    path('emergency-plan/', views.emergency_plan_list, name='emergency_plan_list'), 
    path('emergency-plan/create/', views.emergency_plan_create, name='emergency_plan_create'),
    path('emergency-plan/update/<int:pk>/', views.emergency_plan_update, name='emergency_plan_update'),
    path('emergency-plan/delete/<int:pk>/', views.emergency_plan_delete, name='emergency_plan_delete'),
]
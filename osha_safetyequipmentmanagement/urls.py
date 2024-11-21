from django.urls import path
from . import views

urlpatterns = [

    path('equipment/', views.equipment_list, name='equipment_list'), 
    path('equipment/create/', views.equipment_create, name='equipment_create'),
    path('equipment/update/<int:pk>/', views.equipment_update, name='equipment_update'),
    path('equipment/delete/<int:pk>/', views.equipment_delete, name='equipment_delete'),

    path('maintenance-inspection/', views.maintenance_inspection_list, name='maintenance_inspection_list'), 
    path('maintenance-inspection/create/', views.maintenance_inspection_create, name='maintenance_inspection_create'),
    path('maintenance-inspection/update/<int:pk>/', views.maintenance_inspection_update, name='maintenance_inspection_update'),
    path('maintenance-inspection/delete/<int:pk>/', views.maintenance_inspection_delete, name='maintenance_inspection_delete'),

    path('epi-distribution/', views.epi_distribution_list, name='epi_distribution_list'), 
    path('epi-distribution/create/', views.epi_distribution_create, name='epi_distribution_create'),
    path('epi-distribution/update/<int:pk>/', views.epi_distribution_update, name='epi_distribution_update'),
    path('epi-distribution/delete/<int:pk>/', views.epi_distribution_delete, name='epi_distribution_delete'),
]






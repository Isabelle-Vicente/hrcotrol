from django.urls import path
from . import views

urlpatterns = [

    path('contract-management/', views.contract_list, name='contract_list'), 
    path('contract-management/create/', views.contract_create, name='contract_create'),
    path('contract-management/update/<int:pk>/', views.contract_create, name='contract_create'),
]
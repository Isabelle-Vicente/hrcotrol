from django.urls import path
from . import views

urlpatterns = [

    path('certification/', views.certificate_list, name='certificate_list'), 
    path('certification/create/', views.certificate_create, name='certificate_create'),
    path('certification/update/<int:pk>/', views.certificate_update, name='certificate_update'),
    path('certification/delete/<int:pk>/', views.certificate_delete, name='certificate_delete'),
]
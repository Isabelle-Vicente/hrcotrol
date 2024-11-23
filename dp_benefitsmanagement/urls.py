from django.urls import path
from . import views

urlpatterns = [

    path('benefits-managemen/', views.benefit_list, name='benefit_list'), 
    path('benefits-managemen/create/', views.benefit_create, name='benefit_create'),
    path('benefits-managemen/update/<int:pk>/', views.benefit_update, name='benefit_update'),
]


from django.urls import path
from . import views

urlpatterns = [

    path('training-management/', views.training_list, name='training_list'), 
    path('training-management/create/', views.training_create, name='training_create'),
    path('training-management/update/<int:pk>/', views.training_update, name='training_update'),
    path('training-management/delete/<int:pk>/', views.training_delete, name='training_delete'),
]
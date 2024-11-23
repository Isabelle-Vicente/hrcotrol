from django.urls import path
from . import views

urlpatterns = [
    path('participant-management/', views.participant_list, name='participant_list'), 
    path('participant-management/create/', views.participant_create, name='participant_create'),
    path('participant-management/update/<int:pk>/', views.participant_update, name='participant_update'),
    path('participant-management/delete/<int:pk>/', views.participant_delete, name='participant_delete'),
]
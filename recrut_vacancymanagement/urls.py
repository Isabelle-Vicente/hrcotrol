from django.urls import path
from . import views

urlpatterns = [
    path('vacancymanagement/', views.jobdetails_list, name='jobdetails_list'),
    path('vacancymanagement/new/', views.jobdetails_create, name='jobdetails_create'),
    path('vacancymanagement/<int:pk>/edit/', views.jobdetails_update, name='jobdetails_update'),
    path('vacancymanagement/<int:pk>/delete/', views.jobdetails_delete, name='jobdetails_delete'),
    path('vacancymanagement/<int:pk>/json/', views.jobdetails_detail, name='jobdetails_detail_json'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('applicant/', views.applicant_list, name='applicant_list'),
    path('applicant/new/', views.create_applicant, name='applicant_create'),
    path('applicant/<int:pk>/edit/', views.applicant_update, name='applicant_update'),
    path('applicant/<int:pk>/delete/', views.applicant_delete, name='applicant_delete'),
    path('applicants/<int:pk>/json/', views.applicant_detail, name='applicant_detail_json'),

]



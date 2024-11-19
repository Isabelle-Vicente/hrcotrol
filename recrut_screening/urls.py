# recrut_screening/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rotas para ApplicantScreening
    path('applicant_screening/', views.applicant_screening_list, name='applicant_screening_list'),
    path('applicant_screening/create/', views.applicant_screening_create, name='applicant_screening_create'),
    path('applicant_screening/<int:pk>/update/', views.applicant_screening_update, name='applicant_screening_update'),
    path('applicant_screening/<int:pk>/delete/', views.applicant_screening_delete, name='applicant_screening_delete'),
    path('applicant_screening/<int:pk>/detail/', views.applicant_screening_detail, name='applicant_screening_detail'),

    # Rotas para ApplicantTesting
    path('applicant_testing/', views.applicant_testing_list, name='applicant_testing_list'),
    path('applicant_testing/create/', views.applicant_testing_create, name='applicant_testing_create'),
    path('applicant_testing/<int:pk>/update/', views.applicant_testing_update, name='applicant_testing_update'),
    path('applicant_testing/<int:pk>/delete/', views.applicant_testing_delete, name='applicant_testing_delete'),
    path('applicant_testing/<int:pk>/detail/', views.applicant_testing_detail, name='applicant_testing_detail'),

    # Rotas para ApplicantInterviewing
    path('applicant_interviewing/', views.applicant_interviewing_list, name='applicant_interviewing_list'),
    path('applicant_interviewing/create/', views.applicant_interviewing_create, name='applicant_interviewing_create'),
    path('applicant_interviewing/<int:pk>/update/', views.applicant_interviewing_update, name='applicant_interviewing_update'),
    path('applicant_interviewing/<int:pk>/delete/', views.applicant_interviewing_delete, name='applicant_interviewing_delete'),
    path('applicant_interviewing/<int:pk>/detail/', views.applicant_interviewing_detail, name='applicant_interviewing_detail'),
]

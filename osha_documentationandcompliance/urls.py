from django.urls import path
from . import views

urlpatterns = [
    path('document/update/<int:pk>/', views.document_upload, name='document_upload'),
    path('document/', views.document_list, name='document_list'),
    path('document/create/', views.document_create, name='document_create'),
]

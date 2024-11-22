from django.urls import path
from . import views

urlpatterns = [
    path('document/update/<int:pk>/', views.document_update, name='document_update'),
    path('document/', views.document_list, name='document_list'),
    path('document/create/', views.document_create, name='document_create'),
    path('document/delete/<int:pk>/', views.document_delete, name='document_delete'),

]

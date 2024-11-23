from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('create/', views.create_report, name='create_report'),
    path('<int:pk>/', views.report_detail, name='report_detail'),
    path('<int:pk>/update/', views.update_report, name='update_report'),
    path('<int:pk>/delete/', views.delete_report, name='delete_report'),
]

from django.urls import path
from . import views

urlpatterns = [

    path('instructor-management/', views.instructor_list, name='instructor_list'), 
    path('instructor-management/create/', views.instructor_create, name='instructor_create'),
    path('instructor-management/update/<int:pk>/', views.instructor_update, name='instructor_update'),
    path('instructor-management/delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
]
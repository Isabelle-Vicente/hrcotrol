"""
URL configuration for hr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView

from employees.views import login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('home/', TemplateView.as_view(template_name="base_generic.html"), name='home'),
    path('employees/', include('employees.urls')),


    path('applicant/', include('recrut_applicant.urls')),
    path('vacancymanagement/', include('recrut_vacancymanagement.urls')),
    path('recrut_screening/', include('recrut_screening.urls')),
    path('reports-metrics/', include('recrut_reportsmetrics.urls')),

    path('risk-analysis/', include('osha_riskanalysis.urls')),  
    path('incident-report/', include('osha_incidentreport.urls')),
    path('regular-monitoring-inspections/', include('osha_RMI.urls')), 
    path('safety-equipment-management/', include('osha_safetyequipmentmanagement.urls')), 
    path('osha-documentationand-compliance/', include('osha_documentationandcompliance.urls')), 
    path('osha-safetyplanning-procedures/', include('osha_SPP.urls')), 





]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
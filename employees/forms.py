from django import forms
from django.contrib.auth.models import User
from .models import Employee

class EmployeeForm(forms.ModelForm):

    
      class Meta:
        model = Employee
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', required=True, max_length=11)
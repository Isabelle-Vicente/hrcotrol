from django import forms
from recrut_vacancymanagement.models import JobDetails

class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobDetails
        fields = [
            'title', 
            'description', 
            'requirements', 
            'education',  
            'category',   
            'location', 
            'salary_range', 
            'status'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.TextInput(attrs={'id': 'requirementsInput'}),            
            'education': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Education requirements, e.g., Bachelor’s degree in Computer Science'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'salary_range': forms.TextInput(attrs={'placeholder': 'e.g., $40,000 - $60,000'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Job Title',
            'description': 'Job Description',
            'requirements': 'Job Requirements (multiple entries)',
            'education': 'Education',
            'category': 'Category',        
            'location': 'Location',
            'salary_range': 'Salary Range',
            'status': 'Job Status',
        }

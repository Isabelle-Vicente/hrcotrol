from django import forms
from trg_instructormanagement.models import Instructor

class  InstructorForm(forms.ModelForm):
    class Meta :
        model = Instructor
        fields = ['name', 'specialization', 'email', 'phone', 'trainings']
      
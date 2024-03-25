from django import forms
from . import models
class StudentForm(forms.ModelForm):
    class Meta:
        model= models.Student
        fields=['name','roll','father_name','address']
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'w-25'})
        }
        help_texts={
            'name': 'Write your full name'
        }
        error_messages = {
            'name':{'required' : 'your name is required'}
        }
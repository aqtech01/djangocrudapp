from django import forms
from .models import CrudApp
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = CrudApp
        fields = ['name','email','password']
from .models import student_model
from django import forms

class student_form(forms.ModelForm):
    class Meta:
        model=student_model
        fields='__all__'

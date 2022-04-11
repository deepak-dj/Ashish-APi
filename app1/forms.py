from django import forms
from .models import Student

print('Hello')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

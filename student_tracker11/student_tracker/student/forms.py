from django import forms
from .models import Student, Performance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = '__all__'

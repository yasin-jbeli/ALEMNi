# forms.py (inside your app)

from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'enrollmentCapacity']  # Add the fields you want to modify

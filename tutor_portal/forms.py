from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'enrollment_capacity', 'tutor']
        # Add widgets and other configurations if needed
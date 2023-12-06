# forms.py (inside your app)

from django import forms
from authentification.models import Course
from authentification.models import Material

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'enrollmentCapacity']  # Add the fields you want to modify


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'content', 'documentType']
        # You can include or exclude specific fields based on what you want to modify

    # Optionally, you can add custom form field validation or widgets here if needed

from django.urls import path
from . import views

urlpatterns = [
    path('about_view/', views.about_view, name='about_view'),  # Updated view function name and added a name attribute
    # Add more paths for your app views
]

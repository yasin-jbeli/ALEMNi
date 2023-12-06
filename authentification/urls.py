from django.urls import path
from . import views

urlpatterns = [
    path('about_view/', views.about_view),
    # Add more paths for your app views
]
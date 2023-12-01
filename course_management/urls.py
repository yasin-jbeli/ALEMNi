from django.urls import path
from . import views

urlpatterns = [
    path('about_view/', views.about_view, name='about_view'),
    # Other URL patterns for your app views
]

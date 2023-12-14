from django.urls import path
from . import views

urlpatterns = [
    path('create-tutor/', views.create_tutor, name='create_tutor'),  # Endpoint for creating a tutor
    path('create-student/', views.create_student, name='create_student'),  # Endpoint for creating a student
    path('confirm-email/<str:token>/', views.confirm_email, name='confirm_email'),  # Endpoint for confirming email
]
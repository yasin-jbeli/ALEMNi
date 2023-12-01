from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('', views.home, name='home'),
    path('/form/', views.show_form, name='show_form'),
    path('/submit_course/', views.submit_Course, name='submit_Course'),
    path('/success/', views.success_message, name='success_message'),
    path('/course/<int:course_id>/materials/', views.course_materials, name='course_materials'),
    path('/all_courses/', views.all_courses, name='all_courses'),
]

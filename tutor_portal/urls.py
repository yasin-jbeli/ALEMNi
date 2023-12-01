from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('', views.home, name='home'),
    path('/form/', views.show_form, name='show_form'),
    path('/submit_course/', views.submit_Course, name='submit_Course'),
    path('/success/', views.success_message, name='success_message'),
    path('/course/<int:courseId>/materials/', views.course_materials, name='course_materials'),
    path('/all_courses/', views.all_courses, name='all_courses'),
    path('/delete_course/<int:courseId>/', views.delete_course, name='delete_course'),
    path('/modify_course/<int:courseId>/', views.modify_course, name='modify_course'),
    path('/enter_course/<int:courseId>/', views.enter_course, name='enter_course'),
    path('/course/<int:courseId>/add_material/', views.add_material, name='add_material'),
]


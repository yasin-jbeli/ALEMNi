from django.urls import path
from . import views
from authentification.models import ReportedIncident

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailsView.as_view(), name='user-details'),

]

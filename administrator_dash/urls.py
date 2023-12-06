from django.urls import path
from . import views
from tutor_portal.models import ReportedIncident

urlpatterns = [
    path('/users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('/users/<int:pk>/', views.UserDetailsView.as_view(), name='user-details'),
    path('reported-incidents/', views.ReportedIncidentListView.as_view(), name='reported-incidents-list'),
    path('resolve-incident/<int:pk>/', views.ResolveIncidentView.as_view(), name='resolve-incident'),
]

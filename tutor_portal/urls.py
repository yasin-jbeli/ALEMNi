from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
   path('/courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
   path('courses/<int:pk>/', views.CourseRetrieveUpdateDeleteView.as_view(), name='course-detail'),
   path('/materials/', views.MaterialListCreateView.as_view(), name='material-list'),
   path('/materials/<int:pk>/', views.MaterialRetrieveUpdateDeleteView.as_view(), name='material-detail'),
   path('/assignments/', views.AssignmentListCreateView.as_view(), name='assignment-list'),
   path('/assignments/<int:pk>/', views.AssignmentRetrieveUpdateDeleteView.as_view(), name='assignment-detail'),
   path('/submissions/', views.SubmissionListView.as_view(), name='submission-list'),
   path('/grades/create/', views.GradeCreateView.as_view(), name='grade-create'),
   path('/feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),
]


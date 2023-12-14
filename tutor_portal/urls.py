from django.urls import path
from . import views

urlpatterns = [
   path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
   path('courses/<int:pk>/', views.CourseRetrieveUpdateDeleteView.as_view(), name='course-detail'),
   path('courses/<int:course_id>/materials/', views.MaterialListCreateView.as_view(), name='material-list-create'),
   path('courses/<int:course_id>/materials/<int:pk>/', views.MaterialRetrieveUpdateDeleteView.as_view(), name='material-detail'),
   path('courses/<int:course_id>/assignments/', views.AssignmentListCreateView.as_view(), name='assignment-list'),
   path('courses/<int:course_id>/assignments/<int:pk>/', views.AssignmentRetrieveUpdateDeleteView.as_view(), name='assignment-detail'),
   path('courses/<int:course_id>/assignments/<int:pk>/submissions/', views.SubmissionListView.as_view(), name='submission-list'),
   path('courses/<int:course_id>/assignments/<int:assignment_id>/submissions/<int:pk>/grades/', views.GradeCreateView.as_view(), name='grade-create'),
   path('send-offer/', views.send_offer, name='send_offer'),
   path('send-answer/', views.send_answer, name='send_answer'),
   path('send-ice-candidate/', views.send_ice_candidate, name='send_ice_candidate'), 
]

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentification.models import (
    Course,
    Material,
    Assignment,
    Submission,
    Grade,
    WebRTCSession,
)
from .serializers import (
    CourseSerializer,
    MaterialSerializer,
    AssignmentSerializer,
    SubmissionSerializer,
    GradeSerializer,
)

# Course views
class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Course.objects.all()

    def get(self, request, *args, **kwargs):
        courses = self.get_queryset()
        return render(request, 'course_list.html', {'courses': courses})

class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny] 

    def get_queryset(self):
        return Course.objects.all()

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        return render(request, 'course_detail.html', {'course': course})


# Assignment views
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            assignments = self.queryset
            return render(request, 'assignment_list.html', {'assignments': assignments})
        return Response(status=405) 

class AssignmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.AllowAny] 
    def get(self, request, *args, **kwargs):
        assignment = self.get_object()
        return render(request, 'assignment_detail.html', {'assignment': assignment})

# Material views
class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.AllowAny]  

    def get(self, request, *args, **kwargs):
        materials = self.queryset
        return render(request, 'material_list.html', {'materials': materials})

class MaterialRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.AllowAny]  

    def get(self, request, *args, **kwargs):
        material = self.get_object()
        return render(request, 'material_detail.html', {'material': material})

# Other views
class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        submissions = self.queryset
        return render(request, 'submission_list.html', {'submissions': submissions})

class GradeCreateView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.AllowAny] 

    def post(self, request, *args, **kwargs):
        return render(request, 'grade_created.html', {'message': 'Grade created successfully'})

# WebRTC views (assuming they render HTML as well)
@api_view(['POST'])
def send_offer(request):
    return render(request, 'offer_sent.html', {'message': 'SDP offer received and saved successfully'})

@api_view(['POST'])
def send_answer(request):
    return render(request, 'answer_sent.html', {'message': 'SDP answer received and saved successfully'})

@api_view(['POST'])
def send_ice_candidate(request):
    return render(request, 'ice_candidate_sent.html', {'message': 'ICE candidates received and saved successfully'})

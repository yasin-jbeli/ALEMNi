from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
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
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)


class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# Assignment views
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AssignmentSerializer  # Serializer for listing assignments with details
        return AssignmentSerializer  # Serializer for creating assignments


class AssignmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer  # Serializer with detailed assignment information
    permission_classes = [IsAuthenticated]

# Material views
class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class MaterialRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context


# Other views
class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]


class GradeCreateView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
    
    
@api_view(['POST'])
def send_offer(request):
    session_id = request.data.get('session_id')
    webrtc_session, _ = WebRTCSession.objects.get_or_create(session_id=session_id)
    webrtc_session.sdp = request.data.get('sdp_offer')
    webrtc_session.save()
    return Response({'message': 'SDP offer received and saved successfully'})


@api_view(['POST'])
def send_answer(request):
    session_id = request.data.get('session_id')
    webrtc_session = WebRTCSession.objects.get(session_id=session_id)
    webrtc_session.sdp = request.data.get('sdp_answer')
    webrtc_session.save()
    return Response({'message': 'SDP answer received and saved successfully'})


@api_view(['POST'])
def send_ice_candidate(request):
    session_id = request.data.get('session_id')
    webrtc_session = WebRTCSession.objects.get(session_id=session_id)
    webrtc_session.ice_candidates = request.data.get('ice_candidates')
    webrtc_session.save()
    return Response({'message': 'ICE candidates received and saved successfully'})

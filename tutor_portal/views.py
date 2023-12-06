# tutor_portal/views.py
from rest_framework import generics
from .models import Course, WebRTCSession
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Material
from .serializers import MaterialSerializer
from .models import Assignment
from .serializers import AssignmentSerializer
from .models import Submission
from .serializers import SubmissionSerializer
from .models import Grade
from .serializers import GradeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

def perform_create(self, serializer):
        # Automatically set the tutor field to the current authenticated user
        serializer.save(tutor=self.request.user)


class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

class AssignmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]


class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

class MaterialRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

class GradeCreateView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def send_offer(request):
    # Get session_id from request or payload
    session_id = request.data.get('session_id')

    # Get or create WebRTC session
    webrtc_session = WebRTCSession.objects.get_or_create(session_id=session_id)

    # Save SDP offer to the session model
    webrtc_session.sdp = request.data.get('sdp_offer')
    webrtc_session.save()

    # Return appropriate response
    return Response({'message': 'SDP offer received and saved successfully'})

@api_view(['POST'])
def send_answer(request):
    # Get session_id from request or payload
    session_id = request.data.get('session_id')

    # Retrieve WebRTC session
    webrtc_session = WebRTCSession.objects.get(session_id=session_id)

    # Save SDP answer to the session model
    webrtc_session.sdp = request.data.get('sdp_answer')
    webrtc_session.save()

    # Return appropriate response
    return Response({'message': 'SDP answer received and saved successfully'})


@api_view(['POST'])
def send_ice_candidate(request):
    # Get session_id from request or payload
    session_id = request.data.get('session_id')

    # Retrieve WebRTC session
    webrtc_session = WebRTCSession.objects.get(session_id=session_id)

    # Save ICE candidates to the session model
    webrtc_session.ice_candidates = request.data.get('ice_candidates')
    webrtc_session.save()

    # Return appropriate response
    return Response({'message': 'ICE candidates received and saved successfully'})

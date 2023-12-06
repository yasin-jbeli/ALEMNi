from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tutor_portal.models import User
from .serializers import UserSerializer
from administrator_dash.permissions import IsAdminOrReadOnly
from .serializers import ReportedIncidentSerializer
from tutor_portal.models import ReportedIncident

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_banned = True
        instance.save()
        return self.partial_update(request, *args, **kwargs)

class ReportedIncidentListView(generics.ListAPIView):
    queryset = ReportedIncident.objects.filter(resolved=False)
    serializer_class = ReportedIncidentSerializer

class ResolveIncidentView(generics.UpdateAPIView):
    queryset = ReportedIncident.objects.all()
    serializer_class = ReportedIncidentSerializer




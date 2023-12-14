from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from authentification.models import User
from authentification.serializers import UserSerializer
from administrator_dash.permissions import IsAdminOrReadOnly
from authentification.models import ReportedIncident

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





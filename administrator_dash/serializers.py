# administration_dash/serializers.py

from rest_framework import serializers
from tutor_portal.models import User
from tutor_portal.models import ReportedIncident


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'username', 'email', 'dateJoined', 'role', 'is_banned')

class ReportedIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedIncident
        fields = '__all__'

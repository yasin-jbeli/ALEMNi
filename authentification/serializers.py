from rest_framework import serializers
from .models import User, Tutor, Student, Administrator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'username', 'email', 'dateJoined']

class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Serialize User fields for Tutor

    class Meta:
        model = Tutor
        fields = ['is_active', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        tutor = Tutor.objects.create(user=user, **validated_data)
        return tutor
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Serialize User fields for Student

    class Meta:
        model = Student
        fields = ['is_active', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Serialize User fields for Administrator

    class Meta:
        model = Administrator
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        admin = Administrator.objects.create(user=user)
        return admin

# tutor_portal/serializers.py

from rest_framework import serializers
from .models import Course
from .models import Material
from .models import Assignment
from .models import Submission
from .models import Grade

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseId', 'title', 'description','enrollmentCapacity','tutor')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('materialId', 'title', 'content', 'uploadDate', 'documentType', 'course')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('assignmentId', 'title', 'description', 'dueDate', 'course')


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('submissionId', 'submissionContent', 'submissionDate', 'student', 'assignment')

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('gradeId', 'grade', 'feedback', 'student', 'assignment')
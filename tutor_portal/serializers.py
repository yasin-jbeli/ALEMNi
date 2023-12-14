# tutor_portal/serializers.py

from rest_framework import serializers
from authentification.models import Course
from authentification.models import Material
from authentification.models import Assignment
from authentification.models import Submission
from authentification.models import Grade

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseId', 'title', 'description','enrollmentCapacity','tutor')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('materialId', 'title', 'content', 'uploadDate', 'documentType', 'course')
        read_only_fields = ('uploadDate', 'course')  # Assuming 'uploadDate' should be read-only

    def create(self, validated_data):
        request = self.context.get('request')
        course_id = request.parser_context['kwargs'].get('course_id')
        validated_data['course_id'] = course_id
        return super().create(validated_data)

class AssignmentSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()  # SerializerMethodField to handle course_id

    class Meta:
        model = Assignment
        fields = ('assignmentId', 'title', 'description', 'dueDate', 'course')

    def get_course(self, obj):
        # Extract course_id from the URL kwargs
        request = self.context.get('request')
        course_id = request.parser_context['kwargs'].get('course_id')
        return course_id


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('submissionId', 'submissionContent', 'submissionDate', 'student', 'assignment')

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('gradeId', 'grade', 'feedback', 'student', 'assignment')
        read_only_fields = ('student', 'assignment')  # Make 'student' and 'assignment' read-only

    def create(self, validated_data):
        request = self.context.get('request')
        student_id = request.user.id  # Assuming the authenticated user is a student
        assignment_id = self.context.get('view').kwargs.get('assignment_id')
        validated_data['student_id'] = student_id
        validated_data['assignment_id'] = assignment_id
        return super().create(validated_data)

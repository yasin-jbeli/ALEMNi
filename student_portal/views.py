from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authentification.models import Course, Material, Assignment, Submission, Grade, Interaction
from .serializers import CourseSerializer, MaterialSerializer, AssignmentSerializer, SubmissionSerializer, GradeSerializer, InteractionSerializer



@api_view(['GET'])
def course_list(request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def material_list(request):
        material = Material.objects.all()
        serializer = MaterialSerializer(material, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def assignment_list(request):
        assignment = Assignment.objects.all()
        serializer = AssignmentSerializer(assignment, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def grade_list(request):
        grade = Grade.objects.all()
        serializer = GradeSerializer(grade, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def interaction_list(request):
        interaction = Interaction.objects.all()
        serializer = InteractionSerializer(interaction, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def submission_list(request):
    if request.method == 'GET':
        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
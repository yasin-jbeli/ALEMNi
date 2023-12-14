from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    dateJoined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Tutor(User):
    is_active = models.BooleanField(default=False)
    #cv = models.FileField(upload_to='media/')

class Student(User):
    is_active = models.BooleanField(default=False)

class Administrator(User):
    pass

class Roles(models.TextChoices):
    STUDENT = 'STUDENT', 'Student'
    TUTOR = 'TUTOR', 'Tutor'
    ADMINISTRATOR = 'ADMIN', 'Administrator'

class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    enrollmentCapacity = models.IntegerField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

class Material(models.Model):
    materialId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploadDate = models.DateField(auto_now_add=True)
    documentType = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(models.Model):
    assignmentId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    dueDate = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Submission(models.Model):
    submissionId = models.AutoField(primary_key=True)
    submissionContent = models.TextField()
    submissionDate = models.DateField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

class Grade(models.Model):
    gradeId = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=10)
    feedback = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

class WebRTCSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sdp = models.TextField(blank=True, null=True)
    ice_candidates = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReportedIncident(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(User, related_name='reported_user', on_delete=models.CASCADE)
    description = models.TextField()
    resolved = models.BooleanField(default=False)


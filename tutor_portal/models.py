from django.db import models
from django.core.validators import RegexValidator

class Roles(models.TextChoices):
    STUDENT='STUDENT','Student'
    TUTOR='TUTOR','Tutor'
    ADMINISTRATOR='ADMIN','Administrator'

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default='')
    email = models.EmailField(unique=True)
    dateJoined = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=Roles.choices)

class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    enrollmentCapacity = models.IntegerField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

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

class Feedback(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
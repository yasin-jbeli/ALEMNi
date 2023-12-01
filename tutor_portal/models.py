from django.db import models
from django.core.validators import RegexValidator

validate_alphanumeric = RegexValidator(
    r'^[a-zA-Z0-9]*$', 
    'Only alphanumeric characters are allowed.'
)
class Roles(models.TextChoices):
    STUDENT='STUDENT','Student'
    TUTOR='TUTOR','Tutor'
    ADMINISTRATOR='ADMIN','Administrator'


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100,validators=[validate_alphanumeric], default='')
    email = models.EmailField(unique=True)
    dateJoined = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=Roles.choices)

    class Meta:
        db_table = 'User'

class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    enrollmentCapacity = models.IntegerField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Course'


class Material(models.Model):
    materialId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploadDate = models.DateField(auto_now_add=True)
    documentType = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Material'





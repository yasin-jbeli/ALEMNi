from django.contrib import admin

# Register your models here.

from authentification.models import User
from authentification.models import Course
from authentification.models import Material
from authentification.models import Assignment
from authentification.models import Submission
from authentification.models import Grade
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Material)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Grade)

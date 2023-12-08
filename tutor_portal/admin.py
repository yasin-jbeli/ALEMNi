from django.contrib import admin

# Register your models here.

from .models import User
from .models import Course
from .models import Material
from .models import Assignment
from .models import Submission
from .models import Grade
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Material)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Grade)

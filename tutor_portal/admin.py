from django.contrib import admin

# Register your models here.

from .models import User
from .models import Course
admin.site.register(Course)
admin.site.register(User)

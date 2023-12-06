from django.contrib import admin

# Register your models here.

from authentification.models import User
from authentification.models import Course
from authentification.models import Material
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Material)

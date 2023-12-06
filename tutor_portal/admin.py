from django.contrib import admin

# Register your models here.

from authentification.models import Utilisateur
from authentification.models import Course
from authentification.models import Material
admin.site.register(Course)
admin.site.register(Utilisateur)
admin.site.register(Material)

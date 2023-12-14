from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student_portal/", include("student_portal.urls")),
    path("tutor_portal/", include("tutor_portal.urls")),
    path("administrator_dash/", include("administrator_dash.urls")),
    path("API_module/", include("API_module.urls")),
    path("analytics/", include("analytics.urls")),
    path("course_management/", include("course_management.urls")),
    path("authentification/", include("authentification.urls")),
    path("frontend/", include("frontend.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

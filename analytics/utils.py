from django.db.models import Count

from tutor_portal.models import Grade, ReportedIncident

from authentification.models import Course, Roles, User, Assignment

def get_popular_courses():
    return Course.objects.annotate(num_enrollments=Count('user_set')).order_by('-num_enrollments')[:5]

def get_user_login_frequency():
    return User.objects.filter(last_login__isnull=False).count()

def get_most_active_tutors():
    return User.objects.filter(role=Roles.TUTOR).annotate(num_courses_taught=Count('course')).order_by('-num_courses_taught')[:5]

def get_reported_incidents_count():
    return ReportedIncident.objects.filter(resolved=False).count()

def get_average_assignment_grade(course_id):
    return Grade.objects.filter(assignment__course_id=course_id).aggregate(avg_grade=Avg('grade'))

def get_materials_per_course():
    return Course.objects.annotate(total_materials=Count('material')).order_by('-total_materials')

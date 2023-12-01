from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Course, Material

def about(request):
    return HttpResponse("This is the about page of the API.")


def show_form(request):
    return render(request, 'form.html')

def success_message(request):
    return render(request, 'success.html')


def submit_Course(request):
    if request.method == 'POST':
        # Retrieve form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        enrollmentCapacity = request.POST.get('enrollmentCapacity')
        tutor_id = request.user.id  # Assuming the logged-in user is the tutor
        # Create a new Course object and save it to the database
        new_course = Course(title=title, description=description, enrollmentCapacity=enrollmentCapacity, tutor_id=tutor_id)
        new_course.save()

        # Redirect to a success page or any other page
        return redirect('success_message')  # Redirect to the success page
    else:
        # Handle GET requests or render a different page
        return redirect('show_form')  # Redirect back to the form page if not a POST request
    
def course_materials(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    materials = Material.objects.filter(course=course)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        document_type = request.POST.get('document_type')

        material = Material(
            course=course,
            title=title,
            content=content,
            documentType=document_type
        )
        material.save()

        return redirect('course_materials', course_id=course_id)

    return render(request, 'course_materials.html', {'course': course, 'materials': materials})

def all_courses(request):
    courses = Course.objects.all()  # Retrieve all courses
    context = {
        'courses': courses  # Pass the courses to the template
    }
    return render(request, 'all_courses.html', context)

def home(request):
    return render(request, 'home.html')

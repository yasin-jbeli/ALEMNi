from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from authentification.models import Course, Material
from .forms import CourseForm
from .forms import MaterialForm

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
        tutorId = 1  # Assuming the logged-in user is the tutor
        # Create a new Course object and save it to the database
        new_course = Course(title=title, description=description, enrollmentCapacity=enrollmentCapacity, tutorIid=tutorId)
        new_course.save()

        # Redirect to a success page or any other page
        return redirect('all_courses')
    else:
        # Handle GET requests or render a different page
        return redirect('show_form')  # Redirect back to the form page if not a POST request
    
def course_materials(request, courseId):
    course = get_object_or_404(Course, pk=courseId)
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

        return redirect('course_materials', courseId=courseId)

    return render(request, 'course_materials.html', {'course': course, 'materials': materials})

def all_courses(request):
    courses = Course.objects.all()  # Retrieve all courses
    context = {
        'courses': courses  # Pass the courses to the template
    }
    return render(request, 'all_courses.html', context)

def home(request):
    return render(request, 'home.html')

def delete_course(request, courseId):
    course = get_object_or_404(Course, pk=courseId)
    course.delete()
    return redirect('all_courses')

def all_courses(request):
    courses = Course.objects.all()  # Retrieve all courses
    
    # Filter out courses without valid primary keys
    valid_courses = [course for course in courses if course.courseId is not None]

    context = {
        'courses': valid_courses  # Pass the valid courses to the template
    }
    return render(request, 'all_courses.html', context)

from django.shortcuts import redirect

def modify_course(request, courseId):
    course = get_object_or_404(Course, pk=courseId)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            # Redirect to course.html upon successful modification
            return redirect('enter_course', courseId=courseId)  # Replace 'course_details' with your actual URL name
        
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'modify.html', {'form': form})


def enter_course(request, courseId):
    course = get_object_or_404(Course, pk=courseId)
    materials = Material.objects.filter(course=course)

    return render(request, 'course.html', {'course': course, 'materials': materials})


def add_material(request, courseId):
    course = get_object_or_404(Course, pk=courseId)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        documentType = request.POST.get('documentType')

        material = Material(
            course=course,
            title=title,
            content=content,
            documentType=documentType
        )
        material.save()

        return redirect('enter_course', courseId=courseId)

    return render(request, 'add_material.html', {'course': course})

def material_detail(request, materialId):
    material = get_object_or_404(Material, materialId=materialId)
    return render(request, 'material_detail.html', {'material': material})


def modify_material(request, materialId):
    material = get_object_or_404(Material, pk=materialId)
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_detail', materialId=materialId)
    else:
        form = MaterialForm(instance=material)
    
    return render(request, 'modify_material.html', {'form': form, 'material': material})



def delete_material(request, materialId):
    material = get_object_or_404(Material, pk=materialId)
    courseId = material.course.pk  # Get the course ID before deleting the material
    material.delete()
    return redirect('enter_course', courseId=courseId)



from django.shortcuts import render
from django.http import HttpResponse

def about_view(request):
    return HttpResponse("This is the about page of the API")  # Replace this with your actual logic
    # You can also use render() to render HTML templates
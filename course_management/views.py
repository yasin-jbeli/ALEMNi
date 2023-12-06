from django.shortcuts import render
from django.http import HttpResponse

def about_view(request):
    return HttpResponse("This is the about view of the course management app.")

# Other view functions for your app

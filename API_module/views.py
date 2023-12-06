from django.shortcuts import render
from django.http import HttpResponse

def about_view(request):
    return HttpResponse("This is the about view.")  # Adjusted the response text

# administration_dash/views.py



# Other view functions for your app
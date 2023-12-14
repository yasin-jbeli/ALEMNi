from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Tutor
from .serializers import StudentSerializer, TutorSerializer
from rest_framework import status


import secrets  # For token generation
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tutor
from .serializers import TutorSerializer

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tutor
from .serializers import TutorSerializer
import secrets  # Importing for token generation

@api_view(['POST'])
def create_tutor(request):
    serializer = TutorSerializer(data=request.data)
    
    if serializer.is_valid():
        tutor = serializer.save()
        
        # Generate confirmation token
        confirmation_token = secrets.token_urlsafe(20)  # Generate a random token (adjust length as needed)

        # Save confirmation token in the tutor profile
        tutor.confirmation_token = confirmation_token
        tutor.is_active = False  # Set is_active to False until confirmed
        tutor.save()

        # Send confirmation email
        send_confirmation_email(tutor.email, confirmation_token)  # Implement this function
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def confirm_email(request, token):
    try:
        tutor = Tutor.objects.get(confirmation_token=token)
        tutor.is_active = True  # Activate the tutor account
        tutor.save()
        return Response({'message': 'Email confirmed'}, status=status.HTTP_200_OK)
    except Tutor.DoesNotExist:
        return Response({'message': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

def send_confirmation_email(email, confirmation_token):
    # Construct the email message
    subject = 'Confirmation Email'
    confirmation_link = f'https://example.com/confirm-email/{confirmation_token}/'  # Replace with your confirmation endpoint URL
    message = f'Click the link to confirm your email: {confirmation_link}'
    from_email = 'your@example.com'  # Replace with your sender email
    recipient_list = [email]

    # Send the email
    send_mail(subject, message, from_email, recipient_list)



@api_view(['POST'])
def create_tutor(request):
    serializer = TutorSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
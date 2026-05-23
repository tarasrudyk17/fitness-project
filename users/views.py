from rest_framework import viewsets
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

"""
Views for the User API
"""
from user.serializers import UserSerializer
from rest_framework import generics

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the database"""
    serializer_class = UserSerializer

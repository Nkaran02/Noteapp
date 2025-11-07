from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #we are getting all data for creating the new user so we dont create an existing user again 
    serializer_class = UserSerializer       #this serializer class tells use what kinda data do we need to accept in this case username and password
    permission_classes = [AllowAny] #this specify who can call this in thiscase anyone


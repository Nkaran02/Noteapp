from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer, NoteSerializer
from .models import Note
# Create your views here.


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)  #get only note where auther is user
    
    def perform_create(self, serializer): #over writing default class
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #we are getting all data for creating the new user so we dont create an existing user again 
    serializer_class = UserSerializer       #this serializer class tells use what kinda data do we need to accept in this case username and password
    permission_classes = [AllowAny] #this specify who can call this in thiscase anyone

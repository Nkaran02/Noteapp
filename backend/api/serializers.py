from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
#sirializer takes json data and convert it to python equalivant code and vice versa take python code and return json data
#serializer will look at the model and all its fields , it will make sure its valid and pass it 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

        #here we are getting the validated data and creating an user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
#serializer for Notes
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only" : True}}
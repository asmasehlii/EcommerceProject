from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from user.serializer import UserSerializer
from django.contrib.auth.models import User

# Create your views here.


class ListUserAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUserAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from product.serializer import ProductSerializer
from django.contrib.auth.models import User
from .models import Product


class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

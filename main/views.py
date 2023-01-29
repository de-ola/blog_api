from django.shortcuts import render
from rest_framework import generics, permissions, pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class BlogCategoryView(APIView):
    def get(self, request, format=None, **kwargs):
        blog = Blog.objects.filter(category__id = kwargs("id"))
        serializer = BlogListSerializer(instance=blog, many=True)
        return Response(serializer, status=status.HTTP_200_OK)

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    permission_classes = [permissions.AllowAny]
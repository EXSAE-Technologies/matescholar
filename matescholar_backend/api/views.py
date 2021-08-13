from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import serializers
from schools.models import School, Program, Course

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer
    permission_classes=[
        IsAuthenticatedOrReadOnly
    ]

class SchoolViewSet(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=serializers.SchoolSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset=Program.objects.all()
    serializer_class=serializers.ProgramSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=serializers.CourseSerializer
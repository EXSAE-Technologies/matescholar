from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from schools.models import School, Program, Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username', 'email')
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields=('name', 'code')
        
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields=('school', 'name', 'code')
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=('program', 'name', 'code', 'year', 'semester')
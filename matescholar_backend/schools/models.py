from django.db import models
from django.db.models.base import Model

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Program(models.Model):
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    SEMESTER_CHOICES=[
        (1, "FIRST"),
        (2, "SECOND"),
        (3, "THIRD")
    ]
    YEAR_CHOICES=[
        (1, "FIRST"),
        (2, "SECOND"),
        (3, "THIRD"),
        (4, "FOURTH"),
        (5, "FIFTH"),
        (6, "SIXTH"),
        (7, "SEVENTH")
    ]
    program=models.ForeignKey(Program, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    year=models.CharField(max_length=200, choices=YEAR_CHOICES, default=1)
    semester=models.IntegerField(choices=SEMESTER_CHOICES, default=1)

    def __str__(self):
        return self.name
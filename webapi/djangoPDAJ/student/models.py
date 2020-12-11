from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    index      = models.CharField(max_length = 30, unique = True)

    def __str__(self):
        return self.index + ' ' + self.first_name + ' ' + self.last_name

class Grade(models.Model):
    number_of_points = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    value = models.PositiveIntegerField(default=6, validators=[MinValueValidator(6),MaxValueValidator(10)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.index  + ' ' + str(self.value)
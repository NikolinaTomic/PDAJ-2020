from .models import Student,Grade
from rest_framework  import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'index']

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Grade
        fields = ['id', 'number_of_points', 'value', 'student']
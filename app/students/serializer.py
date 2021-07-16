from rest_framework import serializer

from .models import StudentModel

class StudentSerializer(serializer.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
        
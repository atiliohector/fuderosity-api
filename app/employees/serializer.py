from django.db.models.query import QuerySet
from rest_framework import serializers

from .models import EmployeeModel

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
from rest_framework import serializers

from .models import EmployeesModels

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesModels
        fields = '__all__'
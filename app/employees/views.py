from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmployeeModel
from .serializer import EmployeesSerializer
from app.employees import serializer

from app.employees import models

@api_view(['GET','POST'])
def employees_all(request):
    if request.method == 'GET':
        employee = EmployeeModel.objects.all()
        serializer = EmployeesSerializer(employee,many=True)
        return Response(serializer.data)
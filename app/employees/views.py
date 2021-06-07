from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmployeeModel
from .serializer import EmployeesSerializer

@api_view(['GET','POST'])
def fuderosity_employees(request):
    if request.method == 'GET':
        employes_baby = EmployeeModel.objects.all()
        serializer = EmployeesSerializer(employes_baby,many=True)
        return Response(serializer.data)
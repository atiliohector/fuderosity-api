from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmployeeModel
from .serializer import EmployeesSerializer


@api_view(['GET','POST'])
def employee_totaly(request):
    if request.method == 'GET':
        employes = EmployeeModel.objects.all()
        serializer = EmployeesSerializer(employes, many=True)
        return Response(serializer.data)
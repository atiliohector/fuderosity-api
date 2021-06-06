from rest_framework import generics

from .serializer import EmployeesSerializer
from .models import EmployeeModel

class EmployeesViews(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeesSerializer
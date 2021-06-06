from rest_framework import generics

from .serializer import EmployeeSerializer
from .models import EmployeesModels

class EmployeeViewSet(generics.ListCreateAPIView):
    queryset = EmployeesModels.objects.all()
    serializer_class = EmployeeSerializer
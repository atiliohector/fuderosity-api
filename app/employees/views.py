from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from .models import EmployeeModel
from .serializer import EmployeesSerializer

# Create your views here.
class ListTodoAPIView(ListAPIView):
    """Lists all todos from the database"""
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeesSerializer

class CreateTodoAPIView(CreateAPIView):
    """Creates a new todo"""
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeesSerializer

class UpdateTodoAPIView(UpdateAPIView):
    """Update the todo whose id has been passed through the request"""
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeesSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """Deletes a todo whose id has been passed through the request"""
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeesSerializer
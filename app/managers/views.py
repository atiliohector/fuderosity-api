from rest_framework import generics

from .models import ManagersModel
from .serializer import ManagerSerializer

class CreateManager(generics.CreateAPIView):
    queryset = ManagersModel.objects.all()
    serializer_class = ManagerSerializer

class AllManagers(generics.ListAPIView):
    queryset = ManagersModel.objects.all()
    serializer_class = ManagerSerializer

class UpdateManagers(generics.UpdateAPIView):
    queryset = ManagersModel.objects.all()
    serializer_class = ManagerSerializer

class DeleteManagers(generics.DestroyAPIView):
    queryset = ManagersModel.objects.all()
    serializer_class = ManagerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import ManagersModel
from .serializer import ManagerSerializer


from rest_framework.view import APIView
from rest_framework.response import Response

from .models import ManagersModel
from .serializer import ManagerSerializer

class AllManagers(APIView):

    def get(self, request):

        managers = ManagersModel.objects.all()
        managers_serializer = ManagerSerializer(managers, many=True)
        return Response(managers_serializer.data)
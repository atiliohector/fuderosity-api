from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ManagersModel
from .serializer import ManagerSerializer

class AllManagers(APIView):

    def get(self, request):

        managers = ManagersModel.objects.all()
        serializer = ManagerSerializer(managers,many=True)
        return Response(serializer.data)
    
    
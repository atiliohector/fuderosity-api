from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ManagersModel
from .serializer import ManagerSerializer

class AllManagers(APIView):

    def get(self, request):

        managers = ManagersModel.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = {

            'name':  request.data.get('name'),
            'age':  request.data.get('age'),
            'champions':  request.data.get('champions'),
            'champion_name':  request.data.get('champion_name'),

        }

        serializer = ManagerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros)
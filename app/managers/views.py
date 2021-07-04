from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ManagersModel
from .serializer import ManagerSerializer


class AllManagers(APIView):

    def get(self, request):

        managers = ManagersModel.objects.all()
        manager_serializer = ManagerSerializer(managers, many=True)
        return Response(manager_serializer.data)

class AddManager(APIView):

    def post(self, request):

        data = {

            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'champions': request.data.get('champions'),
            'champion_name': request.data.get('champion_name'),
        }

        manager_serializer = ManagerSerializer(data=data)

        if manager_serializer.is_valid():
            manager_serializer.save()
            return Response(manager_serializer.data)
        else:
            return Response(manager_serializer.errors)

class ManagerById(APIView):

    def get_object(self, id):
        try:
            return ManagersModel.objects.get(id=id)
        except ManagersModel.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        
        manager = self.get_object(id=id)
        manager_serializer = ManagerSerializer(manager)
        return Response(manager_serializer.data)

class ManagersChampions(APIView):

    def get(self, request, champions):
        champions_managers = [champions.champions for champions in ManagersModel.objects.filter(champions=champions)]
        return Response(champions)
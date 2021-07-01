from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import PlayersModels
from .serializer import PlayersSerializer


class TodoListApiView(APIView):
    # add permission to check if user is authenticated

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = PlayersModels.objects.all()
        serializer = PlayersSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
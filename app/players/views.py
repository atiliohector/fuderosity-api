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

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'user': request.user.id,
            'name': request.data.get('name'), 
            'age': request.data.get('age'), 
            'position': request.data.get('position'),
            'guild': request.data.get('guild')
            
        }
        serializer = PlayersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import generics

from .models import PlayersModels
from .serializer import PlayersSerializer


class CreatePlayers(generics.CreateAPIView):
    queryset = PlayersModels.objects.all()
    serializer_class = PlayersSerializer

class AllPlayers(generics.ListAPIView):
    queryset = PlayersModels.objects.all()
    serializer_class = PlayersSerializer

class UpdatePlayers(generics.UpdateAPIView):
    queryset = PlayersModels.objects.all()
    serializer_class = PlayersSerializer

class DeletePlayers(generics.DestroyAPIView):
    queryset = PlayersModels.objects.all()
    serializer_class = PlayersSerializer
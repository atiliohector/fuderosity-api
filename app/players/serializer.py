from rest_framework import serializers

from .models import PlayersModels

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersModels
        fields = '__all__'
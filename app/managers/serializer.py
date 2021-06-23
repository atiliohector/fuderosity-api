from rest_framework import serializers

from .models import ManagersModel

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagersModel
        fields = '__all__'
from rest_framework import serializers
from .models import ReysModel

class ReysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReysModel
        fields = "__all__"

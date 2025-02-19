from rest_framework import serializers
from .models import ReysModel, TransitModel,Capital, Country, CityDetail,SexModel,StatusModel

class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexModel
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = "__all__"


class ReysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReysModel
        fields = "__all__"

class TransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitModel
        fields = "__all__"


class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CityDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()  # Include country details in the response
    class Meta:
        model = CityDetail
        fields = '__all__'
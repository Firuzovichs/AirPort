from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import ReysModel,TransitModel, Capital,CountryCapital,CityDetail
from .serializers import ReysSerializer, TransitSerializer,CapitalSerializer,CityDetailSerializer
# Create your views here.
class ReysListCreateView(generics.ListCreateAPIView):
    queryset = ReysModel.objects.all()
    serializer_class = ReysSerializer

class ReysRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReysModel.objects.all()
    serializer_class = ReysSerializer

class TransitListCreateView(generics.ListCreateAPIView):
    queryset = TransitModel.objects.all()
    serializer_class = TransitSerializer

class TransitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransitModel.objects.all()
    serializer_class = TransitSerializer


class CapitalListView(APIView):
    def get(self, request):
        capitals = Capital.objects.all()
        serializer = CapitalSerializer(capitals, many=True)
        return Response(serializer.data)

class CityDetailByCapital(APIView):
    def get(self, request, capital_id):
        try:
            capital = Capital.objects.get(id=capital_id)
            city_details = CityDetail.objects.filter(capital=capital)
            serializer = CityDetailSerializer(city_details, many=True)
            return Response(serializer.data)
        except Capital.DoesNotExist:
            return Response({"error": "Capital not found"}, status=404)
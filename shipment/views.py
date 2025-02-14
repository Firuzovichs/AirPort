from django.shortcuts import render
from rest_framework import generics
from .models import ReysModel
from .serializers import ReysSerializer
# Create your views here.
class ReysListCreateView(generics.ListCreateAPIView):
    queryset = ReysModel.objects.all()
    serializer_class = ReysSerializer

class ReysRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReysModel.objects.all()
    serializer_class = ReysSerializer
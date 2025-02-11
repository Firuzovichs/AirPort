from rest_framework import generics, status
from .models import Dispatch
from .serializers import DispatchSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView


class DispatchCreateView(APIView):
    def post(self, request):
        serializer = DispatchSerializer(data=request.data)
        
        if not all(request.data.get(field) for field in Dispatch._meta.get_fields() if not getattr(field, 'null', False)):
            return Response({"error": "All required fields must be provided"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DispatchListView(generics.ListCreateAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    def get_queryset(self):
        queryset = Dispatch.objects.all()
        params = self.request.query_params
        filters = Q()

        # Filtering by status
        status_id = params.get('status', None)
        if status_id:
            filters &= Q(status_id=status_id)

        # Filtering by date fields
        data_dispatch = params.get('data_dispatch', None)
        if data_dispatch:
            filters &= Q(data_dispatch__date=data_dispatch)

        data_reception = params.get('data_reception', None)
        if data_reception:
            filters &= Q(data_reception__date=data_reception)

        # Filtering by country and capital relations
        from_country = params.get('from_country', None)
        if from_country:
            filters &= Q(from_country_id=from_country)

        to_country = params.get('to_country', None)
        if to_country:
            filters &= Q(to_country_id=to_country)

        from_capital = params.get('from_capital', None)
        if from_capital:
            filters &= Q(from_capital_id=from_capital)

        to_capital = params.get('to_capital', None)
        if to_capital:
            filters &= Q(to_capital_id=to_capital)

        return queryset.filter(filters)
        
class DispatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer
    lookup_field = 'id'

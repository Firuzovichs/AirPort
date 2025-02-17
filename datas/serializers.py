from rest_framework import serializers
from .models import Dispatch

class DispatchSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)
    tranzit = serializers.CharField(source='tranzit.name', allow_null=True)
    sex_1 = serializers.CharField(source='sex_1.name', allow_null=True)
    sex_2 = serializers.CharField(source='sex_2.name', allow_null=True)
    to_country = serializers.CharField(source='to_country.name', allow_null=True)
    to_capital = serializers.CharField(source='to_capital.name', allow_null=True)
    from_country = serializers.CharField(source='from_country.name', allow_null=True)
    from_capital = serializers.CharField(source='from_capital.name', allow_null=True)
    status = serializers.CharField(source='status.name', allow_null=True)
    category_status = serializers.CharField(source='category_status.name', allow_null=True)
    
    data_reception = serializers.SerializerMethodField()
    data_dispatch = serializers.SerializerMethodField()

    def get_data_reception(self, obj):
        return obj.data_reception.strftime('%d-%m-%Y') if obj.data_reception else None

    def get_data_dispatch(self, obj):
        return obj.data_dispatch.strftime('%d-%m-%Y') if obj.data_dispatch else None
    
    class Meta:
        model = Dispatch
        fields = [
            'id', 'type', 'tranzit', 'sex_1', 'sex_2', 'data_reception', 'data_dispatch',
            'dispatches', 'to_country', 'to_capital', 'from_country', 'from_capital',
            'status', 'category_status', 'quantity', 'weight', 'note', 'flightNumber'
        ]


from rest_framework import serializers
from datas.models import Dispatch, TypeModel, TransitModel, SexModel, Country, Capital, StatusModel, CategoryMailModel

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


class DispatchSerializer2(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=TypeModel.objects.all(), required=False)
    tranzit = serializers.PrimaryKeyRelatedField(queryset=TransitModel.objects.all(), required=False)
    sex_1 = serializers.PrimaryKeyRelatedField(queryset=SexModel.objects.all(), required=False)
    sex_2 = serializers.PrimaryKeyRelatedField(queryset=SexModel.objects.all(), required=False)
    to_country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=False)
    to_capital = serializers.PrimaryKeyRelatedField(queryset=Capital.objects.all(), required=False)
    from_country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=False)
    from_capital = serializers.PrimaryKeyRelatedField(queryset=Capital.objects.all(), required=False)
    status = serializers.PrimaryKeyRelatedField(queryset=StatusModel.objects.all(), required=False)
    category_status = serializers.PrimaryKeyRelatedField(queryset=CategoryMailModel.objects.all(), required=False)
    data_reception = serializers.DateTimeField(required=False)
    data_dispatch = serializers.DateTimeField(required=False)
    quantity = serializers.IntegerField(required=False)
    weight = serializers.FloatField(required=False)
    note = serializers.CharField(required=False)

    class Meta:
        model = Dispatch
        fields = '__all__'
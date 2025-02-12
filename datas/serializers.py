from rest_framework import serializers
from .models import Dispatch

class DispatchSerializer(serializers.ModelSerializer):
    tranzit = serializers.SerializerMethodField()
    sex_1 = serializers.SerializerMethodField()
    sex_2 = serializers.SerializerMethodField()
    to_country = serializers.SerializerMethodField()
    to_capital = serializers.SerializerMethodField()
    from_country = serializers.SerializerMethodField()
    from_capital = serializers.SerializerMethodField()

    class Meta:
        model = Dispatch
        fields = [
            "tranzit", "sex_1", "sex_2", "data_reception", "data_dispatch",
            "to_country", "to_capital", "from_country", "from_capital"
        ]

    def get_tranzit(self, obj):
        return obj.tranzit.name if obj.tranzit else None

    def get_sex_1(self, obj):
        return obj.sex_1.name if obj.sex_1 else None

    def get_sex_2(self, obj):
        return obj.sex_2.name if obj.sex_2 else None

    def get_to_country(self, obj):
        return obj.to_country.name if obj.to_country else None

    def get_to_capital(self, obj):
        return obj.to_capital.name if obj.to_capital else None

    def get_from_country(self, obj):
        return obj.from_country.name if obj.from_country else None

    def get_from_capital(self, obj):
        return obj.from_capital.name if obj.from_capital else None

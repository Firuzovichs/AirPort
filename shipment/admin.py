from django.contrib import admin
from .models import StatusModel,CategoryMailModel, CountryCapital, Country, Capital, StatusModel,TypeModel,SexModel,TransitModel,ReysModel

admin.site.register([StatusModel,CategoryMailModel,Capital, Country,CountryCapital,TypeModel,SexModel,TransitModel,ReysModel])


from django.contrib import admin
from .models import StatusModel,CategoryMailModel, CityDetail, Country, Capital, StatusModel,TypeModel,SexModel,TransitModel,ReysModel

admin.site.register([StatusModel,CategoryMailModel,Capital, Country,CityDetail,TypeModel,SexModel,TransitModel,ReysModel])


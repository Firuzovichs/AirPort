from django.urls import path
from .views import CountryCapitalDetailView

urlpatterns = [
    path('country-capital/<int:id>/', CountryCapitalDetailView.as_view(), name='country-capital-detail'),
]
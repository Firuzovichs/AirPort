
from django.contrib import admin
from django.urls import path, re_path
from datas.views import  DispatchRetrieveUpdateDestroyView,DispatchListView,DispatchCreateView,DispatchListView3
from shipment.views import StatusListCreateView,StatusRetrieveUpdateDestroyView,ReysListCreateView,SexListCreateView,SexRetrieveUpdateDestroyView, ReysRetrieveUpdateDestroyView,TransitListCreateView,CapitalListView,CityDetailByCapital, TransitRetrieveUpdateDestroyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('dispatch/', DispatchListView3.as_view(), name='dispatch-list'),
    path('admin/', admin.site.urls),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('dispatches/<uuid:id>/', DispatchRetrieveUpdateDestroyView.as_view(), name='dispatch-detail'),
    path('dispatches/', DispatchListView.as_view(), name='dispatch-list-view'),
    path('dispatchcreate/', DispatchCreateView.as_view(), name='dispatch-create-view'),
    path('reyslar/', ReysListCreateView.as_view(), name='reys-list'),
    path('reyslar/<int:pk>/', ReysRetrieveUpdateDestroyView.as_view(), name='reys-detail'),
    path('transit/', TransitListCreateView.as_view(), name='transit-list'),
    path('transit/<int:pk>/', TransitRetrieveUpdateDestroyView.as_view(), name='transit-detail'),
    path('capitals/', CapitalListView.as_view(), name='capital-list'),
    path('capitals/<int:capital_id>/details/', CityDetailByCapital.as_view(), name='city-detail-by-capital'),
    path('sexs/', SexListCreateView.as_view(), name='transit-list'),
    path('sexs/<int:pk>/', SexRetrieveUpdateDestroyView.as_view(), name='transit-detail'),
    path('status/', StatusListCreateView.as_view(), name='status-list'),
    path('status/<int:pk>/', StatusRetrieveUpdateDestroyView.as_view(), name='status-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^download_media/(?P<path>.*)$', protected_media, name='protected_media'),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]


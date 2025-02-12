
from django.contrib import admin
from django.urls import path, re_path
from datas.views import  DispatchRetrieveUpdateDestroyView, DispatchListView,DispatchCreateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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
    path('admin/', admin.site.urls),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('dispatches/<uuid:id>/', DispatchRetrieveUpdateDestroyView.as_view(), name='dispatch-detail'),
    path('dispatches/', DispatchListView.as_view(), name='dispatch-list-view'),
    path('dispatchcreate/', DispatchCreateView.as_view(), name='dispatch-create-view'),

]


from django.contrib import admin
from django.urls import path
from datas.views import  DispatchRetrieveUpdateDestroyView, DispatchListView,DispatchCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dispatches/<uuid:id>/', DispatchRetrieveUpdateDestroyView.as_view(), name='dispatch-detail'),
    path('dispatches/', DispatchListView.as_view(), name='dispatch-list-view'),
    path('dispatchcreate/', DispatchCreateView.as_view(), name='dispatch-create-view'),

]

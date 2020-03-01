from django.urls import path
from .views import HostList

urlpatterns = [
    path('',HostList.as_view(),name='hostlist'),
]

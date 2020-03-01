from rest_framework import generics
from .models import Host
from .serializers import HostSerializer

# Create your views here.
class HostList(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

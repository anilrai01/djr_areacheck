from rest_framework import serializers
from .models import Host,Node,DownNode,Acknowledged_node,Department,Reason,SubReason

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','hostname','vendor','snmpIndex')
        model = Host

from areacheck.models import Host,Node
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Import Hosts From CSV to database"

    def handle(self,*args,**kwargs):
        self.stdout.write("Importing Hosts")
        with open("sqlexports/nodes.csv") as f:
            nodelist = f.readlines()

        nodelist = [[h.strip('"') for h in node.split(";")] for node in nodelist]

        for nde in nodelist:
            id,hid,interface,desc,snmpIndex,online,status,_,_ = nde
            node = Node()
            node.host = Host.objects.get(pk=hid)
            node.description = desc
            node.interface = interface
            node.snmp_index = snmpIndex
            node.online = online
            node.save()
            self.stdout.write("{} Node Added".format(node))

from areacheck.models import Host
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Import Hosts From CSV to database"

    def handle(self,*args,**kwargs):
        self.stdout.write("Importing Hosts")
        with open("sqlexports/hosts.csv") as f:
            hostlist = f.readlines()

        hostlist = [[h.strip('"') for h in host.split(";")] for host in hostlist]

        for hst in hostlist:
            id,hostname,community,vendor,snmpIndex = hst
            host = Host()
            host.hostname = hostname
            host.community_string = community
            host.vendor = vendor
            host.snmpIndex = snmpIndex
            host.save()
            self.stdout.write("Added host {}".format(hostname))

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Host(models.Model):
    """Model for Host Devices"""
    hostname = models.CharField(max_length=50)
    community_string = models.CharField(max_length = 49,help_text="Community string used to snmpwalk")
    vendor = models.CharField(max_length = 50,help_text="Name of the vendor")
    snmpIndex = models.CharField(max_length = 50,null=True,help_text="Snmp index of the host")

    def __str__(self):
        return self.hostname.split('.')[0] # ingnoring the .subisu.net.np



class Node(models.Model):
    """Nodes on hosts"""

    host = models.ForeignKey(Host,on_delete=models.PROTECT)
    interface = models.CharField(max_length=255,help_text="Name of the Interface")
    description = models.CharField(max_length=255, help_text="Location or the description of the node")
    snmp_index = models.CharField(max_length = 50,null=True,help_text="Snmp index of the host")
    online = models.IntegerField(help_text="Number of online ports")
    monitor_status = models.BooleanField(default=True,help_text="Status of node")
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.interface



class DownNode(models.Model):

    node = models.ForeignKey(Node,on_delete=models.PROTECT,help_text="ID of the down node")
    ackStatus = models.BooleanField(default=False,help_text="Status of Down nodes if Acknowledged")
    downtime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(blank=True,null=True)

    def get_hostname(self):
        return self.node.host.hostname

    def get_interface(self):
        return self.node.interface

    def get_description(self):
        return self.node.description

    def get_downtime(self):
        if self.uptime:
            return self.uptime - self.downtime
        else:
            return timezone.now() - self.downtime

    # def get_acknowledged_by(self):
    #     pass
        # return self.acknowle


    def __str__(self):
        return self.node.interface

class Acknowledged_node(models.Model):
    RESOLVED = 2
    UP = 1
    DOWN = 0
    STATUS = [
        (DOWN,"Down"),
        (UP,"Up"),
        (RESOLVED,"Resolved"),
    ]
    node = models.OneToOneField(DownNode,on_delete=models.CASCADE,primary_key = True,help_text="Id of Down Node")
    acknowledged_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    acknowledged_date = models.DateTimeField(auto_now_add=True)
    reason = models.ForeignKey('SubReason',on_delete = models.DO_NOTHING)
    assigned_to = models.CharField(max_length=255, help_text="Name of the Person The task is\
                                   Assigned To")
    status = models.IntegerField(choices=STATUS,default=DOWN)

    def __str__(self):
        return self.node.node.interface


class Department(models.Model):
    ACTIVE = 1
    DEACTIVE = 0
    STATUS_CHOICES = [
        (ACTIVE,'Active'),
        (DEACTIVE,'Deactive'),
    ]
    name = models.CharField(max_length=255)
    head = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    status = models.IntegerField(
        choices = STATUS_CHOICES,
        default = ACTIVE
    )

    def __str__(self):
        """Returns Department name in the admin pannel"""
        return self.name



class Reason(models.Model):
    department = models.ForeignKey(Department,on_delete = models.CASCADE,help_text="select which department the reason is concerned with")
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

class SubReason(models.Model):
    reason = models.ForeignKey(Reason,on_delete = models.PROTECT,help_text="Sub Reason of the Reason")
    sub_reason = models.TextField()

    def __str__(self):
        return self.sub_reason

class Comment(models.Model):
    downnode = models.ForeignKey(Acknowledged_node,on_delete=models.CASCADE,blank=False,null=False)
    commented_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return "Comments of {}".format(self.downnode)

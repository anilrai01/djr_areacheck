from django.contrib import admin
from .models import (Host,
                     Department,
                     Node,
                     DownNode,
                     Reason,
                     SubReason,
                     Acknowledged_node,
                     Comment
                    )

# Register your models here.
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ( 'id','hostname','community_string','vendor' )
    list_display_link = ('hostname',)
    ordering = ('id',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','head','email','status')
    list_display_link = ('name',)
    list_per_page = 20
    ordering = ['name']

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('host_id','interface','description','online')

@admin.register(DownNode)
class DownNodeAdmin(admin.ModelAdmin):
    list_display = ('id','node','downtime','ackStatus','uptime')
    list_display_links = ('id','node',)
    search_fields = ['node']
    ordering = ['-downtime']

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('reason','department')

@admin.register(SubReason)
class ReasonAdmin(admin.ModelAdmin):
    pass

@admin.register(Acknowledged_node)
class AckAdmin(admin.ModelAdmin):
    pass
    # list_display = ('node','status','reason')
    # list_display_links = ['id','node',]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_display
    pass

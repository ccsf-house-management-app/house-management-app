from django.contrib import admin

from .models import Rooms, RoomsAssign

class RoomsAdmin(admin.ModelAdmin):
    list_display = ( 'roomId', 'roomName', 'roomDescription', 'rent', 'capacity', 'date_created' )

class RoomsAssignAdmin(admin.ModelAdmin):
    list_display = ( 'roomid', 'tenantid', 'date_start', 'date_end', 'date_transaction', 'transactionId', 'remarks')

# Register your models here.
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(RoomsAssign, RoomsAssignAdmin)

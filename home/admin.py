from django.contrib import admin
from .models import Cottage, Reservation, Complete, Guest

# Register your models here.
admin.site.register(Cottage)
admin.site.register(Complete)
admin.site.register(Guest)
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('res_id', 'cottage', 'start', 'end', 'guest_id', 'is_complete')
    list_editable = ('is_complete',)
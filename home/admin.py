from django.contrib import admin
from .models import Cottage, Reservation, Complete, Guest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    list_display = ('res_id', 'cottage', 'start', 'end', 'guest_id', 'is_complete')
    list_filter = ('is_complete',)
    search_fields = ['res_id']
    list_editable = ('is_complete',)
    summernote_fields = ('res_id',)

admin.site.register(Cottage)
admin.site.register(Complete)
admin.site.register(Guest)
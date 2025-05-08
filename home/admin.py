from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Cottage, Complete, Guest, Reservation

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    list_display = (
        'res_id', 'cottage', 'start', 'end', 
        'guest_id', 'is_complete', 'note', 'created_on'
    )
    list_filter = ('is_complete',)
    search_fields = ['res_id']
    list_editable = ('is_complete',)
    summernote_fields = ('note',)
    readonly_fields = ('res_id', 'created_on')

    def get_fields(self, request, obj=None):
        # Base fields
        fields = [
            "cottage", "start", "end", "guest_id", 
            "discount", "note", "created_on"
        ]
        # Only show 'is_complete' if the user is a superuser
        if request.user.is_superuser:
            fields.append("is_complete")
        return fields

    def get_list_editable(self, request):
        return ('cottage',) if request.user.is_superuser else ()

    def get_readonly_fields(self, request, obj=None):
        readonly = list(self.readonly_fields)
        if not request.user.is_superuser:
            readonly.append("is_complete")
        return readonly

admin.site.register(Cottage)
admin.site.register(Complete)
admin.site.register(Guest)
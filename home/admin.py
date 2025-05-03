from django.contrib import admin
from .models import Cottage, Reservation, Complete, Guest
# Register your models here.
admin.site.register(Cottage)
admin.site.register(Reservation)
admin.site.register(Complete)
admin.site.register(Guest)
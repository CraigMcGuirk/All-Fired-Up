from django.contrib import admin
from booking_app.models import Reservation, Table

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Table)

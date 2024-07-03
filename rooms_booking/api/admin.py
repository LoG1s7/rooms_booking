from django.contrib import admin
from django.contrib.auth import get_user_model
from rooms.models import Room, Booking

User = get_user_model()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'cost_per_day', 'number_of_beds')
    empty_value_display = '-пусто-'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'guest',
        'check_in_date',
        'check_out_date'
    )
    empty_value_display = '-пусто-'

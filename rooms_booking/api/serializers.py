from rest_framework import serializers
from rooms.models import Booking, Room


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("id", "room", "guest", "check_in_date", "check_out_date")

    def validate(self, data):
        start_date = data["check_in_date"]
        end_date = data["check_out_date"]
        if end_date < start_date:
            raise serializers.ValidationError(
                "Дата заезда должна быть раньше даты выезда"
            )
        if end_date == start_date:
            raise serializers.ValidationError(
                "Номер можно забронировать минимум на 1 сутки"
            )
        number = data["room"].room_number
        try:
            room = Room.objects.get(room_number=number)
        except Exception:
            raise serializers.ValidationError("Такой комнаты не существует")
        if room.bookings.filter(
            check_in_date__lt=end_date, check_out_date__gt=start_date
        ).exists():
            raise serializers.ValidationError(
                "Комната уже забронирована в данные даты"
            )
        return super().validate(data)


class RoomSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = (
            "id",
            "room_number",
            "cost_per_day",
            "number_of_beds",
            "bookings",
        )

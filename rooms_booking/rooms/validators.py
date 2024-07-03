from django.core.exceptions import ValidationError
from django.utils import timezone


def check_booking(value):
    if (value.check_in_date < value.check_out_date
            and value.check_out_date > value.check_in_date):
        raise ValidationError(
            'Комната уже забронирована в данные даты')


def validate_check_out_date_is_equal_to_check_in_date(booking):
    if booking.check_out_date == booking.check_in_date:
        raise ValidationError('Номер можно забронировать минимум на 1 сутки')


def validate_check_out_date_is_later_than_check_in_date(booking):
    if booking.check_out_date < booking.check_in_date:
        raise ValidationError('Дата заезда должна быть раньше даты выезда')


def validate_check_in_date_is_not_past(value):
    if value < timezone.now().date():
        raise ValidationError('Дата заезда не может быть в прошлом')

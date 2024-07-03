from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from .validators import (check_booking, validate_check_in_date_is_not_past,
                         validate_check_out_date_is_equal_to_check_in_date,
                         validate_check_out_date_is_later_than_check_in_date)

User = get_user_model()


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField(
        'Номер комнаты',
        validators=[MinValueValidator(
            1, message='Номер должен быть больше 0'
        )],
        unique=True
    )
    cost_per_day = models.DecimalField(
        'Стоимость за сутки', max_digits=6, decimal_places=2,
        validators=[MinValueValidator(
            1, message='Стоимость должна быть больше 0'
        )]
    )
    number_of_beds = models.PositiveSmallIntegerField(
        'Количество спальных мест',
        validators=[MinValueValidator(
            1, message='Количество должно быть больше 0'
        )]
    )

    def __str__(self):
        return f'Комната номер: {self.room_number}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Booking(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, verbose_name='Комната',
        related_name='bookings'
    )
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Гость'
    )
    check_in_date = models.DateField(
        'Дата заезда', validators=[validate_check_in_date_is_not_past]
    )
    check_out_date = models.DateField(
        'Дата выезда',
    )

    def __str__(self):
        return f'{self.room} - {self.check_in_date} до {self.check_out_date}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def clean(self):
        super().clean()
        check_booking(self)
        validate_check_out_date_is_equal_to_check_in_date(self)
        validate_check_out_date_is_later_than_check_in_date(self)

    @property
    def is_room_occupied(self):
        now = timezone.now()
        return self.check_in_date <= now <= self.check_out_date

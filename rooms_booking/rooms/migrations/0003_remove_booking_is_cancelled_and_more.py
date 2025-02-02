# Generated by Django 5.0.6 on 2024-07-02 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_booking_is_cancelled_booking_is_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_cancelled',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='is_confirmed',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Номер должен быть больше 0')], verbose_name='Номер комнаты'),
        ),
    ]

from django_filters.rest_framework import FilterSet, filters

from rooms.models import Room


class RoomFilter(FilterSet):
    start_date = filters.DateFilter(
        field_name="bookings__check_in_date", lookup_expr='lt', exclude=True)
    end_date = filters.DateFilter(
        field_name="bookings__check_out_date", lookup_expr='gt', exclude=True)
    cost_per_day = filters.NumberFilter(field_name='cost_per_day')
    number_of_beds = filters.NumberFilter(field_name='number_of_beds')

    class Meta:
        model = Room
        fields = ['start_date', 'end_date', 'cost_per_day', 'number_of_beds']

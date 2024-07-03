from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from rooms.models import Room, Booking
from .permissions import IsAdminOrReadOnlyPermission
from .serializers import BookingSerializer, RoomSerializer
from .filters import RoomFilter


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [IsAdminOrReadOnlyPermission]
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = RoomFilter
    ordering_fields = ('cost_per_day', 'number_of_beds')
    ordering = ('cost_per_day',)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(guest=self.request.user)

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)

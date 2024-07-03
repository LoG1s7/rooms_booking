from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, RoomViewSet

router = DefaultRouter()
router.register('rooms', RoomViewSet, basename='rooms')
router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]


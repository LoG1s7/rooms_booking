from django.urls import include, path, re_path
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

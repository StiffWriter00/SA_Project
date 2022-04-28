from django import urls
from django.urls import include, path
from rest_framework import routers
from .views import booking
from .views import home_view
router = routers.DefaultRouter()
router.register(r'Book', booking)

urlpatterns = [
    path('', include(router.urls)),
    path('booking/', home_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
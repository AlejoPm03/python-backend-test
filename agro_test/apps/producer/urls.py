# Django
from django.urls import include, path
# Rest
from rest_framework import routers
# Views
from apps.producer.views import ProducerViewSet, CropViewSet


# Creates app router
router = routers.DefaultRouter()

# Connects viewsets to router with user route
router.register(r"producer", ProducerViewSet)
router.register(r"crop", CropViewSet)


# Connects router in base pattern
urlpatterns = [
	path("", include(router.urls)),
]
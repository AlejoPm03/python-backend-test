# Django
from django.urls import include, path
# Rest
from rest_framework import routers
# Views
from apps.user.views import UserViewSet


# Creates app router
router = routers.DefaultRouter()

# Connects viewsets to router with user route
router.register(r"", UserViewSet)

# Connects router in base pattern
urlpatterns = [
	path("", include(router.urls))
]
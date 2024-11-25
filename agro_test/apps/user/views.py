# Rest
from rest_framework import viewsets
# Models
from apps.user.models import User
# Serializers
from apps.user.serializers import UserSerializer


#
# View set definition for User model
#
class UserViewSet(viewsets.ModelViewSet):

	# Query set for this model
	queryset = User.objects.all().order_by("created_at")

	# Serialization
	serializer_class = UserSerializer

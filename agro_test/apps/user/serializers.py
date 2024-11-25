# Rest
from rest_framework import serializers
# Models
from apps.user.models import User

#
# Serializer for User model
#
class UserSerializer(serializers.ModelSerializer):

	# Metadata

	class Meta:
		# Models class
		model = User

		# Fields to serialize
		fields = (
			"id", "created_at", "updated_at", "deleted_at",
			"email", "password", "username", "is_active"
		)

		# Extra kwargs
		extra_kwargs = {
			"password": {
				"write_only": True
			},
			"deleted_at": {
				"read_only": True
			}
		}

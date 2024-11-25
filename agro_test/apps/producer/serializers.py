# Rest
from rest_framework import serializers
# Models
from apps.producer.models import Producer, Crop

#
# Serializer for Producer model
#
class ProducerSerializer(serializers.ModelSerializer):

	# Metadata
	class Meta:
		# Model class
		model = Producer

		# Fields to serialize
		fields = (
			"id",
			"created_at",
			"updated_at",
			"deleted_at",
			"name",
			"farm_name",
			"cpf_cnpj",
			"city",
			"state",
			"total_area",
			"cultivable_area",
			"vegetation_area",
			"planted_crops",
		)

		# Extra kwargs
		extra_kwargs = {
			"deleted_at": {
				"read_only": True,  # Prevent soft delete date from being edited directly
			},
			"created_at": {
				"read_only": True,  # Auto-generated, should not be editable
			},
			"updated_at": {
				"read_only": True,  # Auto-updated, should not be editable
			},
		}

#
# Serializer for Crop model
#
class CropSerializer(serializers.ModelSerializer):
	
	producers = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

	# Metadata
	class Meta:
		# Model class
		model = Crop

		# Fields to serialize
		fields = (
			"id",
			"name",
			"producers"
		)



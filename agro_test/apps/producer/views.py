# Rest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Models
from apps.producer.models import Producer, Crop
# Serializers
from apps.producer.serializers import ProducerSerializer, CropSerializer
# Statistics
from django.db.models import Count, Sum


#
# View set definition for Producer model
#
class ProducerViewSet(viewsets.ModelViewSet):

	# Query set for this model
	queryset = Producer.objects.all().order_by("created_at")

	# Serialization
	serializer_class = ProducerSerializer

	# Returns total area grouped by state.
	@action(detail=False, methods=["get"])
	def by_state(self, request):
		data = (
			Producer.objects.values("state")
			.annotate(total_area=Sum("total_area"), producer_count=Count("id"))
			.order_by("-total_area")
		)
		return Response(data)
	
	# Returns total area grouped by crop.
	@action(detail=False, methods=["get"])
	def by_crop(self, request):
		data = (
			Crop.objects.annotate(total_area=Sum("producers__total_area"))
			.values("name", "total_area")
			.order_by("-total_area")
		)
		return Response(data)

	# Returns total cultivable and vegetation area.
	@action(detail=False, methods=["get"])
	def by_land_use(self, request):
		data = Producer.objects.aggregate(
			total_cultivable_area=Sum("cultivable_area"),
			total_vegetation_area=Sum("vegetation_area"),
		)
		return Response(data)

	# Returns total area
	@action(detail=False, methods=["get"])
	def total_area(self, request):
		data = Producer.objects.aggregate(total_area=Sum("total_area"))
		return Response(data)
	
	# Returns total producers
	@action(detail=False, methods=["get"])
	def total_producers(self, request):
		data = Producer.objects.count()
		return Response(data)

#
# View set definition for Crop model
#
class CropViewSet(viewsets.ModelViewSet):
	
	# Query set for this model
	queryset = Crop.objects.all().order_by("id")

	# Serialization
	serializer_class = CropSerializer
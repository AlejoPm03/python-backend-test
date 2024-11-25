# Django Test Case
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.producer.models import Producer, Crop

class ProducerModelTest(TestCase):
	def setUp(self):
		# Create a sample crop for relationships
		self.crop = Crop.objects.create(name="Soybean")

	#
	# Test  cpf/cnpj
	#
	def test_valid_cpf_cnpj(self):
		# Valid CPF/CNPJ should not raise an error
		producer = Producer(
			cpf_cnpj="075.951.170-54",
			name="John Doe",
			farm_name="Doe Farm",
			city="Farmville",
			state="SP",
			total_area=100,
			cultivable_area=60,
			vegetation_area=30,
		)
		try:
			producer.full_clean()
		except ValidationError as e:
			self.fail(f"Valid CPF/CNPJ raised ValidationError: {e}")

	def test_invalid_cpf_cnpj(self):
		# Invalid CPF/CNPJ should raise an error
		producer = Producer(
			cpf_cnpj="075.951.170-52",
			name="Jane Doe",
			farm_name="Doe Farm",
			city="Farmville",
			state="SP",
			total_area=100,
			cultivable_area=60,
			vegetation_area=30,
		)
		with self.assertRaises(ValidationError):
			producer.full_clean()

	#
	# Test total area
	#
	def test_total_area_valid(self):
		# Total area greater than or equal to sum of cultivable and vegetation area
		producer = Producer(
			cpf_cnpj="075.951.170-54",
			name="John Doe",
			farm_name="Doe Farm",
			city="Farmville",
			state="SP",
			total_area=100,
			cultivable_area=60,
			vegetation_area=30,
		)
		try:
			producer.full_clean()
		except ValidationError as e:
			self.fail(f"Valid total area raised ValidationError: {e}")

	def test_total_area_invalid(self):
		# Total area less than the sum of cultivable and vegetation area should raise an error
		producer = Producer(
			cpf_cnpj="075.951.170-54",
			name="John Doe",
			farm_name="Doe Farm",
			city="Farmville",
			state="SP",
			total_area=80,
			cultivable_area=50,
			vegetation_area=40,
		)
		with self.assertRaises(ValidationError):
			producer.full_clean()

	#
	# Test relationships
	#
	def test_planted_crops_relationship(self):
		# Test ManyToMany relationship with crops
		producer = Producer.objects.create(
			cpf_cnpj="075.951.170-54",
			name="John Doe",
			farm_name="Doe Farm",
			city="Farmville",
			state="SP",
			total_area=100,
			cultivable_area=60,
			vegetation_area=30,
		)
		producer.planted_crops.add(self.crop)
		self.assertIn(self.crop, producer.planted_crops.all())


# Django imports
from django.db import models
from django.forms import ValidationError
# Enums
from apps.common.enums import States
# Validators
from apps.common.validators import CpfCnpjValidator


#
# DB models
#

#
# Represents a agriculture producer
#

from django.core.exceptions import ValidationError

class Crop(models.Model):

	# Crop name
	name = models.CharField(max_length=255, unique=True)

	class Meta:
		verbose_name = "Crop"
		verbose_name_plural = "Crops"

	def __str__(self):
		return self.name

class Producer(models.Model):
	# Creation and update date control
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	# Soft delete date
	deleted_at = models.DateTimeField(default = None, blank = True, null = True)

	# CPF or CNPJ
	cpf_cnpj = models.CharField(validators=[CpfCnpjValidator()])

	# Producer name
	name = models.CharField(max_length = 255)

	# Farm name
	farm_name = models.CharField(max_length = 255)

	# City
	city = models.CharField(max_length = 255)

	# State
	state = models.CharField(max_length = 2, choices = States.choices())

	# Total area in hectares
	total_area = models.DecimalField(max_digits = 10, decimal_places = 2)

	# Cultivable area in hectares
	cultivable_area = models.DecimalField(max_digits = 10, decimal_places = 2)

	# Vegetation area in hectares
	vegetation_area = models.DecimalField(max_digits = 10, decimal_places = 2)

	# Planted crops
	planted_crops = models.ManyToManyField(
		Crop,
		related_name="producers",
		symmetrical = False,
		blank = True
	)


	# Metadata

	class Meta:
		# Ordering
		ordering = ["created_at"]

		# Table name
		db_table = "producers"

		# Verbose name
		verbose_name = "producer"

		# Verbose name plural
		verbose_name_plural = "producers"

	#
	# Overrides
	#

	def clean(self):
		super().clean()
		# Validate total area
		self._total_area_validator()

	def save(self, *args, **kwargs):
		# Validate fields
		self.full_clean()

		# 
		
		# Call parent method
		super().save(*args, **kwargs)

	# Validate total area
	def _total_area_validator(self) -> None:
		if self.vegetation_area and self.cultivable_area and self.total_area:
			if self.total_area < self.vegetation_area + self.cultivable_area:
				raise ValidationError(
					"The total area cannot be less than the sum of vegetation area and cultivable area."
				)


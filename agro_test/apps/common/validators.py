from django.forms import ValidationError
from pycpfcnpj import cpfcnpj
from django.utils.deconstruct import deconstructible

# Validator class for CPF and CNPJ
@deconstructible
class CpfCnpjValidator():
	# Validates CPF or CNPJ
	def __call__(self, value: str):
		if not cpfcnpj.validate(value):
			raise ValidationError(f'CPF or CNPJ {value} is invalid')
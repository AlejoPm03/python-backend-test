# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser
# Hashers
from django.contrib.auth.hashers import make_password

#
# DB models
#

#
# Represents a user
#
class User(AbstractUser):
	# Creation and update date control
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	# Soft delete date
	deleted_at = models.DateTimeField(default = None, blank = True, null = True)

	# Metadata

	class Meta:
		# Ordering
		ordering = ["created_at"]

		# Table name
		db_table = "users"

		# Verbose name
		verbose_name = "user"

		# Verbose name plural
		verbose_name_plural = "users"

	#
	# Overrides
	#

	#
	# Custom save method to hash all password, be careful to not use the default
	# create_user method from django since it can generate a double hash in the
	# password an after that the user will not be able to login due that the
	# authenticate and check_password methods will always fail
	#
	def save(self, *args, **kwargs) -> None:
		# Hashes password
		self.password = make_password(self.password)

		super().save(*args, **kwargs)


	# String representation of the model
	def __str__(self):
		return f'{self.username} / ID: {self.id}'

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.FileField(upload_to='images/', null=True, blank=True)
	contact = models.BigIntegerField()
	class Meta:
		db_table = 'profile'
		managed = True

	def __str__(self):
		return self.user


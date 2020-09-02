from django.db import models
from django.contrib.auth.models import AbstractUser
#class Users(models.Model):
#  name = models.CharField(max_length=255)
#  email = models.EmailField(unique=True)
#  password = models.CharField(max_length=255)
class CustomUser (AbstractUser):
	matricula = models.CharField('matricula', max_length=11)

	def __str__(self):
		return self.matricula
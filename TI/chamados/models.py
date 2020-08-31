from django.db import models

class Users(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)

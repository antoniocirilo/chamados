from django.db import models
from django.contrib.auth.models import AbstractUser
#class Users(models.Model):
#  name = models.CharField(max_length=255)
#  email = models.EmailField(unique=True)
#  password = models.CharField(max_length=255)
class CustomUser (AbstractUser):
	matricula = models.CharField('matricula', max_length=11)

	def __str__(self):
		return self.username

class ProblemaRelacionado(models.Model):
	relacao = models.CharField('problema relacionado', max_length=50)

	def __str__(self):
		return self.relacao

class Chamado(models.Model):
	setor = models.CharField('Setor', max_length=50)
	problema = models.TextField('problema')
	situacao = models.IntegerField('situacao', default=1)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	relacao = models.ForeignKey(ProblemaRelacionado, on_delete=models.CASCADE)
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Chamado

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'apelido', 'email', 'matricula')

class ChamadoForm(ModelForm):
	class Meta:
		model = Chamado
		fields = ('setor', 'relacao', 'problema')

class ComentarioForm(ModelForm):
	class Meta:
		model = Chamado
		fields = ['comentario']
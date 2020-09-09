from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.
def login(request):
	return render(request, 'login.html')

@login_required
def perfil(request):
	return render(request, 'index.html')

def registro(request):
	form = CustomUserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'register.html', contexto)

@login_required
def dados(request,id):
	if request.user.id == id:
		user = CustomUser.objects.get(pk=id)
		form = CustomUserCreationForm(request.POST or None, instance=user)
		if form.is_valid():
			form.save()
			return redirect('perfil')
		contexto = {
			'form': form
		}
	else:
		return redirect('perfil')
	return render(request, 'register.html', contexto)

@login_required
def cadastro(request):
	return render(request, 'registro.html')
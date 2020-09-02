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
	return render(request, 'perfil.html')

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
	user = CustomUser.objects.get(pk=id)
	form = CustomUserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)
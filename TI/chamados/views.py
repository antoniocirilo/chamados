from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ChamadoForm
from .models import CustomUser, Chamado

# Create your views here.
def login(request):
	return render(request, 'login.html')

@login_required
def perfil(request):
	chamados = Chamado.objects.filter(user=request.user).order_by('-id')
	contexto = {
	'lista_chamado': chamados
	}
	return render(request, 'dashboard/chamados.html', contexto)

@login_required
def myCall(request):
	return render(request, 'dashboard/myCall.html')

def registro(request):
	form = CustomUserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registration/register.html', contexto)

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
	return render(request, 'registration/register.html', contexto)

@login_required
def lista_chamados(request):
	chamados = Chamado.objects.filter(user=request.user)
	contexto = {
	'lista_chamado': chamados
	}
	return render(request, 'chamados.html', contexto)

@login_required
def cadastro(request):
	form = ChamadoForm(request.POST or None)
	if form.is_valid():
		chamado = form.save(commit=False)
		chamado.user = request.user
		chamado.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'dashboard/registro.html', contexto)

@login_required
def editar(request,id):
	chamado = Chamado.objects.get(pk=id)
	form = ChamadoForm(request.POST or None, instance=chamado)
	if form.is_valid():
		chamado = form.save(commit=False)
		chamado.user = request.user
		chamado.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

@login_required
def apagar(request,id):
	chamado = Chamado.objects.get(pk=id)
	chamado.delete()
	return redirect('lista_chamados')

@login_required
def usuarios(request):
	user = CustomUser.objects.all()
	contexto = {
	'usuarios': user
	}
	return render(request, 'admin/usuarios.html', contexto)

@login_required
def editaruser(request, id):
	user = CustomUser.objects.get(pk=id)
	form = CustomUserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('usuarios')
	contexto = {
		'form': form
	}
	return render(request, 'registration/register.html', contexto)

def apagaruser(request, id):
	user = CustomUser.objects.get(pk=id)
	user.delete()
	return redirect('usuarios')
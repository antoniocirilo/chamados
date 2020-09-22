from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ChamadoForm
from .models import CustomUser, Chamado, Situacao
from .filters import FiltroChamado

# Create your views here.
def login(request):
	return render(request, 'login.html')

def inicial(request):
	return redirect('login')

@login_required
def perfil(request):
	chamados = Chamado.objects.filter(user=request.user).order_by('-id')
	contexto = {
	'lista_chamado': chamados
	}
	return render(request, 'dashboard/chamados.html', contexto)

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
	return render(request, 'dashboard/registro.html', contexto)

@login_required
def apagar(request,id):
	chamado = Chamado.objects.get(pk=id)
	chamado.delete()
	return redirect('perfil')

@login_required
def adminchamados(request):
	chamado = Chamado.objects.all().order_by('-id')
	meufiltro = FiltroChamado(request.GET, queryset=chamado)
	contexto = {
	'filtro': meufiltro
	}
	return render(request, 'admin/teste-filtro.html', contexto)

@login_required
def resolverchamado(request, id):
	chamado = Chamado.objects.get(pk=id)
	chamado.situacao_id = 2
	chamado.save()
	return redirect('adminchamados')

@login_required
def resolvidochamado(request, id):
	chamado = Chamado.objects.get(pk=id)
	chamado.situacao_id = 3
	chamado.save()
	return redirect('adminchamados')

@login_required
def usuarios(request):
	user = CustomUser.objects.all().order_by('-id')
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
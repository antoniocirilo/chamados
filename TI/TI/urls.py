"""TI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chamados.views import login, perfil, registro, dados, cadastro, lista_chamados, editar, apagar
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('login/', login, name="login"),
    path('',login ),
    path('perfil/', perfil, name="perfil"),
    path('perfil/cadastro/', cadastro, name="cadastro"),
    path('perfil/cadastro/editar/<int:id>/', editar, name="editar"),
    path('perfil/cadastro/apagar/<int:id>/', apagar, name="apagar"),
    path('perfil/chamados/', lista_chamados, name="lista_chamados"),

    #registro
    path('registro/', registro, name='registro'),
    path('dados/<int:id>/', dados, name='dados'),

    #autenticação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

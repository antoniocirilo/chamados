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
from chamados.views import login, perfil, inicial, registro, dados, cadastro, editar, apagar, adminchamados, resolverchamado, resolvidochamado, comentario, usuarios, editaruser, apagaruser, superuser, normaluser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('perfil/', perfil, name="perfil"),
    path('', inicial, name="inicial"),

    #manipulação de chamados
    path('perfil/cadastro/', cadastro, name="cadastro"),
    path('perfil/cadastro/editar/<int:id>/', editar, name="editar"),
    path('perfil/cadastro/apagar/<int:id>/', apagar, name="apagar"),

    #super_usuarios
    path('perfil/chamados/', adminchamados, name="adminchamados"),
    path('perfil/chamados/resolver/<int:id>/', resolverchamado, name="resolverchamado"),
    path('perfil/chamados/resolvido/<int:id>/', resolvidochamado, name="resolvidochamado"),
    path('perfil/chamados/comentario/<int:id>/', comentario, name="comentario"),
    path('perfil/usuarios/', usuarios, name="usuarios"),
    path('perfil/usuarios/editar/<int:id>/', editaruser, name="editaruser"),
    path('perfil/usuarios/apagar/<int:id>/', apagaruser, name="apagaruser"),
    path('perfil/usuarios/super/<int:id>/', superuser, name="superuser"),
    path('perfil/usuarios/normal/<int:id>/', normaluser, name="normaluser"),

    #registro
    path('registro/', registro, name='registro'),
    path('dados/<int:id>/', dados, name='dados'),

    #autenticação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

]

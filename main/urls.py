"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from aluno import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('aluno/',views.aluno_criar,name='aluno_criar'),
    path('aluno/editar/<int:id>/',views.aluno_editar, name='aluno_editar'),
    path('aluno/remover/<int:id>/',views.aluno_remover,name='aluno_remover'),
    path('aluno/listar',views.aluno_listar,name='aluno_listar'),
    path('cidade/listar', views.cidade_listar, name='cidade_listar'),
    path('cidade/criar', views.cidade_criar, name='cidade_criar'),
    path('cidade/editar/<int:id>/', views.cidade_editar, name='cidade_editar'),
    path('cidade/deletar/<int:id>/', views.cidade_deletar, name='cidade_deletar'),
    path('curso/listar', views.curso_listar, name='curso_listar'),
    path('curso/criar', views.curso_criar, name='curso_criar'),
    path('curso/editar/<int:id>/', views.curso_editar, name='curso_editar'),
    path('curso/deletar<int:id>/', views.curso_deletar, name='curso_deletar')


]




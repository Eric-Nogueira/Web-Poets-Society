from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='usuario_criar'),
    path('perfil/', views.perfil, name='perfil'),
    # Faltava a rota do perfil publico: o template perfil-publico.html
    # existia mas nao tinha view nem URL.
    path('<str:username>/', views.perfil_publico, name='perfil_publico'),
]

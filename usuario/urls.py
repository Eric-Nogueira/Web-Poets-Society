from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='usuario_criar'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('deletar/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('perfil/', views.perfil, name='perfil'),
    path('<str:username>/', views.perfil_publico, name='perfil_publico'),
]

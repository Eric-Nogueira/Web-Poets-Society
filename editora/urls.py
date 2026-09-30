from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_editora, name='editora_criar'),
    path('editar/<int:editora_id>/', views.editar_editora, name='editar_editora'),
    path('deletar/<int:editora_id>/', views.deletar_editora, name='deletar_editora'),
]

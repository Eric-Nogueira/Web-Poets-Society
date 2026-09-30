from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_edicao, name='edicao_criar'),
    path('editar/<int:edicao_id>/', views.editar_edicao, name='editar_edicao'),
    path('deletar/<int:edicao_id>/', views.deletar_edicao, name='deletar_edicao'),
]

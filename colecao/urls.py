from django.urls import path

from . import views

app_name = 'colecao'

urlpatterns = [
    path('nova/', views.criar_colecao, name='criar'),
    path('', views.lista_colecoes, name='lista'),
    path('editar/<int:colecao_id>/', views.editar_colecao, name='editar'),
    path('deletar/<int:colecao_id>/', views.deletar_colecao, name='deletar'),
]






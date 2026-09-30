from django.urls import path

from . import views


app_name = 'avaliacao'


urlpatterns = [
    path('register/', views.register_avaliacao,name='criar'),
    path('', views.lista_avaliacoes, name='lista'),
    path('curtir/<int:avaliacao_id>/', views.curtir_avaliacao, name='curtir'),
    path('editar/<int:avaliacao_id>/', views.editar_avaliacao, name='editar'),
    path('deletar/<int:avaliacao_id>/', views.deletar_avaliacao, name='deletar'),
]









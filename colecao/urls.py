from django.urls import path

from . import views

app_name = 'colecao'

urlpatterns = [
    path('nova/', views.criar_colecao, name='criar'),
]

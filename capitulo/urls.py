from django.urls import path

from . import views

app_name = 'capitulo'

urlpatterns = [
    path('novo/', views.criar_capitulo, name='criar'),
    path('livro/<int:livro_id>/', views.lista_capitulos, name='lista'),
]

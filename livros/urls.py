from django.urls import path

from . import views

app_name = 'livros'

# Este arquivo tinha, colado por engano, uma copia inteira do urls.py do
# projeto (com admin/, home/, includes...). Isso criava rotas duplicadas e
# imports desnecessarios. Ficou so o que pertence ao app livros.
urlpatterns = [
    path('', views.lista_livros, name='lista'),
    path('novo/', views.criar_livro, name='criar'),
]

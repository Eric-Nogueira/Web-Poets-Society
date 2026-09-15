from django.urls import path

from . import views

app_name = 'capitulo'

urlpatterns = [
    path('novo/', views.criar_capitulo, name='criar'),
]

"""
URL configuration for webpoetssociety project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView

import usuario.views as usuario_views

urlpatterns = [
    # A raiz "/" nao existia: abrir localhost:8000 dava 404.
    path('', RedirectView.as_view(pattern_name='home', permanent=False)),

    path('admin/', admin.site.urls),
    path('home/', usuario_views.home, name='home'),

    # Login/logout nao existiam, mas varios links apontavam para "login.html".
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='form/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('usuario/', include('usuario.urls')),
    path('editora/', include('editora.urls')),
    path('edicao/', include('edicao.urls')),
    path('livros/', include('livros.urls')),
    path('colecao/', include('colecao.urls')),
    path('capitulo/', include('capitulo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

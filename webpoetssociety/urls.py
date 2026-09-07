"""
URL configuration for webpoetssociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, static
from django.contrib import admin
from django.urls import path

import usuario.views as usuario_views
from webpoetssociety import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', usuario_views.home, name='home'),
    path('usuario/', include('usuario.urls')),
    path('editora/', include('editora.urls')),
    path('edicao/', include('edicao.urls')),
]

"""
Django settings for webpoetssociety project.

Para mais informacoes:
https://docs.djangoproject.com/en/6.0/topics/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ea*h=^n+vj2#y1xeplppz#w9c&&u)y9r_b5n)w*rlh9^9w&5t^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps criados

    'livros.apps.LivrosConfig',
    'editora.apps.EditoraConfig',
    'edicao.apps.EdicaoConfig',
    'usuario.apps.UsuarioConfig',
    'avaliacao.apps.AvaliacaoConfig',
    'colecao.apps.ColecaoConfig',
    'capitulo.apps.CapituloConfig',
    'livro_colecao.apps.LivroColecaoConfig',
    'livro_usuario.apps.LivroUsuarioConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webpoetssociety.urls'

# Havia DOIS blocos TEMPLATES neste arquivo; o de cima era sobrescrito
# silenciosamente pelo de baixo. Agora existe um so, com a pasta template/.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webpoetssociety.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Bahia'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Arquivos enviados pelo usuario (o PDF da Edicao, por exemplo).
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Autenticacao
# Antes LOGIN_URL apontava para a tela de CADASTRO, entao quem nao estava
# logado caia em "criar conta" em vez de "entrar".
from django.contrib.messages import constants as message_constants

# A tag padrao do Django para erro e 'error', que nao existe no Bootstrap.
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

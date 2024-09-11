from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'. / Construir rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings (unsuitable for production) / Configuraciones de inicio rápido (no aptas para producción)
SECRET_KEY = "django-insecure-CHANGE_ME"
DEBUG = True
ALLOWED_HOSTS = []

# Application definition / Definición de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'contabilidad',
    'inventarios',
    'documentos',
    'cuentasporcobrar',
    # 'cuentasporpagar',
    # 'activosfijos',
    # 'presupuesto',
    # 'ordenpedido',
    # 'ordencompra',
    # 'ventas',
    # 'gestionrecaudo',
    # 'gestionventas',
    # 'interfaces',
    'tesoreria',
    # 'nomina'
    # 'transporte',
    # 'produccion',
    # 'pos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "main_system.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

WSGI_APPLICATION = "main_system.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "123456789",
        "HOST": "localhost",
        "PORT": "5432",
        "OPTIONS": {
            "options": "-c client_encoding=UTF8",
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Default language / Idioma por defecto
LANGUAGE_CODE = "en-us"

# Time zone / Zona horaria
TIME_ZONE = "UTC"

# Enable internationalization / Activar internacionalización
USE_I18N = True

# Enable localization / Activar localización
USE_L10N = True

# Enable time zone / Activar zona horaria
USE_TZ = True

# Static files (CSS, JavaScript, Images) / Archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = "static/"

# Field type auto increment by default / Tipo de campo automático por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Supported languages / Idiomas soportados
LANGUAGES = [
    ("en", _("English")),
    ("es", _("Spanish")),
    ("pt", _("Portuguese")),
]

# Traslation files location / Ubicación de los archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / "locale",
]

from datetime import timedelta
SIGNING_KEY = 'registroAppSOAPServiceClienteServidorIISSQLServerExpressMicosoftAzureMMS'

CORS_ALLOW_ALL_ORIGINS = True
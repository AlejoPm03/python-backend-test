"""
Django settings for agro_test project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# System lib
import os

#  Path lib
from pathlib import Path

# Envs
import environ

# Creates env parser
env = environ.Env(
	PROJECT_SECRET_KEY = (str, os.getenv("PROJECT_SECRET_KEY")),
	PROJECT_ENV = (str, os.getenv("PROJECT_ENV")),
)

# Load environments variables
env = environ.Env()
environ.Env.read_env()

# Starts with default server mode with debug false
DEBUG = False

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4$+o&0jsbv2huaeowbvne3!jn@r!s&=xd_et9s!q(#*we9v#ne'

# SECURITY WARNING: don"t run with debug turned on in production!
# If the project is in dev mode, set debug to true
if env("PROJECT_ENV") == "dev":
	DEBUG = True

# Open to all hosts request this API
ALLOWED_HOSTS = [
	"*",
]

# Open to all hosts using CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# CORS
	"corsheaders",
	# Rest framework
	"rest_framework",
	"rest_framework_api_key",
	"rest_framework.authtoken",
	"django_extensions",
	# Swagger docs
	"drf_yasg",
	# Apps
	"apps.user",
	"apps.producer",
]

MIDDLEWARE = [
	# CORS
	"corsheaders.middleware.CorsMiddleware",
	# Django
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agro_test.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		"DIRS": [ os.path.join(BASE_DIR, "templates/") ],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'agro_test.wsgi.application'

AUTH_USER_MODEL="user.User"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": env("POSTGRES_DB"),
		"USER": env("POSTGRES_USER"),
		"PASSWORD": env("POSTGRES_PASSWORD"),
		"HOST": env("POSTGRES_HOST"),
		"PORT": env("POSTGRES_PORT"),
	},
	"memory": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": ":memory:",
	},
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rest framework configuration

REST_FRAMEWORK = {
	"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
	"PAGE_SIZE": 50,
	"DEFAULT_AUTHENTICATION_CLASSES": [
		"rest_framework.authentication.TokenAuthentication",
		"rest_framework.authentication.SessionAuthentication",
	],
}

# Swagger configuration
SWAGGER_SETTINGS = {
	"USE_SESSION_AUTH": False
}

GRAPH_MODELS ={
	"all_applications": True,
	"graph_models": True,
}

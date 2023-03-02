"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = [
    ".elasticbeanstalk.com",
    "localhost",
    "127.0.0.1",
]


# Application definition

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_summernote",
    "corsheaders",
    "storages",
]

CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "concerts.apps.ConcertsConfig",
    "common.apps.CommonConfig",
    "edus.apps.EdusConfig",
    "notices.apps.NoticesConfig",
    "qnas.apps.QnasConfig",
]

SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if not DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": env.str("RDS_HOST"),
            "NAME": env.str("RDS_NAME"),
            "USER": env.str("RDS_USER"),
            "PASSWORD": env.str("RDS_PASSWORD"),
            "PORT": "5432",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

# cors
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://artshelter.co.kr",
    "http://www.artshelter.co.kr",
    "https://artshelter.co.kr",
    "https://www.artshelter.co.kr",
]
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://artshelter.co.kr",
    "http://www.artshelter.co.kr",
    "https://artshelter.co.kr",
    "https://www.artshelter.co.kr",
]
CORS_ALLOW_CREDENTIALS = True


# summernote
X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_CONFIG = {
    "summernote": {
        "height": "700px",
    },
    "attachment_absolute_uri": True,
    "disalbe_class": False,
}

# DRF Pagination
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "common.paginators.CustomResultsSetPagination",
    "PAGE_SIZE": 100,
}


# if not DEBUG:
#     AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
#     AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
#     AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
#     AWS_S3_REGION_NAME = "ap-northeast-2"
#     AWS_DEFAULT_ACL = "public-read"
#     AWS_S3_CUSTOM_DOMAIN = (
#         f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
#     )
#     STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
#     DEFAULT_FILE_STORAGE = "config.custom_storages.UploadStorage"
#     STATICFILES_STORAGE = "config.custom_storages.StaticStorage"

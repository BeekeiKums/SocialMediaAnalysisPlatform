"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv  # Load environment variables
from neo4j import GraphDatabase
from neomodel import config

# Load .env file
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = os.path.join(BASE_DIR, "myproject", ".env")
load_dotenv(ENV_PATH)

# Read from Render's environment variables (fallback to defaults for local development)
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://fa57a3a3.databases.neo4j.io")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "your-default-password")

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "*$3b_xkx*_7-c2bww-rh_sg5$^6-8kwfainfk&*a2_!@u74a06")

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://aunggyi:aung754826@cluster0.pim44.mongodb.net/yeryer")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "yeryer")

DEBUG=False


ALLOWED_HOSTS = ["*"]  # Change this to your domain or Render URL in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'main' / 'templates',
        ],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database Configuration (MongoDB)
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': MONGO_DB_NAME,
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': MONGO_URI,
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}

# -------------------------- Neo4j Configuration -------------------------------






# ----------------------------End of Neo4j Configuration ------------------------

# Maximum size for file uploads (e.g., 100MB)
DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URL
LOGIN_URL = '/admin_login/'  # Replace with actual login path

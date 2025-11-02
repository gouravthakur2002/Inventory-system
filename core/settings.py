"""
Django settings for core project (works for both local and Render deployment)
"""

import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Secret key handling (secure for Render)
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "qyu(9l9v%^+r(vt#ecf+36#lis516#3bo5@bo-rd*d%a=!%8#!"  # fallback for local
)

# 🧩 Detect environment (Render sets 'RENDER' variable)
DEBUG = os.environ.get("DEBUG", "True") == "True"

# ✅ Allowed hosts for both local + Render
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'inventory-system-86yz.onrender.com'  # your Render domain
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'homepage',
    'inventory',
    'transactions',

    # Third-party apps
    'widget_tweaks',
    'crispy_forms',
    'login_required',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Required for Render static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'login_required.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'core.wsgi.application'

# ✅ Database (SQLite for both local and Render small apps)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ Static files (CSS, JS, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # local use
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')   # Render collects here

# ✅ WhiteNoise configuration for Render
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ✅ Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# ✅ Login settings
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [
    'login',
    'logout',
    'about',
]

# ✅ Render-specific configuration
if os.environ.get('RENDER', None):
    ALLOWED_HOSTS.append(os.environ.get('RENDER_EXTERNAL_HOSTNAME'))

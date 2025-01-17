import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mo#v22=*#kd-p^bazqk*wg5%bm(=bfre@#t0d^1+pe)7@$o11u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'rest_framework',
    'corsheaders',
    'goodweather',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

# To use allauth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

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

ROOT_URLCONF = 'pcpo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'goodweather/templates')],
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

WSGI_APPLICATION = 'pcpo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SQLite 3 DB

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'goodweather/static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,   # Отключаем все средства диагностики по умолчанию
    # Форматировщик - задает формат, в котором представляется сообщение, отправленное подсистемой диагностики
    'formatters': {
        # Форматировщик с именем simple
        'simple': {
            # Строка для формирования сообщения (в скобках атрибуты класса LogRecord из модуля logging)
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
            # Строка для формирования даты
            'datefmt': '%Y.%m.%d %H.%M.%S'
        },
    },
    # Фильтры
    'filters': {
        # Выводит сообщения только в эксплуатационном режиме
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        # Выводит сообщения только в отладочном режиме
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    # Обработчики
    'handlers': {
        # Будет сохранять в файл сообщения любого уровня, посредством
        # форматировщика simple. При превышении файлом размера в 1Мб будет создан
        # новый файл. Всего будет храниться 10 файлов с логами (одновременно)
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs.log'),
            'maxBytes': 1048576,
            'backupCount': 2,
            'formatter': 'simple',
        },
    },
    # Регистраторы
    'loggers': {
        'django': {
            'handlers': ['file'],
        },
    }
}

# Auth

# Login
LOGIN_REDIRECT_URL = '/home/7/'
LOGIN_URL = 'accounts/login/'

# Logout
LOGOUT_URL = 'accounts/logout/'
LOGOUT_REDIRECT_URL = 'accounts/login/'

#ACCOUNT_EMAIL_REQUIRED = True
SITE_ID = 1
# Should be "mandatory", "optional" or "none"
ACCOUNT_EMAIL_VERIFICATION = "none"

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
insecure_key = 'insecure'
SECRET_KEY = os.getenv('SECRET_KEY', insecure_key)

DEBUG = SECRET_KEY == insecure_key

ALLOWED_HOSTS = ['*']

DATAPUNT_API_URL = os.getenv('DATAPUNT_API_URL', 'https://api.data.amsterdam.nl/')

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'django_filters',
    'django_extensions',

    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
]

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'authorization_django.authorization_middleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DUMP_DIR = 'mks-dump'

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

REST_FRAMEWORK = dict(
    PAGE_SIZE=100,

    MAX_PAGINATE_BY=100,

    UNAUTHENTICATED_USER=None,
    UNAUTHENTICATED_TOKE=None,

    DEFAULT_AUTHENTICATION_CLASSES=(
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),

    DEFAULT_RENDERER_CLASSES=(
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    DEFAULT_FILTER_BACKENDS=(
        'rest_framework.filters.DjangoFilterBackend',
        # 'rest_framework.filters.OrderingFilter',

    ),
    COERCE_DECIMAL_TO_STRING=True,
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },

    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },

    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
        },

        # Log all unhandled exceptions
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },

    },
}

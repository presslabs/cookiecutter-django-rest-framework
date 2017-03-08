import os
from django.utils.log import DEFAULT_LOGGING

# Project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


DATA_DIR = os.getenv('{{ cookiecutter.project_env_prefix }}_DATA_DIR', PROJECT_ROOT)
WEBROOT_DIR = os.getenv('{{ cookiecutter.project_env_prefix }}_WEBROOT_DIR', os.path.join(PROJECT_ROOT, 'webroot/'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('{{ cookiecutter.project_env_prefix }}_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('{{ cookiecutter.project_env_prefix }}_DEBUG_IN_PRODUCTION', 'False') == 'True'

ALLOWED_HOSTS = list(filter(lambda x: x, map(lambda x: x.strip(),
                                             os.getenv('{{ cookiecutter.project_env_prefix }}_ALLOWED_HOSTS', '').split(','))))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'pl_sugar',  # must be inserted before admin so that we can override some admin templates
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'rest_framework',
    'rest_framework_swagger',
    '{{ cookiecutter.project_slug }}',
]

ROOT_URLCONF = 'django_project.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates/')],
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

WSGI_APPLICATION = 'django_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('{{ cookiecutter.project_env_prefix }}_DB_ENGINE',
                            'django.db.backends.sqlite3'),
        'USER': os.getenv('{{ cookiecutter.project_env_prefix }}_DB_USER', '{{ cookiecutter.project_slug }}'),
        'PASSWORD': os.getenv('{{ cookiecutter.project_env_prefix }}_DB_PASSWORD', 'password'),
        'HOST': os.getenv('{{ cookiecutter.project_env_prefix }}_DB_HOST', ''),
        'PORT': os.getenv('{{ cookiecutter.project_env_prefix }}_DB_PORT', ''),
    }
}

if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
    DATABASES['default']['NAME'] = os.getenv('{{ cookiecutter.project_env_prefix }}_DB_PATH',
                                             os.path.join(DATA_DIR, 'db.sqlite3'))
else:
    DATABASES['default']['NAME'] = os.getenv('{{ cookiecutter.project_env_prefix }}_DB_NAME', '{{ cookiecutter.project_slug }}')

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

LOGIN_URL = '/_auth/login/google-oauth2/'

# Social auth
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_ADMIN_EMAILS = [
    'calin@presslabs.com',
    'mile@presslabs.com',
    'pedro@presslabs.com',
]
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['presslabs.com']
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'profile',
]

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social_core.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social_core.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social_core.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',

    # Set superuser and is_staff
    'pl_sugar.social_auth.pipeline.set_admin_perms',

    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social_core.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('{{ cookiecutter.project_env_prefix }}_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('{{ cookiecutter.project_env_prefix }}_GOOGLE_OAUTH2_SECRET')

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = os.getenv('{{ cookiecutter.project_env_prefix }}_STATIC_URL', '/static/')
STATIC_ROOT = os.path.join(WEBROOT_DIR, 'static/')

# CELERY
BROKER_URL = os.getenv('BROKER_URL', 'redis://localhost:6379/1')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/2')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

REST_FRAMEWORK = {
    'PAGE_SIZE': 50,
    'DEFAULT_PAGINATION_CLASS': 'pl_sugar.rest_framework.pagination.LinkHeaderPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# configure logging
LOG_LEVEL = os.getenv('{{ cookiecutter.project_env_prefix }}_LOG_LEVEL', 'INFO')
LOGGING = DEFAULT_LOGGING.copy()
LOGGING['loggers']['django']['level'] = LOG_LEVEL
LOGGING['loggers']['celery'] = {
    'handlers': ['console'],
    'level': LOG_LEVEL
}


if os.getenv('{{ cookiecutter.project_env_prefix }}_SENTRY_DSN', None):
    import raven
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')
    RAVEN_CONFIG = {
        'dsn': os.getenv('{{ cookiecutter.project_env_prefix }}_SENTRY_DSN'),
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
        'environment': os.getenv('ENV_NAME', None),
    }

    # Sentry logging with celery is a real pain in the ass
    # https://github.com/getsentry/sentry/issues/4565
    CELERYD_HIJACK_ROOT_LOGGER = False
    LOGGING['handlers']['sentry'] = {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
    }
    LOGGING['loggers']['celery.task'] = {
        'level': LOG_LEVEL,
        'handlers': ['console', 'sentry']
    }

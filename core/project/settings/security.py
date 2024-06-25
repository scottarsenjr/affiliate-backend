DEBUG = True
SECRET_KEY = NotImplemented

INTERNAL_IPS = [
    '127.0.0.1',
]

LOGIN_URL = '/admin'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

ALLOWED_HOSTS = ['*']

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
]
CORS_ALLOW_CREDENTIALS = True

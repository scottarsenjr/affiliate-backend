import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path.joinpath(Path(__file__).parent.parent.parent.parent.resolve(), '.env.local')
print(dotenv_path)
load_dotenv(dotenv_path)

DEBUG = True
SECRET_KEY = 'django-insecure-=okvqjswarmd2ymc#jxqo-t7a(9qpvk-dk8v#9$t^c(dlbmw)b'
STATIC_ROOT = '/opt/project/static/'
MEDIA_ROOT = './media/'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/0',
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'},
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 600,
    }
}

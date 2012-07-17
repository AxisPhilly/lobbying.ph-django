from project.settings_common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# CACHE
from memcacheify import memcacheify

CACHES = memcacheify()

MIDDLEWARE_CLASSES += (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATIC_URL = 'https://s3.amazonaws.com/lobbyingph/'
STATIC_URL = 'http://commondatastorage.googleapis.com/lobbyingph/'

AWS_ACCESS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME = 'lobbyingph'

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
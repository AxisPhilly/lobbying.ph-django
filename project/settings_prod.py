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

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'https://s3.amazonaws.com/lobbyingph/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_ACCESS_KEY_ID = os.environ['AWS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME = 'lobbyingph'
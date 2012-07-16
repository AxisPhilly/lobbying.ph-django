from project.settings_common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

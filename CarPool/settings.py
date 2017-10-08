
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'op7*^-7$x#)y9&^3ode$a#ane+7ee!r3o9qphftj#m&1x3xdqy'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WebUI',
    'south',
    'CarPool',
    'django.contrib.admin',
    'jsonify'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CarPool.urls'

WSGI_APPLICATION = 'CarPool.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'WebUI','static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)
API_KEY = 'AIzaSyAx9s1E5g-LEUnBjRk2VrRT78bCRcbD3EM'
AUTH_USER_MODEL = 'WebUI.CustomUser'
LOGIN_URL = '/welcome/'
LOGIN_REDIRECT_URL = '/home/'

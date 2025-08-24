from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'yourapp.herokuapp.com']

# Database for production
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# Security
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

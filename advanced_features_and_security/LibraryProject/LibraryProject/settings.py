INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',   # your app with CustomUser
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']  # set your hosts accordingly

# Security Headers
SECURE_BROWSER_XSS_FILTER = True  # Enables browser XSS filter
X_FRAME_OPTIONS = 'DENY'           # Prevent clickjacking by disallowing iframes
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing

# Secure cookies
CSRF_COOKIE_SECURE = True      # CSRF cookie only sent over HTTPS
SESSION_COOKIE_SECURE = True   # Session cookie only sent over HTTPS

# Recommended: HTTPS redirect (if HTTPS is setup)
SECURE_SSL_REDIRECT = True

# Additional security settings (optional but recommended)
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Middleware should include security middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # other middleware...
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...
]

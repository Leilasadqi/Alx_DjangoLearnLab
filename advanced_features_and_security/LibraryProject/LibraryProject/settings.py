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
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Prevent site from being embedded in frames (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME sniffing the content type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser's XSS filtering
SECURE_BROWSER_XSS_FILTER = True
"""
Security Settings for HTTPS enforcement:

- SECURE_SSL_REDIRECT forces all HTTP traffic to redirect to HTTPS.
- SECURE_HSTS_SECONDS enables HTTP Strict Transport Security for 1 year, telling browsers to always use HTTPS.
- SECURE_HSTS_INCLUDE_SUBDOMAINS includes all subdomains in HSTS.
- SECURE_HSTS_PRELOAD allows site to be included in browser preload lists.
- SESSION_COOKIE_SECURE & CSRF_COOKIE_SECURE ensure cookies are only sent over secure HTTPS connections.
- X_FRAME_OPTIONS prevents clickjacking by disallowing the site to be embedded in frames.
- SECURE_CONTENT_TYPE_NOSNIFF stops browsers from MIME sniffing which can cause security issues.
- SECURE_BROWSER_XSS_FILTER enables browser XSS protection.
"""

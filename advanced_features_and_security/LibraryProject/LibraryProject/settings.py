INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',    # or your app name like 'accounts'
    'accounts',     # add your custom user app here
]

AUTH_USER_MODEL = 'accounts.CustomUser'  # <-- outside INSTALLED_APPS

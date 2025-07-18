from pathlib import Path
import os
import cloudinary

# ========== BASE DIRECTORY ==========
BASE_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "media")

# ========== SECURITY ==========
SECRET_KEY = "d9t&8z1!v@p#q7xw_2h4fj+sk6mz$yl^ncr0eogb5u9a!dt7q1"
DEBUG = False
ALLOWED_HOSTS = ['*']

# ========== APPLICATIONS ==========
INSTALLED_APPS = [
    # Cloudinary apps
    'cloudinary',
    'cloudinary_storage',

    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your app
    'myapp',
]

# ========== MIDDLEWARE ==========
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static file handling
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========== URLS / WSGI ==========
ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

# ========== TEMPLATES ==========
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMP_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========== DATABASE ==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========== PASSWORD VALIDATORS ==========
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========== INTERNATIONALIZATION ==========
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ========== STATIC FILES ==========
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ========== MEDIA FILES (CLOUDINARY) ==========
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ========== CLOUDINARY CONFIG ==========
cloudinary.config(
    cloud_name="drswwrvip",
    api_key="917372382965659",
    api_secret="mn5IKt02cZCalb_-NotfuoA1H8Q"
)

# ========== PRIMARY KEY FIELD TYPE ==========
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional: Print Cloudinary version for debugging
# print("Cloudinary version:", cloudinary.__version__)

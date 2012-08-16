# Django settings for xmlserver project.
#DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_NAME = 'xmlserver'
DATABASES = {
    'default': {
        'ENGINE'  : DATABASE_ENGINE, # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME'    : DATABASE_NAME,                      # Or path to database file if using sqlite3.
        'USER'    : '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }    
}

DEBUG = True

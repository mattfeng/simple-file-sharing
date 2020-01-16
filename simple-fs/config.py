import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2
CSRF_ENABLED = True

CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY', 'secret_session_key')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret')

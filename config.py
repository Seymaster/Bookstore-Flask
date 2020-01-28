DEBUG = True
#Defining the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MONGOURI = 'mongodb://localhost:27017/testingdb'
# Enabling protection against cross-site forgery REQUIRED
CSRF_ENABLED = True
CSRF_SECRET_KEY = 'codded'
SECRET_KEY = 'password'
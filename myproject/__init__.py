from flask import Flask
from mongoengine import connect

app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
connect(host=app.config['MONGOURI'])
app.config['CSRF_ENABLED']
app.config['CSRF_SECRET_KEY']
app.config['SECRET_KEY']
from myproject.reg_modules.views import reg_blu
from myproject.bookstore.views import book_bp
app.register_blueprint(reg_blu)
app.register_blueprint(book_bp)
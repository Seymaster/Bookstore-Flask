from flask import Blueprint,render_template,render_template,redirect,request,url_for
from myproject.bookstore.models import Books
from myproject.bookstore.forms import RegisterBooks
from bson.objectid import ObjectId

book_bp = Blueprint('book',__name__,url_prefix='/book')
@book_bp.route('/')
def index():
    # books = Books.objects()
    form = RegisterBooks()
    books = Books.objects()
    return render_template('index.html',form = form,books = books )
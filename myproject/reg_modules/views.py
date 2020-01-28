from flask import Blueprint,request,redirect,render_template,url_for,flash
import bcrypt
from myproject.reg_modules.forms import Register,Login
from myproject.reg_modules.models import Voters
from pymongo.errors import ServerSelectionTimeoutError,DuplicateKeyError
from mongoengine.errors import FieldDoesNotExist,ValidationError,NotUniqueError,NotRegistered
from jinja2 import TemplateError,TemplatesNotFound,UndefinedError,TemplateSyntaxError

reg_blu = Blueprint('vreg',__name__,url_prefix='/vreg')

@reg_blu.route('/')
def index():
    return redirect(url_for('vreg.signup'))

@reg_blu.route('/signup', methods = ['GET','POST'])
def signup():
    form = Register()
    message = None
    if request.method == 'POST':
        if form.validate == False:
            flash('All fields are required')
            return render_template('/signup.html',form = form, message = message)
        else:
            try:
                voters = Voters()
                hpassword = bcrypt.hashpw(request.form['password'].encode("utf-8"),bcrypt.gensalt())
                data = Voters(firstname = request.form['firstname'],
                                lastname = request.form['lastname'],
                                gender   = request.form['gender'],
                                age      = request.form['age'],
                                username = request.form['username'],
                                email    = request.form['email'],
                                password = hpassword)
                            # c_password = hconpassword)
                data.save()
                return render_template('/thank_you.html')
            except DuplicateKeyError as de:
                message = f"{de} error"
                return "This username already exist"+ message 
            except ValidationError as ve:
                return f"Enter a valid input{ve}"
            except ServerSelectionTimeoutError as se:
                return f"Check server {se}"
            except Exception as e:
                return f"{e} Error occur"

    else:
        return render_template('signup.html', form = form)

@reg_blu.route('/thank_you')
def thank_you():
    username = request.form['username']
    return render_template('/thank_you', username = username)  

@reg_blu.route('/login',methods =['POST','GET'])
def login():
    form = Login()
    if request.method == 'POST':
        username = request.form['username']
        voters = Voters.objects( username = username ).first()
        if voters:
            depw = request.form['password'].encode("utf-8")
            if bcrypt.checkpw(depw,voters['password'].encode("utf-8")):
                return redirect('/book')
            else:
                message = "Invalid Credentials"
                return render_template('/login.html',form = form, message = message )
        else:
            return "Invalid credentials "
    else:
        return render_template('/login.html',form = form)    
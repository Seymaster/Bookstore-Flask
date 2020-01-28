from flask_wtf import FlaskForm
from wtforms import TextAreaField,IntegerField,TextField,SubmitField,DateField,RadioField,SelectField,PasswordField
from wtforms import validators,ValidationError

class Register(FlaskForm):
    firstname  = TextField("First Name ",[validators.Required("Please enter your firstname ")])
    lastname   = TextField("Last Name ",[validators.Required("Please enter your lastname ")])
    gender     = SelectField("Sex ",[validators.Required("Whats your gender ")],choices=[('boy','male'),('girl','female')])
    age        = IntegerField("Age ",[validators.Required("Specify your age ")])
    username   = TextField("Username ",[validators.Required("Please choose a unique username ")])
    email      = TextField("Email ",[validators.Required("Please enter your email "),
                validators.Email("Please enter a valid e-mail address ")])
    password   = PasswordField("Password",[validators.Required("Please enter your password")])
    # c_password = PasswordField("Confirm Password",[validators.Required("Please confirm your password")])
    submit= SubmitField("Register")

class Login(FlaskForm):
    username = TextField("Username",[validators.Required("Please enter your username ")])
    password = PasswordField("Password",[validators.Required("Please enter your password ")])
    submit = SubmitField("Login")

from flask_wtf import FlaskForm
from wtforms import TextAreaField,IntegerField,TextField,SubmitField,DateField,RadioField,SelectField,PasswordField
from wtforms import validators,ValidationError

class RegisterBooks(FlaskForm):
    title = TextField("Book Title ",[validators.Required()])
    author = TextField("Author ",[validators.Required()])
    description = SelectField("Genre ",[validators.Required], choices=[('comedy','Comedy'),
                                                                      ('science','Science'),
                                                                      ('Tech', 'Technology'),
                                                                      ('market','Marketing'),
                                                                      ('business', 'Business'),
                                                                      ('Motivational', 'Motivational'),
                                                                      ('Adventure', 'Adventure'),
                                                                      ('Romance', 'Romance')])
    price = IntegerField("Price ",[validators.required()])
    year  = IntegerField("Year of Production",[validators.Required()])
    quantity = IntegerField("Quantity in Stock",[validators.Required()])
    submit = SubmitField("Register")
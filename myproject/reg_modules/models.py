import mongoengine as me
import datetime

class Voters(me.Document):
    firstname = me.StringField(required = True,max_length=20)
    lastname  = me.StringField(required = True,max_length=20)
    gender    = me.StringField(required= True)
    age       = me.IntField(required=True, max_value=99)
    username  = me.StringField(required = True, max_length=20, unique=True)
    email     = me.EmailField(required= True, max_length=20, unique=True)
    password  = me.StringField(required=True)
    # Conpassword= me.BinaryField(required=True)
    date_joined = me.DateTimeField(default=datetime.datetime.utcnow)
    
    
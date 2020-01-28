import mongoengine as medb
import datetime

class Books(medb.Document):
    title = medb.StringField(required=True, max_length=200)
    author = medb.StringField(required=True,max_length=150)
    description = medb.StringField(required=True)
    price = medb.IntField(required=True)
    year = medb.IntField(required=True)
    quantity = medb.IntField(required=True, default=0)
    date_created = medb.DateField(default=datetime.datetime.utcnow)
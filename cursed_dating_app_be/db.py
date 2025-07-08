from mongoengine import Document, StringField, IntField

class User(Document):
    name = StringField(required=True)
    age = IntField()

users = User.objects.all()
console.log(users)
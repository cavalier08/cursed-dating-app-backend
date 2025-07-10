# db.py
# Contains API endpoints to work with database

from mongoengine import Document, StringField
from rest_framework.decorators import api_view
from rest_framework.response import Response

class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)


@api_view(['POST'])
def signup(request):   # /signup/
    # Check if username is already taken
    if (len(User.objects(username = request.data['username'])) != 0):
        return Response({
            "success": False,
            "error": "Username " + request.data['username'] + " was already taken."
        })
    # If not, create a new User and save it to the users table
    User(name=request.data['name'], username=request.data['username'],
                    password=request.data['password']).save()
    return Response({"success": True})


@api_view(['POST'])
def login(request):   # /login/
    # Get users whose username matches the requested username
    possibleUser = list(User.objects(username = request.data['username']))
    if (len(possibleUser) == 0):  # no user with requested username
        return Response({
            "success": False,
            "error": "Username " + request.data['username'] + " not found."
        })
    currentUser = possibleUser[0]
    # Check password
    if (request.data['password'] != currentUser.password):
        return Response({
            "success": False,
            "error": "Incorrect password."
        })
    return Response({"success": True})  # successful login

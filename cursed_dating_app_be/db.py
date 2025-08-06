# db.py
# Contains API endpoints to work with database

from mongoengine import Document, StringField, ListField
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from django.middleware.csrf import get_token


class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)

class Ranking(Document):
    username = StringField(required=True)
    rankings = ListField(required=True)


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
    return Response({
        "success": True,
        'token': request.session.session_key,
       # 'csrf_token': get_token(request),
        'user': {
            #'email': request.user.email,
            'username': request.user.username
        }})  # successful login chantal also added some other spicy user info


@api_view(['POST'])
def getUser(request):   # /getuser/
    # Get the given user and send their info
    user = list(User.objects(username = request.data['username']))[0]
    return Response({
        "name": user.name,
        "username": user.username
    })


@api_view(['POST'])
def randomUser(request):   # /random/
    if (request.data['username'] == ''):
        return Response({
            "success": False,
            "error": "No username given."
        })
    # Get all users except the given user
    user = random.choice(list(User.objects(username__ne=request.data['username'])))
    # Send a random user
    return Response({
        "success": True,
        "name": user.name,
        "username": user.username
    })


@api_view(['POST'])
def rank(request):   # /rank/
    # Get users whose username matches the requested username
    possibleUser = list(User.objects(username = request.data['thisUsername']))
    if (len(possibleUser) == 0):  # no user with requested username
        return Response({
            "success": False,
            "error": "Username " + request.data['username'] + " not found."
        })
    currentUser = possibleUser[0]
    rankingList = list(Ranking.objects(username = currentUser.username))[0]
    # Save the ranking to the database - TO BE IMPLEMENTED
    return Response({"success": False})  # (currently unsuccessful) rank

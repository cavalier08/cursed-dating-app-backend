# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token

@api_view(['GET'])
def example_endpoint(request):
    return Response({"message": "Hello from Django!"})

@login_required
def get_session(request):
    return JsonResponse({
        'token': request.session.session_key,
        'csrf_token': get_token(request),
        'user': {
            'email': request.user.email,
            'username': request.user.username
        }
    })
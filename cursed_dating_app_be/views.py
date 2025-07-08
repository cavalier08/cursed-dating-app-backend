# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def example_endpoint(request):
    return Response({"message": "Hello from Django!"})
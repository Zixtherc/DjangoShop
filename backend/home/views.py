from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def render_home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def home_page(request):
    return Response({
        'isAuthenticated': request.user.is_authenticated
    })
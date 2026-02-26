from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from ..api.serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many= True)
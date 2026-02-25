from django.urls import path
from .views import render_products

urlpatterns = [
    path(route='products/', view=render_products),
]
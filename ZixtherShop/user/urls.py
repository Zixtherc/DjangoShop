from django.urls import path
from .views import render_login, render_registration

urlpatterns = [
    path(route= 'login/', view=render_login),
    path(route='registration/', view=render_registration)
]
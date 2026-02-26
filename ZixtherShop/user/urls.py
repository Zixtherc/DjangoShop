from django.urls import path
from .views import render_login, render_registration, render_logout

urlpatterns = [
    path(route= 'login/', view=render_login),
    path(route='registration/', view=render_registration),
    path(route='logout/', view=render_logout)
]
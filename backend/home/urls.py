from django.urls import path
from .views import render_home, home_page

urlpatterns = [
    path('', render_home, name='index'), 

    path('api/auth-status/', home_page, name='auth_status'),
]
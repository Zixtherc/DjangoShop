from django.urls import path
from .views import  home_page

urlpatterns = [
    path('api/home/', home_page, name='auth_status'),
]
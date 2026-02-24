from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.
def render_registration(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            username = request.POST.get('username')
            p_number = request.POST.get('number')
            email = request.POST.get('email')

            if not all([username,password,confirm_password,email,p_number]):
                return render(request=request, template_name='user/registration.html')
        
            user = User.objects.create_user(
                username=username,
                password=password,
                phone_number=p_number,
                email=email)
            return redirect('login')
        
        else:
            return render(request=request, template_name='user/registration.html', context={"error": "Password does not match"})
        
    return render(request= request, template_name='user/registration.html')

def render_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(request=request,username=username,password=password,email=email)
        if user is not None:
            login(request=request,user=user)
            return redirect('home')
        else:
            return render(request=request,template_name='user/login.html', context={'error': 'Incorrect login, password or email'})
    return render(request=request,template_name='user/login.html')
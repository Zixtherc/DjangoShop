from django.shortcuts import render

# Create your views here.
def render_registration(request):
    return render(request= request, template_name='user/registration.html')

def render_login(request):
    return render(request=request,template_name='user/login.html')
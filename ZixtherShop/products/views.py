from django.shortcuts import render

# Create your views here.
def render_products(request):
    return render(request=request,template_name='products/products.html')
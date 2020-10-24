from django.shortcuts import render
from products.models import Product

def main(request):
    products = Product.objects.all()[0:8]
    return render(request, 'index.html', {"products":products})
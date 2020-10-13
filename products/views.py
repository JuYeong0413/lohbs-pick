from django.shortcuts import render
from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products':products})

def search(request):
    query = request.GET.get('query')
    search_products = Product.objects.filter(name__contains=query)
    return render(request, 'products/search.html', {'search_products':search_products})
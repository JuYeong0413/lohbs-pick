from django.shortcuts import render
from .models import Product
import pdb

def main(request):
    products = Product.objects.all()
    return render(request, 'products/main.html', {'products':products})

def search(request):
    query = request.GET.get('query')
    search_products = Product.objects.filter(name__contains=query)
    return render(request, 'products/search.html', {'search_products':search_products, 'query':query})

def category_list(request):
    category = request.GET.get('category')
    category = int(category)
    category_lists = Product.objects.filter(category=category)
    return render(request, 'products/category_list.html', {'category_lists':category_lists, 'output':category})
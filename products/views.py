from django.shortcuts import render
from .models import Product
import collections
import pdb

def main(request):
    products = Product.objects.all()
    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))
    return render(request, 'products/main.html', {'products':products, 'category_no':category_no})

def search(request):
    query = request.GET.get('query')
    search_products = Product.objects.filter(name__contains=query)
    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))
    
    return render(request, 'products/search.html', {'search_products':search_products, 'query':query, 'category_no':category_no})

def category_list(request):
    category = request.GET.get('category')
    category = int(category)
    category_lists = Product.objects.filter(category=category)
    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))
    
    return render(request, 'products/category_list.html', {'category_lists':category_lists, 'output':category, 'category_no':category_no})
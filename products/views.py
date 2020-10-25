from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Product
import pdb, collections, json
from picks.models import Collection
from picks.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main(request):
    sort = request.GET.get('sort', '')

    if sort == "lowPrice":
        product_list = Product.objects.all().order_by('price')  
    elif sort == "highPrice":
        product_list = Product.objects.all().order_by('-price')
    elif sort == "popular":
        product_list = Product.objects.all().annotate(num_cps=Count('collectionproduct')).order_by('-num_cps') 
    else:
        product_list = Product.objects.all().order_by('-id')

    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))

    # pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 21)
    try:
        products = paginator.get_page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if request.user.is_active:
        lists = Collection.objects.filter(user=request.user)
        return render(request, 'products/main.html', {'products':products, 'category_no':category_no, 'lists':lists})

    return render(request, 'products/main.html', {'products':products, 'category_no':category_no})


def search(request):
    sort = request.GET.get('sort', '')
    query = request.GET.get('query', '')

    if sort=="lowPrice":
        search_products = Product.objects.filter(name__contains=query).order_by('price')  
    elif sort =="highPrice":
        search_products = Product.objects.filter(name__contains=query).order_by('-price')
    else:
        search_products = Product.objects.filter(name__contains=query).annotate(num_cps=Count('collectionproduct')).order_by('-num_cps') 

    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))
    
    if request.user.is_active:
        lists = Collection.objects.filter(user=request.user)
        return render(request, 'products/search.html', {'search_products':search_products, 'query':query, 'category_no':category_no, 'lists':lists})
    
    return render(request, 'products/search.html', {'search_products':search_products, 'query':query, 'category_no':category_no})

def category_list(request):
    sort = request.GET.get('sort', '')
    category = request.GET.get('category', '')
    category = int(category)
    
    if sort=="lowPrice":
        category_lists = Product.objects.filter(category=category).order_by('price')  
    elif sort =="highPrice":
        category_lists = Product.objects.filter(category=category).order_by('-price')
    else:
        category_lists = Product.objects.filter(category=category).annotate(num_cps=Count('collectionproduct')).order_by('-num_cps') 

    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))
    
    if request.user.is_active:
        lists = Collection.objects.filter(user=request.user)
        return render(request, 'products/category_list.html', {'category_lists':category_lists, 'output':category, 'category_no':category_no, 'lists':lists})
    
    return render(request, 'products/category_list.html', {'category_lists':category_lists, 'output':category, 'category_no':category_no})

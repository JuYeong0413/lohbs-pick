from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Product
import pdb, collections, json
from picks.models import Collection
from picks.models import *

def main(request):
    sort = request.GET.get('sort', '')

    if sort=="lowPrice":
        products = Product.objects.all().order_by('price')  
    elif sort =="highPrice":
        products = Product.objects.all().order_by('-price')
    else:
        products = Product.objects.all().annotate(num_cps=Count('collectionproduct')).order_by('-num_cps') 

    category_no = collections.defaultdict(int)
    for i in range(0, 11):
        category_no[str(i)] = len(Product.objects.filter(category=i))
    lists = Collection.objects.filter(user=request.user)
    return render(request, 'products/main.html', {'products':products, 'category_no':category_no, 'lists':lists})

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
    
    return render(request, 'products/category_list.html', {'category_lists':category_lists, 'output':category, 'category_no':category_no})

# def collection_add(request, product_id, collection_id):
#     lohbs_pick = get_object_or_404(Collection, pk=collection_id)
#     product = get_object_or_404(Product, pk=product_id)

#     quantity = 1 
#     collection_product = CollectionProduct.objects.create(product=product, qunatity=quantity)
#     lohbs_pick.collection_products.add(collection_product)
#     lohbs_pick.collection_total += collection_product.sub_total
#     lohbs_pick.save()
    
#     picks = Collection.objects.all()
#     return render(request, 'picks/lohbs_pick.html', {'picks':picks})
    
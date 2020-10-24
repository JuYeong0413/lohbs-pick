from django.shortcuts import render
from products.models import Product
from picks.models import *

def main(request):
    products = Product.objects.all()[0:8]
    shared_lists = Share.objects.all().order_by('-created_at')[0:3]
    return render(request, 'index.html', {"products":products, 'shared_lists':shared_lists})
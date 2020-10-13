from django.shortcuts import render

def products_list(request):
    return render(request, 'products/products_list.html')

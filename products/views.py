from django.shortcuts import render

def products_list(request):
    return render(request, 'products/products_list.html')

def lohbs_pick(request):
    return render(request, 'products/lohbs_pick.html')
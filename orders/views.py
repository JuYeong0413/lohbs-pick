from django.shortcuts import render, redirect

def main(request):
    return render(request, 'orders/main.html')


def show(request, id):
    return render(request, 'orders/show.html')


def new(request):
    return render(request, 'orders/new.html')

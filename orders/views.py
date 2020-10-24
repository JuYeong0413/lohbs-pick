from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from picks.models import *
import pdb
from django.contrib.auth.decorators import login_required

# 주문 목록 페이지
@login_required
def main(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'orders/main.html', {'orders': orders})


# 주문 상세보기 페이지
@login_required
def show(request, id):
    return render(request, 'orders/show.html')


# 새로운 주문 작성 페이지
@login_required
def new(request):
    user = request.user
    if request.method == "POST":
        collection_id = request.POST.get('collection_id')
        collection = get_object_or_404(Collection, pk=collection_id)
        collection_products = collection.collection_products.all()

        total_price = 0
        for products in collection_products:
            total_price += products.sub_total
        
        delivery_price = 3000
        if total_price >= 20000:
          delivery_price = 0

        context = {
          'collection_name': collection.name,
          'collection_products': collection_products,
          'product_total_price': total_price,
          'delivery_price': delivery_price,
          'final_price': total_price + delivery_price,
          'name': f'{user.last_name}{user.first_name}',
          'collection_id': collection_id,
          'collection_period': collection.get_period_display()
        }
        return render(request, 'orders/new.html', context)
    return redirect('orders:main')


# 새로운 주문 생성
@login_required
def create(request):
    user = request.user
    if request.method == "POST":
        collection_id = request.POST.get('collection_id')
        collection = get_object_or_404(Collection, pk=collection_id)

        if user == collection.user:
            products = collection.collection_products.all()

            final_price = request.POST.get('final_price')
            address1 = request.POST.get('b')
            address2 = request.POST.get('d')
            detail_address = request.POST.get('c')
            zipcode = request.POST.get('a')
            address = f'({zipcode}) {address1} {detail_address} {address2}'
            collection_name = collection.name
            recipient = request.POST.get('recipient_name')
            recipient_phone = request.POST.get('phone')
            delivery_message = request.POST.get('message')
            period = collection.period
            order = Order.objects.create(user=user, order_total=final_price, address=address, collection=collection, collection_name=collection_name, recipient=recipient, recipient_phone=recipient_phone, delivery_message=delivery_message, period=period)

            for product in products:
                o = OrderProduct.objects.create(product=product.product, quantity=product.quantity)
                order.order_products.add(o)

            order.save()

            selected = request.POST.get("save-address", None)
            if selected in 'save_address':
                user.profile.address1 = address1
                user.profile.address2 = address2
                user.profile.detail_address = detail_address
                user.profile.zipcode = zipcode
                user.profile.save()

    return redirect('orders:main')

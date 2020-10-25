from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .models import *
import json, datetime


# 프로필 페이지
def main(request, id):
    user_profile = get_object_or_404(User, pk=id)
    return render(request, 'users/main.html', {'user_profile': user_profile})

# 캘린더 페이지
def schedule(request, id):
    current_user = request.user
    user = get_object_or_404(User, pk=id)
    
    if current_user == user:
        orders = Order.objects.filter(user__id=id)
    else:
        orders = Order.objects.filter(user__id=id, kinds=0)

    for order in orders:
        delivery = {'title':order.collection_name, 'start':order.created_at.date, 'period':order.period}
        return render(request, 'users/schedule.html', {'delivery':delivery, 'user':user})

    #return render(request, 'users/schedule.html', {'orders':orders, 'user':user, 'delivery':delivery})

# 프로필 수정 페이지
@login_required
def edit(request, id):
    current_user = request.user
    user = get_object_or_404(User, pk=id)

    if user == current_user:
        return render(request, 'users/edit.html', {'user': user})
    else:
        return redirect('users:main', id)


# 프로필 수정
@login_required
def update(request, id):
    if request.method == "POST":
        user = get_object_or_404(User, pk=id)
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        profile_address = request.POST.get('profile_address')
        
        if request.FILES.get('profile_image'):
            user.profile.profile_image = request.FILES.get('profile_image')
            
        if request.POST.get('checkbox'):
            user.profile.profile_image = 'images/default_profile.jpg'


        user.profile.nickname = nickname
        user.profile.phone = phone
        user.profile.profile_address = profile_address

        user.profile.address1 = request.POST.get('b')
        user.profile.address2 = request.POST.get('d')
        user.profile.detail_address = request.POST.get('c')
        user.profile.zipcode = request.POST.get('a')

        user.profile.save()
        return redirect('users:main', id)
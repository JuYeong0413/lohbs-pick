from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# 프로필 페이지
def main(request, id):
    user_profile = get_object_or_404(User, pk=id)
    return render(request, 'users/main.html', {'user_profile': user_profile})

# 프로필 수정 페이지
def edit(request, id):
    current_user = request.user
    user = get_object_or_404(User, pk=id)

    if user == current_user:
        return render(request, 'users/edit.html', {'user': user})
    else:
        return redirect('users:main', id)


# 프로필 수정
def update(request, id):
    if request.method == "POST":
        user = get_object_or_404(User, pk=id)
        nickname = request.POST.get('nickname')
        phone = request.POST.get('phone')
        profile_address = request.POST.get('profile_address')
        
        if request.FILES.get('profile_image'):
            user.profile.image = request.FILES.get('profile_image')
            
        if request.POST.get('checkbox'):
            user.profile.image = 'images/default_profile.jpg'

        if user.username == 'testuser':
            user.profile.nickname = 'testuser'
        else:
            user.profile.nickname = nickname
        user.profile.phone = phone
        user.profile.profile_address = profile_address

        user.profile.save()
        return redirect('users:main', id)
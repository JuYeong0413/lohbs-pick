from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from products.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('사용자'), on_delete=models.CASCADE)
    nickname = models.CharField(_('닉네임'), max_length=10, unique=True)
    profile_image = models.ImageField(_('프로필 이미지'), upload_to="profile_images/", default="images/default_profile.jpg")
    profile_address = models.CharField(_('프로필 주소'), max_length=300)
    phone = models.CharField(_('연락처'), max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='프로필'
        verbose_name_plural ='프로필'

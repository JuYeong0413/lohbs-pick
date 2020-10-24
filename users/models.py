from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from products.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('사용자'), on_delete=models.CASCADE)
    nickname = models.CharField(_('닉네임'), max_length=10, unique=True)
    profile_image = models.ImageField(_('프로필 이미지'), upload_to="profile_images/", default="images/default_profile.jpg")
    profile_address = models.CharField(_('프로필 주소'), max_length=300)
    phone = models.CharField(_('연락처'), max_length=20)
    address1 = models.CharField(_('주소1'), max_length=300)
    address2 = models.CharField(_('주소2 참고항목'), max_length=300)
    detail_address = models.CharField(_('상세주소'), max_length=300)
    zipcode = models.CharField(_('우편번호'), max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='프로필'
        verbose_name_plural ='프로필'

        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
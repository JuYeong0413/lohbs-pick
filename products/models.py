from django.db import models
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):

    PRODUCT_KIND_CHOICES = [
        (0, "스킨케어"),
        (1, "메이크업"),
        (2, "헤어케어"),
        (3, "바디케어"),
        (4, "향수/방향"),
        (5, "리빙/잡화"),
        (6, "맨케어"),
        (7, "헬스"),
        (8, "푸드"),
        (9, "베이비케어"),
        (10, "펫케어"),
    ]   

    brand = models.CharField(_('브랜드명'), max_length=100) 
    name = models.CharField(_('상품명'),max_length=100)
    price = models.PositiveIntegerField(_('상품가격'))
    image = models.ImageField(_('상품이미지'),upload_to='product_images/')
    category = models.PositiveSmallIntegerField(_('상품종류'), choices = PRODUCT_KIND_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import User
from products.models import *
from users.models import *
from django.utils.translation import ugettext_lazy as _

class OrderProduct(models.Model):
    product = models.OneToOneField(Product, verbose_name=_('상품'), on_delete=models.SET_NULL)
    quantity = models.PositiveSmallIntegerField(_('수량'))
    price = models.PositiveIntegerField(_('가격'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='주문상품'
        verbose_name_plural='주문상품'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_('사용자'), on_delete=models.CASCADE)
    order_total = models.PositiveIntegerField(_('총 가격'))
    address = models.CharField(_('배송지 주소'), max_length=300)
    collection = models.ForeignKey(Collection, verbose_name=_('컬렉션'), on_delete=models.SET_NULL)
    collection_name = models.CharField(_('컬렉션명'), max_length=100)
    order_products = models.ManyToManyField(OrderProduct, verbose_name=_('주문상품'), related_name="order_products", through="Ordering")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='주문'
        verbose_name_plural='주문'


class Ordering(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('주문'), on_delete=models.CASCADE)
    order_products = models.ForeignKey(OrderProduct, verbose_name=_('주문 상품'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=(('order', 'order_product'))

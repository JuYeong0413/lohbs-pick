from django.db import models
from django.contrib.auth.models import User
from products.models import *
from picks.models import *
from django.utils.translation import ugettext_lazy as _

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('상품'), on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(_('수량'))
    price = models.PositiveIntegerField(_('가격'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='주문상품'
        verbose_name_plural='주문상품'
    
    def save(self, *args, **kwargs):
        self.price = self.product.price*self.quantity
        super().save(*args, **kwargs)


class Order(models.Model):
    PERIOD_CHOICES = [
        ("1W", "1주"),
        ("2W", "2주"),
        ("3W", "3주"),
        ("1M", "1달"),
        ("2M", "2달"),
        ("3M", "3달"),
    ]

    user = models.ForeignKey(User, verbose_name=_('사용자'), on_delete=models.CASCADE)
    order_total = models.PositiveIntegerField(_('총 가격'))
    address = models.CharField(_('배송지 주소'), max_length=300)                    
    collection = models.ForeignKey(Collection, verbose_name=_('컬렉션'), on_delete=models.SET_NULL, null=True)
    collection_name = models.CharField(_('컬렉션명'), max_length=100)
    order_products = models.ManyToManyField(OrderProduct, verbose_name=_('주문상품'), related_name="order_products", through="Ordering")
    recipient = models.CharField(_('받는 사람'), max_length=10)
    recipient_phone = models.CharField(_('수령인 연락처'), max_length=15)
    delivery_message = models.TextField(_('배송 요청사항'), blank=True)
    period = models.CharField(_('주기'), max_length=2, choices=PERIOD_CHOICES)
    isValid = models.BooleanField(_('유효성'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='주문'
        verbose_name_plural='주문'


class Ordering(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('주문'), on_delete=models.CASCADE)
    order_product = models.ForeignKey(OrderProduct, verbose_name=_('주문 상품'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=(
            ('order', 'order_product')
        )

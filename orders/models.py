from django.db import models
from django.contrib.auth.models import User
from products.models import *


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 사용자
    order_total = models.PositiveIntegerField() # 가격합계
    address = models.CharField(max_length=300) # 주소
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL) # 컬렉션
    collection_name = models.CharField(max_length=100) # 컬렉션명
    order_products = models.ManyToManyField(OrderProduct, related_name="order_products", through="OrderProduct") # 주문상품
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL) # 상품
    quantity = models.PositiveIntegerField() # 수량
    price = models.PositiveIntegerField() # 가격
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ordering(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # 주문
    order_products = models.ForeignKey(OrderProduct, on_delete=models.CASCADE) # 주문상품
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=(('order', 'order_product'))


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL) # 작성자(사용자)
    image = models.ImageField(upload_to='s_images/') # 사진
    content = models.TextField() # 내용
    collection_name = models.CharField(max_length=100) # 컬렉션명
    collection_products = models.ManyToManyField(Item, related_name="collection_products", through="CollectionProduct") # 컬렉션상품
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

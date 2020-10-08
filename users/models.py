from django.db import models
from django.utils.translation import ugettext_lazy as _
from products.models import Product
from django.utils.models import User


class CollectionProduct(models.Model):
    product = models.OneToOneField(Product, verbose_name=_('제품'), on_delete=models.CASCADE)
    qunatity = models.PositiveSmallIntegerField(_('수량'))
    sub_total = models.PositiveIntegerField(_('CollectionProduct 가격'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.sub_total = self.product.price*self.qunatity
        super().save(*args, **kwargs)

class Collection(models.Model):
    PERIOD_CHOICES = [
        ("1W", "1주"),
        ("2W", "2주"),
        ("3W", "3주"),
        ("1M", "1달"),
        ("2M", "2달"),
        ("3M", "3달"),
    ]   

    user = models.ForeignKey(User, verbose_name=_('사용자'), on_delete=models.CASCADE)
    collection_products = models.ManyToManyField(CollectionProduct, related_name="collection_products", blank=True, through='Collecting')
    collection_total = models.PositiveIntegerField(_('Collection 가격'), default=0)
    period = models.CharField(_('배송주기'), max_length=2, choices=PERIOD_CHOICES)
    name = models.CharField(_('컬렉션명'), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='컬렉션'
        verbose_name_plural='컬렉션'



class Collecting(models.Model):
    collection = models.ForeignKey(Collection, verbose_name= _('컬렉션'), on_delete=models.CASCADE)
    collection_product = models.ForeignKey(CollectionProduct, verbose_name= _('컬렉션 제품'), on_delete=models.CASCADE)
    
    class Meta:
        unique_together=(
            ('collection', 'collection_product')
        )
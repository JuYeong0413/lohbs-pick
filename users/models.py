from django.db import models
from django.utils.translation import ugettext_lazy as _
from products.models import Product

class CollectionProduct(models.Model):
    product = models.OneToOneField(Product, verbose_name=_('제품'), blank=True, on_delete=models.CASCADE)
    qunatity = models.PositiveSmallIntegerField(_('수량'))
    sub_total = models.PositiveIntegerField(_('가격'))

    def save(self, *args, **kwargs):
        self.price = self.product.price*self.amount
        super().save(*args, **kwargs)

class Collection(models.Model):
    collection_products = models.ManyToManyField(CollectionProduct, related_name="collection_products", symmetrical=False, blank=True, through='Collecting')
    collection_total = models.PositiveIntegerField(_('총 가격'), blank=True)
    period = models.PositiveSmallIntegerField(_('주기'))
    name = models.CharField(_('컬렉션명'), max_length=100)

    class Meta:
        verbose_name='컬렉션'
        verbose_name_plural='컬렉션'



class Collecting(models.Model):
    collection = models.ForeignKey(Collection, verbose_name= _('컬렉션'), on_delete=models.CASCADE)
    collection_product = models.ForeignKey(CollectionProduct, verbose_name= _('컬렉션 제품'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='컬렉팅'
        verbose_name_plural='컬렉팅'
        unique_together=(
            ('collection', 'collection_product')
        )
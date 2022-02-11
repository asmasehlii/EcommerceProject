from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.


class Order(models.Model):
    created_at = models.DateTimeField(verbose_name="created_at")
    delivered_at = models.DateTimeField(verbose_name="delivered_at")
    is_delivered = models.BooleanField()
    paid_at = models.DateTimeField(verbose_name="paid_at")
    is_paid = models.BooleanField()
    payment_method = models.CharField(verbose_name='payment_method', max_length=255)
    tax_price = models.CharField(verbose_name='tax_price', max_length=255)
    total_price = models.CharField(verbose_name='total_price', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user', blank=True, null=True)

    def __str__(self):
        return str(self.created_at)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='address', max_length=255)
    city = models.CharField(verbose_name='city', max_length=255)
    postal_code = models.CharField(verbose_name='postal_code', max_length=255)
    country = models.CharField(verbose_name='country', max_length=255)
    chipping_price = models.CharField(verbose_name='shipping_price', max_length=255)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              blank=True, null=True, related_name='order')
    name = models.CharField(verbose_name='name', max_length=255)
    qty = models.IntegerField()
    price = models.CharField(verbose_name='price', max_length=255)
    image = models.CharField(verbose_name='image', max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                blank=True, null=True, related_name='product_order_item')



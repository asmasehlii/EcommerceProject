from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='product_user', blank=True, null=True)
    name = models.CharField(verbose_name='name', max_length=255, blank=True, null=True)
    image = models.ImageField(verbose_name='product_image', blank=True, null=True)
    brand = models.CharField(verbose_name='brand', max_length=255, blank=True, null=True)
    category = models.CharField(verbose_name='category', max_length=255, blank=True, null=True)
    description = models.CharField(verbose_name='description', max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    num_reviews = models.IntegerField(blank=True, null=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    count_in_stock = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)


class Review(models.Model):
    created_at = models.DateTimeField(verbose_name="created_at")
    name = models.CharField(verbose_name='name', max_length=255)
    rating = models.CharField(verbose_name='rating', max_length=255)
    comment = models.CharField(verbose_name='comment', max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_review', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_review', blank=True, null=True)




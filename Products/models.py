from django.db import models
from django.contrib.auth.models import User


class SampleProducts(models.Model):
    """
    Displaying some sample products in home page..!
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    images = models.ImageField(upload_to='static/images')
    active = models.BooleanField(default=False)
    order = models.IntegerField(unique=True)

    def __unicode__(self):
        return "%s" % (self.name)


class Products(models.Model):
    """
    All the products are added here with price..!
    """
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    images = models.ImageField(upload_to="static/images")
    active = models.BooleanField(default=False)
    order = models.IntegerField(unique=True)
    price = models.IntegerField()
    measurement = models.CharField(max_length=10)
    offer_price = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name)


class UserCartProducts(models.Model):
    """
    User added products in cart are stored here..!
    """
    user = models.ForeignKey(User)
    products = models.ManyToManyField(Products, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.user.username)

    @property
    def cart_item_amount(self):
        total_amount = \
          sum(map(int, self.products.all().values_list('price', flat=True)))
        return float(total_amount)

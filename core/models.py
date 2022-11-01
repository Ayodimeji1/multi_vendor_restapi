from django.db import models
from django.contrib.auth.models import User


# Vendor model
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.user)


# Product Category model
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


#  Product model
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='product_category')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


# Customer model

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.user.username)


# Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_orders')
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.time


# Order Items
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
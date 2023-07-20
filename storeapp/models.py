from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cost = models.FloatField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + " (" + self.category.name + ")"

class CustomerOrder(models.Model):
    total = models.FloatField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    fname = models.CharField(max_length=255, default="Firstname")
    lname = models.CharField(max_length=255, default="Lastname")
    postcode = models.CharField(max_length=8, default="Postcode")
    line1 = models.CharField(max_length=255, default="Line 1")
    line2 = models.CharField(max_length=255, null=True, default=None)
    line3 = models.CharField(max_length=255, null=True, default=None)
    phone_number = models.CharField(max_length=15, null=True, blank=True, default=None)
    country = models.CharField(max_length=100, default="United Kingdom")
    delivery_instructions = models.CharField(max_length=400, null=True, blank=True)  # New field for delivery instructions


    def __str__(self):
        return self.customer.username + ": " + str(self.total)
    
class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField(default=1)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.qty) + "x " + self.product.name
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

class DeliveryAddress(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    postcode = models.CharField(max_length=8)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, null=True)
    line3 = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (self.fname + " " + self.lname + " | " 
                 + self.line1 + ", " + self.line2 + ", "
                   + ". " + self.country +
                     ". ")

class CustomerOrder(models.Model):
    total = models.FloatField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    delivery = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username + ": " + str(self.total)
    
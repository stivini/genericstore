from django.db import models
from django.contrib.auth.models import User
from django.db import models

class DefaultImages(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='default_images/')


class Category(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)



class Products(models.Model):
    def __str__(self):
        return self.name
    
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # this is the orderd amounts
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True)
    sellp = models.FloatField()
    buyp = models.FloatField(default=0)
    # this is the number of Product instance in stock
    quantity = models.IntegerField(default=0,)
    cart = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True)

        
    def cart_data(self):
        if self.amount>0:
            return int(0)
        elif self.amount == 0:
            return int(0)
        else:
            return int(0)

        
    def group_by_category(self):
        cat = self.category
        return cat
    
    def get_total(self):
        a=self.amount
        b=self.sellp
        c=a*b
        return c    


class Users(User):
    def __str__(self):
        return self.firstname
    
    products = models.ManyToManyField(Products, default='none',related_name='user_products')
    firstname = models.CharField(max_length=200)
    phone = models.IntegerField(unique=True)



from django.db import models

class products(models.Model):
    name  = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.CharField(max_length=200)

class contacts(models.Model):
    contact_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)



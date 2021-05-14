from django.db import models

class products(models.Model):
    name  = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)


